FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#RUN addgroup --group sport_shop_group

#RUN useradd -ms /bin/bash sport_shop_user
#RUN adduser sport_shop_user sport_shop_group

RUN mkdir /sportShopBot
ENV BOTDIR=/sportShopBot

WORKDIR $BOTDIR
COPY . $BOTDIR/

#RUN chown -R sport_shop_user:sport_shop_group $BOTDIR
#RUN chmod +w $BOTDIR/settings/

ADD sh_files/main.sh /main.sh
RUN chmod +x /main.sh

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#USER sport_shop_user
