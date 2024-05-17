# CRIAR AMBIENTE VIRTUAL
# python -m venv venv

# ATIVAR PROJETO
# .\venv\Scripts\activate

# INSTALAR DJANGO
# pip install django

# CRIAR PROJETO DJANGO
# django-admin startproject nome_do_projeto . (DETELHE NO PROJECT . - CRIA PASTA DO PROJETO NA RAIZ DELE)

# RODAR SERVIDOR
# python .\manage.py runserver

# CRIAR NOVO APP
# python manage.py startapp nome_da_aplicacao
# vai criar uma pasta com o nome da aplicacao e configuracoes essenciais
# Colocar as views dentro do arquivo views.py

# ROOT > NOME_DO_PROJETO > urls.py
# onde devem ser colocadas as urls
# detalhe em colocar a / depois do nome
# urlpatterns = [
#     path('', home_view.home),       ### detalhe em colocar vazio para página home
#     path('blog/', blog_view.blog), # detalhe
#     path('admin/', admin.site.urls),
# ]

# CRIAR VÁRIOS NÍVEIS DE CAMINHOS
# Criar um arquivos urls.py dentro de cada app
# na url da raiz importar include de django.urls
# importar a view para dentro do urls.py
# from django.urls import include, path
# urlpatterns = [
#     path('', include('home.urls')),       ### detalhe em colocar vazio para página home
#     path('blog/', include('blog.urls')), # detalhe
#     path('admin/', admin.site.urls),
# ]
