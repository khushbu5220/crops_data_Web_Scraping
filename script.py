import requests
from bs4 import BeautifulSoup
import json 
url = "https://www.apnikheti.com/en/pn/agriculture/crops/cereals/barley-jow"

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify) 


crop_data = {}

key = "name"
# crop name 
value = soup.find("div", class_="inner-crop-header")
value = value.find("h1").get_text().strip()


crop_data[key] = value



# First part  
data = soup.find_all("article", class_="crop-info-repeater")[0]
key = data.find("h2").get_text()
value = data.find("p").get_text()

crop_data[key] = value



# # Second part 
# key = soup.find("article", class_="crop-info-repeater climate-info")
# value = key.get_text()
# print(value.strip())
                            # # second part 1-4
                            # key = soup.find_all("article", class_="crop-info-repeater")[1]   
                            # print(key.get_text())
# # third part
# key = soup.find_all("article", class_="crop-info-repeater")[5]
# print(key.get_text())




# forth part 
# key = soup.find_all("article", class_="crop-info-repeater")[6]
# print(key.get_text())
# # fifth part 
# key = soup.find_all("article", class_="crop-info-repeater")[7]
# print(key.get_text())
# # sixth part
# key = soup.find_all("article", class_="crop-info-repeater")[8]
# print(key.get_text())
#                             # testing in sixth part
#                             # key = soup.find_all("article", class_="crop-info-repeater")[8]
#                             # value = key.find_all("p")
#                             # next = key.find_all("strong")
#                             # print(next)
# # seventh part
# key = soup.find_all("article", class_="crop-info-repeater")[9]
# print(key.get_text())
# # eighth part
# key = soup.find_all("article", class_="crop-info-repeater")[10]
# print(key.get_text())
#                             # trial fertilizer
#                             # key = soup.find_all("article", class_="crop-info-repeater")[10]
#                             # value = key.find_all("tbody")[1]
#                             # next = value.find_all("tr")[0]
#                             # nex = next.find_all("td")[0]
#                             # print(nex)
# # ninth part
# key = soup.find_all("article", class_="crop-info-repeater")[11]
# print(key.get_text())
# # tenth part
# key = soup.find_all("article", class_="crop-info-repeater")[12]
# print(key.get_text())
# # eleventh part
# key = soup.find_all("article", class_="crop-info-repeater")[13]
# print(key.get_text())
#                             # trial eleventh part
#                             # key = soup.find_all("article", class_="crop-info-repeater")[13]
#                             # value = key.find("div", class_="more")
#                             # next = value.find_all("p")[1]
#                             # nex = next.find_all("strong")
#                             # print(next)
# # twelfth part
# key = soup.find_all("article", class_="crop-info-repeater")[14]
# print(key.get_text())
# # thirteenth part
# key = soup.find_all("article", class_="crop-info-repeater")[15]
# print(key.get_text())
# # forteenth part
# key = soup.find_all("article", class_="crop-info-repeater")[16]
# print(key.get_text())
# # fifteenth part
# key = soup.find_all("article", class_="crop-info-repeater")[17]
# print(key.get_text())
# # sixteenth part
# key = soup.find_all("article", class_="crop-info-repeater")[18]
# print(key.get_text())
# # seventeenth part
# key = soup.find_all("article", class_="crop-info-repeater")[19]
# print(key.get_text())
# # eighteenteenth part
# key = soup.find_all("article", class_="crop-info-repeater")[20]
# print(key.get_text())
# # nineteenth part
# key = soup.find_all("article", class_="crop-info-repeater")[21]
# print(key.get_text())
# # twentyth part
# key = soup.find_all("article", class_="crop-info-repeater")[22]
# print(key.get_text())
# # twentyone part
# key = soup.find_all("article", class_="crop-info-repeater")[23]
# print(key.get_text())
# # twentytwo part
# key = soup.find_all("article", class_="crop-info-repeater")[24]
# print(key.get_text())



# print(crop_data)
print(json.dumps(crop_data))
