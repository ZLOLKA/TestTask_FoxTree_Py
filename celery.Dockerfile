FROM python:3

WORKDIR /celery_sample

COPY ./req.txt /celery_sample
RUN pip install -r req.txt
RUN pip install redis

COPY . /celery_sample/

EXPOSE 443

COPY ./celery.entrypoint.sh /bin/celery.entrypoint.sh
ENTRYPOINT [ "bash", "celery.entrypoint.sh" ]
