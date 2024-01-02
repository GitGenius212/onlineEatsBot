#-----------------Début---------------------------
#print("Début".center(50,'-'))
# Programme : 1986111-Achraf Louragli_Fonctions_OnlineEatsBot.py
# Auteur    : Achraf Louragli
#Date de création: 2021/04/06
# Date de dernière modification : 2021/05/28
# Objectif :
#   Programme qui contient les fonctions pour chaque tâche
#   du programme principal OnlineEatsBot.py
import random
import time
#--------------------Intention de salutation--------------------------

#objectif:
#    lorsque le client envoie un message de salutation au chatbot, le chatbot doit être
#    capable de saluer également
def Saluer_client(pSalutation:str)->list:
    import datetime
    
    #--------------Déclaration variable------------------------
    intentions_salutationmatin =["Salut !", "Bonjour !","Bon matin !","Hey !","Hay !"]
    intentions_salutationapmidi =["Bon après midi !","Hey !","Hay !","Salut !","Bonjour !"]
    intentions_salutationsoir =["Bonsoir !","Hey !","Hay !","Salut !"]
    heure_actuelle=datetime.datetime.now().hour
    minute_actuelle = datetime.datetime.now().strftime("%M")
    message = ""
    #-----------------Traitements-------------------------
    if heure_actuelle >= 6 and heure_actuelle <= 11:
        pSalutation_client=saluer_avec_IntentionMatin(intentions_salutationmatin,pSalutation)
        return pSalutation_client
    #end-if
    elif heure_actuelle >= 12 and heure_actuelle < 14:
        message = "Bon-midi !"
        return message
    #end-if
    elif heure_actuelle >= 14 and heure_actuelle < 18:
        pSalutation_client=saluer_avec_IntentionApMidi(intentions_salutationapmidi,pSalutation)
        return pSalutation_client
    #end-if
    elif heure_actuelle >= 18 and heure_actuelle < 24:
        pSalutation_client=saluer_avec_IntentionSoir(intentions_salutationsoir,pSalutation)
        return pSalutation_client
    #end-if
    elif heure_actuelle >= 0 and heure_actuelle < 6:
        message = "Bonne nuit !"
        return message
    #end-if

#end-fonction
#--------------------------Fonction intention_matin------------------

def saluer_avec_IntentionMatin(pIntention_matin:list,p_Salutation:str)->str:
    #------------------Déclaration de variables------------
    i=0
    test_existence_dans_liste=0
    #------------------Traitements-------------------------
    while i < (len(pIntention_matin)):
        if  pIntention_matin[i].upper().replace(' !','') in p_Salutation.upper():
            salutation_chatbot=random.choice(pIntention_matin)
            test_existence_dans_liste+=1 
        #end-if
    #end-while
        i+=1
    if test_existence_dans_liste>0:
    #------------Résultats---------
        return salutation_chatbot
    else:
        return pIntention_matin[0]
    #end-if
#end-fonction
    
#--------------------------Fonction intention_matin------------------

def saluer_avec_IntentionApMidi(pIntention_apMidi:list,p_Salutation:str)->str:
    #------------------Déclaration de variables------------
    i=0
    test_existence_dans_liste=0
    #------------------Traitements-------------------------
    while i < (len(pIntention_apMidi)):
        if  pIntention_apMidi[i].upper().replace(' !','') in p_Salutation.upper().replace(' ',''):
            salutation_chatbot=random.choice(pIntention_apMidi)
            test_existence_dans_liste+=1 
        #end-if
        i+=1
    #end-while
    if test_existence_dans_liste>0:
    #------------Résultats---------
        return salutation_chatbot
    else:
        return pIntention_apMidi[0]
    #end-if
#end-fonction  

#--------------------------Fonction intention_matin------------------

def saluer_avec_IntentionSoir(pIntention_soir:list,p_Salutation:str)->str:
    #------------------Déclaration de variables------------
    i=0
    test_existence_dans_liste=0
    #------------------Traitements-------------------------
    while i < (len(pIntention_soir)):
        if  pIntention_soir[i].upper().replace(' !','') in p_Salutation.upper():
            salutation_chatbot=random.choice(pIntention_soir)
            test_existence_dans_liste+=1 
        #end-if
    #end-while
        i+=1
    if test_existence_dans_liste>0:
    #------------Résultats---------
        return salutation_chatbot
    else:
        return pIntention_soir[0]
    #end-if
