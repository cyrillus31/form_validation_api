# Form validation API

<div align="left">
  <img src="https://skillicons.dev/icons?i=py" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://skillicons.dev/icons?i=fastapi" height="40" alt="fastapi logo"  />
  <img width="12" />
  <img src="https://skillicons.dev/icons?i=mongodb" height="40" alt="mongodb logo"  />
  <img width="12" />
  <img src="https://skillicons.dev/icons?i=docker" height="40" alt="docker logo"  />
  <img width="12" />
  <img src="https://skillicons.dev/icons?i=nginx" height="40" alt="nginx logo"  />
</div>

<br>
<br>

[http://form-validation-api.fvds.ru/get\_form](http://form-validation-api.fvds.ru/get_form)

[Подробное техническое задание](technical_task/Тестовое%20задание%20Python%20Junior%20-.pdf)

Сервис принимает POST запрос с данными нейкой формы. Ответом будет либо имя формы, чьи поля и тип совпадают хотя бы с частью полей из присланной формы. Если присланная форма не найдет себе эквивалента в базе данных сервиса, то ответом будет форма с типами на основе правил валидации. 

В качестве БД поднимается MongoDB в контейнере.

|Тип данных   | Парвило валидации |
|------|--------------------------|
|phone |          +7 xxx xxx xx xx|
|date  | DD.MM.YYYY или YYYY-MM-DD| 


> [!NOTE]
> Последовательность валидации: date, phone, email, text.



В настоящий момент сервис ожидает три следующих вида форм:

```python
# Client
{
    "client name": "text",
    "date registered": "date",
    "client email": "email",
    "phone number": "phone"
}

# Order
{
    "order description": "text",
    "date created": "date",
    "customer email": "email"
}

# Seller
{
    "seller name": "text",
    "phone number": "phone"
}
```

<br>

## Запуск

Клонирование репозитория:

```console
git clone https://github.com/cyrillus31/form_validation_api.git
```

<br>


### Запуск локально в контейнере

```docker
sudo docker compose up -d
```

API будет доступен по следующему URL:  
http://127.0.0.1:8000/get_form

<br>

### Скрипт для тестирования работы
Запустить скрипт из корня репозитория, который, c помощью библиотеки Requests, может отправлять тестовые POST запросы или на localhost, или на сервер [http://form-validation-api.fvds.ru/get\_form](http://form-validation-api.fvds.ru/get_form): 

```console
python tests/test_script.py
```


<br>

## Запуск на сервере

### Конфигурация NGINX 
Создать файл конфигурации в любом текстовом редакторе:

```console
sudo vim /etc/nginx/conf.d/form_validation_api.conf
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



