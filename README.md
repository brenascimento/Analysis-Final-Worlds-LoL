# Projeto - Análise e Extração de Dados - Mundial de League of Legends 2022

<em>A melhor forma de aprender e adquirir experiência é fazendo um projeto de assuntos que gostamos, e para mim `eSports` e `League of Legends` é um dos que mais gosto. </em>

## O que é League of Legends?
<img src="https://elchapuzasinformatico.com/wp-content/uploads/2021/11/League-of-Legends.jpeg">
League of Legends é um MOBA 5v5, onde 5 jogadores jogam em equipe contra outra equipe de 5 jogadores em que o objetivo das duas equipes é destruir o <em>Nexus inimigo</em>(coração da partida). Para chegar ao Nexus cada jogador tentará: 

* Vencer o jogador inimigo(eliminando-o) e o deixando cada vez mais fraco(fazendo-o perder experiência e ouro)
* Destruir as torres que protegem a base inimiga

A base de uma partida de <em>LoL</em> é ouro e experiência:
* Ouro - faz com que o jogador possa comprar itens e ficar cada vez mais forte
* Experiência - Sobe de nível do personagem, aumentando a força das habilidades e outros atributos do personagem

Com a falta desses componentes é bem provável que o jogador seja eliminado mais vezes e por fim perdendo a partida.

Para conseguir ouro e experiência dentro de uma partida de LoL é necessário:
* <em>Farmar</em> - ato de ganhar ouro e experiência por meio de minions que andam pelo jogo
* Eliminar monstros épicos - Dragão e Barão - Dois monstros que dão mais poder de forças dentro de jogo(seja velocidade de movimento, poder de ataque, durabilidade, maior regeneração de vida). 

É um jogo que tem conquistado o coração de muitos fãs e vem crescendo a cada ano devido a liberdade de que se tem para criar jogadas e estratégias.

## O que é então o Mundial de League of Legends?

<img src="https://s2.glbimg.com/sB_5iWkN7LJUJjb_6H9m8gw_7-o=/0x0:1600x900/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_bc8228b6673f488aa253bbcb03c80ec5/internal_photos/bs/2022/V/v/hbqVgQQEmskuhAglnXgA/worlds-2022-thumb.jpg" />

O Mundial de League of Legends é um dos maiores eventos(se não o maior) e campeonato de eSports do mundo. 

O evento ocorre sempre no final do ano, agrupando os melhores times de cada região, as maiores e principais sendo China, Coréia do Sul, Europa, Vietnam, Taiwan e Estados Unidos(também conhecidos como Majors). 

É no Mundial que ocorre as melhores partidas, as melhores batalhas, e as melhores viradas. Lá também é onde os players fãs do eSport aprendem novas estratégias, novas mecânicas, novas maneiras de fazer as coisas acontecerem. Todos os times lutam pela taça.

Nesse Mundial, o time da `DRX` levou a melhor contra o time da `T1`. Mas nesse Mundial, como foi a performance de cada jogador? quais foram os personagens que mais trouxeram vitórias para os times? 

É com essa e algumas perguntas que irei extrair, limpar e analisar os dados de `partidas por jogadores` e `partida por campeões` e apresenta-la em um Dashboard utilizando POWER BI

## Sobre o projeto

Nesse projeto vou analisar usando dados extraídos do site: `lol.fandom.com`(conhecido como leaguepedia) utilizando a ferramenta Scrapy. Também fiz o requerimento de dados utilizando o modelo de Diagrama Entidade-Relacionamento no LucidChart - Pois facilita na hora de saber quais dados extrair. 

<img src="imagens/diagram_data_requirements_worlds_2022.jpeg" width="550" alt="Requerimento de dados"/><br>
<em>Diagrama de Entidade-Relacionamento(Work in Progress)</em>

Fiz as extrações de dados e populei em um Banco de Dados SQL Server utilizando o `pyodbc`, também fiz mudanças em:
* `items.py` - criar os meus modelos de dados para uso no <em>items pipelines</em>
* `pipelines.py` - um pipeline de dados para popular o banco de dados
* `settings.py` - ativação do `ITEM_PIPELINES`

## Dicionario de Dados
 - <h3>Teams</h3>
<table>
    <tr>
        <th>Coluna</th>
        <th>Descrição</th>
    <tr>
    <tr>
        <td>ID_Team</td>
        <td>Id de cada time especifícado no Banco de Dados</td>
    </tr>
    <tr>
        <td>team_name</td>
        <td>Nome da equipe participante do Worlds 2022(Main Event)</td>
    </tr>
    <tr>
        <td>image_link</td>
        <td>Link para a imagem do brasão do time</td>
    </tr>
</table>

 - <h3>Player</h3>
<table>
    <tr>
        <th>Coluna</th>
        <th>Descrição</th>
    <tr>
    <tr>
        <td>ID_Player</td>
        <td>Id de cada player especifícado no Banco de Dados</td>
    </tr>
    <tr>
        <td>player_name</td>
        <td>Nome(<em>nickname</em>) de cada time participante do Worlds 2022</td>
    </tr>
    <tr>
        <td>player_role</td>
        <td>Posição do jogador em seu time</td>
    </tr>
</table>



## Libs/Tools
* Scrapy
* BeautifulSoup
* Pandas
* Power BI
* pyodbc
* SQL Server Management System