#end-fonction  
#--------------------Intention de connaissance-----------------------------
#objectif:
#     Lorsque le chatbot souhaite connaître le nom du client

def faire_connaissance_avec_client()->str:
    #---------------------Déclaration de variables-------------------------
    intention_connaissance=["Quel est votre nom ?","Comment vous appeler-vous?","Quel est votre nom complet?"]
    bienvenue_nom_user=['OnlineEatsBot: Bienvenue','OnlineEatsBot: Salut','OnlineEatsBot: Avec plaisir de vous voir','OnlineEatsBot: Votre présence est chaleureuse']
    #----------------Traitements-----------------------
    connaissance_chatbot=random.choice(intention_connaissance)
    print("OnlineEatsBot:",connaissance_chatbot)
    time.sleep(2)
    #------------------Entrée---------------------
    nom_client=str(input("Client: "))
    #----------------------Traitements------------------------
    #si le message est un espace
    nom_client=analyser_saisi_avec_seulement_Unespace(nom_client)
    acceuil=random.choice(bienvenue_nom_user)
    time.sleep(6)
    nom_client=chercher_nomUser_dans_la_phrase(nom_client,acceuil)
    #------------Résultats---------
    return nom_client
#end-fonction


#----------------------------Fonction analyser_saisi_avec_seulement_Unespace()---------------------------
def analyser_saisi_avec_seulement_Unespace(p_phrase):
    
    '''
    Si le client répond avec un espace seulement
    '''
    
    #---------------Traitements--------------
    while p_phrase=='':
        #-------Entrée---------
        print("Client: ",end="")
        p_phrase=str(input()) 
    #end-while
    #------------Résultats---------
    return p_phrase
#end-fonction
#----------------------------Fonction-------------------------------------

def chercher_nomUser_dans_la_phrase(p_phrase: str, pAcceuil: str)-> str:
    #--------Déclaration de variables----
    liste_indice_espace = []
    #-------------Traitements---------
    #effacer les espaces du début et de la fin 
    p_phrase=p_phrase.strip()
    for espace in range(len(p_phrase)):
        if p_phrase[espace] == ' ':
            liste_indice_espace.append(espace)
        #end-if
    #end-for
    if liste_indice_espace != []:
        avant_dernier_espace = liste_indice_espace[-1]
        #print(avant_dernier_espace)
        #--------------------Résultats---------------------
        print(pAcceuil,p_phrase[avant_dernier_espace:].strip(),"!")
        return p_phrase[avant_dernier_espace:].strip()
    else:
        print(pAcceuil,p_phrase,"!")
        return p_phrase
    #end-if
#end-fonction 


#-------------------Intention de demande-----------------------------------
#objectif:
#    Lorsque le chatbot souhaite veut savoir le choix du client

def poser_demande_client()->str:
    #----------------------Déclaration de variables------------------------
    intention_demande=["Quel est votre choix?", "Quelle repas désiriez-vous acheter?","Que préférez-vous acheter?","Comment puis-je vous aider?"]
    #----------------------Traitements------------------------
    question_demande=random.choice(intention_demande)
    time.sleep(6)
    print("OnlineEatsBot:",question_demande)
    time.sleep(2)
    #-----------------------Entrée----------------
    choix=str(input("Client: "))
    choix=analyser_saisi_avec_seulement_Unespace(choix)
    #------------Résultats---------
    return choix
#end-Fonction

#-------------------menu du jour-----------------------------------
def afficher_menu_du_jour(p_dict)->dict:
    #--------------------Résultats----------
    print("OnlineEatsBot:",end="")
    print("Menu du jour".center(40,"-"))
    for nourriture,prix in p_dict.items():
        print("{}:{}$".format(nourriture,prix))
    #end-for
    print("-".ljust(40,"-"))
#--------------------Intention passer une commande--------------------------

#objectif:
#    Lorsque le client fait une commande, le chatbot doit être capable de lui indiquer le prix
#    de la nourriture commandée. le chatbot doit vérifier si le restaurant dispose de
#    la nourriture commandée et combien cela coûte.

