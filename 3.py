import matplotlib.pyplot as plt
import japanize_matplotlib
x = [3231, 3747, 3726, 5853, 8866, 10913]
y = [1452, 1796, 1894, 2584, 2735, 3447]
list=["2014年","2015年","2016年","2017年","2018年","2019年"]
plt.scatter(x,y)
plt.xlabel("志願者数(人)")
plt.ylabel("参加者数（人）")
plt.title("オープンキャンパスの志願者数と参加者数の推移")
plt.grid(True)
for i, label in enumerate(list):
    plt.annotate(label, (x[i], y[i]))
plt.show()