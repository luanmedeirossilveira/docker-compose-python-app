# Exemplo de Aplicação Docker Compose

Exemplo de Aplicação Docker Compose com Flask. A intenção desta aplicação é mostrar um exemplo de como utilizar o Docker Compose para criar e gerenciar containers Docker para uma aplicação Flask.

## Instalação

1. Certifique-se de ter o Docker instalado em seu sistema.

2. Certifique-se de ter o Docker Compose instalado em seu sistema.

## Configuração

1. Execute o arquivo `docker-compose.yml` com o seguinte comando:

```bash
docker compose up --build
```

2. Execute o seguinte comando para acessar a aplicação:

```bash
docker-compose exec web flask run --host=0.0.0.0
```
