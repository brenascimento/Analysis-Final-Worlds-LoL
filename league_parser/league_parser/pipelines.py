import os 
import pyodbc
from itemadapter import ItemAdapter
from dotenv import load_dotenv

load_dotenv()

SERVER = os.getenv('SERVER')
DATABASE = "WorldsDB"
CONN = pyodbc.connect(f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;Encrypt=no")

class TeamPipeline:

    def open_spider(self, spider):
        self.cursor = CONN.cursor()

    def process_item(self, item, spider):
        self.cursor.execute("INSERT INTO dbo.Teams VALUES(?, ?)", item["team_name"], item["image_link"])
        CONN.commit()

    def close_spider(self, spider):
        self.cursor.close()
    

class PlayerPipeline:
    def open_spider(self, spider):
        self.cursor = CONN.cursor()

    def process_item(self, item, spider):
        self.cursor.execute("INSERT INTO dbo.Player VALUES(?, ?)", item["player_name"], item["player_role"])
        CONN.commit()
        rows = self.cursor.fetchone()
        print(rows)

    def close_spider(self, spider):
        self.cursor.close()

class SelectPipeline:
    def open_spider(self, spider):
        self.cursor = CONN.cursor()

    def process_item(self, item, spider):
        self.cursor.execute("SELECT * FROM dbo.Teams")
        # CONN.commit()
        rows = self.cursor.fetchall()
        print(rows)

    def close_spider(self, spider):
        self.cursor.close()
