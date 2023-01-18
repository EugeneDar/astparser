FROM python:3

RUN pip3 install numpy
RUN pip3 install requests
RUN pip3 install clang

COPY . .

ENTRYPOINT ["python3", "./src/main.py"]

# docker build -t app .
# docker run app