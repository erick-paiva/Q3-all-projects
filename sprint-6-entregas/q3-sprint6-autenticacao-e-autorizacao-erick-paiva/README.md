<p align="center">
<img src="https://emoji.slack-edge.com/TQZR39SET/kenzie/6b5310a5161dc157.png" width="200px" >
</p>
# Entrega Autenticação e Autorização

## Introdução

A api tem um total de **“2”** Endpoints

**O url base da API:**

[https://entrega-vacina.herokuapp.com](https://entrega-vacina.herokuapp.com)

## **Endpoints**

- Registrar um vacina ⇒ “/vaccinations
- Pegar todas as vacinas ⇒ “/vaccinations"

## EndPoint ⇒ Registrar uma vacina

`POST /vaccinations - FORMATO DA REQUISIÇÃO - STATUS 201`

Endpoint para cadastrar uma vacina.

```json
{
  "cpf": "12345678912",
  "name": "John Doe",
  "vaccine_name": "Pfizer",
  "health_unit_name": "Santa Rita"
}
```

Caso dê tudo certo, a resposta será assim:

```json
{
  "cpf": "12345678912",
  "first_shot_date": "Mon, 25 Apr 2022 19:46:31 GMT",
  "health_unit_name": "Santa Rita",
  "name": "John Doe",
  "second_shot_date": "Sun, 24 Jul 2022 19:46:31 GMT",
  "vaccine_name": "Pfizer"
}
```

## Possíveis erros

`POST /vaccinations FORMATO DA RESPOSTA - STATUS 409`

Caso você mandar um cpf que já está cadastrado, a resposta será assim:

`"cpf ja foi cadastrado"`

cpf ja cadastrado:

```json
{
  "error": "cpf ja foi cadastrado"
}
```

## EndPoint Obter todas as vacinas

`GET /vaccinations - FORMATO DA REQUISIÇÃO - STATUS 200`

Caso dê tudo certo, a resposta será assim:

```json
[
  {
    "cpf": "12345678912",
    "first_shot_date": "Fri, 22 Apr 2022 20:30:15 GMT",
    "health_unit_name": "Santa Rita",
    "name": "John Doe",
    "second_shot_date": "Thu, 21 Jul 2022 20:30:15 GMT",
    "vaccine_name": "Pfizer"
  }
]
```

by Erick Paiva 🕵🏽‍♀️
