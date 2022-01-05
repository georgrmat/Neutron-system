import numpy as np
from random import random,randint, uniform
from matplotlib import pyplot as plt



class neutron:

    def __init__(self,r,v):
        self.pos = r
        self.vel = v


lim_gauche = -10   # limite physique a gauche
lim_droite = 10    # limite physique a droite


p_fis = 0.005   # probabilite de fission
p_dif = 0.1     # probabilite de diffusion
p_abs = 0.001   # probabilite d absorption
p_r_l = 1/2     # probabilite de passer de vitesse rapide a lente
p_l_r = 1/2     # probabilite de passer de vitesse lente a rapide


def affiche_figure():

    plt.plot([lim_gauche,0,lim_droite],[0,0,0], '|', color = (0,0,0))
    plt.plot([lim_gauche,0],[0,0], 'g-')
    plt.plot([0,lim_droite],[0,0], 'b-')


v_rap = 0.4   # vitesse rapide
v_len = 0.1   # vitesse lente


# simulation
def simul_neut_1d(N,T):

    x        = [neutron(0,-0.1) for k in range(N)]
    fissions = []
    nb_fiss  = 0
    nb_absor = 0

    for t in range(T):

        if t == 0:
            affiche_figure()
            line, = plt.plot([x[k].pos for k in range(len(x))],[0 for k in range(len(x))],'k.')

        else:
            for ne in x:

                if ne.pos - abs(ne.vel) < lim_gauche or ne.pos + abs(ne.vel) > lim_droite:
                    ne.vel = -ne.vel
                    ne.pos += ne.vel

                # si le neutron est a gauche, il peut y avoir
                # une fission avec proba p_fis à tout instant
                if ne.pos < 0 and random() < p_fis:
                    nb_fiss += 1
                    nb_alea = randint(1,2)
                    for i in range(nb_alea):
                        vi = randint(-1,1)
                        ni = neutron(ne.pos,vi*ne.vel)
                        x.append(ni)
                    plt.cla()
                    affiche_figure()
                    z = [x[k].pos for k in range(len(x))]
                    line, = plt.plot(z,[0 for k in range(len(x))],'k.')
                    fissions.append(ne.pos)
                    plt.plot(fissions,[0 for k in range(len(fissions))],'r*')

                # proba de se faire absorber
                elif random() < p_abs:
                    nb_absor += 1
                    x.remove(ne)
                    if len(x) == 0:
                        return 'Aucun neutron restant'
                    else:
                        plt.cla()
                        affiche_figure()
                        z = [x[k].pos for k in range(len(x))]
                        line, = plt.plot(z,[0 for k in range(len(x))],'k.')
                        plt.plot(fissions,[0 for k in range(len(fissions))],'r*')

                # proba de changer des sens
                elif random() < p_dif:
                    ne.vel = -ne.vel
                    ne.pos += ne.vel

                # proba de ralentir quand le neutron est dans l eau
                elif ne.vel == v_rap and ne.pos >= 0 and random() < p_r_l:
                    ne.vel = v_len
                    ne.pos += ne.vel

                # proba d accelerer quand le neutron est dans la zone avec materiaux fissiles
                elif ne.vel == v_len and ne.pos < 0 and random() < p_l_r:
                    ne.vel = v_rap
                    ne.pos += ne.vel

                else:
                    ne.pos += ne.vel

        line.set_xdata([x[k].pos for k in range(len(x))])
        plt.pause(0.05)
        print(f"t = {t}   nb_neutrons: {len(x)}   nb_fissions: {nb_fiss}  nb_absorptions: {nb_absor}")

    plt.show()
    plt.cla()




