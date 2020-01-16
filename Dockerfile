FROM smartlab/flask:latest
LABEL maintainer="smartlab-dev@mpt.mp.br"

COPY app /app/
COPY uwsgi.ini /etc/uwsgi/

RUN pip install -Iv cython == 0.29.14 sklearn == 0.0

EXPOSE 5000
WORKDIR /app

ENTRYPOINT ["sh", "/start.sh"]
