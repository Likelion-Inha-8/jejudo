FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["/app/run.sh"]