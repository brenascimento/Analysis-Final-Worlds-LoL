import scrapy 
from bs4 import BeautifulSoup

DRX_MATCHES_WORLDS = "https://lol.fandom.com/wiki/Special:RunQuery/MatchHistoryGame?MHG%5Bpreload%5D=Tournament&MHG%5Btournament%5D=2022+Season+World+Championship%2FPlay-In%2C+2022+Season+World+Championship%2FMain+Event&MHG%5Bteam%5D=DRX&MHG%5Bteam1%5D=&MHG%5Bteam2%5D=&MHG%5Bban%5D=&MHG%5Brecord%5D=&MHG%5Bascending%5D%5Bis_checkbox%5D=true&MHG%5Bascending%5D%5Bvalue%5D=&MHG%5Blimit%5D=&MHG%5Boffset%5D=&MHG%5Bregion%5D=&MHG%5Byear%5D=&MHG%5Bstartdate%5D=&MHG%5Benddate%5D=&MHG%5Bwhere%5D=&MHG%5Btextonly%5D%5Bis_checkbox%5D=true&_run=&pfRunQueryFormName=MatchHistoryGame&wpRunQuery=&pf_free_text="
T1_MATCHES_WORLDS = "https://lol.fandom.com/wiki/Special:RunQuery/MatchHistoryGame?MHG%5Bpreload%5D=Tournament&MHG%5Btournament%5D=2022+Season+World+Championship%2FPlay-In%2C+2022+Season+World+Championship%2FMain+Event&MHG%5Bteam%5D=T1&MHG%5Bteam1%5D=&MHG%5Bteam2%5D=&MHG%5Bban%5D=&MHG%5Brecord%5D=&MHG%5Bascending%5D%5Bis_checkbox%5D=true&MHG%5Bascending%5D%5Bvalue%5D=&MHG%5Blimit%5D=&MHG%5Boffset%5D=&MHG%5Bregion%5D=&MHG%5Byear%5D=&MHG%5Bstartdate%5D=&MHG%5Benddate%5D=&MHG%5Bwhere%5D=&MHG%5Btextonly%5D%5Bis_checkbox%5D=true&_run=&pfRunQueryFormName=MatchHistoryGame&wpRunQuery=&pf_free_text="

class LeagueParserSpider(scrapy.Spider):
    name = "league_parser"

    def start_requests(self):
        urls = [
            DRX_MATCHES_WORLDS, 
            T1_MATCHES_WORLDS
        ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        table = response.css('table.wikitable').get()
        soup = BeautifulSoup(table, 'lxml')
        tbody = soup.find('tbody')
        for tr in tbody.find_all('tr')[3:]:
            td = tr.find_all('td')
            j = {
                "date": td[0].string,
                "patch": td[1].string,
                "team_1": td[2].a["title"],
                "team_2": td[3].a["title"],
                "winner_team": td[4].a["title"],
            }
            for count, ban in enumerate(td[5].find_all('span')):
                j[f'team_1_ban_{count+1}'] = ban["title"]
            for count, ban in enumerate(td[6].find_all('span')):
                j[f'team_2_ban_{count+1}'] = ban["title"]
            for count, pick in enumerate(td[7].find_all('span')):
                j[f'team_1_pick_{count+1}'] = pick["title"]
            for count, pick in enumerate(td[8].find_all('span')):
                j[f'team_2_pick_{count+1}'] = pick["title"]
            for count, player in enumerate(td[9].find_all('a')):
                j[f'team_1_player_{count+1}'] = player.string
            for count, player in enumerate(td[10].find_all('a')):
                j[f'team_2_player_{count+1}'] = player.string
            print(j)
            yield j