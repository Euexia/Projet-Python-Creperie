# ------------------------Aestetique--------------------
# import
from os import system
import shutil

# center text
columns = shutil.get_terminal_size().columns

# ------------------------Dictionnaires--------------------

crepe = [{
    'nom': 'Nutella',
    'prix': 4.50,
    'categorie': 'Crêpe sucrée',
    'ingredient': ['Nutella','Chantilly']

},

{
    'nom': 'Confiture Fraise',
    'prix': 5,
    'categorie': 'Crêpe sucrée',
    'ingredient': ['Confiture de fraise','Sucre glace']
},

{
    'nom': 'Kebab Poulet',
    'prix': 25,
    'categorie': 'Crêpe salée',
    'ingredient': ['Kebab','Poulet','Tomate','Salade','Sauce du Chef']

},

{
    'nom': 'Jambon fromage',
    'prix': 9,
    'categorie': 'Crêpe salée',
    'ingredient': ['Jambon','Cheddar','Oeuf']

},

{
    'nom': 'Sarasin au trois fromage',
    'prix': 7,
    'categorie': 'Crêpe végétarien',
    'ingredient': ['Cheddar','Chevre','Mozzarella']
},

{
    'nom': 'Crêpe Végéta',
    'prix': 10,
    'categorie': 'Crêpe végétarien',
    'ingredient': ['Courgette','Poivron rouge','Tomate']
}]


# ------------------------Fonctions--------------------

# ----Tri par ordre alphabetique----

def ordre_alpha():
    print()
    alphabetique = sorted(crepe, key=lambda d: d['nom'])
    nm = 1        
    for i in range (len(alphabetique)):
        print ("\t\t", nm,". ",alphabetique[i]['nom'],' - ',alphabetique[i]['prix'],'€ -',alphabetique[i]['categorie'],' - ',alphabetique[i]['ingredient'], '\n')
        nm += 1
    return alphabetique



# ----Tri a bulle pour ordre croissant----
def tri_bulle_croissant(crepe):
    n = len(crepe)
    # Traverser tous les éléments du tableau
    for i in range(n):
         for j in range(0, n-i-1):
            # Échanger si l'élément trouvé est plus grand que le suivant
            if crepe[j]['prix'] > crepe[j+1]['prix'] :
                crepe[j]['prix'], crepe[j+1]['prix'] = crepe[j+1]['prix'], crepe[j]['prix']
    return crepe




# ----Tri selectif pour ordre decroissant----
def tri_selection_decroissant(crepe):
   for i in range(len(crepe)):
      # Trouver le min
       min = i
       for j in range(i+1, len(crepe)):
           if crepe[min]['prix'] < crepe[j]['prix']:
               min = j
       tmp = crepe[i]
       crepe[i] = crepe[min]
       crepe[min] = tmp



# ----Trouve le prix max----
def max_prix():
    print()
    maxPricedItem = max(crepe, key=lambda x:x['prix'])
    return maxPricedItem



# ----Trouve le prix min----
def min_prix():
    print()
    minPricedItem = min(crepe, key=lambda x:x['prix'])
    return minPricedItem


