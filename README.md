# Auth JWT com Flask

Esse projeto é uma API REST com autenticação JWT, onde foi utilizado principalmente **Python**.

## Técnologias

- Python
- Flask
- Flask SQLAlchemy
- Postgres
- PyJWT
- Marshmallow

## Instalando e rodando o projeto

Para rodar o projeto é bem simples, basta ter o Python instalado e seguir as instruções a seguir. Utilizei a versão 3.9.6, mas acredito que qualquer versão 3 funcione da mesma forma.

<br>
Primeiro precisamos clonar o projeto do github executando o seguinte comando:

```sh
$ git clone https://github.com/jaovito/flask-auth.git
```

Após isso você precisa abrir a pasta clonada em seu terminal:

```sh
$ cd flask-auth
```

Com o repositório criado você precisa instalar as bibliotecas necessárias do projeto, todas estão no arquivo **requirements.txt**, para baixar todas basta dar o seguinte comando com o **pip**:

```sh
$ pip install -r requirements.txt
```

Antes de rodar o projeto você deve renomear o arquivo config.example.py para config.py e adicionar a url do seu banco de dados. Com isso seu projeto já está configurado, basta usar o comando abaixo e sair usando a API.

```sh
$ python run.py
```

Com isso a aplicação será executada na porta **3333**.


## Rotas

A aplicação possúi apenas 2 endpoints, um que é o **/auth** e o outro é o **/users**, a rota **/users** pode se realizar um CRUD completo, com GET, POST, PUT e DELETE, já a rota **/auth** é somente POST.


### Listar usuários (/users) [GET]

Nesta rota podemos listar todos usuários da aplicação. Basta dar um GET simples e receberá uma resposta como:

```json
{
  "data": [
    {
      "created_on": "2021-07-30T09:44:31.816348",
      "email": "aw",
      "id": 5,
      "name": "aw@gmail.com",
      "password": "pbkdf2:sha256:260000$DoRrVb5k1rqZReNG$3c291a79a67f260aa0fc62d0332e0b55634e21410c2a2a4cca33a6e70c05af22",
      "username": "aw"
    },
    ...
  ],
  "message": "successfully fetched"
}
```

### Cadastrar um usuários (/users) [POST]

Nesta rota é possível cadastrar um usuário, basta enviar ao corpo da requisição os seguintes dados (em json):

- name (string)
- username (string)
- email (string)
- password (string)


### Deletar/alterar um usuários (/users/:id) [DELETE/PUT]

Este endpoint deleta ou altera um usuário, dependendo do método HTTP utilizado.