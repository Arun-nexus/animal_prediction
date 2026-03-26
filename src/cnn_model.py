import torch
from torchvision import models
from torch import nn
from logger import logging

BACKBONE_PATH = "model/inital_model.pth"


class AnimalCNN(nn.Module):
    def __init__(self, num_classes: int):
        super(AnimalCNN, self).__init__()

        self.base = models.efficientnet_b0(weights=None)
        backbone_state = torch.load(
            BACKBONE_PATH, map_location="cpu", weights_only=True
        )
        self.base.load_state_dict(backbone_state)
        logging.info("Backbone weights loaded from local file.")

        for param in self.base.features.parameters():
            param.requires_grad = False

        in_features = self.base.classifier[1].in_features
        self.base.classifier = nn.Sequential(
            nn.Linear(in_features, 512),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(512, num_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.base(x)


def load_model(
    model_path: str,
    num_classes: int = 90
) -> tuple[nn.Module, torch.device]:
    try:
        logging.info("Loading AnimalCNN model...")

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        logging.info(f"Using device: {device}")

        model = AnimalCNN(num_classes=num_classes).to(device)

        model.load_state_dict(
            torch.load(model_path, map_location=device, weights_only=True)
        )

        model.eval()
        logging.info("AnimalCNN loaded and ready.")
        return model, device

    except FileNotFoundError:
        logging.error(f"Model file not found: {model_path}")
        raise
    except RuntimeError as e:
        logging.error(f"State dict mismatch: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error loading model: {e}")
        raise