def aficher_prix_commande(P_commande:str,p_intention_menu:dict)->float:
    '''
    Dans l’intention de commande, une fois
    que le client aura fait son choix, le chatbot
    doit vérifier si le restaurant dispose de la
    nourriture commandée et combien cela coûte.  
    '''
    #time.sleep(6)
    #--------------------Déclaration de variables--
    platRecherche = ''      #str
    #---------------------Traitements--------------
    for nourriture in p_intention_menu.keys():
        if nourriture.lower() in P_commande.lower() :
            platRecherche="Trouvé"
            prix=p_intention_menu[nourriture]
            #------------Résultats---------
            return prix, nourriture,platRecherche
        
        #end-if
    #end-for
    if platRecherche!="Trouvé":
        prix,nourriture,platRecherche=choisir_quel_brochettes_commander(p_intention_menu,P_commande,platRecherche)
        #print(platRecherche)
        if platRecherche=="Trouvé":
            #------------Résultats---------
            return prix,nourriture,platRecherche
        #end-if
    #end-if
    if platRecherche!="Trouvé":
        time.sleep(6)
        prix=préciser_indisposition_nourriture()
        #------------Sortie---------
        print(prix)
    #end-if

#end-Fonction
#------------------Fonction préciser_indisposition_nourriture()-------------
def préciser_indisposition_nourriture()->str:
    #---------------------Déclaration de variables------------
    indisposition_nourriture = ["OnlineEatsBot: Je ne dispose pas cette nourriture","OnlineEatsBot: Malheureusement,je n'obtient pas ce plat","OnlineEatsBot: Hélas,je n'obtient pas ce plat","OnlineEatsBot: Par malheur,je ne le possède pas","OnlineEatsBot: Nous n’avons pas cette nourriture" ]
    #---------------------Traitements-------------
    phraseIndispositionAléatoire=random.choice(indisposition_nourriture)
    return phraseIndispositionAléatoire
#end-fonction
#------------------------État de la commande-----------------------------
#objectif:
#    Lorsque le client souhaite connaître l'état de sa commande

def intention_status_commande(p_demande_status:str,pId_client:int)->str:
    #------------------------éclaration de variables---------
    question_trouve=''  #str
    i = 0               #int
    #-------------------------Traitements--------------
    
    intention_ordre_status=['Dites-moi où est ma nourriture?',"Pouvez-vous s'il vous plaît m'aider à connaître l'état de ma commande de nourriture ?",'Où est ma commande?','Bonjour quand vais-je recevoir ma commande de nourriture?',"Je n'ai pas encore reçu ma commande"]
    while question_trouve !="Trouvé":
        for question_status in intention_ordre_status:
            if p_demande_status.upper().replace(' ','') in question_status.upper().replace(' ','') or question_status.upper().replace(' ','') in p_demande_status.upper().replace(' ',''):
                question_trouve="Trouvé"
                Comprendre_Order_ID_client(pId_client)
            #end-if
        #end-for
        i+=1
        if question_trouve !="Trouvé":
            time.sleep(2)
            #----------------Entrée-------------------
            print("Client: ", end="")
            p_demande_status=str(input())
            #------------------------Traitements-----------
            #appel de la fonction analyser_saisi_avec_seulement_Unespace()
            p_demande_status=analyser_saisi_avec_seulement_Unespace(p_demande_status)
        #end-if
    #end-while
#end-fonction

