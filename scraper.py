import requests
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com/"

response = requests.get(url)

if response.status_code == 200:
    print("Successfully fetched the webpage")
    
    soup = BeautifulSoup(response.text , "html.parser")
    
    headlines= []
    
    for h2_tag in soup.find_all("h2"):
        headline = h2_tag.get_text(strip=True)
        headlines.append(headline)
        
    with open("headlines.txt", "w" ,encoding="utf-8") as file :
        for line in headlines :
            file.write(line + "\n")
            
            print(f"H2 tag  Headline  :  {line}")
            
    print("headlines Scareped successfully and saved to hedalines.text file")
else:
    print(f"failed to fetch the webpage url with status code :{response.status_code}")
        