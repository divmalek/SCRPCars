import requests
from bs4 import BeautifulSoup
import csv
print()#
print("Welcome to my code! This Python script is designed to scrape cars.com and extract car listings based on various parameters. By inputting specific details, you can customize your search to find the perfect car that meets your requirements.")
page_number = input("Entre the Number of the Page> ")
brand = input("Entre The Brand of The Cars e,g: Tesla > ")
model = input("Entre The Car Model (Optional) > ")
min_price = input("Entre The Min Price (Optional) > ")
max_price = input("Entre The Max Prics (Optional) >")
page = requests.get(f"https://www.cars.com/shopping/results/?&list_price_max=6000&list_price_min={min_price}&makes[]={brand}&models={model}page={page_number}").text
soup = BeautifulSoup(page,'lxml')
cars = soup.find_all("div",class_="vehicle-details")
cars_list = []

def main():
    for car in cars:
        car_name = car.find("h2",class_="title").text.strip()
        car_mileage = car.find("div",class_="mileage").text
        car_price = car.find("span",class_="primary-price").text.strip()
        car_link = car.find("a",class_="vehicle-card-link").get("href")
        full_link = f"https://www.cars.com{car_link}"
        cars_list.append({"Car Name":car_name,"Car Mileage":car_mileage,"Car Price":car_price,"Car Link":full_link})

    keys = cars_list[0].keys()
    with open("cars.csv","w",newline="") as f:
        writer = csv.DictWriter(f,keys)
        writer.writeheader()
        writer.writerows(cars_list)
    print("File Created")
main()