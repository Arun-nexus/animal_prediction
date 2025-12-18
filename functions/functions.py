from database.animal_information import get_animal_details, class_names
from model.cnn_model import model, device
from torchvision import transforms
from PIL import Image
import io
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

async def image_name(image):

        # 1. UploadFile se raw bytes read karein
        img_bytes = await image.read()

        # 2. Bytes ko PIL Image mein convert karein
        img = Image.open(io.BytesIO(img_bytes)).convert('RGB')

        # 3. Transform apply karein (jo Tensor banayega)
        # Maan lete hain aapka transform variable ka naam 'transform' hai
        img_tensor = transform(img).unsqueeze(0)  # Batch dimension add karein

        # 4. Model Prediction
        model.eval()
        with torch.no_grad():
            logits = model(img_tensor)  # Ab yahan Tensor jayega, UploadFile nahi
            probs = torch.nn.functional.softmax(logits, dim=1)
            top3_prob, top3_idx = torch.topk(probs, 3, dim=1)

        return top3_prob[0].tolist(), top3_idx[0].tolist()

def info(out, prob):
    info_list = {}
    for i in range(len(out)):
        info_list[class_names[out[i]]] = prob[i]

    main_animal_info = get_animal_details(out[0])
    return main_animal_info, info_list
