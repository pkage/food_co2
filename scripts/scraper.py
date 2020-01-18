from bs4 import BeautifulSoup
import requests
import json

doc = requests.get("https://www.thelifeimpact.com/carbon-footprint-of-foods").text
soup = BeautifulSoup(doc, 'html.parser')

data = []

for ul in soup.find_all("ul"):
    try:
        if ul.previous.previous["id"] != "block-yui_3_17_2_1_1556431745228_679394":
            for li in ul.find_all("li"):
                if len(li.find_all("strong")) > 0:
                    co2 = li.find("strong").text
                    keywords = li.contents[0].contents[0].decode("utf8").split(",")
                    for keyword in keywords:
                        if len(keyword.strip(" ")) == 0:
                            del keywords[keywords.index(keyword)]
                        else:
                            keywords[keywords.index(keyword)] = keyword.strip(" ")
                    data.append({
                        "co2": co2,
                        "keywords": keywords
                    })
    except:
        continue
with open("pollution.json", "w+") as outfile:
    outfile.write(json.dumps(data))
