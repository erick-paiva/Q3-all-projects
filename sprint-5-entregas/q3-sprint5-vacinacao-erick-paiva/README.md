<p align="center">
<img src="https://emoji.slack-edge.com/TQZR39SET/kenzie/6b5310a5161dc157.png" />
</p>
# Entrega Vacinação

## Introdução

A api tem um total de **“2”** Endpoints

**O url base da API:**

[https://entrega-vacina.herokuapp.com](https://entrega-vacina.herokuapp.com)

## **Endpoints**

- Adcionar vacina ⇒ “/vaccinations”
- Pegar todas as vacinas ⇒ “/vaccinations”

## EndPoint ⇒ Adcionar vacina

`POST /vaccinations - FORMATO DA REQUISIÇÃO - 200`

Endpoint para cadastrar uma vacina na api.

```json
{
  "cpf": "12345678912",
  "name": "Jhon doe",
  "vaccine_name": "Pfizer",
  "health_unit_name": "Santa Rita"
}
```

Caso dê tudo certo, a resposta será assim:

```json
{
  "cpf": "12345678912",
  "first_shot_date": "Fri, 22 Apr 2022 20:30:15 GMT",
  "health_unit_name": "Santa Rita",
  "name": "Jhon doe",
  "second_shot_date": "Thu, 21 Jul 2022 20:30:15 GMT",
  "vaccine_name": "Pfizer"
}
```

## Possíveis erros

`POST /vaccinations FORMATO DA RESPOSTA - STATUS 400`

Caso você esqueça de passar as chaves necessárias a reposta do erro será assim: No exemplo a requisição foi feita faltando o name, vaccine_name e o health_unit_name.

`"Você deve passar todas as chaves"`

```json
{
  "error": "Você deve passar todas as chaves !"
}
```

`POST /vaccinations FORMATO DA RESPOSTA - STATUS 409`

Caso você passar um cpf que ja esta em uso.

`"CPF já cadastrado"`

```json
{
  "error": "cpf ja foi cadastrado"
}
```

## EndPoint => Pegar todas as vacinas

`GET /vaccinations - FORMATO DA RESPOSTA - STATUS 200`

EndPoint para para obter todas as pessoas vacinadas no banco de dados.

Caso dê tudo certo, a resposta será assim:

```json
[
  {
    "cpf": "12345678912",
    "first_shot_date": "Fri, 22 Apr 2022 20:30:15 GMT",
    "health_unit_name": "Santa Rita",
    "name": "Jhon doe",
    "second_shot_date": "Thu, 21 Jul 2022 20:30:15 GMT",
    "vaccine_name": "Pfizer"
  }
]
```

by Erick Paiva 🕵🏽‍♀️
