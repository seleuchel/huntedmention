from bs4 import BeautifulSoup
import requests

#http request
req = requests.get('https://www.youtube.com/results?search_query=%EB%A9%94%EC%9D%B4%ED%94%8C%EC%8A%A4%ED%86%A0%EB%A6%AC')

html  = req.text

soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all('a',{'class':'yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link'})


for i in title:
    print(i.text)

#youtube_title crawler 