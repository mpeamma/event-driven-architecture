FROM python:3

ADD consumer.py /
ADD requirements.txt /

RUN pip install -r requirements.txt

CMD [ "python", "./consumer.py" ]
