# 3D Bounching Ball ~ Yavuz Selim Büke-2022 

import numpy as np
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Metre/saniye^2 cinsinden yer çekimi kuvveti tanımı
g = 9.80655


# Yer çekimi için ivme vektörü. (a = acceleration == İvme)
ag = np.array((0, 0, -g))

# Sıçrama sonrası ve öncesi hız oranı
cor = 0.9

# 1milisaniye delta t
delta_t = 0.001

# Simülasyona dahil olacak top sayısı
num_balls = 64

# X, y ve Z eksenlerinin boyutları
size = 20

# Topların renk parametreleri ile listeden obje ataması.

colors = ['b', 'g', 'r', 'y', 'm']

# İlk bakış açımız

yuksek = 30
alcak = 30

# Eksenlerin sınırlarını belirleme, Her biri 0'dan belirlediğimiz boyuta kadar.
xlim = (0,size)
ylim = (0,size)
zlim = (0,size)

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
ax.set_zlim(zlim)
ax.view_init(yuksek, alcak)

# Top Sınıfı Oluşturma.

class Ball:
    def __init__(self, xyz, v, fmt):
        self.xyz = np.array(xyz)
        self.v = np.array(v)

        self.scatter, = ax.plot([], [], [], fmt, animated = True)
    
    # Güncelleştirme

    def update(self):
        
        # Topun X ekseninin başlangıç kısımlarına çarpma durumu.
        
        if self.xyz[0] <= xlim[0]:
            self.v[0] = cor * np.abs(self.v[0]) 
                # Mutlak değere alarak topu tam aksine zıplattık.

        # Topun X ekseninin bitiş kısımlarına çarpma durumu.

        elif self.xyz[0] >= xlim[1]:
            self.v[0] = - cor * np.abs(self.v[0])

        # Topun Y ekseninin başlangıç kısımlarına çarpma durumu.

        if self.xyz[1]  <= ylim[0]:
            self.v[1] = cor * np.abs(self.v[1])

        # Topun Y ekseninin bitiş kısımlarına çarpma durumu.

        elif self.xyz[1] >= ylim[1]:
            self.v[1] = - cor * np.abs(self.v[1])

        # Topun Z ekseninin başlangıç kısımlarına çarpma durumu.

        if self.xyz[2] <= zlim[0]:
            self.v[2] = cor * np.abs(self.v[2])

        # Topun Z ekseninin bitiş kısımlarına çarpma durumu.

        elif self.xyz[2] >= zlim[1]:
            self.v[2] = - cor * np.abs(self.v[2])
        
        if self.xyz[2] >= 0:
            air_friction = (3 * 1**2 * 1 * (delta_t * ag)**2)
            self.v -= air_friction
        
        for j in range(11):
            if self.xyz[2] == 0:
                j + 1
                if j >= 10:
                    self.v -=self.v * 0.15 
                        # Bu bloktaki 0.15 ground friction olarak kabul edilmiştir.

        delta_v = (delta_t * ag)
        self.v += delta_v 
        self.xyz += self.v

        # Topların eksenlerde hapis kalmasını sağlamak. (Aralık verip geri kalanları kırpma işlemi.)
        self.xyz[0] = np.clip(self.xyz[0], xlim[0], xlim[1])
        self.xyz[1] = np.clip(self.xyz[1], ylim[0], ylim[1])
        self.xyz[2] = np.clip(self.xyz[2], zlim[0], zlim[1])

        self.scatter.set_xdata(self.xyz[0])
        self.scatter.set_ydata(self.xyz[1])
        self.scatter.set_3d_properties(self.xyz[2])

# Rastgele renklerde, pozisyonlarda ve hızlarda toplar oluşturma kısmı.

balls = []

for i in np.arange(0, num_balls):
    xyz = np.random.rand(1,3)[0]*size
    v = np.random.rand(1,3)[0]*0.1
    fmt = str(colors[np.random.randint(0, len(colors))] + 'o')
    balls.append(Ball(xyz, v, fmt))



def init():
    return []

def update(t):
    
    global yuksek, alcak

    for ball in balls:
        ball.update()

    oyuncular = [ball.scatter for ball in balls]

    # Görüntüyü Çevirme Kısmı.

    alcak = alcak + t/2
    ax.view_init(yuksek, alcak)

    oyuncular.append(ax)

    return oyuncular

ani = FuncAnimation(fig, update, frames = np.arange(0,0.5, delta_t), init_func = init, interval = 10, blit = True, repeat = True)
#ani.save('3D_Ball.gif', writer='imagemagick', fps = 60)
plt.show() 