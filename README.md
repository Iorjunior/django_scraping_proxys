<div align="center">
    <h1>Django Scraping Proxys</h1>
    <i>🔗 CRUD em Django + Scraping do Freeproxys</i>
</div>
<br/>

<div align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-%5E3.8-green" />
  <img alt="Framework" src="https://img.shields.io/badge/Framework-Django-blue" />
</div>
<br/>


---

### :earth_americas: Acessar o projeto

O projeto esta rodando no Heroku, [Acesse]() 

para habilitar a parte de edição, use as seguintes credencias: 
<br/>
username:`visitante`
<br/>
password:`visi1234`

---

### :electric_plug: Como rodar localmente

Clone o repositorio:

```sh
 git clone https://github.com/iorjunior/github_trending_api.git
```

Abra a pasta, e instale as dependencias:

```sh
 pip install requirements.txt
 or
 poetry install
```

Entre no diretorio `/django_proxys` e rode:

```sh
  cd django_proxy
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
```
Volte ao diretorio Raiz e Execute o script de Scraping

```sh
 cd .. 
 python ./scraping/scrap.py
```
Agora inicie o Servidor do django

```sh
 cd django_proxy 
 python manage.py runserver
```

✅ Servidor iniciado go to `localhost:8000` 🎊 🎉.

---

### :blue_book: Documentação

Existem 7 endpoints na aplicação:

| Endpoints             | Retorno                                   |  |
| --------------------- | ----------------------------------------- | -|
| /                     | Lista as Proxys                           |  |
| /proxys/cadastrar     | Cadastro de novas Proxys|   login required|
| /proxys/editar/[id]   | Editar Proxys Existentes | login required|
| /proxys/deletar/[id]  | Deletar uma Proxy| login required|
| /entrar               | Logar na aplicação | 
| /sair                 | Deslogar da aplicação |
| /admin                | Entrar no admin do Django |




---

### 📂 Sobre

Projeto feito com base em um desafio tecnico. 
