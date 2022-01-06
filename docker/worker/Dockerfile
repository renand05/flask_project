FROM python:3

ENV PYTHONUNBUFFERED 1

RUN pip install pika
RUN pip install asyncio
RUN pip install requests

RUN mkdir /opt/code
RUN mkdir /opt/requirements
WORKDIR /opt/code

ADD requirements /opt/requirements
RUN pip install -r /opt/requirements/development.txt

ENTRYPOINT ["python3"]
CMD ["worker/app.py"]