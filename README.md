# port-router
An API that routs specific IP's to specific internal ports.

![Screenshot](https://i.imgur.com/QBqYnKF.png)

### Requirements:

#### Python:
```
sudo apt install python3 python-is-python3
```
or, for Python 2:
```
sudo apt install python2 python-is-python2
```
#### Python modules:
```
pip install fastapi uvicorn jinja2
```

### NGINX sample configuration for reverse proxy:

```nginx
codeserver { 
    listen 8000; 
    server_name localhost:8000; 
 
    location /erp1/ { 
        proxy_pass http://localhost:1/; 
    } 
 
    location /erp2/ { 
        proxy_pass http://localhost:2/; 
    } 

    location /erp3/ { 
        proxy_pass http://localhost:3/; 
    } 

    location /erp4/ { 
        proxy_pass http://localhost:4/; 
    } 
} 
```
