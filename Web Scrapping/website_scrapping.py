import requests
import pandas
from bs4 import BeautifulSoup

# Extract the total number of pages
r = requests.get("http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c= r.content
soup = BeautifulSoup(c, "html.parser")
page_nbr = int(soup.find_all("a",{"class":"Page"})[-1].text)

elements = []
base_url = "http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="

#iterate through all the pages and extract the elements needed
for page in range(0, page_nbr*10, 10):
	
	r = requests.get(base_url + str(page) +".html")
	c= r.content
	soup = BeautifulSoup(c, "html.parser")
	all = soup.find_all("div", {"class":"propertyRow"})

	for item in all:
		d = {}
		
		d["Address"] = item.find_all("span", {"class":"propAddressCollapse"})[0].text
		d["Locality"] = item.find_all("span", {"class":"propAddressCollapse"})[1].text
		d["Price"] = item.find("h4", {"class":"propPrice"}).text.replace("\n","").strip()

		try:
			d["Beds"] = item.find("span", {"class":"infoBed"}).find("b").text
		except:
			d["Beds"] = None
		try:
			d["Area"] = item.find("span", {"class":"infoSqFt"}).find("b").text
		except:
			d["Area"] = None
		try:
			d["Full Baths"] = item.find("span", {"class":"infoValueFullBath"}).find("b").text
		except:
			d["Full Baths"] = None
		try:
			d["Half Baths"] = item.find("span", {"class":"infoValueHalfBath"}).find("b").text
		except:
			d["Half Baths"] = None

		# Extract the lot size
		for column_group in item.find_all("div",{"class":"columnGroup"}):
			for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}), column_group.find_all("span",{"class":"featureName"})):
				if "Lot Size" in feature_group.text:
					d["Lot Size"] = feature_name.text

		elements.append(d)
		
#add the elements to a dataframe and export it to a csv file		
df = pandas.DataFrame(elements)
df.to_csv("Output.csv")