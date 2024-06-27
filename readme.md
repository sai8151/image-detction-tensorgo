# Image Detection Flask App with Elasticsearch Logging

This project demonstrates a Flask application for image detection using a pre-trained ResNet-101 model from torchvision. The application allows users to upload an image and receive predictions about its contents with confidence levels.

# Task assigned:

1. **Create a VM:**

- Create an Ubuntu 22.04 virtual machine on any cloud platform.

2. **Develop a Docker Application:**

- Write a Dockerfile for a small deep learning or full-stack application.
- Build the Docker image and run the Docker container.
- Ensure the application is accessible via a web UI.

3. **Implement Security and Vulnerability Scanning:**

- Use the best free and open-source scanning tools to implement vulnerability and security scanning for the Docker
images and containers.

4. **Set Up Monitoring and Logging:**

- Implement a monitoring and logging system using tools like Prometheus, Grafana, Elasticsearch, Logstash, and
Kibana.
- Ensure that logs are stored and visible even if the container restarts.

5. **Documentation and Architecture:**

- Create detailed documentation and an architectural diagram for the above assignment.

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
   git clone https://github.com/sai8151/image-detction-tensorgo
   cd image-detection-flask-elasticsearch
   ```
2. **Build the Docker image**:
   ```bash
   sudo docker build -t my-ubuntu-flask-app .
   ```
3. **Run the Docker container**:
   ```bash
   sudo docker run -d -p 8501:8501 --name my-ubuntu-flask-app my-ubuntu-flask-app
   or
   sudo docker run 8501:8501 my-ubuntu-flask-app
   or
   sudo docker run -d -p 8501:8501 my-ubuntu-flask-app
   
   Auto run after restart
   sudo docker run -d -p 8501:8501 --restart unless-stopped --name my-ubuntu-flask-app my-ubuntu-flask-app
   ```
4. **Verify the running container**:
   ```bash
   sudo docker ps
   ```
5. **Check logs**:
   ```
   sudo docker logs c64863d3ee6d
   ```
6. **Delete the data of docker**:
   ```
   sudo docker system prune -a --volumes
   ```
