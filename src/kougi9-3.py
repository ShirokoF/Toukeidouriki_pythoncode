import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from scipy.stats import linregress

# フォントをTimes New Romanに設定
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']
plt.rcParams["mathtext.fontset"] = "stix"

# 変位の有限時間平均値を計算する関数
def compute_mean(data, sample_size):
    means = []
    for i in range(len(data) - sample_size + 1):
        mean = np.mean(data[i:i+sample_size])
        means.append(mean)
    return means

# データファイルのパス
data_file1 = 'C:\\toukeidouriki\\03_05.dat'

# データを読み込む
heni1 = np.loadtxt(data_file1, comments='#', usecols=2)

#データ範囲設定
heni1 = heni1[:10000]

# サンプル数ごとに変位の有限時間平均値を計算する
sample_sizes = [1,2,5,10,20,50,100]

# サンプルごとの変位の有限時間平均値を保存するリスト
all_means1 = []
all_means2 = []
all_means3 = []

tot=0
hensa=[]
#関数の実行・保存
for sample_size in sample_sizes:
    means1 = compute_mean(heni1, sample_size)
    x=np.average(means1)
    for i in range(len(means1)):
        tot+=(means1[i]-x)**2
    tot=tot/len(means1)
    hensa.append(np.sqrt(tot))
    tot=0

# 最小二乗フィッティング
slope, intercept, r_value, p_value, std_err = linregress(np.log(sample_sizes), np.log(hensa))
fit_line = np.exp(intercept) * np.power(sample_sizes, slope)
plt.plot(sample_sizes, fit_line, 'r-', label=r'$\mathit{σ} = \mathit{α}\mathit{N}^{-0.5}$')
# グラフのプロット
plt.xscale('log')
plt.yscale('log')
plt.ylim(10**-7, 10**-5)
plt.xlim(1,100)
plt.xlabel('Numbe of samples, $\it{N}$')
plt.ylabel('Standard devitation, $\mathit{σ}$')
plt.plot(sample_sizes,hensa,'o',markersize=5,label='03_05.dat')
plt.legend(loc = 'upper left',fontsize=8)
plt.show()