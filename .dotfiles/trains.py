#!/usr/bin/python

from datetime import datetime
import json


#Funciones para saber el proximo tren
def next_train(city): #city puede ser 'cor' (Cordoba) o 'rab' (Rabanales)
	hora_act = datetime.now().time()

	with open('/home/diego/.dotfiles/trains.json', 'r') as jsonfile:
		trains = json.load(jsonfile)[city]

	return tell_train(trains, hora_act)


def tell_train(trains, hora_act):
	#Recorre el horario de trenes hasta encontrar el proximo 
	for train in trains:
		train = datetime.strptime(train, "%X").time()
		if (train > hora_act):
			#El formato de la hora es "hh:mm:ss" pero solo devuelve "hh:mm"
			return str(train)[:-3]


def main():
	print 'next train from Cordoba  is at ',next_train('Cordoba')
	print 'next train from Rabanaes is at ',next_train('Rabanales')
  
  
if __name__== "__main__":
	main()