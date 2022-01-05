import numpy as np
from random import random,randint,uniform



class neutron2d:

    def __init__(self,r,v):
        self.pos = r
        self.vel = v

lim_gauche = -10   # limite physique a gauche
lim_droite = 10    # limite physique a droite
lim_haut   = 5     # limite physique en haut
lim_bas    = -5    # limite physique en bas


  # probabilite de fission
p_dif = 0.01    # probabilite de diffusion
p_abs = 0.001   # probabilite d absorption
p_r_l = 1/2     # probabilite de passer de vitesse rapide a lente
p_l_r = 1/2     # probabilite de passer de vitesse lente a rapide


v_rap = 0.4   # vitesse rapide
v_len = 0.1   # vitesse lente

# fonction qui fait avancer le neutron en le gardant dans la figure
def avancer(r,v,lg,ld):

    if r[0] - abs(v[0]) < lg or r[0] + abs(v[0]) > ld:
        v = [-v[0],v[1]]
        r[0] += v[0]
        r[1] += v[1]

    if r[1] - abs(v[1]) < lg or r[1] + abs(v[1]) > ld:
        v = [v[0],-v[1]]
        r[0] += v[0]
        r[1] += v[1]


# simulation
def simul_neut(N,T):

    x        = []
    for i in range(N):
        teta = uniform(0,2*np.pi)
        x.append(neutron2d([0,0],[np.cos(teta)*v_len , np.sin(teta)*v_len]))
    fissionsx = []
    fissionsy = []
    absorpx   = []
    absorpy   = []
    nb_fiss   = 0
    nb_absor  = 0
    p_ = []

    for t in range(T):

        p_fis = (1-len(x)/500)*0.1
        p_fis*=(p_fis>0)
        print(p_fis)
        p_.append(p_fis)
        for ne in x:

            if ne.pos[0] - abs(ne.vel[0]) < lim_gauche or ne.pos[0] + abs(ne.vel[0]) > lim_droite:
                ne.vel = [-ne.vel[0],ne.vel[1]]
                ne.pos[0] += ne.vel[0]
                ne.pos[1] += ne.vel[1]

            if ne.pos[1] - abs(ne.vel[1]) < lim_bas or ne.pos[1] + abs(ne.vel[1]) > lim_haut:
                ne.vel = [ne.vel[0],-ne.vel[1]]
                ne.pos[0] += ne.vel[0]
                ne.pos[1] += ne.vel[1]

            v = np.sqrt(ne.vel[0]**2+ne.vel[1]**2)

            # si le neutron est dans la partie gauche, il peut y avoir
            # une fission avec proba p_fis à tout instant
            if ne.pos[0] < 0 and random() < p_fis:
                nb_fiss += 1
                nb_alea = randint(1,2)
                for i in range(nb_alea):
                    tetai = uniform(0,2*np.pi)
                    ni    = neutron2d([ne.pos[0],ne.pos[1]],[np.cos(tetai)*v , np.sin(tetai)*v])
                    x.append(ni)
                fissionsx.append(ne.pos[0])
                fissionsy.append(ne.pos[1])


            # proba de se faire absorber
            elif random() < p_abs:
                nb_absor += 1
                absorpx.append(ne.pos[0])
                absorpy.append(ne.pos[1])
                x.remove(ne)

                if len(x) == 0:
                    return 'Aucun neutron restant'

            # proba de changer de direction
            elif random() < p_dif:
                teta   = uniform(0,2*np.pi)
                ne.vel = [np.cos(teta)*v, np.sin(teta)*v]
                ne.pos[0] += ne.vel[0]
                ne.pos[1] += ne.vel[1]

            # proba de ralentir quand le neutron est dans l eau
            elif abs(v-v_rap)<0.1 and ne.pos[0] >= 0 and random() < p_r_l:
                ne.vel    = [ne.vel[0]/v_rap*v_len , ne.vel[1]/v_rap*v_len]
                ne.pos[0] += ne.vel[0]
                ne.pos[1] += ne.vel[1]

            # proba d accelerer quand le neutron est dans la zone avec materiaux fissiles
            elif abs(v-v_len)<0.1 and ne.pos[0] < 0 and random() < p_l_r:
                ne.vel    = [ne.vel[0]*v_rap/v_len , ne.vel[1]*v_rap/v_len]
                ne.pos[0] += ne.vel[0]
                ne.pos[1] += ne.vel[1]

            else:
                ne.pos[0] += ne.vel[0]
                ne.pos[1] += ne.vel[1]



        print(f"t = {t}   nb_neutrons: {len(x)}   nb_fissions: {nb_fiss}  nb_absorptions: {nb_absor}")
    return p_


