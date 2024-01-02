#-----------------Début---------------------------
print("Début".center(50,'-'))
print("")
# Programme : OnlineEatsBot.py
# Auteur    : Achraf Louragli
#Date de création: 2021/04/06
# Date de dernière modification : 2021/05/28
# Objectif :
#   Programme d'un chatbot d'un restaurant
#   qui parle avec le client pour faire des commandes en lignes

#importer le fichier qui contiennt les fonction à appeler
from Achraf_Louragli_Fonctions_OnlineEatsBot import * #pour que ce fichier marche, vous devez renommer
                                                       #le fichier où il y a les fonctions avec ce
                                                       #nom Achraf_Louragli_Fonctions_OnlineEatsBot
                                                       #que j'ai fait dans la commande de (from import)
                                                       #Ce nom marchera très bien et sans erreur si vous
                                                       #renommer l'autre fichier qui contient les fonction de
                                                       #de ce programme. 

#------------------Déclaration de variables-----------------------------
salutationduClient=""     #str
reponse_salutation=""     #str
intention_menu={"Crevettes":12,"Steak":15,"Brochettes de Poulet":25,"Brochettes de boeuf":15}

#------------------------Sortie-------------------------
#time.sleep(6)
afficher_presentation_chatbot_a_utilisateur()
print("")

#------------------------Entrée------------------------------
#Le client salue au chatbot
time.sleep(4)
print("Client: ",end="")
salutationduClient=str(input())
salutationduClient=analyser_saisi_avec_seulement_Unespace(salutationduClient)
time.sleep(5)


#------------------------Traitements-----------------------
#appel fonction Saluer_client
reponse_salutation=Saluer_client(salutationduClient)
print("OnlineEatsBot:",reponse_salutation)

#appel fonction faire_connaissance_avec_client
time.sleep(6)

nom_user=faire_connaissance_avec_client()


time.sleep(6)
#appel de la fonction afficher_menu_du_jour
afficher_menu_du_jour(intention_menu)
time.sleep(7)




#appel fonction faire_nouvelle_commande
liste_commande,prix=faire_nouvelle_commande(intention_menu)
#print(liste_commande)

if liste_commande != [] :
    #appel de la fonction génerer_id_client
    id_client=génerer_id_client()
    #print(id_client)
    
    #calculer les taxes,le sous-total et le total
    #appel de la fonction calculer_prix_sousTotal()
    prix_sousTotal=calculer_prix_sousTotal(prix)
    
    #appel de la fonction afficher_facture
    afficher_facture(id_client,liste_commande,prix_sousTotal)
    
    #appel de la fonction intention_status_commande()
    #Entrée----
    print("Client: ", end="")
    demande_status_client=str(input())
    #Traitements---
    demande_status_client=analyser_saisi_avec_seulement_Unespace(demande_status_client)
    question_status=intention_status_commande(demande_status_client,id_client)

    #remerciement et message de remerciement
    #--------------------Entrée--------------------
    print("Client: ", end="")
    remerciement_client=str(input())
    ##--------------------Traitements--------------------
    #appel de la fonction analyser_saisi_avec_seulement_Unespace()
    remerciement_client=analyser_saisi_avec_seulement_Unespace(remerciement_client)
    #appel de la fonction tester_remerciement()
    time.sleep(6)
    remerciement_final=tester_remerciement(remerciement_client,nom_user)
    #--------------------Sortie--------------------
    print(remerciement_final)
else:
    #remerciement ou message de remerciement
    time.sleep(6)
    print("OnlineEatsBot: En conclusion, aucune commande n'a été effectuée par vous")
    time.sleep(6)
    print(tester_remerciement('',nom_user))

#end-if
time.sleep(5)
print("")
print("Fin du programme".center(50,"-"))

   
    

#------------------------Fin du programme-------------------------