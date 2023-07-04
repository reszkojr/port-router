FROM debian

# Atualize os pacotes e instale os programas desejados via apt
RUN apt update && apt install -y python3 python-is-python3 python3-pip git nginx
RUN pip install jinja2 fastapi uvicorn --break-system-packages
RUN mkdir -m /www/port-router && git clone https://github.com/reszkojr/port-router /www/port-router

EXPOSE 8080

COPY ./nginx.conf /etc/nginx/nginx.conf

# Defina qualquer outra configuração necessária

# Defina o comando padrão para o contêiner

CMD ["/bin/bash"]