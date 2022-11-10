import scrapy
from bs4 import BeautifulSoup
import pandas as pd 

from ..items import TeamItem, PlayerItem

TEAMS_WORLDS = "https://lol.fandom.com/wiki/2022_Season_World_Championship/Main_Event"

class GetTeamsSpider(scrapy.Spider):
    name = "get_team"
    
    def start_requests(self):
        url = TEAMS_WORLDS
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        table = response.css("table.wikitable2 tbody tr td.tournament-results-team")
        team_links = table.css("span.teamname a::attr(href)").getall()
        # for team_link in team_links:
        #     team_page = "https://lol.fandom.com"+team_link
        #     yield response.follow(url=team_page, callback=self.parse_team)
        
        team_image_link = table.css("span.teamimage-right a img::attr(src)").getall()
        team_name = table.css("span.teamname a::text").getall()

        for i in range(0, len(team_name)-1):
            teams_item = TeamItem()
            teams_item["team_name"] = team_name[i]
            teams_item["image_link"] = team_image_link[i]
            yield teams_item

    def parse_team(self, response):
        # using parsel to extract table html of team wiki page
        team_members = response.css("table.team-members-current")

        player_name = team_members.css('td.team-members-player a::text').getall()
        player_role = team_members.css('td.team-members-role .markup-object span:nth-child(2)::text').getall()

        for index in range(0, len(player_name)-1):
            player_item = PlayerItem()
            player_item["player_name"] = player_name[index]
            player_item["player_role"] = player_role[index]
            yield player_item
        


