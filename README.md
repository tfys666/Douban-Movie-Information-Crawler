# Scrapy Spider Project: Movie Information Crawler
## 1. Project Overview
This project aims to use the Scrapy crawler framework to crawl movie-related information from the Douban movie website (https://movie.douban.com/). The information to be crawled includes movie name, director name, author name, the names of the first three main actors, and the movie rating.
## 2. Environment Preparation
Ensure that Python and the Scrapy framework are installed on your computer. You can download Python from the official website (https://www.python.org/) and obtain the Scrapy framework from the official website (https://scrapy.org/).
## 3. Create a Scrapy Project
In the command line, navigate to the directory where you want to store the project, and then run the following command to create a new Scrapy project:
```
scrapy startproject douban_movie_spider
scrapy genspider demo <domain>
```
This will create a new Scrapy project named `douban_movie_spider`, which includes the following files and directories:
- `douban_movie_spider/`: The root directory of the project
  - `douban_movie_spider/douban_movie_spider/`: The Python package of the project
    - `items.py`: Defines the Item for crawling data
    - `pipelines.py`: Defines the data processing pipeline
    - `settings.py`: The project settings file
    - `spiders/`: The folder containing the spider files
      - `demo.py`: An example spider file
    - `__init__.py`: The package initialization file
## 4. Modify USER_AGENT
To simulate real user behavior, we usually modify the default USER_AGENT of Scrapy. In the `douban_movie_spider/settings.py` file, find the `USER_AGENT` setting and modify it to your custom USER_AGENT. For example:
```python
# settings.py
USER_AGENT = ''  # Add the User-Agent
```
## 5. Write Spider Code
In the `douban_movie_spider/spiders/demo.py` file, write the spider code.   
You can see the detail in 'demo.py'.

## 6. Run the Spider
In the project root directory, run the following command to start the spider:
```
scrapy crawl demo
```
This will start crawling movie information from the Douban movie website and store the results in the defined Item.

## 7. Example
- url:  
https://movie.douban.com/subject/36369452/

- results:  
Movie Name: 飞驰人生2  
Director: 韩寒 Han Han  
Author: 韩寒 Han Han  
Main Actors: 沈腾 Teng Shen, 范丞丞 Chengcheng Fan, 尹正 Zheng Yin
