# TOI Newspaper Parser #



# README #

This project uses splash to first render a webpage in docker and then parse it using scrapy. 

### Steps for Server Execution ###

    run the virtual environment by moving to the project directory cd assignment/
    a folder env should be visible now. Run source env/bin/activate to start the virtual environment
    Run spider with:

	$ scrapy crawl bot

    	A file data_file.csv will be created having all the data.

### The Working ###

    The URLs that need to be parsed are first placed in the start_url function.
    URLs to all the articles present are then taken and thereafter each link is then hit to scrape article name, author of the article and the time of posting if each article.
    The code will send a GET request to the sever to get the 'created url' which contains the details which we want to scrape.
    Then the data is cleaned.
    The data is then converted to dictionary and then parsed in csv format to be written to the file.
    Error log is maintained in error.log file

### Steps To Run ###

    Docker needs to be running(Install Here)
    Pull Docker Image :

sudo docker pull scrapinghub/splash:2.3.3

    Start Container :

$ sudo docker run -d --restart=always -p 8050:8050 -p 5023:5023 scrapinghub/splash:2.3.3 --max-timeout 99999`


