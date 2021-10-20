import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from bs4 import BeautifulSoup
import requests
import csv

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/94.0.4606.81 Safari/537.36 '
}


def get_source_html(url):
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
    driver.maximize_window()

    try:
        driver.get(url=url)
        driver.implicitly_wait(10)
        time.sleep(3)

        while True:
            find_last_element = driver.find_element_by_class_name('shop-clear')
            if driver.find_elements_by_tag_name("li"):
                with open('html-pages/hair-care.html', 'w') as file:
                    file.write(driver.page_source)
                break
            else:
                actions = ActionChains(driver)
                actions.move_to_element(find_last_element).perform()
                time.sleep(3)

    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()


def get_items_url(file_path):
    with open(file_path) as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    item_divs = soup.find_all('div', class_='product-image')
    urls = []
    for item in item_divs:
        item_url = item.find('a').get('href')
        urls.append(item_url)

    with open('hair-care-urls.txt', 'w') as file:
        for url in urls:
            file.write(f'{str(url)}\n')
    print("SUCCESSFULLY COLLECTED")


def get_data(file_path):
    with open(file_path) as file:
        url_list = [url.strip() for url in file.readlines()]

        for url in url_list:
            response = requests.get(url=url, headers=HEADERS)
            soup = BeautifulSoup(response.text, 'lxml')

            try:
                title = soup.find('h1').find('a').text.strip()
            except Exception as e:
                title = "Test"
            try:
                price = soup.find('span', class_='css-12nhxov-paragraph-sansSerif-currentPriceLabel').text
            except Exception as e:
                price = "Test price"
            try:
                img = soup.find_all('img')[31]['alt'].replace(' ', '-').replace('/', '') + '.jpg'
            except Exception as e:
                img = "Test Image"
            try:
                description = soup.find_all("div",
                                            class_="css-g0vocb-paragraph-sansSerif-accordionInnerContent "
                                                   "accordion-inner-content")[1].text
            except Exception as e:
                description = "Test Description"
            random_id = random.randrange(145, 182)

            data = {
                'ID': random_id,
                'Type': 'simple',
                'Name': title,
                'Published': 1,
                'Is featured?': 1,
                'Visibility in catalog': 'visible',
                'Short description': description[15:],
                'Tax status': 'taxable',
                'In stock?': 1,
                'Backorders allowed?': 0,
                'Sold individually?': 0,
                'Allow customer reviews?': 1,
                'Regular price': price,
                'Categories': 'body',
                'Tags': 'body',
                'Position': 0,
                'Images': 'http://localhost:8888/wp-content/uploads/2021/10/' + img.replace('+', '').replace('&', '').replace('---', '-').replace('--', '-').replace('(', '').replace(')', '').replace('é', 'e').replace("'", ''),
            }
            write_csv(data)


def write_csv(data):
    with open('all-new-products.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow((data['ID'], data['Type'], data['Name'], data['Published'], data['Is featured?'],
                         data['Visibility in catalog'], data['Short description'], data['Tax status'],
                         data['In stock?'], data['Backorders allowed?'], data['Sold individually?'],
                         data['Allow customer reviews?'], data['Regular price'], data['Categories'],
                         data['Tags'], data['Images'], data['Position'],
                         ))


def main():
    # get_source_html(url="https://www.mecca.com.au/hair-care/")
    # get_items_url(file_path='/Users/azamatjumma/Desktop/Selenium/html-pages/body-personal-care.html')
    get_data(file_path='/Users/azamatjumma/Desktop/Selenium/body-personal-care-urls.txt')


if __name__ == '__main__':
    main()
