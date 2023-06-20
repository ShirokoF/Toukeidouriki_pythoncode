import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# フォントをTimes New Romanに設定
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']

# 変位の有限時間平均値を計算する関数
def compute_mean(data, sample_size):
    means = []
    for i in range(len(data) - sample_size + 1):
        mean = np.mean(data[i:i+sample_size])
        mean = mean * (10**6)
        means.append(mean)
    return means

# データファイルのパス
data_file1 = 'C:\\toukeidouriki\\03_07.dat'
data_file2 = 'C:\\toukeidouriki\\03_08.dat'
data_file3 = 'C:\\toukeidouriki\\03_09.dat'

# データを読み込む
heni1 = np.loadtxt(data_file1, comments='#', usecols=2)
heni2 = np.loadtxt(data_file2, comments='#', usecols=2)
heni3 = np.loadtxt(data_file3, comments='#', usecols=2)

#データ範囲設定
heni1 = heni1[:10000]
heni2 = heni2[:10000]
heni3 = heni3[:10000]



# サンプル数ごとに変位の有限時間平均値を計算する
sample_sizes = [1, 10, 100]

# サンプルごとの変位の有限時間平均値を保存するリスト
all_means1 = []
all_means2 = []
all_means3 = []

#関数の実行・保存
for sample_size in sample_sizes:
    means1 = compute_mean(heni1, sample_size)
    means2 = compute_mean(heni2, sample_size)
    means3 = compute_mean(heni3, sample_size)
    all_means1.append(means1)
    all_means2.append(means2)
    all_means3.append(means3)

# グラフのプロット
labels = ['unit1', 'unit10', 'unit100']
colors = ['red', 'green', 'blue']
markers=['s','o','^']
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

ax1.set_xlim(-3, 3)
ax1.set_ylim(0, 0.3)
ax1.set_title(f"03_07.dat")
ax1.set_xlabel("Finite mean of displacement", size = 10)
ax1.set_ylabel("Fraction", size = 10)

ax2.set_xlim(-3, 3)
ax2.set_ylim(0, 0.3)
ax2.set_title(f"03_08.dat")
ax2.set_xlabel("Finite mean of displacement", size = 10)
ax2.set_ylabel("Fraction", size = 10)

ax3.set_xlim(-3, 3)
ax3.set_ylim(0, 0.3)
ax3.set_title(f"03_09.dat")
ax3.set_xlabel("Finite mean of displacement", size = 10)
ax3.set_ylabel("Fraction", size = 10)

#各ファイルについてプロットする操作
for i, means in enumerate(all_means1):
    freq, bins = np.histogram(means, bins=30)
    freq=freq/10000
    bin_centers = (bins[:-1] + bins[1:]) / 2
    ax1.plot(bin_centers, freq,markersize=3, linestyle='solid',marker=markers[i],label=labels[i], color=colors[i],linewidth=0.4)


for i, means in enumerate(all_means2):
    freq, bins = np.histogram(means, bins=30)
    freq=freq/10000
    bin_centers = (bins[:-1] + bins[1:]) / 2
    ax2.plot(bin_centers, freq,markersize=3, linestyle='solid',marker=markers[i],label=labels[i], color=colors[i],linewidth=0.4)

for i, means in enumerate(all_means3):
    freq, bins = np.histogram(means, bins=30)
    freq=freq/10000
    bin_centers = (bins[:-1] + bins[1:]) / 2
    ax3.plot(bin_centers, freq,markersize=3, linestyle='solid',marker=markers[i],label=labels[i], color=colors[i],linewidth=0.4)

ax1.legend(loc = 'upper left',fontsize=8) #凡例
ax2.legend(loc = 'upper left',fontsize=8) #凡例
ax3.legend(loc = 'upper left',fontsize=8) #凡例
plt.subplots_adjust(hspace=0.5,wspace=0.3)
plt.show()