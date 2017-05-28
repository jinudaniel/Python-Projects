import time
from datetime import datetime as dt
import configparser

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

config = configparser.ConfigParser()
config.read("config.txt")

# get the values from config file
website_list = config["Default"]["website"].split(",")
start_hour = int(config["Default"]["start_hour"])
end_hour = int(config["Default"]["end_hour"])

while True:
	if (dt(dt.now().year, dt.now().month, dt.now().day, start_hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end_hour)):
		
		with open(hosts_path, "r+") as file:
			content = file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect + " " + website + "\n")
	
	else:
		with open(hosts_path, "r+") as file:
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()
				
	time.sleep(5)	
		

