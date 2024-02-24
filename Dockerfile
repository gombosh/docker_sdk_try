# from the default python image, and change the command to echo "Hello, DORON!"
FROM python:3.12

WORKDIR /app

COPY . /app 

# RUN apt-get update && apt-get install -y \
#     curl \
#     wget \
#     git \
#     vim \
#     nano \
#     && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD "python3 test_docker_sdk.py"