import requests
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint

URL_ENDPOINT = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/"

results = []
for page in range(1,2):
    url = f"{URL_ENDPOINT}{page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    rows = (soup.find_all(class_="data-table__row"))
    for row in rows:
        cols = row.find_all(class_="data-table__value")
        try:
            hm = int((cols[5].text).split("%")[0])
        except ValueError:
            hm = "-"
        finally:
            data = {
                "Rank": int(cols[0].text),
                "Major": f"{cols[1].text}-{cols[2].text}",
                "Early Career Pay": int("".join(str(cols[3].text).split("$")[1].split(","))),
                "Mid-Career Pay": int("".join(str(cols[4].text).split("$")[1].split(","))),
                "High Meaning%": hm
            }
        results.append(data)

pprint(results)
# final_data = pd.DataFrame(results)
# final_data.to_csv("data.csv",index=False)
