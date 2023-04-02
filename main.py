
import json
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def isNumeric(elem):
    try:
        float(elem)
        return True
    except ValueError:
        return False

def collect_data(pages):
    price = list()
    result = list()
    price_list = list()
    href_list = list()
    name_list = list()

    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")

    s = Service(executable_path="C:/Users/Misha Pinchuk/PycharmProjects/Parcer_2/chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=options)

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        'source': '''
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol
        '''
    })

    try:
        try:
            size = 1
            butch = 1
            counter = 0
            for item in range(2, pages + 2):
                counter += 1
                size += butch
                driver.get(f'https://lis-skins.ru/market/csgo/?price_to=900&page={item}')
                time.sleep(1)
                html_source = driver.page_source

                soup = BeautifulSoup(html_source, 'lxml')

                data = soup.find(class_='skins-market-skins-list')
                try:
                    for skin_data in data:
                        card = skin_data.find('a')
                        if type(card) != int:
                            href = card.get('href')
                            href_list.append(href)
                            name_card = skin_data.find('img', class_='image')
                            full_name = name_card.get('title')
                            name_list.append(full_name)

                        for dls in skin_data:
                            price_class = dls.find('div')
                            if type(price_class) != int and price_class is not None:
                                price.append(price_class.text)

                except Exception:
                    pass

            for elem in price:
                if isNumeric(elem) == True:
                    price_list.append(elem)

            for b in range(len(price_list)):
                tag_name1 = name_list[b].replace(' ', '%20')
                tag_name2 = tag_name1.replace('|', '%7C')
                tag_name3 = tag_name2.replace('(', '%28')
                tg_name4 = tag_name3.replace(')', '%29')
                url = 'https://market.csgo.com/ru/?search=' + tg_name4
                driver.get(url=url)
                time.sleep(2)
                html_source2 = driver.page_source
                soup2 = BeautifulSoup(html_source2, 'lxml')
                skin_dis_data = soup2.find('div', class_='cdk-virtual-scroll-content-wrapper')
                try:
                    for element in skin_dis_data:
                        if type(element) != int and element is not None:
                            href_false = element.get('href')
                            href_true = 'https://market.csgo.com/ru/?search=' + href_false[href_false.rfind('/') + 1:]
                            second_price = element.find('span')
                            if second_price is not None and type(second_price) != int:
                                price_dis = second_price.text
                                if float(price_dis) / float(price_list[b]) > 1.2 and href_true == url:
                                    discount = float(price_dis) / float(price_list[b]) - 1
                                    result.append({
                                        'name': name_list[b],
                                        'price_first': price_list[b],
                                        'price_second': price_dis,
                                        'discount': discount,
                                        'link': url,
                                        'href': href_list[b]
                                    })

                except Exception :
                    pass

            with open('result.json', 'w', encoding='UTF-8') as file:
                json.dump(result, file, indent=4, ensure_ascii=False)
                file.close()

        except Exception as ex:
            print(ex)

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()
