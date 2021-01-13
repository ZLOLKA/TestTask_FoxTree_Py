FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/work

COPY ./req.txt /usr/src/work/
RUN pip install -r req.txt

COPY . /usr/src/work/

COPY ./entrypoint.sh /bin/entrypoint.sh
ENTRYPOINT [ "bash", "entrypoint.sh" ]
