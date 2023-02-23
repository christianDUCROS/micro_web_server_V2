def modifications_dico_valeurs_dynamiques(dico) :
#####################################################################
# pass     #pour pas de variables dynamiques 
####################### A programmer en fonction des capteurs #############
    #simulation mesure capteurs 
    valeur_temperature = 22 
    # modification  de la variable temperature  
    dico["temperature"] = str(valeur_temperature)    #str car texte

    #modification valeurs {{couleur_background}} du CSS et images{{carre_couleur}} du HTML
    if valeur_temperature > 21 :
       dico["couleur_background"] = "#1E90FF"
       dico["carre_couleur"] = " images/carre_rouge.jpg"
    else :
       dico["couleur_background"] = "#FFDC33"
       dico["carre_couleur"] = " images/carre_vert.jpg"
#####################################################################
    return(dico)
