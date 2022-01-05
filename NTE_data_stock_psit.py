import os
os.chdir('C:\\Users\\toshi\\Documents\\Georges\\Python\\Master1\\Projet_NTE\\')

from neutron_class import systeme_neutrons

N             = 2000
zonex         = [-0.2,-0.2]
zoney         = [-5,5]
p_abs         = 0.001
p_ralentir    = 1/3
p_dif         = 0.5
p_fis         = 0.00375

sn1 = systeme_neutrons(N, zonex, zoney, p_abs, p_ralentir, p_dif, p_fis)

# tps_simul = 10000
# nb_moyen  = 1
#
# os.chdir('C:\\Users\\toshi\\Documents\\Georges\\Python\\Master1\\Projet_NTE\\data_psit\\tests2')
# nom_fichier = 'psit_pfis00075_t10000.txt'
#
# G = [0 for k in range(tps_simul)]
# for i in range(nb_moyen):
#     sn1.reset(N, x, y, p_abs, p_ralentir, p_dif, p_fis)
#     L = []
#     for j in range(tps_simul):
#         print(i," ",j, len(sn1.list_neut))
#         sn1.update()
#         L.append(len(sn1.list_neut))
#         if len(sn1.list_neut) == 0:
#             L += [0 for k in range(tps_simul-j)]
#             break
#     for k in range(len(G)):
#         G[k] += L[k]
# psi_t = [1/nb_moyen*k for k in G]
#
#
# with open(nom_fichier,'w') as fichier:
#     for nb in psi_t:
#         print(nb, file = fichier)