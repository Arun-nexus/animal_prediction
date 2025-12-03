from database.animal_information import get_animal_details, class_names
from model.cnn_model import model, device
from torchvision import transforms
from PIL import Image
import torch.nn.functional as F
import torch

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

def image_name(image_path):
    try:
        img = Image.open(image_path).convert("RGB")
        img = transform(img)
        img = img.unsqueeze(0).to(device)

        model.eval()
        with torch.no_grad():
            logits = model(img)
            probs = F.softmax(logits, dim=1)


            top3_prob, top3_idx = torch.topk(probs, 3, dim=1)

            top3_prob = top3_prob[0].tolist()
            top3_idx = top3_idx[0].tolist()
            top3_prob = [round(p, 2) for p in top3_prob]

            return top3_prob,top3_idx

    except Exception as e:
        return {"error": str(e)}

image = r"C:\Users\Arun\Downloads\images.webp"
prediction = image_name(image)
prob,out = prediction

def info(out,prob):
    info_list = {}
    for n in range(len(out)):
         info_list[class_names[out[n]]]=prob[n]
    return get_animal_details(out[0]),info_list
