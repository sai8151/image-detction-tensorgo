# Use Ubuntu 22.04 LTS as the base image
FROM ubuntu:22.04

# Set the working directory in the container
WORKDIR /app

# Install the required packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    python3 -y\
    python3-pip\
    curl\
    git\
    && ls

RUN git clone https://github.com/sai8151/image-detction-tensorgo
RUN curl -o imagenet_classes.txt https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json
COPY . /app
RUN pip3 install --no-cache-dir -r requirements.txt 
RUN echo "heloo"
RUN pip install --upgrade Flask Werkzeug
# Expose the port the app runs on
EXPOSE 5000
EXPOSE 8501
EXPOSE 8080
#RUN curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.14.1-amd64.deb
#RUN dpkg -i filebeat-8.14.1-amd64.deb

# Run the application
CMD ["python3", "app2.py"]
