from time import sleep
import requests, csv
from bs4 import BeautifulSoup as BSoup

def ReqByPage(page : int):
    for pg in range(page):
        sleep(0.5) # 페이지 조회 시간 차
        response = requests.get(f"https://movie.naver.com/movie/point/af/list.naver?&page={pg+1}") # get request
        print(f"current page : {pg+1}")
        soup = BSoup(response.text, 'html.parser')
        body = soup.find(name='tbody')
        for element in body.find_all(name='td', attrs={'class':'title'}):
            texts = list(element.stripped_strings)
            movie = texts[0]
            score = texts[2]
            if len(texts) < 5:
                sentence = None
            else:
                sentence = texts[3]
            yield {'movie':movie,'sentence':sentence,'score':score}

def ReviewCrawl():
    with open('samples.csv','w', encoding="utf8") as fd:
        writer = csv.DictWriter(fd, fieldnames=['movie','sentence','score'])
        writer.writeheader()
        for sample in ReqByPage(1000):
            writer.writerow(sample)

if __name__ == '__main__':
    ReviewCrawl()