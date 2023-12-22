import numpy as np

# 2つの点p, qの座標位置の配列を定義
p = np.array([1, 2, 3, 4])
q = np.array([4, 3, 2, 1])
# 2点間のユークリッド距離を計算する
dist = np.linalg.norm(p - q)
print(dist) 
# 出力結果：5.830951894845301