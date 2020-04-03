FROM nginx:alpine

COPY build /usr/share/nginx/html
COPY deploy/nginx.conf /etc/nginx/conf.d/default.conf
COPY deploy/uwsgi_params /etc/nginx/uwsgi_params
