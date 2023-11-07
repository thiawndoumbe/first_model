def rech(liste):
    lst = {}
    for chiffre in liste:
        if chiffre in lst:
            lst[chiffre] += 1
        else:
            lst[chiffre] = 1
    for valeur in lst.values():
        if valeur == 3:
            return True
    
    return False
ma_liste = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
resultat = rech(ma_liste)
print(resultat)  
