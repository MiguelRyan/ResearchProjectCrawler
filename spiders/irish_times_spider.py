import scrapy


class IrishTimesSpider(scrapy.Spider):
    name = 'IrishTimes'
    start_urls = ['https://www.irishtimes.com/ireland/dublin/']

    def parse(self, response):
        article_links = response.css("a.text-align_left::attr(href)").extract()
        article_links2 = response.css(".results-list--headline-container a::attr(href)").extract()

        all_articles = article_links + article_links2
        for link in all_articles:
            yield response.follow(link, callback=self.parse_article)

    def parse_article(self, response):
        item = {
            'title': response.css('h1::text').get(),
            'url': response.url,
            'date': response.css('.byline-date::text').get(),
            'author': response.css('.author-name a::text').get(),
            'body': '\n'.join(response.css('article > p::text').getall())
        }
        yield item
