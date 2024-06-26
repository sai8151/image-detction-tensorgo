from flask import Flask, request, jsonify, render_template
from torchvision import models, transforms
from PIL import Image
import torch
import torch.nn.functional as F
import json
import os

app = Flask(__name__)

# Load the pre-trained ResNet-101 model
resnet = models.resnet101(pretrained=True)
resnet.eval()

# Define the image preprocessing pipeline
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Load the ImageNet labels from the JSON file
with open('imagenet_classes.txt') as f:
    labels = json.load(f)

def predict(image):
    img_t = preprocess(image)
    batch_t = torch.unsqueeze(img_t, 0)

    with torch.no_grad():
        out = resnet(batch_t)
        _, index = torch.max(out, 1)
        percentage = F.softmax(out, dim=1)[0] * 100
        label = labels[index[0]]
        confidence = percentage[index[0]].item()

    return label, confidence

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_route():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    img = Image.open(file.stream)
    label, confidence = predict(img)

    return jsonify({'label': label, 'confidence': confidence})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8501)
