import scrapy
import json

class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["movie.douban.com"]
    start_urls = [""]  # the <domain>

    def parse(self, response):
        script_text = response.xpath("//script[@type='application/ld+json']/text()").get()

        json_data = json.loads(script_text)

        movie_name = json_data['name']
        director_name = json_data['director'][0]['name']
        author_name = json_data['author'][0]['name']
        main_actors = json_data['actor'][:3]
        rating = json_data['aggregateRating']['ratingValue']

        print(f'Movie Name: {movie_name}')
        print(f'Director: {director_name}')
        print(f'Author: {author_name}')
        print(f'Main Actors: {", ".join(actor["name"] for actor in main_actors)}')
        print(f'Rating: {rating}')
