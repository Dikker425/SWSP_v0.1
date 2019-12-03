import re
import requests
from bs4 import BeautifulSoup as bs

headers = {
    'accept': '*/*',
    'user-agent': 'Googlebot/2.1 (+http://www.google.com/bot.html)'
    #'user-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
}

#v.02 - December 03, 2019
#Check 123
# так это чек ради чека
#check


url = open('input.txt', 'r', encoding='utf-8').read().split('\n')
print('================================')
print(f'Reading input file... We have {len(url)} websites')
print('Go Go Go!')
print('================================')

a = 0

my_file = open('output.txt', 'w')
my_file.write('Website' + '\t' + 'Country' + '\t' + 'Traffic,%' + '\t' + 'Traffic' + '\t' + 'Check' + '\n')

session = requests.session()

for a in range(len(url)):

    base_url = ('https://www.similarweb.com/website/' + url[a])
    # print(base_url)
    # print(type(url))

    request = session.get(base_url, headers=headers)
    soup = bs(request.content, 'html.parser')
    if request.status_code == 200:
        # print('OK')
        # print(soup)

        wtest = '*'

        try:
            wtraffic = soup.find_all('span', attrs={'engagementInfo-valueNumber js-countValue'}, limit=1)[0].text
            # print(wtraffic)


            wtest = wtraffic
            wtraffic = re.sub(r'[\sB]', '0.000.000', wtraffic)
            wtraffic = re.sub(r'[\sM]', '0.000', wtraffic)
            wtraffic = re.sub(r'[\sK]', '0', wtraffic)
            wtraffic = re.sub(r'[\s.]', '', wtraffic)
            wtraffic = int(wtraffic)


        # ================================
        # Top 5 Country Name + Traffic by %
        # ================================

        # Достаем Трафик с каждой страны (в процентах)


            Country1 = soup.find_all('span', attrs={'traffic-share-valueNumber js-countValue'}, limit=5)[0].text
            Country2 = soup.find_all('span', attrs={'traffic-share-valueNumber js-countValue'}, limit=5)[1].text
            Country3 = soup.find_all('span', attrs={'traffic-share-valueNumber js-countValue'}, limit=5)[2].text
            Country4 = soup.find_all('span', attrs={'traffic-share-valueNumber js-countValue'}, limit=5)[3].text
            Country5 = soup.find_all('span', attrs={'traffic-share-valueNumber js-countValue'}, limit=5)[4].text

            # Удаляем лишний мусор из данных

            Country1 = float(re.sub(r'[\s%]', '', Country1))
            Country2 = float(re.sub(r'[\s%]', '', Country2))
            Country3 = float(re.sub(r'[\s%]', '', Country3))
            Country4 = float(re.sub(r'[\s%]', '', Country4))
            Country5 = float(re.sub(r'[\s%]', '', Country5))

            # Трафик других стран

            Country1traffic = wtraffic * Country1 / 100
            Country2traffic = wtraffic * Country2 / 100
            Country3traffic = wtraffic * Country3 / 100
            Country4traffic = wtraffic * Country4 / 100
            Country5traffic = wtraffic * Country5 / 100

            # Возращаем траффик% в значения строк, чтобы заменить точку на запятую
            # чтобы в эксел вставлялось красиво

            Country1 = str(Country1)
            Country1 = re.sub(r'[.]', ',', Country1)
            Country2 = str(Country2)
            Country2 = re.sub(r'[.]', ',', Country2)
            Country3 = str(Country3)
            Country3 = re.sub(r'[.]', ',', Country3)
            Country4 = str(Country4)
            Country4 = re.sub(r'[.]', ',', Country4)
            Country5 = str(Country5)
            Country5 = re.sub(r'[.]', ',', Country5)

        # Достаем Названия стран

            Country1Name = soup.find_all(None, attrs={'country-name'}, limit=5)[0].text
            Country2Name = soup.find_all(None, attrs={'country-name'}, limit=5)[1].text
            Country3Name = soup.find_all(None, attrs={'country-name'}, limit=5)[2].text
            Country4Name = soup.find_all(None, attrs={'country-name'}, limit=5)[3].text
            Country5Name = soup.find_all(None, attrs={'country-name'}, limit=5)[4].text


        # Вывод данных

            # Принты для провеки
            # print(url[a] + '\t' + 'Total' + '\t' + '100' + '%' + '\t' + str(wtraffic) + '\t' + str(wtest))
            # print(url[a] + '\t' + Country1Name + '\t' + Country1 + '%' + '\t' + str(round(Country1traffic)))
            # print(url[a] + '\t' + Country2Name + '\t' + Country2 + '%' + '\t' + str(round(Country2traffic)))
            # print(url[a] + '\t' + Country3Name + '\t' + Country3 + '%' + '\t' + str(round(Country3traffic)))
            # print(url[a] + '\t' + Country4Name + '\t' + Country4 + '%' + '\t' + str(round(Country4traffic)))
            # print(url[a] + '\t' + Country5Name + '\t' + Country5 + '%' + '\t' + str(round(Country5traffic)))

            data = (url[a] + '\t' + 'Total' + '\t' + '100' + '%' + '\t' + str(wtraffic) + '\t' + str(wtest) + '\n' +
                url[a] + '\t' + Country1Name + '\t' + Country1 + '%' + '\t' + str(round(Country1traffic)) + '\n' +
            url[a] + '\t' + Country2Name + '\t' + Country2 + '%' + '\t' + str(round(Country2traffic)) + '\n' +
            url[a] + '\t' + Country3Name + '\t' + Country3 + '%' + '\t' + str(round(Country3traffic)) + '\n' +
            url[a] + '\t' + Country4Name + '\t' + Country4 + '%' + '\t' + str(round(Country4traffic)) + '\n' +
            url[a] + '\t' + Country5Name + '\t' + Country5 + '%' + '\t' + str(round(Country5traffic)) + '\n')

        except:

            # Принты для провеки
            # print(url[a] + '\t' + 'ERROR' + '\t' + 'ERROR' + '\t' + 'ERROR' + '\t' + 'ERROR')
            # print(url[a] + '\t' + 'ERROR' + '\t' + 'ERROR' + '\t' + 'ERROR')
            # print(url[a] + '\t' + 'ERROR' + '\t' + 'ERROR' + '\t' + 'ERROR')
            # print(url[a] + '\t' + 'ERROR' + '\t' + 'ERROR' + '\t' + 'ERROR')
            # print(url[a] + '\t' + 'ERROR' + '\t' + 'ERROR' + '\t' + 'ERROR')
            # print(url[a] + '\t' + 'ERROR' + '\t' + 'ERROR' + '\t' + 'ERROR')

            data = (url[a] + '\t' + 'ERROR' + '\t' + 'ERROR' + '\t' + 'ERROR' + '\t' + 'ERROR' + '\n' +
            url[a] + '\t' + 'ERROR' + '\t' + 'ERROR' + '\t' + 'ERROR' + '\n' +
            url[a] + '\t' + 'ERROR' + '\t' + 'ERROR' + '\t' + 'ERROR' + '\n' +
            url[a] + '\t' + 'ERROR' + '\t' + 'ERROR' + '\t' + 'ERROR' + '\n' +
            url[a] + '\t' + 'ERROR' + '\t' + 'ERROR' + '\t' + 'ERROR' + '\n' +
            url[a] + '\t' + 'ERROR' + '\t' + 'ERROR' + '\t' + 'ERROR' + '\n')

        my_file.write(data)
        print('Parsed:', url[a])
    else:
        print(f'Error : {url[a]} | Status Code: {request.status_code}')
        # print(request.text)
        # print(request.content)

print('================================')
print('Go to output.txt and see results')
print('================================')