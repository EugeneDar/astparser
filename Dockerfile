FROM python:3

RUN pip3 install numpy

COPY . .

ENTRYPOINT ["python3", "./main.py"]

# docker build -t app .
# docker run app