from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import time

from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


news_url = 'https://redplanetscience.com/'
featured_img = 'https://spaceimages-mars.com/'
table_url = 'https://galaxyfacts-mars.com/'
hemispheres_url = 'https://marshemispheres.com/'


def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # News URL
    browser.visit(news_url)
    time.sleep(1)

    html = browser.html
    soup = bs(html, 'html.parser')

    news_title = soup.find_all('div', class_='content_title')[0].text
    news_p = soup.find_all('div', class_='article_teaser_body')[0].text


    # Featured Image
    browser.visit(featured_img)
    time.sleep(1)

    browser.links.find_by_partial_text('FULL IMAGE').click()
    html = browser.html
    soup = bs(html, 'html.parser')

    featured_image_link = soup.find_all('img', class_='fancybox-image')[0]['src']
    featured_image_url = f'{featured_img}{featured_image_link}'
    

    # Table
    table = pd.read_html(table_url)
    table_df = table[0].rename({0:'Description', 1:table[0][1][0], 2:table[0][2][0]}, axis='columns').set_index('Description')
    html_table = table_df.to_html(justify='left', classes="table table-bordered")


    # Hemisphere
    browser.visit(hemispheres_url)
    time.sleep(1)

    hemisphere_image_urls = []
    html = browser.html
    soup = bs(html, 'html.parser')

    for n in range(0, len(soup.find_all('div', class_='description'))):
        click_text = soup.find_all('div', class_='description')[n].h3.text
        browser.links.find_by_partial_text(click_text).click()
        
        time.sleep(1)
        
        html = browser.html
        soup = bs(html, 'html.parser')
        
        img_url = f'{hemispheres_url}{soup.find_all("a", text="Sample")[0]["href"]}'
        
        url_dict={}
        url_dict["title"] = click_text
        url_dict["img_url"] = img_url
        hemisphere_image_urls.append(url_dict)
        
        browser.links.find_by_partial_text('Back').click()
        
        time.sleep(1)
        
        html = browser.html
        soup = bs(html, 'html.parser')

    browser.quit()

    listings = {}
    listings['news_title'] = news_title
    listings['news_p'] = news_p
    listings['featured_img_url'] = featured_image_url
    listings['hemisphere_img_url'] = hemisphere_image_urls
    listings['table'] = html_table


    return listings
