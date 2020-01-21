FROM smartlab/flask:latest
LABEL maintainer="smartlab-dev@mpt.mp.br"

# Installing scipy
RUN apk update --no-cache build-base gfortran libffi-dev openssl-dev python3-dev musl-dev && \
    mkdir scipy && cd scipy && \
    # wget https://github.com/scipy/scipy/releases/download/v1.4.1/scipy-1.4.1.tar.gz && \
    # tar -xvf scipy-1.4.1.tar.gz && cd scipy-1.4.1 && \
    # python3 -m pip --no-cache-dir install . && \
    pip3 install -Iv scipy==1.4.1 && \
    rm -rf scipy 2> /dev/null && rm -rf /var/cache/apk/* 2> /dev/null && rm -rf ~/.cache/ 2> /dev/null

# Installing scikit-learn
# RUN apk add --no-cache openblas-dev freetype-dev pkgconfig && \
#     pip3 install -Iv scikit-learn==0.21.3
#     pip3 install -Iv scikit-learn==0.22.1

# Removing packages
# RUN apk del build-base gofortran libffi-dev openssl-dev python3-dev musl-dev

COPY app /app/
COPY uwsgi.ini /etc/uwsgi/

EXPOSE 5000
WORKDIR /app

ENTRYPOINT ["sh", "/start.sh"]
