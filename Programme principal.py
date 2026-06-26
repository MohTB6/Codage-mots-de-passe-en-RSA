import AuxiliairesRSA
import os
flag=1
entete=0
print("Bienvenue dans ce programme de codage de mots de passe à l'aide de la méthode RSA.\n" )
while flag!=0:
    print("Quelle action parmi celles proposées dans le menu voulez vous réaliser ?\n" \
    "MENU :\n" \
    "1. Saisir un nouveau couple identifiant-mot de passe\n" \
    "2. Corriger ou mettre à jour un mot de passe ou identifiant\n" \
    "3. Supprimer un mot de passe-identifiant\n" \
    "4. Afficher un mot de passe ou identifiant\n")
    rep=AuxiliairesRSA.controle_rep('menu')
    if rep==1:
        f=open("base_de_données_mdp.csv",'a')
        c=open("decryptage_mdp.csv",'a')
        if entete==0:
            f.write("site,nom_utilisateur,mdp\n")
            c.write("site,type,clefpub,clefpriv\n")
        entete=1
        AuxiliairesRSA.ecriture(f,c)
        f.flush()
        f.close()
        c.flush()
        c.close()
        flag=AuxiliairesRSA.gestion_continuation()
    elif rep==2:
        f=open("base_de_données_mdp.csv",'a')
        c=open("decryptage_mdp.csv",'a')
        uti=str(input("Saisir le nom du site ou service dont vous voulez changer les données de connexion"))
        while AuxiliairesRSA.verification("base_de_données_mdp.csv","decryptage_mdp.csv",uti)==False:
            print("ERREUR DE SAISIE, SITE INTROUVABLE !")
            uti=str(input("Saisir le nom du site ou service dont vous voulez changer les données de connexion"))
        f.close()
        c.close()
        AuxiliairesRSA.rectification_avec_saisi("base_de_données_mdp.csv","decryptage_mdp.csv",uti)
        flag=AuxiliairesRSA.gestion_continuation()
    elif rep==3:
        f=open("base_de_données_mdp.csv",'a')
        c=open("decryptage_mdp.csv",'a')
        uti=str(input("Saisir le nom du site ou service dont vous voulez supprimer les données de connexion"))
        while AuxiliairesRSA.verification("base_de_données_mdp.csv","decryptage_mdp.csv",uti)==False:
            print("ERREUR DE SAISIE, SITE INTROUVABLE !")
            uti=str(input("Saisir le nom du site ou service dont vous voulez supprimer les données de connexion"))
        f.close()
        c.close()
        AuxiliairesRSA.suppression("base_de_données_mdp.csv","decryptage_mdp.csv",uti)
        flag=AuxiliairesRSA.gestion_continuation()
    elif rep==4:
        f=open("base_de_données_mdp.csv",'r')
        c=open("decryptage_mdp.csv",'r')
        uti=str(input("Saisir le nom du site ou service dont vous voulez afficher les données de connexion"))
        while AuxiliairesRSA.verification("base_de_données_mdp.csv","decryptage_mdp.csv",uti)==False:
            print("ERREUR DE SAISIE, SITE INTROUVABLE !")
            uti=str(input("Saisir le nom du site ou service dont vous voulez afficher les données de connexion"))
        f.flush()
        f.close()
        c.flush()
        c.close()
        f=open("base_de_données_mdp.csv",'r')
        c=open("decryptage_mdp.csv",'r')
        cods=AuxiliairesRSA.decodage(uti,f,c)
        print(f"Votre IDENTIFIANT est {cods[0]}\n Votre MOT DE PASSE est {cods[1]}\n")
        f.flush()
        f.close()
        c.flush()
        c.close()
        flag=AuxiliairesRSA.gestion_continuation()