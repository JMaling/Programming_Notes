from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com" # uniform resource locator
page = requests.get(url) # the get request to the website
# print(page.text)

# Make a BS Object to Scrape, Beautiful Soup Parse The Page
soup = BeautifulSoup(page.text, "html.parser") # you need to input the (page your scraping, parser)
print(soup.prettify()) # the .prettify() adds the formatting back to the HTML text

# Find Data/Text Using the findAll Function
# the findAll can search by tagname, attributes (kwargs), css class(kwarg), or string

# By Tagname
title = soup.findAll("title") # "title" is the tagname for the title of the webiste
print(title) # prints the title, which is given in a list
# By Attribute
header = soup.findAll(style="text-decoration: none")
print(header)
# By CSS Class
tags = soup.findAll(class_="tags")
print(tags)
# By String
einstein = soup.find_all(string="Albert Einstein") # only shows his name however many times it appears
print(einstein)
# By Any Combination of the Above
quotes = soup.findAll("span", class_="text")
for quote in quotes:
    print(quote.text) # the .text strips out any extraneous HTML, and leaves you just with the text
# Find All The Authors
authors = soup.findAll("small", class_="author")
for i in range(len(quotes)):
    print(quotes[i].text)
    print("- ", authors[i].text, "\n")

# Regal Webster Place 11 Scrape
url = "https://www.regmovies.com/theaters/regal-webster-place-11/C00129681357"
page = requests.get(url)
# print(page.text)
soup = BeautifulSoup(page.text, "html.parser")
# print(soup.prettify())

titles = soup.findAll("h3", class_="title") # tagname, class
for i in range(len(titles)):
    print(titles[i].text) # takes a single item in the list, and then prints all the text elements of it
showtimes = soup.findAll("ul", class_="format-showtimes")
print(showtimes[0].text)
movietimes= []
for time in showtimes:
    movietime = time.findAll("li", class_="showtime-entry")
    movietimes.append(movietime)
    print(movietimes)
for i in range(11):
    print("\n")
    print(titles[i].text)
    for time in movietimes[i]:
        print(time.text)