#------------------------Order_ID------------------------------
#objectif:
#    le chatbot doit comprendre l'ID de commande de l'utilisateur pour le suivi.
def Comprendre_Order_ID_client(Pid:int)->int:
    #-----------------Déclaration de variables---------------------
    reponse_id=0    #int
    intention_user_id=["OnlineEatsBot: Pouvez-vous m'aider avec votre identifiant de commande? ","OnlineEatsBot: Puis-je avoir votre numéro de commande? ","OnlineEatsBot: Quel est le numéro de commande? "]
    question=random.choice(intention_user_id)
    #----------------Entrée---------------
    time.sleep(6)
    print(question)
    time.sleep(2)
    reponse_id=str(input("Client: "))
    #----------------Traitements-----------------
    #appel de la fonction analyser_saisi_avec_seulement_Unespace()
    reponse_id=analyser_saisi_avec_seulement_Unespace(reponse_id)
    reponse_id=chercher_quantite_dans_la_phrase(reponse_id)
    while (str(Pid) != str(reponse_id)):
        question=random.choice(intention_user_id)
        #appel de la fonction donner__messageID_introuvable()
        idMasque=donner__messageID_introuvable()
        time.sleep(6)
        #-----------------Entrée-------------------
        print("\nOnlineEatsBot:",idMasque)
        time.sleep(7)
        print(question)
        time.sleep(2)
        reponse_id=str(input("Client: "))
        #---------------Traitements--------------------
        #appel de la fonction analyser_saisi_avec_seulement_Unespace()
        reponse_id=analyser_saisi_avec_seulement_Unespace(reponse_id)
        #Utiliser cette fonction chercher_quantite_dans_la_phrase() pour chercher le id dans la chaine
        #IL y a le nom quantite dans le nom de cette fonction, car je l'utilise aussi pour chercher le nombre de
        #quantite d'aliment que l'utilisateur veut aacheter
        #Cette fonction fonctionne de la même façon pour chercher l'id
        reponse_id=chercher_quantite_dans_la_phrase(reponse_id)
    #end-while
    time.sleep(9)
    #---------------------Sortie-----------------
    print("\nOnlineEatsBot: Statut de la commande pour le numéro de commande:",reponse_id,". Le livreur est dans votre localité, votre nourriture arrivera dans environ 5 minutes.")
 
#end-Fonction

#----------------------------Fonction ID Introuvable-------------------------------
    
def donner__messageID_introuvable()->str:
    #-----------------Déclaration de variables-------------
    id_introuvable = ["ID Incorrect !","ID Invalide !","ID Inconnu !","ID Introuvable !"]
    messageId_pasTrouve = random.choice(id_introuvable)
    #-------------Résultats-----------
    return messageId_pasTrouve

#end-fonction

#--------------------Intention de remerciement--------------------------------
#objectif:
#   lorsque le client remercie le chatbot, il doit être capable de le remercie également en
#   mentionnant son nom

def tester_remerciement(p_remerciement:str,p_nomClient)->list:
    #----------------Déclaration de variables--------------
    intentions_remerciement_chatbot =["OnlineEatsBot: Merci beaucoup {} pour votre coopération !".format(p_nomClient),"OnlineEatsBot: Au plaisir {} !".format(p_nomClient),"OnlineEatsBot: Au plaisir de vous revoir {} !".format(p_nomClient),"OnlineEatsBot: Bienvenue {} !".format(p_nomClient),"OnlineEatsBot: Merci {} , bye-bye et à la prochaine ! ".format(p_nomClient)]
    #-------------------Traitements---------------------
    if ("Merci" ) in p_remerciement or ("merci") in p_remerciement:
        p_reponse=random.choice(intentions_remerciement_chatbot )
        return p_reponse
    
    else:
        return intentions_remerciement_chatbot [4]
    #end-if
        
    #end-if
#end-fonction

#---------------------------------Fonction chercher_quantite_dans_la_phrase()----------------------------
 
def chercher_quantite_dans_la_phrase(p_phrase: str)-> str:
    #--------Déclaration de variables----
    amount = ""     #str
    #-------------Traitements---------
    for num in range(len(p_phrase)):
        if p_phrase[num].isnumeric():
            amount += p_phrase[num]
        #end-if
    #end-for
    #------------Résultats---------
    return amount   
#end-fonction 

#-------------------------quantite-----------------------------------
#objectif:
#   quelle est la quantité d’aliments que le client est prêt à commander?

def calculer_quantite_aliments_prix(p_prix:float)->float:
    
    '''

    Calculer la quantite d'aliment et prix
    '''
    #----------------Déclaration de variables-----------
    question_quantite=demander_leNombreQuantiteAliment_Au_Client()
    time.sleep(6)
    #----------Entrée------------
    print(question_quantite,end="")
    time.sleep(2)
    quantite_saisir=str(input('\nClient: '))
    #----------------Traitements----------------
    quantite_saisir = analyser_saisi_avec_seulement_Unespace(quantite_saisir)
    p_quantite = chercher_quantite_dans_la_phrase(quantite_saisir)
    while p_quantite.isnumeric()==False:
        #appeler la fonction qui va choisir au hasard les question
        incomprehension=poser_question_incomprehension_quantite()
        time.sleep(6)
        #-------------Entrée-------------------------
        print("OnlineEatsBot:",incomprehension)
        quantite_saisir=str(input("Client: "))
        #------------------Traitements-------------
        quantite_saisir = analyser_saisi_avec_seulement_Unespace(quantite_saisir)
        p_quantite = chercher_quantite_dans_la_phrase(quantite_saisir)
    #end-while
    quantite_prix=int(p_quantite)*p_prix
    #----------------Résultats---------
    return quantite_prix,p_quantite

