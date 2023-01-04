from saucenao_api import SauceNao

import os, random
# Replace the key with your own
minsim='80!'
sauce = SauceNao('c6648cad510b683fc9767a185ef7bb9a57207320')
Randfile = random.choice(os.listdir("C:\\Users\\ashle\\Desktop\\Python attempts\\sort batch"))
f = open('C:\\Users\\ashle\\Desktop\\Python attempts\\sort batch\\' + Randfile , 'rb')
print("File Sent - " + Randfile) 
results = sauce.from_file(f) 
f.close() 
# sauce.from_url('') 

thumbnail = results[0].thumbnail     # temporary URL for picture preview
similarity = results[0].similarity   # 93.3
title = results[0].title             # めぐみん
urls = results[0].urls               # ['https://www.pixiv.net/member_illust.php?mode=medium&illust_id=77630170']
author = results[0].author           # frgs
raw = results[0].raw                 # raw result


#print(thumbnail)
#print(urls)
#print(similarity)
#print(title)
#print(author)
print(raw)

