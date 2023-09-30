FROM python:3.8

WORKDIR /root/app/

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/root/app/"
EXPOSE 10000

CMD ["bash", "-c", "python receiver.py"]
