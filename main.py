import requests
from bs4 import BeautifulSoup as bs

github_user = input("Enter name of Github User :- ")

url = "https://github.com/"+github_user
req = requests.get(url)
soup = bs(req.content , 'html.parser')
#not mandatory to write in other file , it is just for sake of convinience
f = open("demofile2.html", "w")
f.write(str(soup))
profile_img_url = soup.find('img',{'alt':'@'+github_user})['src']
n = profile_img_url.index("s=88")
profile_img = profile_img_url[0:n] + "v=4"
print(profile_img)

#Similarly we can fetch other files using different tags