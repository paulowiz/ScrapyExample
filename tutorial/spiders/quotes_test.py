import scrapy
from scrapy.http import FormRequest
from ..items import TutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls=[
        'http://quotes.toscrape.com/login'
    ]
    
    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response,formdata={
            'csrf_token':token,
            'username':'admin',
            'password':'1234'
        }, callback = self.start_scraping)
        
    def start_scraping(self,response):
        items = TutorialItem()
                
        all_div_quotes = response.css('div .quote')
        
        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()
        
            items['title'] = title  
            items['author'] = author 
            items['tag'] = tag 
            
            yield items
        
        #use get    
        next_page = response.css('li.next a::attr(href)').get()
        #next_page = 'http://quotes.toscrape.com/page/'+page_number+'/' outra forma
        if next_page is not None:
            yield response.follow(next_page, callback = self.start_scraping)
            
       
            
                        