import lxml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import json
import time

def isNumeric(elem):
    try:
        float(elem)
        return True
    except ValueError:
        return False

def collect_data():
    price = list()
    result = list()
    price_list = list()
    href_list = list()
    name_list = list()

    global href

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
            for item in range(2, 5):
                counter += 1
                size += butch
                driver.get(f'https://lis-skins.ru/market/csgo/?sort_by=price_desc&price_from=200&price_to=300&page={item}')
                time.sleep(2)
                html_source = driver.page_source

                soup = BeautifulSoup(html_source, 'lxml')

                data = soup.find(class_='skins-market-skins-list')
                try:
                    for skin_data in data:
                        card = skin_data.find('a')
                        if type(card) != int:
                            href = card.get('href')
                            name = card.find('div', class_='name-inner').text
                            href_list.append(href)
                            name_list.append(name)
                        for dls in skin_data:
                            price_class = dls.find('div')
                            if type(price_class) != int and price_class is not None:
                                price.append(price_class.text)
                except Exception:
                    pass

            for elem in price:
                if isNumeric(elem) == True:
                    price_list.append(elem)

            print(len(price_list))
            print(href_list[65])
            print(name_list[65])
            print(price_list[65])

            for b in range(len(price_list)):
                result.append(
                    {
                        "name": name_list[b],
                        'price': price_list[b],
                        'link': href_list[b]
                    }
                )
            print(result[65])
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


def main():
    collect_data()


if __name__ == '__main__':
    main()