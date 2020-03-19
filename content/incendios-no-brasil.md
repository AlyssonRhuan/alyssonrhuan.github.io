Title: Incêndios no Brasil
Date: 2020-03-19
Modified: 2010-12-05 19:30
Category: Análise
Tags: Análise, Artigo
Slug: Analise
Authors: Alysson Rhuan

# Indicadores de incendio em florestas do Brasil

Percebemos recentemente um crescente número de focos de incendio em florestas brasileiras, e devido a este assunto, vamos analisar o que as estatísticas conseguem nos dizer sobre isso.

A seguir iremos responder as seguinte questões:

1. Quais são os meses com maior incidência de focos de incêndio.
2. Qual foi o número de incêndios por estado.
3. Qual é o número de incêndios relatado ao longo dos anos.
4. Qual é a tendência de crescimento.

Neste dataset temos dados desde 1998 até 2017, onde cada registro indica o ano do foco de incendio reportado, o estado, o mês e o número de incêndios florestais relatados.

## Quais são os meses com maior incidência de focos de incêndio

```python
df.groupby(['month']).sum()['number']
```

Primeiramente agrupando os registros por meses e somando a quantidade de focos de incêncios reportados, chegamos ao seguinte gráfico.

<figure class="wp-block-image size-large"><img src="https://galaxiadadoshome.files.wordpress.com/2020/03/image.png?w=912" alt="" class="wp-image-41"/></figure>

Percebemos que os meses mais secos, onde no Brasil temos um menor indice de chuvas, é onde se concentra mais os focos de incêncio. Outro indicador, é que nos meses mais frios é onde há muitas fogueiras afim de aumentar o calor.

## Qual foi o número de incêndios por estado.

Agora agrupando os dados por estado, e somando os registros reportados.

```python
df.groupby(['state']).sum()['number']
```

Temos o seguinte gráfico ordenado pela quantidade:

<figure class="wp-block-image size-large"><img src="https://galaxiadadoshome.files.wordpress.com/2020/03/image-1.png?w=912" alt="" class="wp-image-47"/></figure>

Percebemos que São Paulo, o estado brasileiro mais populoso, com 12,18 milhões segundo o IBGE (2018), lidera o ranking de focos de incêndios em florestas reportados. Podemos ver tambem que os estados com vegetação seca ficam localizados em sua maioria, na primeira metade dos registros.

Analisando estes dados no mapa do Brasil, temos:

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

Notebook no Kaggle<br><a href="https://www.kaggle.com/alyssonrhuan/forest-fires-in-brazil">https://www.kaggle.com/alyssonrhuan/forest-fires-in-brazil</a>'<br>Datasets<br><a href="https://www.kaggle.com/gustavomodelli/forest-fires-in-brazil">https://www.kaggle.com/gustavomodelli/forest-fires-in-brazil</a><br><a href="https://www.kaggle.com/lukebm/forest-fires-in-brazil-adjusted">https://www.kaggle.com/lukebm/forest-fires-in-brazil-adjusted</a>
