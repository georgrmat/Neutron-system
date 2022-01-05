from neutron_class import systeme_neutrons
import matplotlib.pyplot as plt
from math import log, exp


fichiers_ =  [['psit_pfis0_t5000.txt'     , '0'      ],
              ['psit_pfis00005_t5000.txt' , '0.00005'],
              ['psit_pfis0005_t6000.txt'  , '0.0005' ],
              ['psit_pfis00075_t10000.txt', '0.00075'],
              ['psit_pfis001_t8000.txt'   , '0.001'  ],
              ['psit_pfis0012_t10000.txt' , '0.0012' ],
              ['psit_pfis0015_t10000.txt' , '0.0015' ],
              ['psit_pfis0017_t10000.txt' , '0.0017' ],
              ['psit_pfis002_t10000.txt'  , '0.002'  ],
              ['psit_pfis0025_t10000.txt' , '0.0025' ],
              ['psit_pfis003_t10000.txt'  , '0.003'  ],
              ['psit_pfis0032_t10000.txt' , '0.0032' ],
              ['psit_pfis0035_t10000.txt' , '0.0035' ],
              ['psit_pfis0037_t10000.txt' , '0.0037' ],
              ['psit_pfis0038_t10000.txt' , '0.0038' ],
              ['psit_pfis004_t10000.txt'  , '0.004'  ],
              ['psit_pfis0042_t10000.txt' , '0.0042' ],
              ['psit_pfis0045_t10000.txt' , '0.0045' ],
              ['psit_pfis0047_t10000.txt' , '0.0047' ],
              ['psit_pfis005_t10000.txt'  , '0.005'  ]]

"""
for data in fichiers_:
    nom_fichier  = data[0]
    pfis_fichier = data[1]
    L = []
    with open(nom_fichier, 'r') as fichier:
        for i in fichier:
            L.append(float(i[0:-1]))
    print(L)
    plt.plot([k for k in range(len(L))], L, label = pfis_fichier)
plt.grid()
plt.legend()
plt.xlabel('Nemps (en itérations)')
plt.ylabel('Nombre de neutrons')
plt.title('Evolution du nombre de neutrons en fonction du temps en itérations')
plt.show()








for data in fichiers_:
    moyennes = []

    log_psi = []
    with open(nom_fichier, 'r') as fichier:
        for i in fichier:
            log_psi.append(log(float(i[0:-1])))
        T = len(log_psi)
        for i in np.arange(100,T,100):
            petite_moy = T[i]-T[i-100]
        moyennes.append(petit_moyenne)
        lambda_ = log(psi[-1])-log(psi[T//2])/(T/2)
        lambdas.append(lambda_)
        pfisz.append(float(pfis_fichier))
    res = 0
    for i in moyennes:
        res += i
    print(res/len(moyennes))


pfisz = []
lambdas = []

for data in fichiers_:
    nom_fichier  = data[0]
    pfis_fichier = data[1]
    psi = []
    with open(nom_fichier, 'r') as fichier:
        for i in fichier:
            psi.append(float(i[0:-1]))
    T = len(psi)
    print(T)
    lambda_ = (log(psi[-1])-log(psi[T//2]))/(T/2)
    print(lambda_)
    lambdas.append(lambda_)
    pfisz.append(float(pfis_fichier))

# psi2 = []
# with open('psit_pfis0039_t30000_nb20.txt', 'r') as fichier:
#     for i in fichier:
#         psi2.append(float(i[0:-1]))
#     lambda2 = log(psi2[-1]-log(psi2[15000]))/15000

plt.plot(pfisz,lambdas,'-')
plt.xlabel('$p_\mathrm{fis}$')
plt.ylabel('$\lambda_*$')
plt.title('Evoluton de $\lambda_*$ en fonction de $p_\mathrm{fis}$')
plt.grid()
plt.show()
"""


cg_phi = []
lambdas = []
pfisz = []
psi_dernier = []
T_ = []
with open('lambda_star.txt', 'r') as fichier:
    for i in fichier:
        lambdas.append(float(i[0:-1]))




for data in fichiers_:
    psi = []
    nom_fichier  = data[0]
    pfis_fichier = data[1]
    pfisz.append(pfis_fichier)
    L = []
    with open(nom_fichier, 'r') as fichier:
        for i in fichier:
            psi.append(float(i[0:-1]))
    T_.append(len(psi))
    psi_dernier.append(psi[-1])



for i in range(len(lambdas)):

    cg_phi.append(exp(-lambdas[i]*T_[i])*psi_dernier[i])
plt.plot(pfisz, cg_phi)
plt.show()














