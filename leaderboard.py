from requests_html import HTMLSession
import csv
sesson=HTMLSession()
r=sesson.get('https://www.billboard.com/charts/hot-100?rank=8')
song=r.html.find('span.chart-element__information__song.text--truncate.color--primary')
songwriter=r.html.find('span.chart-element__information__artist.text--truncate.color--secondary')
ytlink='https://www.youtube.com/results?search_query='

with  open('music.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['rank','song','songwriter','ytlink'])
    for i in range(len(song)):
        print(song[i].text)
        print(songwriter[i].text)
        print(ytlink+(song[i].text))
        songlink=ytlink+song[i].text
        writer.writerow([i+1,song[i].text,songwriter[i].text,songlink.replace(' ','+')])
