import json

from selenium import webdriver
import time
from PIL import Image
import matplotlib.pyplot as plt

url = 'https://live.bilibili.com/24003948?broadcast_type=0&is_room_feed=1&spm_id_from=333.999.0.0'
driver = webdriver.Edge('msedgedriver.exe')
driver.get(url)
driver.delete_all_cookies()
with open('c') as f:
    c = json.loads(f.read())
for a in c:
    driver.add_cookie(a)
driver.get(url)

input('Begin？')
print('OK.')

name = ['a.png']
j = 1
flag = True
crop = [10, 175, 920, 685]
while True:
    time.sleep(3.6)
    driver.get_screenshot_as_file(name[0])
    img = Image.open(name[0])
    t = img.crop(crop).save('ok/%d.png' % j)
    print(crop)
    print('Saved %d' % j)
    if flag:
        plt.imshow(img.crop(crop))
        plt.show()
        s = input('offset:x1, y1, x2, y2:')
        if s == 'ok':
            flag = False
        else:
            s = s.split()
            for i in range(4):
                crop[i] += int(s[i])
    j += 1
