-- Python CA - Beautiful Soup

# This line of code creates a BeautifulSoup object from a webpage:

soup = BeautifulSoup(webpage.content, "html.parser")

# Within the `soup` object, tags can be called by name:

first_div = soup.div

# or by CSS selector:

all_elements_of_header_class = soup.select(".header")

# or by a call to `.find_all`:

all_p_elements = soup.find_all("p")

# Exercises
import requests
from bs4 import BeautifulSoup

webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage,"html.parser")

print(soup)
print(soup.div.name)
print(soup.div.attrs)
print(soup.div.string)
print(soup.p.string)

for children in soup.div.children:
  print(children)
  
for parent in soup.li.parents:
  print(parent)
  
print(soup.find("h1"))
print(soup.find_all("div"))

# REGEX 
import re
soup.find_all(re.compile("[ou]l"))
soup.find_all(re.compile("h[1-9]"))
soup.find_all(['h1', 'a', 'p'])
soup.find_all(attrs={'class':'banner'})
soup.find_all(attrs={'class':'banner', 'id':'jumbotron'})

# Define function to find the targets
def has_banner_class_and_hello_world(tag):
    return tag.attr('class') == "banner" and tag.string == "Hello world"

soup.find_all(has_banner_class_and_hello_world)
# Finds 
<div class="banner">Hello world</div> # but must match both attributes to return

turtle_links = soup.find_all('a')
print(turtle_links)


# Selecting CSS elements - Classes - IDs
soup.select(".recipeLink")
soup.select("#selected")

# Iterate through all links on a webpage, parse all the webpage content and create dictionary list of all turtle names by targeting their element. 
import requests
from bs4 import BeautifulSoup

prefix = "https://content.codecademy.com/courses/beautifulsoup/"
webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

turtle_links = soup.find_all("a")
links = []
#go through all of the a tags and get the links associated with them:
for a in turtle_links:
  links.append(prefix+a["href"])
    
#Define turtle_data:
turtle_data = {}
#follow each link:
for link in links:
  webpage = requests.get(link)
  turtle = BeautifulSoup(webpage.content, "html.parser")
  #Add your code here:
  turtle_name = turtle.select(".name")[0]
  turtle_data[turtle_name] = []
print(turtle_data)

# Get the text from inside the HTML Elements
soup.get_text()
# Seperator character to split up the text returned.
soup.get_text('|')


# COCOA EXAMPLES -- GOOD examples

import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage,"html.parser")

td_ratings = soup.find_all(attrs={"class": "Rating"})
# print(td_ratings)

ratings = []

for rating in td_ratings[1:]:
  ratings.append(float(rating.get_text()))

# print(ratings)
plt.hist(ratings)
# plt.show()

company_names = soup.find_all(attrs={"class": "Company"})

companies = []

for company in company_names[1:]:
  companies.append(company.get_text())
# print(companies)

# d = {"Company": companies, "Rating": ratings}
# cacao_df = pd.DataFrame.from_dict(d)
# print(cacao_df)

# mean_ratings = cacao_df.groupby("Company").Rating.mean()
# ten_best = mean_ratings.nlargest(10)
# print(ten_best)

cocoa_percents = []
cocoa_percent_tags = soup.select(".CocoaPercent")


for td in cocoa_percent_tags[1:]:
  percent = float(td.get_text().strip('%'))
  cocoa_percents.append(percent)

# print(cocoa_percents)
# plt.clf()
# d = {"Company": companies, "Rating": ratings, "CocoaPercent": cocoa_percents}
# df = pd.DataFrame.from_dict(d)
# print(cacao_df)

# plt.scatter(df.CocoaPercent, df.Rating)

# z = np.polyfit(df.CocoaPercent, df.Rating, 1)
# line_function = np.poly1d(z)
# plt.plot(df.CocoaPercent, line_function(df.CocoaPercent), "r--")
# plt.clf()
# plt.show()

company_location = []
locations = soup.find_all(attrs={"class": "CompanyLocation"})

for location in locations[1:]:
  company_location.append(location.get_text())

# print(company_location)

d = {"Company": companies, "Rating": ratings, "CocoaPercent": cocoa_percents, "CompanyLocation": company_location}
df = pd.DataFrame.from_dict(d)

# print(df)

