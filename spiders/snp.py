import scrapy
from stocks.items import StocksItem


class SnpSpider(scrapy.Spider):
    name = "snp"
    allowed_domains = ["www.slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    def parse(self, response):
        rows = response.xpath('//table//tr')

        for row in rows[1:]:  # Skip the header row
            number = row.xpath('td[1]/text()').get()
            company = row.xpath('td[2]/a/text()').get()
            symbol = row.xpath('td[3]/a/text()').get()
            ytd_return = row.xpath('td[4]/text()').get()

            if number and company and symbol and ytd_return:
                yield {
                    'Number': number.strip(),
                    'Company': company.strip(),
                    'Symbol': symbol.strip(),
                    'YTD_Return': ytd_return.strip(),
                }
