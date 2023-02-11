FROM python:3.7.3-alpine3.9
WORKDIR /app
COPY app/requirements.txt /app
RUN pip install -r requirements.txt
COPY app /app
CMD ["python3","main.py"]