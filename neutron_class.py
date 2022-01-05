import numpy as np
from random import random, randint, uniform, choice
from matplotlib import pyplot as plt

class neutron:


    def __init__(self, x, y, v, t):


        self.x       = x
        self.y       = y
        self.pos     = [x,y]
        self.vel     = v
        self.angle   = t
        self.vel2d   = [np.cos(t)*v, np.sin(t)*v]
        self.tps_vie = 0
        self.event   = None



class systeme_neutrons:

    def __init__(self, N, zonex, zoney, p_abs, p_ralentir, p_dif, p_fis = None):

        self.nb_neut       = N
        self.vit_len       = 0.05
        self.vit_rap       = 0.1
        self.list_neut     = []
        self.zonex         = zonex
        self.zoney         = zoney
        self.fissions      = []
        self.absorptions   = []
        self.nb_fiss       = 0
        self.nb_absorp     = 0
        self.p_abs         = p_abs
        self.p_ralentir    = p_ralentir
        self.p_dif         = p_dif
        self.p_fis         = p_fis
        self.lim           = {'gauche':-10, 'droite':10, 'haut': 5, 'bas': -5}


        for i in range(N):
            t = uniform(0,2*np.pi)
            v = choice([self.vit_len, self.vit_rap])
            x = uniform(zonex[0],zonex[1])
            y = uniform(zoney[0],zoney[1])
            self.list_neut.append(neutron(x,y, v, t))


    # fonction qui met a jour le systeme de neutrons
    def update(self):

        lg = self.lim['gauche']
        ld = self.lim['droite']
        lh = self.lim['haut']
        lb = self.lim['bas']

        for ne in self.list_neut:

            if self.p_fis == None:
                if ne.vel == self.vit_len:
                    p_fis = (self.p_abs)*3/2*(1-self.p_abs)
                else:
                    p_fis = 0
            else:
                if ne.vel == self.vit_len:
                    p_fis = self.p_fis
                else:
                    p_fis = 0


            if ne.pos[0] - abs(ne.vel2d[0]) < lg or ne.pos[0] + abs(ne.vel2d[0]) > ld:
                ne.vel2d = [-ne.vel2d[0],ne.vel2d[1]]
            ne.pos[0] += ne.vel2d[0]
            ne.pos[1] += ne.vel2d[1]

            if ne.pos[1] - abs(ne.vel2d[1]) < lb or ne.pos[1] + abs(ne.vel2d[1]) > lh:
                ne.vel2d = [ne.vel2d[0],-ne.vel2d[1]]
            ne.pos[0] += ne.vel2d[0]
            ne.pos[1] += ne.vel2d[1]

            # si le neutron est dans la partie gauche, il peut y avoir
            # une fission avec proba p_fis à tout instant
            if ne.pos[0] < 0 and random() < p_fis:
                ne.event = "fission"
                nb_alea = randint(2,3)
                for i in range(nb_alea):
                    tetai = uniform(0,2*np.pi)
                    ni    = neutron(ne.pos[0],ne.pos[1], self.vit_rap, tetai)
                    self.list_neut.append(ni)
                self.list_neut.remove(ne)

                self.fissions.append([ne.pos[0],ne.pos[1],0])
                self.nb_fiss += 1

            # proba de se faire absorber
            elif random() < self.p_abs:
                ne.event = "absorption"
                self.absorptions.append([ne.pos[0],ne.pos[1],0])
                self.nb_absorp += 1
                self.list_neut.remove(ne)

                if len(self.list_neut) == 0:
                    return 'Aucun neutron restant'

            # proba de changer de direction
            elif random() < self.p_dif:
                ne.event = "diffraction"
                if ne.pos[0] > 0 and random() < self.p_ralentir:
                    ne.vel = self.vit_len
                teta   = uniform(0,2*np.pi)
                ne.vel2d = [np.cos(teta)*ne.vel, np.sin(teta)*ne.vel]
                if ne.pos[0] - abs(ne.vel2d[0]) < lg or ne.pos[0] + abs(ne.vel2d[0]) > ld:
                    ne.vel2d = [-ne.vel2d[0],ne.vel2d[1]]
                ne.pos[0] += ne.vel2d[0]
                ne.pos[1] += ne.vel2d[1]

                if ne.pos[1] - abs(ne.vel2d[1]) < lb or ne.pos[1] + abs(ne.vel2d[1]) > lh:
                    ne.vel2d = [ne.vel2d[0],-ne.vel2d[1]]
                ne.pos[0] += ne.vel2d[0]
                ne.pos[1] += ne.vel2d[1]

            # sinon le neutron avance en restant dans la zone definie
            else:
                if ne.pos[0] - abs(ne.vel2d[0]) < lg or ne.pos[0] + abs(ne.vel2d[0]) > ld:
                    ne.vel2d = [-ne.vel2d[0],ne.vel2d[1]]
                ne.pos[0] += ne.vel2d[0]
                ne.pos[1] += ne.vel2d[1]

                if ne.pos[1] - abs(ne.vel2d[1]) < lb or ne.pos[1] + abs(ne.vel2d[1]) > lh:
                    ne.vel2d = [ne.vel2d[0],-ne.vel2d[1]]
                ne.pos[0] += ne.vel2d[0]
                ne.pos[1] += ne.vel2d[1]

        for i in self.fissions:
            i[2] += 1
            if i[2] == 20:
                self.fissions.remove(i)

        for i in self.absorptions:
            i[2] += 1
            if i[2] == 20:
                self.absorptions.remove(i)

        for i in self.list_neut:
            i.tps_vie += 1


    # fonction qui donne des infos (nombre de neutrons, de fissions et d absorptions)
    def info(self):

        print(f"nb_neut: {len(self.list_neut)}   nb_fiss: {self.nb_fiss}  nb_abs: {self.nb_absorp}  p_fis:{self.p_fis}")


    # fonction qui simule les neutrons, avec ou sans simulation
    def simul(self, T, animate = False):

        # sans animation
        if animate == False:
            self.info()
            for t in range(T):
                print(f"\nt: {t}")
                self.update()
                self.info()
                if len(self.list_neut) == 0:
                    print("Tous les neutrons ont été absorbés.")
                    break

        # avec animation
        else:
            plt.xlim(self.lim['gauche'], self.lim['droite'])
            plt.ylim(self.lim['bas'], self.lim['haut'])

            for t in range(T):
                self.info()
                plt.cla()
                plt.xlim(self.lim['gauche'], self.lim['droite'])
                plt.ylim(self.lim['bas'], self.lim['haut'])

                temps_vie_ = [i.tps_vie for i in self.list_neut]
                couleurs_  = [(2/np.pi*np.arctan(k/75),0,1-2/np.pi*np.arctan(k/50),1) for k in temps_vie_]
                z1 = [self.list_neut[k].pos[0] for k in range(len(self.list_neut))]
                z2 = [self.list_neut[k].pos[1] for k in range(len(self.list_neut))]

                plt.scatter(z1,z2, s = 10, c = couleurs_ )
                self.update()

                for i in self.fissions:
                    plt.plot(i[0],i[1],'*', color = (1,0,0,1-0.05*i[2]))

                for i in self.absorptions:
                    plt.plot(i[0],i[1],'*', color = (0,1,0,1-0.05*i[2]))

                if len(self.list_neut) == 0:
                    print("Tous les neutrons ont été absorbés.")
                    break

                #plt.savefig(f'simul_image{t}')

                plt.pause(0.01)
            plt.show()

    # fonction qui reinitialise le systeme de neutrons tel qu il a ete defini
    def reset(self,N=10,zonex=[0,0],zoney=[0,0],p_abs=0.001,p_ralentir=1/6,p_dif=0.1, p_fis = None):

        self.nb_neut       = N
        self.zonex         = zonex
        self.zoney         = zoney
        self.list_neut     = []
        self.fissions      = []
        self.absorptions   = []
        self.nb_fiss       = 0
        self.nb_absorp     = 0
        self.p_abs         = p_abs
        self.p_ralentir    = p_ralentir
        self.p_dif         = p_dif


        for i in range(self.nb_neut):
            t = uniform(0,2*np.pi)
            v = choice([self.vit_len, self.vit_rap])
            x = uniform(zonex[0],zonex[1])
            y = uniform(zoney[0],zoney[1])
            self.list_neut.append(neutron(x,y, v, t))




