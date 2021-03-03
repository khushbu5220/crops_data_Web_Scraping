#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import re
import json 

crop_links = ['https://www.apnikheti.com/en/pn/agriculture/crops/cereals/barley-jow', 'https://www.apnikheti.com/en/pn/agriculture/crops/cereals/maize-kharif', 'https://www.apnikheti.com/en/pn/agriculture/crops/cereals/maize-rabi', 'https://www.apnikheti.com/en/pn/agriculture/crops/cereals/oats', 'https://www.apnikheti.com/en/pn/agriculture/crops/cereals/pearl-millet', 'https://www.apnikheti.com/en/pn/agriculture/crops/cereals/rice', 'https://www.apnikheti.com/en/pn/agriculture/crops/cereals/wheat-kanak-gehu', 'https://www.apnikheti.com/en/pn/agriculture/crops/fibre-crops/cotton', 'https://www.apnikheti.com/en/pn/agriculture/crops/fodder/bajra-napier-hybrid', 'https://www.apnikheti.com/en/pn/agriculture/crops/fodder/berseem', 'https://www.apnikheti.com/en/pn/agriculture/crops/fodder/finger-millet', 'https://www.apnikheti.com/en/pn/agriculture/crops/fodder/guar', 'https://www.apnikheti.com/en/pn/agriculture/crops/fodder/guinea-grass', 'https://www.apnikheti.com/en/pn/agriculture/crops/fodder/lucerne', 'https://www.apnikheti.com/en/pn/agriculture/crops/fodder/senji-hybrid', 'https://www.apnikheti.com/en/pn/agriculture/crops/fodder/shaftal', 'https://www.apnikheti.com/en/pn/agriculture/crops/fodder/sorghum', 'https://www.apnikheti.com/en/pn/agriculture/crops/fodder/teosinte', 'https://www.apnikheti.com/en/pn/agriculture/crops/green-manure/cowpea', 'https://www.apnikheti.com/en/pn/agriculture/crops/green-manure/dhaincha', 'https://www.apnikheti.com/en/pn/agriculture/crops/green-manure/mesta', 'https://www.apnikheti.com/en/pn/agriculture/crops/green-manure/sunhemp', 'https://www.apnikheti.com/en/pn/agriculture/crops/oilseeds/groundnut', 'https://www.apnikheti.com/en/pn/agriculture/crops/oilseeds/linseed-flax', 'https://www.apnikheti.com/en/pn/agriculture/crops/oilseeds/mustard', 'https://www.apnikheti.com/en/pn/agriculture/crops/oilseeds/safflower', 'https://www.apnikheti.com/en/pn/agriculture/crops/oilseeds/soybean', 'https://www.apnikheti.com/en/pn/agriculture/crops/oilseeds/sunflower', 'https://www.apnikheti.com/en/pn/agriculture/crops/pulses/lentil-masur', 'https://www.apnikheti.com/en/pn/agriculture/crops/pulses/bengal-gram-chickpea', 'https://www.apnikheti.com/en/pn/agriculture/crops/pulses/green-gram-moong', 'https://www.apnikheti.com/en/pn/agriculture/crops/pulses/kidney-bean-rajma', 'https://www.apnikheti.com/en/pn/agriculture/crops/pulses/mash-urd', 'https://www.apnikheti.com/en/pn/agriculture/crops/pulses/pigeon-pea-tur', 'https://www.apnikheti.com/en/pn/agriculture/crops/pulses/ricebean', 'https://www.apnikheti.com/en/pn/agriculture/crops/sugar-and-starch-crops/sugarcane', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/citrus/lemon', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/citrus/lime-nimboo', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/flowers/carnation', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/flowers/chrysanthemum', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/flowers/gerbera', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/flowers/gladiolus', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/flowers/jasmine', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/flowers/marigold', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/flowers/rose', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/flowers/tuberose-rajnigandha', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/forestry/drek', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/forestry/eucalyptus', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/forestry/poplar', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/forestry/sagwan', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/fruit/banana', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/fruit/ber', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/fruit/date-palm', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/fruits/grapes', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/fruit/guava', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/fruit/jamun', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/fruit/kinnow', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/fruit/litchi', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/fruit/loquat', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/fruit/mango', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/fruit/mulberry', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/fruit/muskmelon', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/fruit/orange-mandarins-santra', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/fruit/papaya', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/fruit/peach', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/fruit/pear-nashpati', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/fruit/plum', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/fruit/pomegranate', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/fruit/sapota', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/fruit/sweet-oranges-malta', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/fruit/watermelon', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/medicinal-plants/aloe-vera', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/medicinal-plants/amla', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/medicinal-plants/ashwagandha', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/medicinal-plants/bahera', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/medicinal-plants/bhumi-amalaki', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/medicinal-plants/brahmi', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/medicinal-plants/dill-seeds', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/medicinal-plants/honey', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/medicinal-plants/indian-bael', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/medicinal-plants/kalihari', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/medicinal-plants/lemon-grass', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/medicinal-plants/mulethi', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/medicinal-plants/neem', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/medicinal-plants/pudina', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/medicinal-plants/sadabahar', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/medicinal-plants/safed-musli', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/medicinal-plants/sarpagandha', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/medicinal-plants/shankhpushpi', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/medicinal-plants/shatavari', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/medicinal-plants/stevia', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/medicinal-plants/sweet-flag', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/medicinal-plants/tulsi', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/plantation-crops/fig', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/spice-and-condiments/coriander', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/spice-and-condiments/fennel', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/spice-and-condiments/fenugreek', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/spice-and-condiments/ginger-adrakh', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/spice-and-condiments/turmeric-haldi', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/arum-arvi', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/ash-gourd', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/beetroot', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/bitter-gourd', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/bottle-gourd', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/brinjal', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/broccoli', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/cabbage', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/capsicum', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/carrot', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/cauliflower', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/celery', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/chilli', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/cucumber', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/garlic', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/kharif-onion-pyaz', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/lettuce', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/long-melon', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/mushroom', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/okra', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/peas', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/potato', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/pumpkin', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/rabi-onion-pyaz', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/radish', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/spinach', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/sponge-gourd', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/squash-melon', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/summer-squash', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/sweet-potato', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/tomato', 'https://www.apnikheti.com/en/pn/agriculture/horticulture/vegetable-crops/turnip']