#end-fonction
#-----------------------------Fonction demander_leNombreQuantiteAliment_Au_Client()-------------------------
def demander_leNombreQuantiteAliment_Au_Client()->str:
    #-------------------Déclaration de variables---------
    propos_quantite = ["OnlineEatsBot:Combien vous en voulez?","OnlineEatsBot:Combien de cet aliment désiriez-vous commander? ","OnlineEatsBot:Quelle quantité en aimeriez vous prendre?"]
    Aleatoire_affaire = random.choice(propos_quantite)
    #------------Résultats---------
    return Aleatoire_affaire
#end-fonction
#------------------------------Fonction Intention_incompréhenision de la question de quantité--------------

def poser_question_incomprehension_quantite()->str:
    #----------------Déclaration de variables-----------
    intentionIncompréhension = ["Je n'ai pas bien compris! Combien vous en voulez?" , "Combien?" , "Combien vous en voulez? Soyez clair!" , "Combien? Donnez-moi un nombre qui représente la quantité de cet aliment. "]
    p_question=random.choice(intentionIncompréhension)
    #------------Résultats---------
    return p_question

#end-fonction

#------------------------order_id-------------------------
def génerer_id_client():
    '''
     l’id du client
    '''
    #-------------Déclaration de variables-----
    order_id=random.randint(100000,999999 )
    #------------Résultats---------
    return order_id
#end-fonction

#-------------------------lister_commande_client---------------

def lister_commande_client(derniere_commande:list,pcommandeNouvelle:str)->list:
    '''
    la liste liste_commande qui va contenir l’ensemble des commandes passés par
    le client sous forme de chaine de caractère
    '''
    #--------------Traitements-------------
    derniere_commande.append(pcommandeNouvelle)
    #------------Résultats---------
    return derniere_commande
#end-fonction

#------------------------------afficher_facture--------------------------
def afficher_facture(p_id:int,P_liste_commandes:list,p_sousTotal:float)->str:
    #-----------------Traitements---------
    #faire une pause pour faire un bon effet dans le programme
    pause()
    time.sleep(6)
    #-----------------Sorties-------------------
    print("\nOnlineEatsBot: Voici votre facture: ")
    time.sleep(6)
    p_id=str(p_id)
    print("")
    print("OnlineEatsBot".upper().center(60,'|'))
    print("Numéro de commande:",end="")
    print(p_id.center(30,'*'))
    
    afficher_commandes(P_liste_commandes)
    print("\n\n")
    print("Sous-Total ${}".format(p_sousTotal))
    #appel de la fonction Calculer_taxe_TVQ_TPS()
    TPS,TVQ=Calculer_taxe_TVQ_TPS(p_sousTotal)
    print("TPS 5%     ${} \nTVQ 9.975% ${}".format(TPS,TVQ)) # Afficher les taxes
    prix_total=calculer_prix_total(p_sousTotal,TPS,TVQ)  #appel de la fonction qui va calculer le montant total des commandes
    print("Total      ${}".format(prix_total))
    print("")
#end-fonction

#------------------------------ajouter_nouvelle_commande--------------------------

