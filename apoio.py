###########################################################################################################################################################################
### Comandos

# inicia projeto simples
django-admin startproject projectAlpha

#  inica projeto com template
django-admin startproject --template=https://github.com/Mischback/django-project-skeleton/archive/development.zip projectBeta

# executa server no localhost
python manage.py runserver  

# cria aplicação
python manage.py startapp personal

# executar construir migração
python manage.py makemigrations

# executar migração
python manage.py migrate

# ajuda
python manage.py help

# executa server no IP
python manage.py runserver 192.168.0.115:8000 

###########################################################################################################################################################################
### Alterações

# incluir no settings.py pra acesso remoto
ALLOWED_HOSTS = ['192.168.0.115', 'localhost']