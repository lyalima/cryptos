# Distribuição e agendamento de tarefas de cotação de criptomoedas com Python, Django/DRF, Celery e RabbitMQ.

O projeto usa a API do site DefiLlama para pegar as cotações de criptomoedas, através do nome da cripto(chain) e do endereço de contrato(address), que podem ser obtidos no site da Coingecko e da EtherScan, e salva essas cotações no banco de dados.

Para distribuição e agendamento das tarefas é usado o Celery e o Celery Beat, integrados com o Django, e o RabbitMQ como broker de mensagens. 

O agendamento pode ser feito através do Django Admin, e caso não seja usado, as tarefas podem ser executadas através do Django Shell ou usando a API feita em DRF.

Para instalar as dependências necessárias para usar o projeto, execute: 

```bash
pip install -r./requirements.txt
```

Para executar o projeto use: 

```bash
python manage.py runserver
```

Para executar o RabbitMQ use: 

```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
```

Para executar o Celery sem agendamento de tarefas use: 

```bash
celery -A core worker -l INFO.
```

Para executar o Celery com agendamento de tarefas(Celery Beat) use: 

```bash
celery -A core beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler.
```

## Uso com Docker

### Requisitos 

- Docker 
- Docker Compose

### Construir e iniciar os containers

```bash
docker-compose up --build
```

A aplicação estará disponível em http://127.0.0.1:8000/.

### Executando comandos no container

```bash
docker-compose exec cryptos-container <comando>
```

#### Exemplo de comando: aplicar as migrações no container

```bash
docker-compose exec cryptos-container python manage.py migrate
```
