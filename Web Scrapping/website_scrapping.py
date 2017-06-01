import requests
from bs4 import BeautifulSoup

r = requests.get("http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c= r.content

soup = BeautifulSoup(c, "html.parser")

all = soup.find_all("div", {"class":"propertyRow"})
#print(all[0].find("h4", {"class":"propPrice"}).text.replace("\n","").strip())

for item in all:
	print(item.find("h4", {"class":"propPrice"}).text.replace("\n","").strip())
	print(item.find_all("span", {"class":"propAddressCollapse"})[0].text)
	print(item.find_all("span", {"class":"propAddressCollapse"})[1].text)
	try:
		print(item.find("span", {"class":"infoBed"}).find("b").text)
	except:
		print(None)
	try:
		print(item.find("span", {"class":"infoSqFt"}).find("b").text)
	except:
		print(None)
	try:
		print(item.find("span", {"class":"infoValueFullBath"}).find("b").text)
	except:
		print(None)
	try:
		print(item.find("span", {"class":"infoValueHalfBath"}).find("b").text)
	except:
		print(None)

	for column_group in item.find_all("div",{"class":"columnGroup"}):
		for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}), column_group.find_all("span",{"class":"featureName"})):
			if "Lot Size" in feature_group.text:
				print(feature_name.text)


	print(" ")
