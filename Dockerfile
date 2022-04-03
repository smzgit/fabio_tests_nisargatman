FROM python:3.8-alpine
RUN mkdir -p /app
COPY requirements.txt /app/

COPY wiki_app /app/wiki_app


COPY main.py /app/

RUN pip install -r /app/requirements.txt \
     && rm -rf /app/requirements.txt

EXPOSE 5000

CMD ["python", "app/main.py"]