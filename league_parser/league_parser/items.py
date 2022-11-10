# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LeagueParserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class TeamItem(scrapy.Item):
    team_name = scrapy.Field()
    image_link = scrapy.Field()

class PlayerItem(scrapy.Item):
    player_name = scrapy.Field()
    player_role = scrapy.Field()
