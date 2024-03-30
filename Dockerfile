FROM python:3.10

COPY . /usr/crest-ave-test-py
WORKDIR /usr/crest-ave-test-py

RUN pip install -r requirements.txt

CMD [ "python", "-u", "main.py" ]
CMD tail -f /dev/null