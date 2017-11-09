# Blog Django

Desenvolvido para exemplo da palestra.

Baseado no tutorial Django Girls.

## Instalando e rodando
```
$ git clone https://github.com/PyladiesCaxias/blog-django.git
```
Entre na pasta do repositório e crie um ambiente virtual (virtualenv). Se você não sabe como criar uma virtualenv, é altamente recomendado que leia o [tutorial DjangoGirls](http://tutorial.djangogirls.org/pt/django_installation/). Ative a virtualenv.

```
$ virtualenv -p python3 venv
$ source venv/bin/activate
```

Criando um virtualenv:
```
cd <repo-path>
virtualenv -p python3 venv
```


Ativando o ambiente (**sempre** faça isto antes de qualquer ação):  
```
cd <repo-path>
source venv/bin/activate
```

Instalando as dependências do projeto:  
```
cd <repo-path>
source venv/bin/activate
pip install -r requirements.txt
```

## Executando o projeto local

```
python manage.py migrate
python manage.py runserver

```
