import os
os.chdir('C:\\Users\\toshi\\Documents\\Georges\\Python\\Master1\\Projet_NTE\\')
#os.chdir('') permet de se placer dans le dossier où se trouve le fichier neutron_class
# par exemple os.chdir('C:\\User1\\Documents\\NTE\\')

import matplotlib.pyplot as plt
import numpy as np
from random import random, uniform
from neutron_class import systeme_neutrons

N             = 10
zonex         = [-10,10]
zoney         = [-5,5]
p_abs         = 0.001
p_ralentir    = 1/3
p_dif         = 0.5
p_fis         = 0.00005

sn1 = systeme_neutrons(N, zonex, zoney, p_abs, p_ralentir, p_dif, p_fis)








