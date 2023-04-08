import scrapy


class DublinLiveSpider(scrapy.Spider):
    name = 'DublinLive'
    start_urls = ['https://www.dublinlive.ie/news/dublin-news/']

    def parse(self, response):
        article_links = response.css(".headline::attr(href)").extract()

        for link in article_links:
            yield response.follow(link, callback=self.parse_article)

        next_page = response.css(".pagi-next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_article(self, response):
        body_list = response.css("article p::text").getall()
        body_string = ""
        for line in body_list:
            body_string += line
            body_string += " "

        item = {
            'title': response.css('h1::text').get(),
            'url': response.url,
            'date': response.css('time .date-published::text').get(),
            'author': response.css('.author a::text').get(),
            'body' : body_string

            # 'body': '\n'.join(response.css('article p::text').getall())
            # 'body': "\n".join(response.xpath("//article/p::*/text()").extract())
        }
        yield item
