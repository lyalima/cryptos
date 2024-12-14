# Distribuição e agendamento de tarefas de cotação de criptomoedas com Python, Django/DRF, Celery e RabbitMQ.

O projeto usa a API do site DefiLlama para pegar as cotações de criptomoedas, através do nome da cripto(chain) e do endereço de contrato(address), que podem ser obtidos no site da Coingecko e da EtherScan, e salva essas cotações no banco de dados.

Para distribuição e agendamento das tarefas é usado o Celery e o Celery Beat, integrados com o Django, e o RabbitMQ como broker de mensagens. 

O agendamento pode ser feito através do Django Admin, e caso não seja usado, as tarefas podem ser executadas através do Django Shell ou usando a API feita em DRF.

Para instalar as dependências necessárias para usar o projeto, execute: pip install -r./requirements.txt.

Para executar o projeto use: python manage.py runserver.

Para executar o RabbitMQ use: docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management.

Para executar o Celery sem agendamento de tarefas use: celery -A core worker -l INFO.

Para executar o Celery com agendamento de tarefas(Celery Beat) use: celery -A core beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler.

