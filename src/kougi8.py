# ライブラリのインポート
import numpy as np
import matplotlib.pyplot as plt

# データファイルのパス
data_file1 = 'C:\\toukeidouriki\\03_07.dat'
data_file2 = 'C:\\toukeidouriki\\03_08.dat'
data_file3 = 'C:\\toukeidouriki\\03_09.dat'

# データを読み込む
time1 = np.loadtxt(data_file1, comments='#', usecols = 0)
position1 = np.loadtxt(data_file1, comments='#', usecols = 1)
time2 = np.loadtxt(data_file2, comments='#', usecols = 0)
position2 = np.loadtxt(data_file2, comments='#', usecols = 1)
time3 = np.loadtxt(data_file3, comments='#', usecols = 0)
position3 = np.loadtxt(data_file3, comments='#', usecols = 1)


# 平均二乗変位の計算

#データ数
n = 10000 

#データプロット用のリストの作成
msd1 = []
msd2 = []
msd3 = []
time11=[]
time22=[]
time33=[]

#　近似直線を引くためのリストを用意する
ans=[]
time=[]

#　平均二乗変位の計算
#　for文は計算量を減らすために1からデータ数nを100で割った値までで回している
#　dxの計算は位置の差を取っている(ここではsから-sまでの差を取る.)
#　2乗の平均を取る
#　sにおける時刻を格納する
for s in range(1,n//100):
    dx1 = position1[s:] - position1[:-s]
    msd1.append(np.average(dx1**2))
    dx2 = position2[s:] - position2[:-s]
    msd2.append(np.average(dx2**2))
    dx3 = position3[s:] - position3[:-s]
    msd3.append(np.average(dx3**2))
    time11.append(time1[s])
    time22.append(time2[s])
    time33.append(time3[s])
    
    #近似直線を引くためにデータを一か所に格納
    ans.append(np.average(dx1**2))
    ans.append(np.average(dx2**2))
    ans.append(np.average(dx3**2))
    time.append(time1[s])
    time.append(time2[s])
    time.append(time3[s])    

#グラフ形状を両対数グラフにする．
plt.xscale('log')
plt.yscale('log')
plt.ylim(10**(-11), 10**(-9))
plt.xlim(20,120)
# グラフの作成
plt.plot(time11, msd1, 'o', label='Data1',markersize=5)
plt.plot(time22, msd2, '^', label='Data2',markersize=5)
plt.plot(time33, msd3, 's', label='Data3',markersize=5)


# 最小二乗法の直線フィット(近似直線にする)
fit_coeffs = np.polyfit(time, ans, 1)
fit_line = np.polyval(fit_coeffs, time)

# 直線の表示
plt.plot(time, fit_line, 'r-', label='Fit')

# グラフの軸ラベルと凡例
plt.xlabel('Time')
plt.ylabel('Mean Squared Displacement')
plt.legend()

# 傾きの計算
slope = fit_coeffs[0]/2
print(f"傾き:", slope*2)
print(f"拡散係数: {slope:.0e}")

# グラフの表示
plt.show()
