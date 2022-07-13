#ce script calcule et affiche un tableau d'amortissement d'un prêt v0,une fois qu l'on connait
#le taux d'intérêt annuel j (en%) et le nombre de versements périodiques [(mensualités,2fois par mois,chaque 2 semaine,hebdomadaire)selon le choix]vp.
#le programme comporte 3 parties.
#Partie 1:fonction calculant les versements périodiques
def calculvp(v0,i,n):
    vp = (i*v0*(1+i)**n)/(-1+(1+i)**n) #Calcul du versement périodique (mensualité)
    return round(vp,2)                #Renvoie de la mensualité arrondie au cent prés




def affichemenu():
    print(8*"-","Menu:choix du versement périodique",8*"-")
    print("\t versement mensieul:1")
    print("\t versement 2 fois par moi:2")
    print("\t versement chaque 2semaine:3")
    print("\t versement hebdomadaire:4")
    print("\t Quitter:5")
    print(50*"-")
    return 
    
def affiche_nombversement_et_taux(i,n):
    print("le nombre de versement est:",n)
    print("le taux de versement est:",round(i,3))
    return(n,i)
    
#Partie 2:Saisie du montant du prêt,du taux d'intérêt annuel, du terme (la durée de la période
#         de remboursement) en années et affichage du montant du versement périodique

v0=float(input("\n\t saisissez le montant du prêt en $:"))
terme=float(input("\n\t saisissez la durée du remboursement en année:"))
n=n=int(12*terme)                           
j=float(input("\n\t saisissez le taux d'intérêt annuel en %:"))
i=j/(12*100)


# Partie 3 : affichage du tableau d'amortissement
# Affichage de l'en-tête dutableau d'amortissement

choice=1
while choice!=5:
    affichemenu()
    choice=float(input("       saisissez 1,2,3,4,ou5 svp--->:"))
    if choice==1:
        print("              versement mensieul:1            ")
        n=12*terme            #Nombre de versements périodiques
        i=j/(12*100)             #Taux d'interêt périodique
        affiche_nombversement_et_taux(i,n)
        vp = (i*v0*(1+i)**n)/(-1+(1+i)**n)
    elif choice==2:
        print:("           versement 2fois par mois:2         ")
        n=24*terme          #Nombre de versements périodiques
        i=j/(24*100)        #Taux d'interêt périodique
        affiche_nombversement_et_taux(i,n)
        vp = (i*v0*(1+i)**n)/(-1+(1+i)**n)
    elif choice==3:
        print:("          versement chaque 2semaine:3        ")
        n=26*terme                 #Nombre de versements périodiques
        i=j/(26*100)                  #Taux d'interêt périodique
        affiche_nombversement_et_taux(i,n)
        vp = (i*v0*(1+i)**n)/(-1+(1+i)**n)
    elif choice==4:
        print:("          versement hebdomadaire:1           ")
        n=52*terme             #Nombre de versements périodiques
        i=j/(52*100)             #Taux d'interêt périodique
        affiche_nombversement_et_taux(i,n)
        vp = (i*v0*(1+i)**n)/(-1+(1+i)**n)
    elif choice==5:
        print:(" \n\t         vous avez choisir de Qitter:5") #arrêt de programme
        break    
    else:
        print("            choix invalide saisissez 1ou 2 ou3 ou4 ou5 svp:               ")
        affichemenu()
        choice=float(input("-------->saisissez 1,2,3,4,ou5 svp--->:                       "))

    vp = calculvp(v0,i,n)              #Calcul du versement périodique (mensualité)
    print("\n\t le versement périodique est de :",round (vp,3),"$")           
    print("\n\t ________________________________________________________")       #Affichage du tableau
    print("\t |        |           |           |           |           |")       #Affichage du tableau
    print("\t | Numéro | Versement |  Intérêt  |  Capital  |  Capital  |")        #Affichage du tableau
    print("\t |   vp   | périodique|    payé   |  remboursé|    dû     |")
    print("\t |________|___________|___________|___________|___________|")      #Affichage du tableau
    print("\t |        |           |           |           |","%.2f"%v0,"|")      #Affichage du tableau
    n=int(n)
    for nvp in range (1,n+1):
        ip=v0*i                #calcul de l'intérêt payé à chaque versement
        cr=vp-ip               #calcul du capital remboursé à chaque versement
        v0=v0-cr               #Calcul de capital dû après chaque versement
        nvp=str(nvp).zfill(3)
        print("\t | ",  nvp ," |","%7.2f"   %vp,"|","%7.2f"  %ip,"|","%7.2f" %cr,"|""%8.2f" %v0,"|") 
        print("\t |________|___________|___________|___________|___________|")
    
