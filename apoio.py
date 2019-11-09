###########################################################################################################################################################################
### Comandos

# inicia projeto simples
django-admin startproject projectAlpha

#  inica projeto com template
django-admin startproject --template=https://github.com/Mischback/django-project-skeleton/archive/development.zip projectBeta

# executa server no localhost
python manage.py runserver

# cria aplicação
python manage.py startapp blog

# executar construir migração
python manage.py makemigrations

# executar migração
python manage.py migrate

# ajuda
python manage.py help

# executa server no IP
python manage.py runserver 192.168.0.115:8000

# exibe sql do modelo
python manage.py sqlmigrate blog 0001

###########################################################################################################################################################################
### Alterações

# incluir no settings.py pra acesso remoto
ALLOWED_HOSTS = ['192.168.0.115', 'localhost']


###########################################################################################################################################################################
### git

echo "# ambiente_teste" >> README.md
  git init
  git add README.md
  git commit -m "first commit"
  git remote add origin https://github.com/vinibfr/ambiente_teste.git
  git push -u origin master

  git remote add origin https://github.com/vinibfr/ambiente_teste.git
  git push -u origin master
  https://rogerdudler.github.io/git-guide/index.pt_BR.html
###########################################################################################################################################################################
### outros
  https://docs.djangoproject.com/en/1.11/

# restart server
  sudo systemctl restart uwsgi
