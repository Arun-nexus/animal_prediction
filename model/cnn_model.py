import torch
from torchvision import models
from torch import nn

class animal_cnn(nn.Module):
    def __init__(self, num_classes):
        super(animal_cnn, self).__init__()
        self.base = models.efficientnet_b0(
            weights=models.EfficientNet_B0_Weights.DEFAULT
        )

        for param in self.base.features.parameters():
            param.requires_grad = False

        infeatures = self.base.classifier[1].in_features
        self.base.classifier = nn.Sequential(
            nn.Linear(infeatures, 512),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(512, num_classes),
        )

    def forward(self, x):
        return self.base(x)

device = ("cuda" if torch.cuda.is_available() else "cpu")
model = animal_cnn(num_classes=90).to(device)
model.load_state_dict(torch.load(r"C:\Users\Arun\PycharmProjects\animal_prediction\model\inital_model.pth", map_location=device))

