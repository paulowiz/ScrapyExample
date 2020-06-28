# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class TutorialPipeline(object):
    
    def __init__(self):
        pass
    
    def create_connection(self):
       self.conn = sqlite3.connect('myquotes.db')  
       self.curr = self.conn.cursor()
       
    def create_table(self):
      self.curr.execute("""create table quotes_tb(
                     title text,
                    author text,
                    tag text
                 )""")  
      
    def create_table(self):
          self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
          self.curr.execute("""
                    create table quotes_tb(
                     title text,
                     author text,
                     tag text
                 )""")  
          
    def store_db(self,item):
        
        query = """insert into quotes_tb values ("%s","%s","%s")""" % (item['title'][0],item['author'][0],item['tag'][0])
        query = str(query)
        self.curr.execute(query)
        self.conn.commit()

       
    def process_item(self, item, spider):
        self.create_connection()
        #self.create_table()
        self.store_db(item)
        return item
    
    