def faire_nouvelle_commande(p_intention_menu:dict)->list:
    #----------------Déclaration de variables------------------
    autre_choix= ''           #str
    liste_commandes= []       #list
    compteur_commande=1       #int
    liste_prix = []           #list
    #----------------Traitements--------------
    while "non" not in autre_choix.lower() :
        choix=poser_demande_client()  #demander à l'utilisateur de choisir son repas
        #----------------------------------------
        #appel de la fonction aficher_prix_commande()
        cout=(aficher_prix_commande(choix,p_intention_menu)) #tester s'il a trouvé le  prix ou pas
        #print(cout)
        if cout!=None : #Si le cout n'est pas vide
            if cout[-1]!="Trouvé":
                cout=(aficher_prix_commande(choix,p_intention_menu)) #chercher le pix du repas et retourner le repas choisi
                print(cout)
            #end-if
            if cout!=None :
                time.sleep(6)
                print("OnlineEatsBot: Le(s)",cout[-2],"coûte(nt)", cout[-3],"$") #afficher le cout
                prix,quantite=calculer_quantite_aliments_prix(cout[-3]) #claculer le prix * la quantite
                #convertir  dans l’ordre la quantité, la nourriture et le prix total sous forme d’une chaine de caractère
                commande=str(quantite)+ ' ' + str(cout[-2])+ " $" + str(prix)
                chaine_commande=commande
                liste_prix.append(prix)
            #end-if
        #end-if
            #print(commande_chaine)
            if compteur_commande==1:
                premierecommande=chaine_commande
                liste_commandes=[premierecommande]  #la variable final des commandes du client
                if commande[0]=='0':  #Si la quantité de l'aliment est 0, on en a pas besoin de cette aliment
                                      #dans la liste
                    liste_commandes.remove(commande)
                #end-if
            elif compteur_commande>1:
                #assigner à la variable liste_commandes tous les commandes que le client a faites
                liste_commandes=(lister_commande_client(liste_commandes,chaine_commande))
                if commande[0]=='0':  #Si la quantité de l'aliment est 0, on en a pas besoin de cette aliment
                                      #dans la liste
                    liste_commandes.remove(commande)
                #end-if
                #assigner  tous les commandes que le client a faite à la variable premierecommande
                premierecommande=liste_commandes
                
            #end-if
            compteur_commande+=1
        #else:
            #print("Je ne dispose pas cette nourriture")
        #end-if
        choixQuestionAleatoire=demander_si_client_souhaite_faire_un_autre_choix_liste()
        time.sleep(6)
        #-------------------Entrée----------------
        print(choixQuestionAleatoire,end="")
        autre_choix=str(input("\nClient: "))
        autre_choix = analyser_saisi_avec_seulement_Unespace(autre_choix)
        #---------Traitements-------------------
        while ('oui' not in autre_choix.lower() ) and ('non' not in (autre_choix.lower())) :
            time.sleep(6)
            choixIncorrect=direMessage_choixIncorrect()
            #-------------Entrée----------------
            print(choixIncorrect,end="")
            autre_choix=str(input())
            autre_choix = analyser_saisi_avec_seulement_Unespace(autre_choix)
        #end-while
        
    #end-while
    #-----------------Résultats--------------
    return(liste_commandes), liste_prix
#end-fonction
#---------------------------------Fonction demander_si_client_souhaite_faire_un_autre_choix_liste()-------------

def demander_si_client_souhaite_faire_un_autre_choix_liste():
    #-----------------Déclaration de variables----------------
    demande_autre_choix = ["OnlineEatsBot: Voulez-vous faire un autre choix? ","OnlineEatsBot: Souhaitez-vous accomplir une autre commande? ","OnlineEatsBot: Aimeriez-vous effectuer une autre sélection? "]
    interrogation_Hasard = random.choice(demande_autre_choix)
    #--------------------Résultats----------------
    return interrogation_Hasard
#end-fonction
#---------------------------------Fonction dire choix invalide()------------------------------------------------
def direMessage_choixIncorrect():
    #----------------Déclaration de variables-------
    intention_choixInvalide=["OnlineEatsBot:Invalide ! Voulez-vous faire un autre choix?\nClient: ","OnlineEatsBot:Incorrect ! Voulez-vous faire un autre choix (oui ou non)?\nClient: ","OnlineEatsBot:Incompréhensible ! Voulez-vous faire un autre achat?Est-ce que c'est oui ou bien c'est non?\nClient: "]
    question_choix=random.choice(intention_choixInvalide)
    #-----------Résultats---------
    return question_choix
