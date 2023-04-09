import scrapy


class TheJournalSpider(scrapy.Spider):
    name = 'TheJournal'
    start_urls = ['https://www.thejournal.ie/irish/']

    def parse(self, response):
        article_links = response.css(".link-overlay-redesign::attr(href)").extract()

        for link in article_links:
            yield response.follow(link, callback=self.parse_article)

        next_page = response.css(".right-redesign a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_article(self, response):
        body_list = response.css("#article-body-container-redesign p::text").getall()
        body_string = ""
        for line in body_list:
            body_string += line
            body_string += " "
        item = {
            'title': response.css('.title-redesign span::text').get(),
            'url': response.url,
            'date': response.css('.metadata-date-redesign span::text').get(),
            'author': response.css('.author-contact-name-redesign::text').get(),
            'body': body_string.strip()
            # 'body': '\n'.join(response.css("#article-body-container-redesign p::text").extract())
        }
        yield item
