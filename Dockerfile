FROM  alpine:3.11

LABEL maintainer="smartlab-dev@mpt.mp.br"

# Fix versions of pip and setuptools
ARG PIP=20.0.1
ARG STS=41.2.0 

COPY requirements.txt /app/requirements.txt

RUN apk --update --no-cache add --virtual toRemove build-base libffi-dev \
                                          openssl-dev python3-dev \
                                          cyrus-sasl-dev openblas-dev \
                                          openblas-dev gfortran \
                                          g++ gcc musl-dev lapack-dev \
 && apk --update --no-cache add libffi openssl ca-certificates python3 \
                                libstdc++ lapack libgcc libquadmath musl\
                                libgfortran cython openblas libgomp \
 && pip3 install --upgrade pip==${PIP} setuptools==${STS} \
 && pip3 install -r /app/requirements.txt \
 && apk del toRemove \
 && rm -rf /root/.cache \
 && rm -rf /var/cache/apk/* 

COPY uwsgi.ini /etc/uwsgi/conf.d/
COPY start.sh /start.sh
COPY app /app

RUN chown -R uwsgi:uwsgi /app \
 && chmod +x /start.sh \
 && mkdir -p /var/run/flask \
 && chown -R uwsgi:uwsgi /var/run/flask /etc/uwsgi/conf.d /app

ENV DEBUG 0
ENV FLASK_APP /app/main.py
ENV PYTHONPATH /app:/usr/lib/python3.8/site-packages

EXPOSE 5000
WORKDIR /app
ENTRYPOINT ["sh", "/start.sh"]
