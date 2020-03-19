Title: Incendios no Brasil
Date: 2010-12-03 10:20
Category: Analise

Indicadores de incendio em florestas do Brasil

<!-- wp:paragraph -->
<p>Percebemos recentemente um crescente número de focos de incendio em florestas brasileiras, e devido a este assunto, vamos analisar o que as estatísticas conseguem nos dizer sobre isso.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A seguir iremos responder as seguinte questões:</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol><li>Quais são os meses com maior incidência de focos de incêndio.</li><li>Qual foi o número de incêndios por estado.</li><li>Qual é o número de incêndios relatado ao longo dos anos.</li><li>Qual é a tendência de crescimento.</li></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Neste dataset temos dados desde 1998 até 2017, onde cada registro indica o ano do foco de incendio reportado, o estado, o mês e o número de incêndios florestais relatados.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Quais são os meses com maior incidência de focos de incêndio.</h2>
<!-- /wp:heading -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted">df.groupby(['month']).sum()['number']</pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p>Primeiramente agrupando os registros por meses e somando a quantidade de focos de incêncios reportados, chegamos ao seguinte gráfico.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":41,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://galaxiadadoshome.files.wordpress.com/2020/03/image.png?w=912" alt="" class="wp-image-41"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Percebemos que os meses mais secos, onde no Brasil temos um menor indice de chuvas, é onde se concentra mais os focos de incêncio. Outro indicador, é que nos meses mais frios é onde há muitas fogueiras afim de aumentar o calor.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Qual foi o número de incêndios por estado.</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Agora agrupando os dados por estado, e somando os registros reportados.</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted">df.groupby(['state']).sum()['number']</pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p>Temos o seguinte gráfico ordenado pela quantidade:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":47,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://galaxiadadoshome.files.wordpress.com/2020/03/image-1.png?w=912" alt="" class="wp-image-47"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Percebemos que São Paulo, o estado brasileiro mais populoso, com 12,18 milhões segundo o IBGE (2018), lidera o ranking de focos de incêndios em florestas reportados. Podemos ver tambem que os estados com vegetação seca ficam localizados em sua maioria, na primeira metade dos registros.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Analisando estes dados no mapa do Brasil, temos:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":48,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://galaxiadadoshome.files.wordpress.com/2020/03/image-2.png?w=575" alt="" class="wp-image-48"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Qual é o número de incêndios relatado ao longo dos anos.</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Agrupando os indicadores pelos anos</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted">df.groupby(['year']).sum()['number']</pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p>Poderemos visualizar graficamente a variação ao longo deste período:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":49,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://galaxiadadoshome.files.wordpress.com/2020/03/image-3.png?w=912" alt="" class="wp-image-49"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Percebe-se que em 2003 tivemos o nosso pico de indicadores de incêndio, e recentemente em 2016 quase aproximamos a este pico novamente.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Qual é a tendência de crescimento.</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":50,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://galaxiadadoshome.files.wordpress.com/2020/03/image-4.png?w=912" alt="" class="wp-image-50"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":51,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://galaxiadadoshome.files.wordpress.com/2020/03/image-5.png?w=912" alt="" class="wp-image-51"/></figure>
<!-- /wp:image -->

<!-- wp:separator -->
<hr class="wp-block-separator"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p>Notebook no Kaggle<br><a href="https://www.kaggle.com/alyssonrhuan/forest-fires-in-brazil">https://www.kaggle.com/alyssonrhuan/forest-fires-in-brazil</a>'<br>Datasets<br><a href="https://www.kaggle.com/gustavomodelli/forest-fires-in-brazil">https://www.kaggle.com/gustavomodelli/forest-fires-in-brazil</a><br><a href="https://www.kaggle.com/lukebm/forest-fires-in-brazil-adjusted">https://www.kaggle.com/lukebm/forest-fires-in-brazil-adjusted</a></p>
<!-- /wp:paragraph -->