# Code pour SAE 15

import module as stat

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

tracerCourbe=stat.courbe(T,L1)
print(tracerCourbe)