import scrapy
""" This spider cannot be used since the site is unable to handle the requests
    TODO: Figure out how to throttle requests"""

class DublinPeopleSpider(scrapy.Spider):
    name = 'DublinPeople'
    start_urls = ['https://dublinpeople.com/news/category/southside/']

    def parse(self, response):
        article_links = response.css(".news-details a::attr(href)").get()

        for link in article_links:
            yield response.follow(link, callback=self.parse_article)

        next_page = response.css(".catnav a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_article(self, response):
        item = {
            'title': response.css('.page-title::text').get(),
            'url': response.url,
            'date': response.css('.news-date::text').get(),
            'author': response.css('.news-date strong::text').get(),
            'body': '\n'.join(response.css('.single-copy p::text').getall())
        }
        yield item