def writeJsonToFile(web_url):
    r = requests.get(web_url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    crop_data = {}
    #crop name
    key = "name"
    value = soup.find("div", class_="inner-crop-header").find("h1").get_text().strip()
    crop_data[key] = value

    # # First part  
    # data = soup.find_all("article", class_="crop-info-repeater")[0]
    # key = data.find("h2").get_text()
    # value = data.find("p").get_text()
    # crop_data[key] = value


    # # Second part 
    # data = soup.find("article", class_="crop-info-repeater climate-info")
    # key = data.find("h2").get_text()
    # value = data.find("h4").get_text()
    # temp = data.find("div", class_="winter-Temp").get_text()
    # crop_data[key[value]] = temp 


    # # third part
    # data = soup.find_all("article", class_="crop-info-repeater")[5]
    # key = data.find("h2").get_text()
    # value = data.find("p").get_text()
    # crop_data[key] = value

    # # 4 part
    # data = soup.find_all("article", class_="crop-info-repeater")[6]
    # key = data.find("h2").get_text()
    # value = data.find("p").get_text()
    # crop_data[key] = value

    # # 5 part
    # data = soup.find_all("article", class_="crop-info-repeater")[7]
    # key = data.find("h2").get_text()
    # value = data.find("p").get_text()
    # crop_data[key] = value

    # # 6 part
    # data = soup.find_all("article", class_="crop-info-repeater")[8]
    # key = data.find("h2").get_text()
    # value = data.find("p").get_text()
    # crop_data[key] = value

    # # 7 part
    # data = soup.find_all("article", class_="crop-info-repeater")[9]
    # key = data.find("h2").get_text()
    # value = data.find("p").get_text()
    # crop_data[key] = value

    # 8 part
    data = soup.find_all("article", class_="crop-info-repeater")[10]
    key = data.find("h2").get_text()
    value = data.find("p").get_text()
    crop_data[key] = value


    jsonData = json.dumps(crop_data)

    with open('cropsdb.json', 'a') as outfile:
        outfile.write(jsonData)
        outfile.write(",\n")
        outfile.close()
    

# writeJsonToFile("https://www.apnikheti.com/en/pn/agriculture/crops/cereals/barley-jow")


for each in crop_links:
    writeJsonToFile(each)


# temp = soup.find_all("div", class_="climate-body")
# print(temp[0].get_text())