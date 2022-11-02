import scrapy
from bs4 import BeautifulSoup
import pandas as pd
import os

CHAMPIONS_STAT_WORLDS_TOP = "https://lol.fandom.com/wiki/Special:RunQuery/TournamentStatistics?TS%5Bpreload%5D=TournamentByChampionRole&TS%5Brole%5D=Top&TS%5Bspl%5D=Yes&TS%5Btournament%5D=2022+Season+World+Championship%2FMain+Event%2C+2022+Season+World+Championship%2FPlay-in&_run="
CHAMPIONS_STAT_WORLDS_JUNGLE = "https://lol.fandom.com/wiki/Special:RunQuery/TournamentStatistics?TS%5Bpreload%5D=TournamentByChampionRole&TS%5Brole%5D=Jungle&TS%5Bspl%5D=Yes&TS%5Btournament%5D=2022+Season+World+Championship%2FMain+Event%2C+2022+Season+World+Championship%2FPlay-in&_run="
CHAMPIONS_STAT_WORLDS_MID = "https://lol.fandom.com/wiki/Special:RunQuery/TournamentStatistics?TS%5Bpreload%5D=TournamentByChampionRole&TS%5Brole%5D=Mid&TS%5Bspl%5D=Yes&TS%5Btournament%5D=2022+Season+World+Championship%2FMain+Event%2C+2022+Season+World+Championship%2FPlay-in&_run="
CHAMPIONS_STAT_WORLDS_BOT = "https://lol.fandom.com/wiki/Special:RunQuery/TournamentStatistics?TS%5Bpreload%5D=TournamentByChampionRole&TS%5Brole%5D=Bot&TS%5Bspl%5D=Yes&TS%5Btournament%5D=2022+Season+World+Championship%2FMain+Event%2C+2022+Season+World+Championship%2FPlay-in&_run="
CHAMPIONS_STAT_WORLDS_SUPPORT = "https://lol.fandom.com/wiki/Special:RunQuery/TournamentStatistics?TS%5Bpreload%5D=TournamentByChampionRole&TS%5Brole%5D=Support&TS%5Bspl%5D=Yes&TS%5Btournament%5D=2022+Season+World+Championship%2FMain+Event%2C+2022+Season+World+Championship%2FPlay-in&_run="

class ChampionStatSpider(scrapy.Spider):
    name = "champion_stat"

    def start_requests(self):
        urls = [CHAMPIONS_STAT_WORLDS_TOP, CHAMPIONS_STAT_WORLDS_JUNGLE, CHAMPIONS_STAT_WORLDS_MID, CHAMPIONS_STAT_WORLDS_BOT, CHAMPIONS_STAT_WORLDS_SUPPORT]
        lanes = ["Top", "Jungle", "Mid", "Bot", "Support"]

        for index, url in enumerate(urls):
            yield scrapy.Request(url=url, callback=self.parse, cb_kwargs={"lane": lanes[index]})
    
    def parse(self, response, lane):
        table = response.css('table.wikitable')[0].get()
        soup_table = BeautifulSoup(table, 'lxml')
        
        s = f"<html><body><table><thead>{str(soup_table.find_all('tr')[2])}</thead><tbody>{''.join(str(tr) for tr in soup_table.find_all('tr')[3:])}</tbody></table></body></html>"
        filename = f'table_{lane}.html'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(BeautifulSoup(s, 'lxml').prettify()))
            
        table_df = pd.read_html(filename)[0]
        table_df["Lane"] = lane
        os.remove(filename)
        table_df.to_csv(f"df_{lane}.csv")