from scrapy import Spider

class exemplo_screpy(Spider):
    name = "curso python pro"
    start_urls = ["http://quotes.toscrape.com/page/1",
                  "http://quotes.toscrape.com/page/2"]

    def parse(self, response):
        #quote = estação
        for quote in response.css("div.quote"): 
            yield{
                "text"  : quote.css("span.text::text").extracr(),
                "author": quote.css("small.author::text").extract(),
                "tags"  : quote.css("div.tags a.tag::text").extract(),
            }     
# O out put em linha de comando tende a ser ruim de ler, por isso faça...
#... -o nome_do_Arquivo.extenção recomendo cvs