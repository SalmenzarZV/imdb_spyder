import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['www.imdb.com']
    initial_url = 'https://www.imdb.com'
    start_urls = ['https://www.imdb.com/search/title/?genres=comedy&explore=title_type,genres']
    start_url = 'https://www.imdb.com/search/title/?genres=comedy&explore=title_type,genres'
    console_alert = 'MARADONA'
    movie_list = []
    index = 0
    def parse(self, response):
        print(response)
        movies_html = response.css('div.lister-item > div.lister-item-content')
        
        for movie in movies_html:
            num_movie = movie.css('span::text').get()
            link = response.urljoin(self.initial_url + movie.css('a::attr(href)').get())
            yield scrapy.Request(link, callback = self.another_func)
           

        next_link = response.urljoin(self.initial_url + response.css('a.next-page')[0].css('a::attr(href)').get())
        self.index += 1
        if self.index < 5:
            yield scrapy.Request(next_link, callback = self.parse)
        else: 
            print(self.movie_list)
            
        
       
        
        
    
    def another_func(self, response):
        movie = {}
        # FALTA SACAR EL RESTO DE CAMPOS DE LA PELICULA, PERO ALMACENA TODOS DENTRO DE MOVIE_LIST
        movie['title'] = response.css('h1.sc-b73cd867-0::text').get()
        self.movie_list.append(movie)
        print(movie)
        return None

    def get_movie(self, response):
        return response.css('h1.sc-b73cd867-0::text').get()
    