# ----Crepe perso----
panier = []
ingredients = [('Nutella',0.50),('Chantilly', 1),('Sucre Glace',0.80),('Confiture a la fraise', 0.60), ('Viande Kebab', 4),('Poulet', 5),('Tomate', 2),('Courgette',1.50),('Salade', 1.80),('Cheddar',0.50),('Mozzarella',0.50),('Poivron Rouge', 1)]
crepeperso = ["Crepe custom :", 3]
def perso():
    print("Que souhaitez-vous ajouter dans votre commande ? A tout moment, vous pouvez annuler en tapant : stop ! \n")
    choixIngredientsTemp = "" #stock qu'un seul ingrédient le temps de la boucle
    liste_ing = [] #stock tous les ingrédients
    for i in range (len(ingredients)):
        print ("\t\t",". ",ingredients[i][0],' - ',ingredients[i][1],'€','\n')

    while choixIngredientsTemp != 0:
        try:
            userInput = input("Rentrer le nom de l'ingredient à ajouter : ")
            for i in range (len(ingredients)):
                if userInput in ingredients[i][0]:
                    choixIngredientsTemp = ingredients[i]
                    print('Votre crêpe personnalisé coûte :',crepeperso[-1] + choixIngredientsTemp[-1],'€', 'vous pouvez la terminer en tapant : stop')
                    crepeperso[-1] = crepeperso[-1]+choixIngredientsTemp[-1]
                    liste_ing.append(choixIngredientsTemp[0])
                elif userInput == "stop" :
                    if len(choixIngredientsTemp) == 0:
                        menu()
                    else:
                        panier.append(crepeperso[-1])
                        carte_crepe = open("Menu.txt", "w", encoding='utf-8')
                        carte_crepe.write("Voici votre crêpe personnalisé :\n")
                        for j in range(len(liste_ing)):
                            carte_crepe.write(' - ' + liste_ing[j] + "\n")

                        carte_crepe.write("\n\n")
                        carte_crepe.close()
                        menu()
        except KeyError :
            print("Prenez un ingrédient de la liste")

# ------------------------Debut--------------------

print()
print("_____________________________________________".center(columns))
print(" Bienvenue à la meilleure Creperie du monde!".center(columns))
print("_____________________________________________".center(columns))
print()

# ------------------------Choix de l'utilisateur--------------------

def menu():
    while True:
        system("pause")
        print()
        print("1- Afficher la liste des crêpes par ordre alphabétique".center(columns))
        print("2- Afficher la liste des crêpes par prix croissant".center(columns))
        print("3- Afficher la liste des crêpes par prix décroissant".center(columns))
        print("4- Afficher la crêpe la plus chère".center(columns))
        print("5- Afficher la crêpe la moins chère".center(columns))
        print("6- Personnaliser votre propre crêpe".center(columns))
        print("7- Abandonner la commande".center(columns))
        choix=int(input("Choisisez une option : "))
        system("cls")

        # verifie si le nombre fais partie des choix disponible
        if not 1 <= choix <= 7:
            print("Merci de choisir une option disponible s'il vous plait !".center(columns))

    # ------------------------Choix 1--------------------
        #si choix 1 : tri par ordre aplhabetique avec la def ordre_alpha
        if choix==1:
            ordre_alpha()

    # ------------------------Choix 2--------------------
        # si choix 2 : tri par prix croissant avec la def tri_a_bulle
        if choix==2:
            print ("Le tableau trié par ordre croissant:".center(columns))
            nm = 1        
            for i in range(len(crepe)):
                tri_bulle_croissant(crepe)
                print ("\t\t\033", nm,". ",crepe[i]['nom'],' - ',crepe[i]['prix'], '€','\n')
                nm += 1

    # ------------------------Choix 3--------------------
        # si choix 3 : tri par ordre decroissant avec la def tri_selection_decroissant
        if choix == 3:
            print ("La liste de crêpes par prix croissant : ".center(columns))
            nm = 1        
            for i in range (len(crepe)):
                tri_selection_decroissant(crepe)
                print ("\t\t\033", nm,". ",crepe[i]['nom'],' - ',crepe[i]['prix'], '€','\n')
                nm += 1

    # ------------------------Choix 4--------------------
        #si choix 4 : affiche la crepe la plus chere avec la def min prix
        if choix==4:
            print('La crêpe la plus chère est la',max_prix()['nom'], 'au prix de', max_prix()['prix'], '€', '\n\n\n')
    # ------------------------Choix 5--------------------
        #si choix 5 = affiche la crepe la moins chere avec la def max prix
        if choix==5:
            print('La crêpe la moins chère est la ',min_prix()['nom'], 'au prix de', min_prix()['prix'], '€', '\n\n\n')


    # ------------------------Choix 6--------------------
        # si choix 6= custom crepe avec la def perso
        if choix==6:
            perso()

    # ------------------------Choix 7--------------------
        #Quitte le programme
        if choix==7:
            print("A la prochaine fois !".center(columns))
            exit()
        
menu()