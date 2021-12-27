FROM ubuntu:18.04

ENV PYTHONUNBUFFERED 1
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

RUN pip3 install pika
RUN pip3 install asyncio
RUN mkdir /opt/code
RUN mkdir /opt/requirements
WORKDIR /opt/code

COPY . /opt/code

ENTRYPOINT ["python3"]

CMD ["worker/app.py"]