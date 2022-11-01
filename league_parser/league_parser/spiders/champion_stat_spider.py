import scrapy 

CHAMPIONS_STAT_WORLDS = "https://lol.fandom.com/wiki/Special:RunQuery/TournamentStatistics?TS%5Bpreload%5D=TournamentByChampion&TS%5Btournament%5D=2022+Season+World+Championship%2FMain+Event%2C+2022+Season+World+Championship%2FPlay-in&TS%5Blink%5D=&TS%5Bchampion%5D=&TS%5Brole%5D=&TS%5Bteam%5D=&TS%5Bpatch%5D=&TS%5Byear%5D=&TS%5Bregion%5D=&TS%5Btournamentlevel%5D=&TS%5Bwhere%5D=&TS%5Bincludelink%5D%5Bis_checkbox%5D=true&TS%5Bshownet%5D%5Bis_checkbox%5D=true&_run=&pfRunQueryFormName=TournamentStatistics&wpRunQuery=&pf_free_text="

class ChampionStatSpider(scrapy.Spider):
    name = "champion_stat"

    def start_requests(self):
        url = CHAMPIONS_STAT_WORLDS

        yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        print("Hello World")