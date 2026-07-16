FROM python:3.13-slim
WORKDIR /app
COPY app/requirements.txt /app
RUN pip install -r requirements.txt
COPY app /app
CMD ["python3","main.py"]