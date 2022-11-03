from selenium import webdriver
import time
from PIL import Image

driver = webdriver.Edge('msedgedriver.exe')
# driver.get('https://live.bilibili.com/6910388?hotRank=0&session_id=02091566372f3aa7925c2c1d43cbf7f0_724D7439-DB6C-4319-9182-6CBFD3CC0989&launch_id=1000229')
driver.get('https://live.bilibili.com/24003948?broadcast_type=0&is_room_feed=1&spm_id_from=333.999.0.0')
input('Begin:')
print('OK.')

name = ['a.png']
driver.get_screenshot_as_file(name[0])
j = 1

while True:
    time.sleep(5)
    driver.get_screenshot_as_file(name[0])
    img = Image.open(name[0])
    img.crop((10, 175, 920, 685)).save('ok/%d.png' % j)
    print('Saved %d' % j)
    j += 1
