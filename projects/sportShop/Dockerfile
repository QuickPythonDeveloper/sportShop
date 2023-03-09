FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /sportShop
ENV APIDIR=/sportShop
RUN mkdir $APIDIR/media

WORKDIR $APIDIR
COPY . $APIDIR/

RUN addgroup --group sport_shop_group

RUN useradd -ms /bin/bash sport_shop_user
RUN adduser sport_shop_user sport_shop_group

RUN chown -R sport_shop_user:sport_shop_group $APIDIR

ADD docker/sh_files/api.sh /api.sh
RUN chmod +x /api.sh

ADD docker/celery/sh_files/celery.sh /celery.sh
RUN chmod +x /celery.sh

ADD docker/celery-beat/sh_files/celery-beat.sh /celery-beat.sh
RUN chmod +x /celery-beat.sh

#RUN sysctl vm.overcommit_memory=1

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

USER sport_shop_user
