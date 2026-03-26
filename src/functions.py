from database.animal_information import get_animal_details, class_names
from torchvision import transforms
from PIL import Image
from logger import logging
import io
import torch
import torch.nn.functional as F


transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


async def image_name(image, model, device):
    """
    Run inference on uploaded image.
    model aur device lifespan se pass honge — import nahi honge.
    Returns: (top3_probs as list, top3_indices as list)
    """
    try:
        logging.info("Reading and transforming image...")

        img_bytes = await image.read()
        img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
        img_tensor = transform(img).unsqueeze(0).to(device)

        logging.info("Running model inference...")

        with torch.no_grad(): 
            logits = model(img_tensor)
            probs  = F.softmax(logits, dim=1)
            top3_prob, top3_idx = torch.topk(probs, k=3, dim=1)

        logging.info("Inference successful.")
        return top3_prob[0].tolist(), top3_idx[0].tolist()

    except Exception as e:
        logging.error(f"image_name() failed: {e}")
        raise
    


def info(out: list, prob: list):
    """
    Fetch animal details for top prediction.
    Returns: (main_animal_info, info_dict)
    """
    try:
        if not out or not prob:
            raise ValueError("Empty prediction lists received in info()")

        logging.info("Fetching animal details...")

        info_dict = {
            class_names[out[i]]: prob[i]
            for i in range(len(out))
            if i < len(class_names)  
        }

        main_animal_info = get_animal_details(out[0])
        logging.info("Animal details fetched successfully.")
        return main_animal_info, info_dict

    except Exception as e:
        logging.error(f"info() failed: {e}")
        raise