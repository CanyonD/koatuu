FROM iron/python:2-dev

#RUN apk update && apk upgrade && apk add tin


ENV TINI_VERSION v0.9.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-static /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

WORKDIR /src

COPY requirements.txt ./
COPY *.py ./
COPY *.sh ./

RUN pip install -r requirements.txt
