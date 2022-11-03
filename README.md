# Projeto Análise de Dados - Análise Final Mundial de League of Legends 2022

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

A <b>final</b> do Mundial 2022 já chegou(sábado - 05/11) e quem disputará a taça será os dois times sul-coreanos `T1` e `DRX`

<img src="https://noticias.maisesports.com.br/wp-content/uploads/2021/12/t1-line-up-lck-2022.jpeg" width=500>

A T1 é conhecida por ser o time do `Faker` que é um <em>pro-player</em> experiente, já ganhou alguns outros mundiais, e mesmo com a idade de 26 continua na ativa (pois é bem comum que os <em>pro-players</em> de <em>LoL</em> se aposentarem depois dos 24 anos). Mas além do Faker a T1 também contém outros ótimos talentos: `Zeus`, `Oner`, `Gumayusi` e `Keria` e como reserva `Asper`, e é a favorita para ganhar esse mundial.

<img src="https://pbs.twimg.com/media/FdAPU1faAAAusq6.jpg:large" width=500>

A DRX foi um time que regionalmente não desempenhou muito bem, porém mostrou seu valor no Mundial, sendo o primeiro time de fase de entrada (que jogou contra regiões menores) a chegar na Final do Mundial. Depois de uma virada épica nas Quartas de Finais, e depois derrotando a gigante `GenG`(outro time sul-coreano), ela finalmente chegou na final. Ela conta com um elenco de: `Kingen`, `Pyosik`, `Zeka`, `Deft`, `BeryL` e como reservas `Juhan` e `Taeyoon`. sendo `Deft` e `BeryL` dois jogadores experientes, e tendo dois outros talentos: `Pyosik` e `Zeka`. Mesmo assim terá um caminho difícil para vencer a T1 que vem muito forte.

Essa última partida será no formato de Melhor de 5 (MD5) em que o primeiro time a ter 3 vitórias, leva a taça.

## Sobre o projeto

Nesse projeto vou analisar usando dados extraídos do site: `lol.fandom.com`(conhecido como leaguepedia)

### Datasets
* `match_history_teams.csv` - dataset contendo as partidas de ambos os times no decorrer do Mundial 2022
* `league_parser/champion_stats.csv` - dataset contendo os dados dos campeões/personagens jogados ao decorrer do Mundial 2022


## Hipóteses
1. É mais provável a T1 ganhar essa final em um jogo melhor de 5 da DRX?

## Ideias
1. Quais campeões/personagens com a maior probabilidade de vencer contra a T1?
2. Quais campeões/personagens com a maior probabilidade de vencer a DRX?
3. Quais campeões/personagens provavelmente será escolhido pela T1?
4. Quais campeões/personagens provavelmente será escolhido pela DRX?

## Libs/Tools
* Scrapy
* BeautifulSoup
* Pandas
* Power BI









