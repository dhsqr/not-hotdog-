import torch
import torchvision.transforms as transforms
from torchvision import models
from torchvision.models import ResNet18_Weights
from PIL import Image
import gradio as gr
import urllib

# Load pretrained ResNet18 (ImageNet)
model = models.resnet18(weights=ResNet18_Weights.DEFAULT)
model.eval()

# ImageNet classes
classes = urllib.request.urlopen(
    "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
).read().decode().splitlines()

# Transform pipeline
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

def classify(img):
    img_t = transform(img).unsqueeze(0)
    with torch.no_grad():
        out = model(img_t)
    _, idx = torch.max(out, 1)
    label = classes[idx]
    return "Hotdog 🌭" if "hotdog" in label.lower() else "Not Hotdog ❌"

# Gradio app (only upload, no webcam)
demo = gr.Interface(
    fn=classify,
    inputs=gr.Image(type="pil", sources=["upload"]),
    outputs="label"
)

demo.launch()
