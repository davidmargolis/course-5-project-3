# syntax=docker/dockerfile:1

FROM python:latest
EXPOSE 5000
COPY app.py .
RUN pip install flask
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
