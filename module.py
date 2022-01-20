# Module Fonction

from math import sqrt
import requests
from lxml import etree

#from matplotlib import pylab
#from pylab import *

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

#def courbe(T,L):
#	for i in range (len(T)) :
#		x = array(T[i])
#		y = array(L[i])
#		plot(x, y)
#
#		a=show()
#	return a 

def afficherHTML(a) :
	for i in range (len(a)) :
		b='https://data.montpellier3m.fr/sites/default/files/ressources/'+a[i]+'.xml'
		z=[b]
		print(z)
		response=requests.get(z[i])
		print(response.text)
		t=str(a[i])+'.txt'
		tree = etree.parse(t)
		for user in tree.xpath("Name"):
			print('Nom du parking :',user.text)
		for user in tree.xpath("Total"):
			print('Nombre total de places :',user.text)
		for user in tree.xpath("Free"):
			print('Nombre de places libres :',user.text)
	f1=open(t,"w", encoding='utf8')
	f1.write(response.text)
	f1.close()