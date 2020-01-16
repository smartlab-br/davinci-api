FROM smartlab/flask:latest
LABEL maintainer="smartlab-dev@mpt.mp.br"

COPY app /app/
COPY uwsgi.ini /etc/uwsgi/

#RUN apk --update --no-cache add build-base libffi-dev openssl-dev python3-dev libffi openssl ca-certificates python3 cyrus-sasl-dev libstdc++ uwsgi-python3 gfortran openblas-dev && \
#    pip3 install --upgrade pip setuptools && \
#    pip3 install -r /app/requirements.txt && \
#    apk del build-base libffi-dev openssl-dev python3-dev libffi openssl ca-certificates && \
#    rm -rf /var/cache/apk/* && \
#    rm -rf ~/.cache/ && \
RUN pip3 install -Iv cython==0.29.14 sklearn==0.0

EXPOSE 5000
WORKDIR /app

ENTRYPOINT ["sh", "/start.sh"]
