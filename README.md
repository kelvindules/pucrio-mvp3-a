# pucrio-mvp3-a

Este é um projeto básico (MVP) para estudo e avaliação da disciplina **Arquitetura de Software**.

O projeto é o componente A da solução, contendo a parte endpoints que podem funcionar como BFF e integração com serviço externo para obter tokens de autorização com base em usuário e senha.

O serviço externo utilizado é a api [Platzi Fake Store API](https://fakeapi.platzi.com/en/rest/auth-jwt) e não demanda de cadastro.

## Rodando o projeto

### Instale o Docker

```bash
sudo apt install docker-ce
```

Caso a instalação não seja concluída com sucesso, siga [esses passos](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04) para pré-configurar seu ambiente.

### Construa a imagem

```bash
docker build --tag mvp3-a .
```

### Suba seu container

```bash
docker run -d -p 5000:5000 mvp3-a
```
