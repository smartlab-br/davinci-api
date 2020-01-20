FROM smartlab/flask:latest
LABEL maintainer="smartlab-dev@mpt.mp.br"

# RUN apk add --no-cache gcc g++ gfortran libffi-dev libressl-dev python3-dev musl-dev && \
RUN apk add --no-cache build-base gfortran libffi-dev openssl-dev python3-dev musl-dev && \
    mkdir scipy && cd scipy && \
    wget https://github.com/scipy/scipy/releases/download/v1.3.2/scipy-1.3.2.tar.gz && \
    tar -xvf scipy-1.3.2.tar.gz && cd scipy-1.3.2 && \
    pip3 -Iv install scikit-learn==0.22.1 && \
    python3 -m pip --no-cache-dir install .

# Falhando esse remove
# RUN apk del build-base gofortran libffi-dev openssl-dev python3-dev musl-dev
RUN rm -rf scipy 2> /dev/null && rm -rf /var/cache/apk/* 2> /dev/null && rm -rf ~/.cache/ 2> /dev/null

COPY app /app/
COPY uwsgi.ini /etc/uwsgi/

EXPOSE 5000
WORKDIR /app

ENTRYPOINT ["sh", "/start.sh"]
