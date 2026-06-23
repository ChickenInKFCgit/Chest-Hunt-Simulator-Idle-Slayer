import random

# CONSTANTES
NB_COFFRES_TOTAUX = 30
NB_MIMICS_TOTAUX = 4


#JEU
class JeuChasseTresor:
    def __init__(self):
        self.LCoffres = self.__generer_coffres(chests=NB_COFFRES_TOTAUX, mimics=NB_MIMICS_TOTAUX)

        #stats
        self.nb_coffres_ouverts = 0
        self.nb_mimics_slayed = 0

        #status
        self.partie_perdue = False
        self.shield_dispo = 0
        self.x2_dispo= 0

    def __coffre_encore_la(self) -> bool:
        #le shield est toujours au rang 0
        return self.LCoffres[0] == "shield"
    
    def __X2_encore_la(self) -> bool:
        for elt in self.LCoffres:
            if elt =="X2":
                return True
        return False

    def __generer_coffres(self,chests, mimics):
        res =  ["X2"]
        res += ["mimic"]*mimics
        res += ["."] * (chests - 1 - len(res))
        random.shuffle(res)

        return ["shield"] + res
    
    def __trigger_effet(self, res, protection=False):
        self.nb_coffres_ouverts+=1
        match(res):
            case "shield":
                if self.x2_dispo > 0:
                    self.x2_dispo -= 1
                    self.shield_dispo += 2
                else:
                    self.shield_dispo += 1
            case "X2":
                if self.x2_dispo > 0:
                    self.x2_dispo = 2
                else :
                    self.x2_dispo = 1
            case "mimic":
                if protection :
                    self.nb_mimics_slayed += 1
                elif self.shield_dispo > 0:
                    self.shield_dispo -= 1
                    self.nb_mimics_slayed += 1
                else : 
                    self.partie_perdue = True
            case _ :
                if self.x2_dispo > 0:
                    self.x2_dispo -= 1


    def ouvrir(self, i):
        if (len(self.LCoffres)>0):
            res = self.LCoffres.pop(i)
        else:
            self.partie_perdue=True
            return ''

        sauveur_argent1 = self.nb_coffres_ouverts == 0
        sauveur_argent2 = self.nb_coffres_ouverts == 1
        dernier_coffre = self.nb_coffres_ouverts == NB_COFFRES_TOTAUX-1
        if sauveur_argent1 or sauveur_argent2 or dernier_coffre:
            self.__trigger_effet(res, protection=True)
        else :
            self.__trigger_effet(res, protection=False)
        
        return res

    def est_active(self)->bool:
        return not self.partie_perdue and len(self.LCoffres)>0

    def getnbcoffres(self):
        return NB_COFFRES_TOTAUX - self.nb_coffres_ouverts
    
