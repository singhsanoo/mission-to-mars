# Mission-to-Mars

This web application scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

## Instructions 

This project is divided into two main parts: 

1. Scraping 

2. MongoDB and Flask Application

## Part  1: Scraping

Firstly scraping websites using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* A Jupyter Notebook file called [`mission_to_mars.ipynb`](mission_to_mars.ipynb) does all the scraping and analysis tasks.

### NASA Mars News

* From [Mars News Site](https://redplanetscience.com/) collected the latest News Title and Paragraph Text. 


### JPL Mars Space Images—Featured Image

* URL for the Featured Space Image site [here](https://spaceimages-mars.com).

* Used Splinter to navigate the site to find the image URL for the current Featured Mars Image.


### Mars Facts

* From [Mars Facts webpage](https://galaxyfacts-mars.com) scrapped the table containing facts about the planet including diameter, mass, etc.


### Mars Hemispheres

* From [astrogeology site](https://marshemispheres.com/) collected high-resolution images for each hemisphere of Mars.


## Part 2: MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all the information that was scraped from the URLs above.

* Python script called [scrape_mars.py](scrape_mars.py) contains a function called `scrape()`. This function `scrape()` executes all the scraping code from your Jupyter notebook and return one Python dictionary that contains all of the scraped data

* Next, a Flask route called `/scrape` will import `scrape_mars.py` script and call the `scrape()` function. Then stores the return value in Mongo as a Python dictionary.

* Index route `/` will query your Mongo database and pass the Mars data into an HTML template for displaying the data.

* Template HTML file called [index.html](templates/index.html) will take the Mars data dictionary and display all the data in the appropriate HTML elements. 
[final_webpage_image.png](127.0.0.1_5000_.png)

- - -



