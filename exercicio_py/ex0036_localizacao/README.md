# Sobre o uso da API

- Foi feito o registro no site [AccuWeather](https://developer.accuweather.com/) para conseguir uma chave da API seguindo os passos abaixo:

Após o registro ir em **MY APPS**

![my apps](img/ex0036-0.png)

Adicione uma nova aplicação e preencha as informações requisitadas. Em seguida, clique no nome da sua aplicação para pegar a chave da API.

![detalhes da app](img/ex0036-1.png)

![chave da api](img/ex0036-2.png)

----

## Pegando o código do local

Agora vá em **API PREFERENCE** e em **LOCATIONS API**.

![preferências da api](img/ex0036-3.png)

Vá em **Geoposition Search**

![api de localização](img/ex0036-4.png)

Preencha os parâmetros como a chave da API, longitude e latitude, e linguagem

![parâmetros da api](img/ex0036-5.png)

E clique no botão para enviar a requisição. Se estiver tudo funcionando, ele retornará 200.

![resposta da requisição](img/ex0036-6.png)

Vá até a **aba cURL** e pegar a url que está entre aspas.

![url](img/ex0036-7.png)

Essa url será usada no código com as devidas modificações.
