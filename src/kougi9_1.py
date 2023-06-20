# ライブラリのインポート
import numpy as np
import matplotlib.pyplot as plt

# データファイルのパス
data_file1 = 'C:\\toukeidouriki\\03_05.dat'

delta1 = np.loadtxt(data_file1, comments='#', usecols = 2)
delta1=np.sort(delta1)

ave=np.average(delta1)

tot=0
for i in range(len(delta1)):
    tot+=(ave-delta1[i])**2
bunsan=tot/len(delta1)


y=[]
z=0
for i in range(len(delta1)):
    z+=(delta1[i]-ave)**4
z=z/len(delta1)
sendo=(z/(bunsan**2))-3

print("平均値 =",ave)
print("分散 =",bunsan)
print("尖度 =",sendo)

