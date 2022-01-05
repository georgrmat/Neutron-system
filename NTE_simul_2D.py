import numpy as np
from random import random, randint, uniform
from matplotlib import pyplot as plt



class neutron2d:

    def __init__(self,r,v):
        self.pos = r
        self.vel = v


lim_gauche = -10   # limite physique a gauche
lim_droite = 10    # limite physique a droite
lim_haut   = 5     # limite physique en haut
lim_bas    = -5    # limite physique en bas



p_dif = 0.01    # probabilite de diffusion
p_abs = 0.001   # probabilite d absorption
p_r_l = 1/2     # probabilite de passer de vitesse rapide a lente
p_l_r = 1/2     # probabilite de passer de vitesse lente a rapide


# fonction qui affiche la figure
def affiche_figure():

    plt.plot([lim_gauche,0],[lim_haut,lim_haut], 'g-')
    plt.plot([lim_gauche,0],[lim_bas,lim_bas], 'g-')
    plt.plot([lim_gauche,lim_gauche],[lim_haut,lim_bas], 'g-')
    plt.plot([lim_droite,0],[lim_haut,lim_haut], 'b-')
    plt.plot([lim_droite,0],[lim_bas,lim_bas], 'b-')
    plt.plot([lim_droite,lim_droite],[lim_haut,lim_bas], 'b-')
    plt.plot([0,0],[lim_haut,lim_bas],'k-')


v_rap = 0.4   # vitesse rapide
v_len = 0.1   # vitesse lente


# simulation
def simul_neut_2d(N,T):

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

    for t in range(T):

        if t == 0:
            affiche_figure()
            line, = plt.plot([x[k].pos[0] for k in range(len(x))],[x[k].pos[1] for k in range(len(x))],'k.')

        else:
            p_fis = (1-len(x)/50)*0.2
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
                    plt.cla()
                    affiche_figure()
                    z1 = [x[k].pos[0] for k in range(len(x))]
                    z2 = [x[k].pos[1] for k in range(len(x))]

                    line, = plt.plot(z1,z2,'k.')
                    fissionsx.append(ne.pos[0])
                    fissionsy.append(ne.pos[1])
                    plt.plot(fissionsx,fissionsy,'r*')
                    plt.plot(absorpx,absorpy,'y*')

                # proba de se faire absorber
                elif random() < p_abs:
                    nb_absor += 1
                    absorpx.append(ne.pos[0])
                    absorpy.append(ne.pos[1])
                    x.remove(ne)

                    if len(x) == 0:
                        return 'Aucun neutron restant'
                    else:
                        plt.cla()
                        affiche_figure()
                        z1 = [x[k].pos[0] for k in range(len(x))]
                        z2 = [x[k].pos[1] for k in range(len(x))]
                        line, = plt.plot(z1,z2,'k.')

                        plt.plot(fissionsx,fissionsy,'r*')
                        plt.plot(absorpx,absorpy,'y*')

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

            line.set_xdata([x[k].pos[0] for k in range(len(x))])
            line.set_ydata([x[k].pos[1] for k in range(len(x))])

        print(f"t = {t}   nb_neutrons: {len(x)}   nb_fissions: {nb_fiss}  nb_absorptions: {nb_absor}")
        plt.pause(0.01)
    plt.show()











