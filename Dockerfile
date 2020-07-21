FROM python:3.8
RUN apt-get update
COPY src/ /src/
RUN ls -la /src/
RUN pip install -r /src/requirements.txt
WORKDIR /src

CMD ["python", "api.py"]
