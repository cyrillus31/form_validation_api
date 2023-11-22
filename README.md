## Form validation API

[http://form-validation-api.fvds.ru/get\_form](http://form-validator-api.fvds.ru/get_form)

### Запуск
#### Вручную локально
Установить все необходимые библиотеки в виртульное окружение (BASH):

```console
python -m venv venv; source venv/bin/activate;
pip install -r requirements.txt
```

Зайти в директорию [app](app/) и выполнить команду:

```console
uvicorn main:app
```
После этого сервер развернется на localhost:8000.

Запустить скрипт, который будет отправлять тестовые POST запросы на localhost или на сервер: 
```console
python ../tests/test_script.py
```

### Запуск на сервере

#### Конфигурация systemd сервиса

Создать сервисный файл systemd:

```console
sudo vim /etc/systemd/system/forms_validation_api.service
```

Заполнить его конфигурацией по шаблону:

```console
[Unit]
Description=My FastAPI App
After=network.target

[Service]
User=myuser
Group=mygroup
WorkingDirectory=/path/to/app
ExecStart=/path/to/venv/bin/uvicorn main:app --host 127.0.0.1 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```
Запустить сервис:

```console
sudo systemctl daemon-reload; sudo systemctl enable forms_validation_api; sudo systemctl start forms_validation_api;
```

#### Конфигурация NGINX 
Создать файл конфигурации в любом текстовом редакторе:

```console
sudo vim /etc/nginx/conf.d/forms_validation_api.conf
```

Добавить в него следующую конфигурацию:

```nginx
server {
  listen 80;
  server_name your-web-address.com;

  location / {
    proxy_pass http://localhost:8000;
  }
}
```

Перезапустить NGINX:

```console
sudo systemctl restart nginx
```



