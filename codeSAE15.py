# Code pour SAE 15

import module as stat
import requests

# Instants de la mesure ( h )
T=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

# Série 1 : températures ( °C )
L1=[3,3,4,3,2,5,8,9,13,16,18,18,19,21,22,22,21,17,17,12,10,8,7,4]

# Série 2 : températures ( °C )
L2=[103,203,4,3,2,5,8,9,13,16,18,18,19,21,22,22,21,17,17,12,10,-92,-93,-96]


moyenneL1=stat.moyenne(L1)
print(moyenneL1)

EcartTypeL1=stat.ecartType(L1)
print(EcartTypeL1)

#tracerCourbe=stat.courbe(T,L1)
#print(tracerCourbe)

#Ecrire un programme permettant de récupérer et d’afficher toutes les
#données de tous les parkings de la ville.


parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO',
'FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT',
'FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_SABL',
'FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA',
'FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']


for i in range (len(parkings)) :
    a='https://data.montpellier3m.fr/sites/default/files/ressources/'+parkings[i]+'.xml'
    lparkings=[a]
    print(lparkings)
    for i in range (len(lparkings)) :
        response=requests.get(lparkings[i])
        print(response.text)
