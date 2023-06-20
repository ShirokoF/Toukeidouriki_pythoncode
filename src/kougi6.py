import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# フォントをTimes New Romanに設定
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']

time1=[]
position1=[]
q1=[]
data_file = 'C:\\toukeidouriki\\02_01.dat'
time1 = np.loadtxt(data_file, comments='#', usecols = 0)
position1 = np.loadtxt(data_file, comments='#', usecols = 1)
q1 = np.loadtxt(data_file, comments='#', usecols = 2)
ansp=[]
ansq=[]

time4=[]
position4=[]
q4=[]
data_file = 'C:\\toukeidouriki\\02_04.dat'
time4 = np.loadtxt(data_file, comments='#', usecols = 0)
position4 = np.loadtxt(data_file, comments='#', usecols = 1)
q4 = np.loadtxt(data_file, comments='#', usecols = 2)
ansp4=[]
ansq4=[]

time5=[]
position5=[]
q5=[]
data_file = 'C:\\toukeidouriki\\02_05.dat'
time5 = np.loadtxt(data_file, comments='#', usecols = 0)
position5 = np.loadtxt(data_file, comments='#', usecols = 1)
q5 = np.loadtxt(data_file, comments='#', usecols = 2)
ansp5=[]
ansq5=[]

time6=[]
position6=[]
q6=[]
data_file = 'C:\\toukeidouriki\\02_06.dat'
time6 = np.loadtxt(data_file, comments='#', usecols = 0)
position6 = np.loadtxt(data_file, comments='#', usecols = 1)
q6 = np.loadtxt(data_file, comments='#', usecols = 2)
ansp6=[]
ansq6=[]

for i in range(900000):
    if(i>0 and time1[i]-2*(np.pi)*int(time1[i]/(2*np.pi)) < (time1[i+1]-time1[i])/2):
        ansp.append(position1[i])
        ansq.append(q1[i])
        ansp4.append(position4[i])
        ansq4.append(q4[i])
        ansp5.append(position5[i])
        ansq5.append(q5[i])
        ansp6.append(position6[i])
        ansq6.append(q6[i])

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

ax1.set_xlim(1, 5)
ax1.set_ylim(-10, 10)
ax1.set_xlabel("q", size = 5)
ax1.set_ylabel("p", size = 5)
ax1.plot(ansp, ansq, 'o',markersize=0.5,color="red", label="example1")
ax1.legend(loc = 'upper left') #凡例
ax2.set_xlim(1, 5)
ax2.set_ylim(-10, 10)
ax2.set_xlabel("q", size = 5)
ax2.set_ylabel("p", size = 5)
ax2.plot(ansp4, ansq4, 'o',markersize=0.5,color="blue", label="example4")
ax2.legend(loc = 'upper left') #凡例
ax3.set_xlim(1, 5)
ax3.set_ylim(-10, 10)
ax3.set_xlabel("q", size = 5)
ax3.set_ylabel("p", size = 5)
ax3.plot(ansp5, ansq5, 'o',markersize=0.5,color="green", label="example5")
ax3.legend(loc = 'upper left') #凡例
ax4.set_xlim(1, 5)
ax4.set_ylim(-10, 10)
ax4.set_xlabel("q", size = 5)
ax4.set_ylabel("p", size = 5)
ax4.plot(ansp6, ansq6, 'o',markersize=0.5,color="purple", label="example6")
ax4.legend(loc = 'upper left') #凡例
plt.show()