#Simulateur Chest Hunt Idle Slayer
class SimulateurCHID:
    def __init__(self, nbgenerations:int, simulations:int):
        self.final_data = {}
        self.n = nbgenerations

        self.texte = ""

        for simulation in range(simulations):
            self.executer_algorithmes() 


        self.texte+="\n--------------------------------------------------------------------------------------"
        self.texte+=f"\n# RESULTATS FINAUX POUR **{simulations} SIMULATIONS** DE **{nbgenerations} GENRATIONS**"
        self.texte+="\n--------------------------------------------------------------------------------------"

        for algo, resultat in self.final_data.items():
            resultat[0] = algo
            for k in range(1, len(resultat)):
                resultat[k] = round(resultat[k]/simulations,3)
            self.affichage_console(tuple(resultat))


    def executer_algorithmes(self):
        for algorithme in (self.algo_FULL_GAMBLE,self.algo_SHIELD_DIRECT, self.algo_DOUBLE_SHIELD, self.algo_RAISONNABLE):
            res = [] 
            self.simulation_partie(algorithme, res)

            data = self.analyser(res,algorithme.__name__)

            self.rassembler_data(data)

    def simulation_partie(self, algorithme, res):
        #jeu de la partie
        for k in range(self.n):
            partie = JeuChasseTresor()
            algorithme(partie)
            res.append( (partie.nb_coffres_ouverts, partie.nb_mimics_slayed, partie.getnbcoffres()==0) )

    def rassembler_data(self,data):
        if not data[0] in self.final_data.keys():
            self.final_data[data[0]] = [0,0,0,0,0]
        for k in range(1,len(data)):
            self.final_data[data[0]][k] += (data[k])

    def affichage_console(self,data:tuple):
        self.texte+=f"\n### {data[0]} \nMoyenne Mimics : {data[1]} | Moyenne Coffres : {data[2]} | Winrate : {data[3]}% | wins : {data[4]}/{self.n}"

    def analyser(self, res:tuple, nomalgo:str)->tuple:
        avgmimics = 0
        avgchests = 0
        wins = 0

        for chests, mimics, victoire in res:
            avgmimics += mimics
            avgchests += chests
            if victoire:
                wins+=1
        avgmimics = round(avgmimics/self.n,3)
        avgchests = round(avgchests/self.n,3)
        winrate = round(wins/self.n *100,3)
        return (nomalgo,avgmimics, avgchests, winrate, wins)
            

    def algo_FULL_GAMBLE(self,partie:JeuChasseTresor):
        #full aléatoire, on prie.
        while partie.est_active(): 
            rang_coffre = gamble(0, partie.getnbcoffres()-1)
            partie.ouvrir(rang_coffre)
    

    def algo_SHIELD_DIRECT(self, partie:JeuChasseTresor):
        #consiste à prendre le bouclier une fois que les boucliers crystal sont épuisés
        #   ou si un X2 est trouvé.

        for k in range(2):
            if not partie.x2_dispo > 0:
                rang_coffre = gamble(1, partie.getnbcoffres()-1)
                partie.ouvrir(rang_coffre)
            else:
                #on va doubler ce petit bouclier
                partie.ouvrir(0) 
        
        #on ouvre le premier coffre comme ça pas de soucis, le bouclier est récupéré
        partie.ouvrir(0)

        #puis on finit la partie
        while partie.est_active():
            rang_coffre = gamble(0, partie.getnbcoffres()-1)
            partie.ouvrir(rang_coffre)

    def algo_DOUBLE_SHIELD(self, partie:JeuChasseTresor):
        #consiste à prendre le bouclier une fois que les boucliers crystal sont épuisés
        #   ou si un X2 est trouvé.
        bouclier_dispo = True
        while partie.est_active():
            if bouclier_dispo :
                if partie.x2_dispo > 0 :
                    partie.ouvrir(0)
                else : 
                    rang_coffre = gamble(1, partie.getnbcoffres()-1)
                    partie.ouvrir(rang_coffre)
            else: 
                rang_coffre = gamble(0, partie.getnbcoffres()-1)
                partie.ouvrir(rang_coffre)

    def algo_RAISONNABLE(self,partie:JeuChasseTresor):
        #consiste à faire algo DOUBLE SHIELD si mimic tué et sinon prendre le bouclier simple
        for k in range(2):
            rang_coffre = gamble(1, partie.getnbcoffres()-1)
            res = partie.ouvrir(rang_coffre)
            match (res):
                case 'mimic':
                    self.algo_DOUBLE_SHIELD(partie)
                case 'X2':
                    partie.ouvrir(0)
                    self.algo_SHIELD_DIRECT(partie)
                case _:
                    pass
        while partie.est_active():
            rang_coffre = gamble(0, partie.getnbcoffres()-1)
            partie.ouvrir(rang_coffre)
    

    
def gamble(a,b):
    if a>=b:
        return min(a,b)
    else:
        try :
            return random.randint(a,b)
        except Exception as e:
            pass #chuuut


def simuler(nbgenerations:int, nbsimulations:int)->str:
    simu = SimulateurCHID(nbgenerations,nbsimulations)
    return simu.texte
