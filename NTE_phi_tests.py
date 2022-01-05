import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir('C:\\Users\\toshi\\Documents\\Georges\\Python\\Master1\\Projet_NTE\\')

from neutron_class import systeme_neutrons

os.chdir('C:\\Users\\toshi\\Documents\\Georges\\Python\\Master1\\Projet_NTE\\data_phi')

"""
N             = 2000
zonex         = [0,0]
zoney         = [-5,5]
p_abs         = 0.001
p_ralentir    = 1/3
p_dif         = 0.5
p_fis         = 0.00375

sn1 = systeme_neutrons(N, zonex, zoney, p_abs, p_ralentir, p_dif, p_fis)

nb_tranches = 50
x_ = np.linspace(-10,10,nb_tranches)



for k in range(len(x_)-1):

    nb_par_tranches = []
    N             = 1000
    zonex         = [x_[k],x_[k+1]]
    zoney         = [-5,5]
    p_abs         = 0.001
    p_ralentir    = 1/3
    p_dif         = 0.5
    p_fis         = 0.00375

    sn1.reset(N, zonex, zoney, p_abs, p_ralentir, p_dif, p_fis)

    for i in range(4000):
        print(k, ' ',i)
        sn1.update()
    for n in range(nb_tranches-1):
        nb_par_tranches.append(len([neut for neut in sn1.list_neut if neut.pos[0]>=x_[n] and neut.pos[0]< x_[n+1]]))

    with open('nb_neut_pos.txt','a') as fichier:
        print(len(sn1.list_neut), file = fichier)

    plt.plot([l for l in x_[0:-1]],nb_par_tranches)
    plt.grid()
    plt.title(f'Repartition des neutrons dans le domaine D, {k}')
    plt.xlabel('Abcisses')
    plt.ylabel('Nombre de neutrons')
    plt.legend()
    plt.savefig(f'repart_neut_{k}')
"""



