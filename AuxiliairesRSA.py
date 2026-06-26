import secrets as sc
import pandas as pd
import sympy as sy
def saisi_reponse():
    flag=0
    while flag==0:
        c=str(input("Repondre par oui ou non"))
        if c.upper() == "OUI" or c.upper() == "NON":
            flag=1
        else:
            print("ERREUR DE SAISI? RECOMMENCER !")
        if c.upper()=="OUI":
            return 1
        else:
            return 0        

def saisi(utilisation):
    c=""
    s=""
    flag=0
    print(f"Vous allez saisir votre {utilisation}, pour mettre fin a la saisie, appuuyer sur ENTREE ")
    while flag==0:
        s=""
        s=str(input("Commencer saisi : "))
        if utilisation=="service d'accès":
            while verification("base_de_données_mdp.csv","decryptage_mdp.csv",s)==True:
                print("EERREUR , VOUS AVEZ DEJA SAISI DES INFORMATIONS POUR CE SERVICE")
                s=str(input("Recommencer saisi : "))
        print(f"Etes vous d'accord avec votre saisie : {s} ?")
        flag=saisi_reponse()
        if flag==0:
            print("On recommence")
    return s

def convert_unicod_hexadecimal(mdp):
    L=[ord(c) for c in mdp]
    return [hex(x)[2:] for x in L]
def verif_longueur2(L):
    for i in range(len(L)):
        if len(L[i])%2!=0:
            L[i]='0'+L[i]
    return L
def convert_120bit(L):
    L1=[]
    print(L)
    R1=convert_unicod_hexadecimal(L)
    R2=verif_longueur2(R1)
    a=len(R2)//15
    if a<len(R2)/15:
        a=a+1
    for i in range(a):
        M=R2[i*15:(i+1)*15]
        s=""
        for x in M:
            s=s+x
        L1.append(int(s,base=16))
    return L1
def choix_nbr_premier():
    a=sc.randbits(64)
    while sy.isprime(a)==False:
        a=sc.randbits(64)
    return a
def algo_euclide(a,b):
    if b==0:
        return a
    else:
        return algo_euclide(b,a%b)
def identite_bezout(a,b):
    r0=a
    r1=b
    u0=1
    v0=0
    u1=0
    v1=1
    while r1!=0:
        q=r0//r1
        r=r1
        r1=r0-r1*q
        r0=r
        u=u1
        u1=u0-u1*q
        u0=u
        v=v1
        v1=v0-v1*q
        v0=v
    return u0,v0
def inverse_modulaire(a,n):
    return identite_bezout(a,n)[0]%n
def codage(mdp):

    #L=convert_unicod_hexadecimal(mdp)
    #L1=verif_longueur2(L)
    L2=convert_120bit(mdp)
    p=choix_nbr_premier()
    q=choix_nbr_premier()
    a=p*q
    m=65537
    w=(p-1)*(q-1)
    k=inverse_modulaire(m,w)
    L3=[]
    for n in L2:
        h=pow(n,m,a)
        L3.append(h)
    return L3,a,k