#end-fonction
#-----------------------------------Fonction choisir_quel_brochettes_commander()----------------------------------------
def choisir_quel_brochettes_commander(p_intention_menu:dict,p_phrase_commande:str,Pplatrouve:str)->str:
    
    '''
    Si l'utilisateur saisi le mot brochettes dans la phrase, on va lui donner une chance
    de choisir quels brochettes il veut commander. 
    '''
    #-------------------------Traitements--------------------
    if "Brochettes".upper() in p_phrase_commande.upper():
        question_au_hasard = Questionner_achat_de_brochettes()
        time.sleep(6)
        print(question_au_hasard)
        time.sleep(2)
        #--------------Entrée--------------
        p_phrase_commande=str(input("Client: "))
        #Si l'utilisateur clique sur entrée sans rien écrire
        #--------------------Traitements----------------
        p_phrase_commande=analyser_saisi_avec_seulement_Unespace(p_phrase_commande)
        p_phrase_commande="brochettes"+p_phrase_commande
        for nourriture in p_intention_menu.keys():
            if nourriture.lower().replace(' ','') in p_phrase_commande.lower().replace(' ',''):
                Pplatrouve="Trouvé"
                #----------------Résultats-------------
                return p_intention_menu[nourriture],nourriture,Pplatrouve
            #end-if
        #end-for
        #---------------Traitements---------
        if Pplatrouve!="Trouvé":
            prix=''
            plat=''
            #-------------Résultats-----------
            return prix,plat,Pplatrouve
    else:
        prix=''
        plat=''
        return prix,plat,Pplatrouve
    #end-if
#end-fonction
#--------------------------------------Fonction Questionner_achat_de_brochettes()-------------------
    
def Questionner_achat_de_brochettes()->str:
    #-------------Déclaration de variables-----------
    questions_choix_brochettes = ["OnlineEatsBot: Nous avons des brochettes, mais lesquels voulez-vous?", "OnlineEatsBot: Nous avons deux genres de brochettes (de boeuf ou de poulet). Quels brochettes préfèrez-vous commander?", "OnlineEatsBot: Vous voulez des brochettes de quoi?"]
    questions_choix_brochettes_aleatoire = random.choice(questions_choix_brochettes)
    #-------------Résultats---------
    return questions_choix_brochettes_aleatoire
#end-fonction
#--------------------------------------Fonction calculer_prix_sousTotal()---------------------------

def calculer_prix_sousTotal(liste_commandeFinal:list)->float:
    
    '''
    On va additioner les prix de tous les commandes que l'utilisateur a prises
    '''
    #----------Déclaration de variables---------
    payement_prix = 0
    #-----------Traitements---------
    for argent in liste_commandeFinal:
        payement_prix+=argent
        
    #end-for
    #---------Résultats------
    return payement_prix
#end-fonction

#--------------------------Fonction Taxe-----------------------

def Calculer_taxe_TVQ_TPS(p_sousTotal:float)->float:
    #------------Traitements-------
    p_TPS= (p_sousTotal*0.05)+ p_sousTotal
    p_TVQ= (p_sousTotal*0.09975)+ p_sousTotal
    #------------Résultats----------
    return round(p_TPS,2), round(p_TVQ,2)

#end-fonction

#--------------------------Fonction calculer_prix_total-----------------------

def calculer_prix_total(p_sousTotal:float,pTPS:float,pTVQ:float)->float:
    #---------------Traitements---------
    prixTotal=p_sousTotal+pTPS+pTVQ
    #----------Résultats------
    return round(prixTotal,2)

#end-fonction

#--------------------------Fonction afficher notre présentation à l'utilisateur-----------------------
def afficher_presentation_chatbot_a_utilisateur()->str:
    #-------------------Sortie-------------
    print("OnlineEatsBot: Salut Mesdadames et Messieurs ! Je suis votre assistante virtuelle pour vous aider à prendre des commandes\n en ligne des plats du restaurant ALPHA du célèbre homme, nommé Achraf Louragli.")
#end-Fonction  
        

#--------------------------Fonction afficher_commandes-----------------------
def afficher_commandes(P_lescommandes:list)->str:
    #---------------Sortie------------
    print("")
    #---------------Traitements-------
    for commande in P_lescommandes:
        #---------Sortie---------
        print('\t',commande)
    #end-for
#end-fonction   
    
#--------------------------Fonction pause-----------------------   
def pause()->str:
    #--------------Entrée------------
    print("\nTapez sur Entrée pour continuer ",end="")
    tape=str(input())
#end-fonction



#-------------------------------------Fin des Fonctions-----------------------------------------------------






