import scrapy
from ..items import Assignment1Item

class BooksSpider(scrapy.Spider):
    name = "books" 
    start_urls = [
        'https://books.toscrape.com/'
    ]

    def parse(self, response):
        all_books = response.css('article.product_pod')

        for book in all_books:
            items = Assignment1Item()

            
            items['book_name'] = book.css('h3 a::attr(title)').get()
            items['book_price'] = book.css('p.price_color::text').get()
            items['book_availability'] = ''.join(book.css('p.availability::text').getall()).strip()
            items['book_rating'] = book.css('p.star-rating::attr(class)').re_first(r'star-rating\s+(\w+)')

            yield items

       
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
