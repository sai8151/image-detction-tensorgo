# Image Detection Flask App with Elasticsearch Logging

This project demonstrates a Flask application for image detection using a pre-trained ResNet-101 model from torchvision. The application allows users to upload an image and receive predictions about its contents with confidence levels.

## Features

- **Prediction Endpoint**: Upload an image and receive predictions about its contents (e.g., object classification).
- **Logging to Elasticsearch**: Logs predictions including labels, confidence scores, and client IP addresses to Elasticsearch for monitoring and analysis.

## Setup Instructions

### Prerequisites

- Docker installed on your machine or server.
- Elasticsearch endpoint and API key for logging.

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd image-detection-flask-elasticsearch
   ```
2. **Build the Docker image**:
   ```bash
   sudo docker build -t image-detection-app .
   ```
3. **Run the Docker container**:
   ```bash
   sudo docker run -d -p 5000:5000 --name image_detection_app image-detection-app
   ```
4. **Verify the running container**:
   ```bash
   sudo docker ps
   ```
