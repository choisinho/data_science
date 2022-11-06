import bs4 as BeautifulSoup4
import requests
import csv
import pandas as pd

url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
file = open('homework.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(file)


def financialData(page):
    res = requests.get(page)
    soup = BeautifulSoup4(res.text, 'html.parser')

    body = soup.find('tbody')
    items = body.find_all('tr', onmouseover="mouseOver(this)")

    for item in items:
        information = item.text
        info = information.split('\n')
        writer.writerow(['N', '종목명', '현재가', '전일비', '등락률', '액면가', '시가총액', '상장주식수', '외국인비율', '거래량', 'PER', 'ROE'])

        try:
            writer.writerow(
                [info[1], info[2], info[3], info[6].strip(), info[11].strip(), info[14], info[15], info[16], info[17],
                 info[18], info[19], info[20]])
            print([info[1], info[2], info[3], info[6].strip(), info[11].strip(), info[14], info[15], info[16], info[17],
                   info[18], info[19], info[20]])

        except:
            writer.writerow(
                [info[1], info[2], info[3], info[6].strip(), info[11].strip(), info[14], info[15], info[16], info[17],
                 info[18]])
            print([info[1], info[2], info[3], info[6].strip(), info[11].strip(), info[14], info[15], info[16], info[17],
                   info[18]])
        # 1, 2, 3, 6[strip], 11[strip], 14, 15, 16, 17, 18, 19, 20
        # print(len(info))

for i in range(1, 39):
    financialData(url + str(i))

file.close()
