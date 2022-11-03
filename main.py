from selenium import webdriver
import time
from PIL import Image

driver = webdriver.Edge('msedgedriver.exe')
driver.get('https://live.bilibili.com/6366787?hotRank=0&session_id=aceba109cb0675845468a909bdb7022f_62794219-714C-44A4-BAB8-7E16E91393BE&launch_id=1000229')
# driver.get('https://live.bilibili.com/24003948?broadcast_type=0&is_room_feed=1&spm_id_from=333.999.0.0')
input('Begin？')
print('OK.')

name = ['a.png']
driver.get_screenshot_as_file(name[0])
j = 1
flag = True
crop = [10, 175, 920, 685]
while True:
    time.sleep(5)
    driver.get_screenshot_as_file(name[0])
    img = Image.open(name[0])
    img.crop(crop).save('ok/%d.png' % j)
    print(crop)
    print('Saved %d' % j)
    if flag:
        s = input('offset:x1, y1, x2, y2:')
        if s == 'ok':
            flag = False
        else:
            s = s.split()
            for i in range(4):
                crop[i] += int(s[i])
    j += 1