def deconvert_120bits(L):
    L1=[]
    for n in L:
        h=hex(n)[2:]
        if len(h)%2!=0:
            h='0'+h
        for j in range(len(h)//2):
            L1.append(h[2*j:2*(j+1)])
    return L1
def verification(f,c,utilisation):
    try:
        f1=pd.read_csv(f)
        for x in f1['site'].tolist():
            if x==utilisation:
                return True
        return False
    except pd.errors.EmptyDataError:
        return False
    except FileNotFoundError:
        return False
def rectification_avec_saisi(nom_f,nom_c,utilisation):
    f=open(nom_f,'r')
    c=open(nom_c,'r')
    f1=pd.read_csv(f)
    c1=pd.read_csv(c)
    f2="base_de_données_mdp.csv"
    c2="decryptage_mdp.csv"
    i=f1[f1['site']==utilisation].index
    f1.drop(i,inplace=True)
    i=c1[c1['site']==utilisation].index
    c1.drop(i,inplace=True)
    f1.to_csv(f2,index=False)
    c1.to_csv(c2,index=False)
    f3=open(f2,'a')
    c3=open(c2,'a')
    ecriture(f3,c3)
    f3.flush()
    f3.close()
    c3.flush()
    c3.close()
    f.close()
    c.close()
def suppression(nom_f,nom_c,utilisation):
    f2="base_de_données_mdp.csv"
    c2="decryptage_mdp.csv"
    f1=pd.read_csv(nom_f)
    c1=pd.read_csv(nom_c)
    i=f1[f1['site']==utilisation].index
    f1.drop(i,inplace=True)
    i=c1[c1['site']==utilisation].index
    c1.drop(i,inplace=True)
    f1.to_csv(f2,index=False)
    c1.to_csv(c2,index=False)
def ecriture(f,c):
    print("Nous allons enregister de maniere securisée votre mot de passe et votre nom d'utilisateur")
    print("Saisir d'abord le service auquel donne accès ce mot de passe")
    u=saisi("service d'accès")
    id=saisi("identifiant")
    mdp=saisi("mot de passe")
    result=codage(id)
    id_code=result[0]
    id_clefpub=result[1]
    id_clefpriv=result[2]
    result1=codage(mdp)
    mdp_code=result1[0]
    mdp_clefpub=result1[1]
    mdp_clefpriv=result1[2]
    f.write(u + ',"' + str(id_code) + '","' + str(mdp_code) + '"\n')
    c.write(u+','+'nom_utilisateur'+','+str(id_clefpub)+','+str(id_clefpriv)+'\n')
    c.write(u+','+'mdp'+','+str(mdp_clefpub)+','+str(mdp_clefpriv)+'\n')
def nettoyage(c):
    s = str(c).replace("[", "").replace("]", "").strip()
    if s=="":
        return []
    return [int(x) for x in s.split(",")]
def decodage(utilisation,f,c):
    mclef=pd.read_csv(c)
    mcods=pd.read_csv(f)
    clef_a_mdp=int(mclef.loc[(mclef["site"]==utilisation) & (mclef['type']=='mdp'),'clefpub'].tolist()[0])
    clef_k_mdp=int(mclef.loc[(mclef["site"]==utilisation)&(mclef['type']=='mdp'),'clefpriv'].tolist()[0])
    clef_a_n_user=int(mclef.loc[(mclef["site"]==utilisation) & (mclef['type']=='nom_utilisateur'),'clefpub'].tolist()[0])
    clef_k_n_user=int(mclef.loc[(mclef["site"]==utilisation)&(mclef['type']=='nom_utilisateur'),'clefpriv'].tolist()[0])
    mdp=nettoyage(mcods.loc[mcods['site']==utilisation,'mdp'].tolist()[0])
    n_user=nettoyage(mcods.loc[mcods['site']==utilisation,'nom_utilisateur'].tolist()[0])
    mdp1=[pow(mdp_terme,clef_k_mdp,clef_a_mdp) for mdp_terme in mdp]
    n_user1=[pow(n_user_terme,clef_k_n_user,clef_a_n_user) for n_user_terme in n_user]
    mdp2=deconvert_120bits(mdp1)
    n_user2=deconvert_120bits(n_user1)
    mdp3=[chr(int(a,16)) for a in mdp2]
    mdpf=''.join(mdp3)
    n_user3=[chr(int(a,16)) for a in n_user2]
    n_userf=''.join(n_user3)
    return  n_userf,mdpf
def controle_rep(utilisation):
    if utilisation=='menu':
        x=1
        y=4
    elif utilisation=='flag':
        x=0
        y=1
    else:
        return 0
    while True:
        a=input("saisir numero reponse")
        try:
            a=int(a)
        except:
            print("ERREUR SAISIE !")
            continue
        if a>=x and a<=y:
            return a
        else:
            print("ERREUR SAISIE !")
def gestion_continuation():
    print("Voulez vous effectuer une autre action ou voulez vous mettre un terme à l'execution du programme ?\nREPONDRE PAR 0 (mettre fin au programme) ou 1 (effectuer autre action)")
    n=controle_rep('flag')
    return n





