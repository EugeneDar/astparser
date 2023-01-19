FROM python:3

RUN apt-get update && apt-get upgrade -y
RUN pip3 install numpy
RUN pip3 install requests
RUN apt-get install clang -y

COPY . /repo

# sudo docker build -t foo .
# sudo docker run -it -v /home/eugene/tmp:/data --rm foo python3 repo/src/main.py