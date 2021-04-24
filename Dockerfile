FROM python:3.9.4-slim

WORKDIR /backend
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 8888

CMD [ "python3", "app.py"]