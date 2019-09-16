# This tool helps you calculate
# the Delta-v of your spacecraft
#
#        |
#       / \
#      / _ \
#     |.o '.|
#     |'._.'|
#     |     |
#   ,'|  |  |`.
#  /  |  |  |  \
#  |,-'--|--'-.|

from math import log

while True:
    print("Entrez 'dv' pour calculer le Delta-v de votre engin spatial")
    print("Entrez 'quit' pour quitter le programme")
    user_input = input(": ")
    
    if user_input == "quit":
        break
  
    elif user_input == "dv":
        isp = float(input("Entrez ISP de votre moteur:"))
        m_vide = float(input("Entrez la masse à vide de l'engin spatial:"))
        m_plein = float(input("Entrez la masse totale de l'engin spatial:"))
        dv = str(log(m_plein/m_vide)*isp*9.81)
        
        print("")
        print("^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        print("Le Delta-v de votre engin spatial est de " + dv +"m/s")
        print("^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~")
        print("")
    else:
        print("Unknown Input")
