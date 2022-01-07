FROM nginx

RUN apt-get update
RUN apt-get install -y wget

ENV ENTRYKIT_VERSION 0.4.0

RUN wget https://github.com/progrium/entrykit/releases/download/v${ENTRYKIT_VERSION}/entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz
RUN tar -xvzf entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz
RUN rm entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz
RUN mv entrykit /usr/local/bin/
RUN entrykit --symlink
RUN rm /etc/nginx/conf.d/*

COPY frontend.conf.tmpl /etc/nginx/conf.d/

ENTRYPOINT [ \
    "render", \
        "/etc/nginx/conf.d/frontend.conf", \
        "--" \
]

CMD ["nginx", "-g", "daemon off;"]
