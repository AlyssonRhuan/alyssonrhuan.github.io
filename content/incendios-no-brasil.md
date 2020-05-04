Title: Incêndios no Brasil
Date: 2020-03-19 10:00
Modified: 2020-03-19 12:00
Category: Análise
Tags: Análise, Artigo
Slug: incendios_no_brasil
Authors: Alysson,

# Indicadores de incêndios em florestas do Brasil

Percebemos recentemente um crescente número de focos de incendio em florestas brasileiras, e devido a este assunto, vamos analisar o que as estatísticas conseguem nos dizer sobre isso. 

A seguir iremos responder as seguinte questões:

1. Quais são os meses com maior incidência de focos de incêndio.
2. Qual foi o número de incêndios por estado.
3. Qual é o número de incêndios relatado ao longo dos anos.
4. Qual é a tendência de crescimento.

Neste dataset temos dados desde 1998 até 2017, onde cada registro indica o ano do foco de incendio reportado, o estado, o mês e o número de incêndios florestais relatados.

## Quais são os meses com maior incidência de focos de incêndio

Primeiramente, iremos agrupar os registros por meses e somar a quantidade de focos de incêncios reportados:

```python
df.groupby(['month']).sum()['number']
```

E com estes dados, chegamos ao seguinte gráfico, denominado Total de queimadas reportadas no Brasil de 1998 até 2017 por meses:

<figure class="wp-block-image size-large"><img src="https://galaxiadadoshome.files.wordpress.com/2020/03/image.png?w=912" alt="" class="wp-image-41"/></figure>

Percebe-se que o menor indice de focos de incêncios reportados foram em Abril, onde o número gira em torno de 28.188, chegando até Julho, com aproximadamente 92.326 casos reportados.

Os meses onde o clima é mais seco, ou seja, no inverno, é quando no Brasil temos um menor indice de chuvas, é quando se concentra a maior quantidade de focos de incêncio. Por ser uma época mais fria, é onde se concentra o maior número de fogueiras, sendo está um dos principais motivos do início de queimadas.

## Qual foi o número de incêndios por estado.

Agora agrupando os dados por estado, e somando os registros reportados:

```python
df.groupby(['state']).sum()['number']
```

Temos o seguinte gráfico, quantidade de focos por estado, ordenado pela quantidade:

<figure class="wp-block-image size-large"><img src="https://galaxiadadoshome.files.wordpress.com/2020/03/image-1.png?w=912" alt="" class="wp-image-47"/></figure>

Percebemos que São Paulo, o estado brasileiro mais populoso, com 12,18 milhões segundo o IBGE (2018), lidera o ranking de focos de incêndios em florestas reportados. É nesta região onde fica a Mata Atlântica, uma importante floresta brasileira. 
Podemos ver tambem que os estados com vegetação seca ficam localizados em sua maioria, na primeira metade dos registros. Analisando estes dados no mapa do Brasil, temos:

<figure class="wp-block-image size-large"><img src="https://galaxiadadoshome.files.wordpress.com/2020/03/image-2.png?w=575" alt="" class="wp-image-48"/></figure>

## Qual é o número de incêndios relatado ao longo dos anos.

Agrupando os indicadores pelos anos

```python
df.groupby(['year']).sum()['number']
```

Poderemos visualizar graficamente a variação ao longo deste período:

<figure class="wp-block-image size-large"><img src="https://galaxiadadoshome.files.wordpress.com/2020/03/image-3.png?w=912" alt="" class="wp-image-49"/></figure>

Percebe-se que em 2003 tivemos o nosso pico de indicadores de incêndio, e recentemente em 2016 quase aproximamos a este pico novamente.

## Qual é a tendência de crescimento.

<figure class="wp-block-image size-large"><img src="https://galaxiadadoshome.files.wordpress.com/2020/03/image-4.png?w=912" alt="" class="wp-image-50"/></figure>

<figure class="wp-block-image size-large"><img src="https://galaxiadadoshome.files.wordpress.com/2020/03/image-5.png?w=912" alt="" class="wp-image-51"/></figure>

Fontes:

[Notebook no Kaggle por Alysson](https://www.kaggle.com/alyssonrhuan/forest-fires-in-brazil){:target="_blank"}

[Dataset original por Luís Gustavo Modelli](https://www.kaggle.com/gustavomodelli/forest-fires-in-brazil){:target="_blank"}

[Dataset ajustado por Lucas Benevenuto](https://www.kaggle.com/lukebm/forest-fires-in-brazil-adjusted){:target="_blank"}
