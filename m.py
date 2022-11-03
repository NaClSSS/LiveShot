import pandas as pd

a = pd.read_csv('a.csv', encoding='gbk')
# print(a.shape[0])
# exit()
while True:
    n = input('学号：')
    for i in range(a.shape[0]):
        if n in str(a['学号'][i]):
            print(a.loc[i])

    # c = a['学号'] == n
    # print(a[c])
    # exit()
