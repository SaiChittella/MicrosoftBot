import requests
from bs4 import BeautifulSoup
# https://forecast.weather.gov/MapClick.php?lat=47.613440000000026&lon=-122.03538999999995#.Y3Gp1HbMK3A

page = requests.get('https://rewards.bing.com/')
soup = BeautifulSoup(page.content, 'html.parser')
# daily_set = soup.find(class_='btOptionText')
# print(daily_set)
print(soup)
# print(soup.find_all('img'))


# print(daily_set.find_all('span'))
