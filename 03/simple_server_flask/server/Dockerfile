FROM python:3.8

RUN mkdir /root/app/
WORKDIR /root/app/
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/root/app/"

CMD ["python", "server.py"]
