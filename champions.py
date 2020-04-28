from bs4 import BeautifulSoup
import requests

url= "https://champion.gg/"

#This is the root page of champions here we have all the details of champions and in which lane they play

r=requests.get(url)
soup= BeautifulSoup(r.content,'html.parser')
temp=soup.find_all(style="display:block")
role=[]
final_champ=[]

for i in range(len(temp)):
    temp2=temp[i].get('href').split("/")
    final_champ.append(temp2[2])
    role.append(temp[i].text.strip())

for i in range(len(temp)):
    print(final_champ[i])
    print(role[i])

champ_dict={final_champ[i]:role[i] for i in range(len(final_champ))}
print(champ_dict)