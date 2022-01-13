# Module Fonction

from math import sqrt

def moyenne(L) :
	somme=0
	for i in range (len(L)):
		somme=somme+L[i]
	moy=somme/len(L)
	return moy

def ecartType(L) :
	moy=moyenne(L)
	x=[]
	for i in range (len(L)) :
		x.append((L[i]-moy)**2)
	y=moyenne(x)
	sigma=sqrt(y)
	return sigma
