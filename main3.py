import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")
    laptop_blocks = soup.find_all("div", class_="col-sm-4 col-lg-4 col-md-4")

    for laptop_block in laptop_blocks:

        laptop_name = laptop_block.find("a", class_="title").text.strip()
        laptop_price = laptop_block.find("h4", class_="pull-right price").text.strip()
        laptop_description = laptop_block.find("p", class_="description").text.strip()

        print("Назва: ", laptop_name)
        print("Ціна: ", laptop_price)
        print("Опис: ", laptop_description)
        print("\n")

else:
    print("Помилка при отриманні вмісту сторінки. Код статусу:", response.status_code)
