#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
import json


#Funciones para saber el proximo tren
def next_train(trip): #city puede ser 'cor' (Cordoba) o 'rab' (Rabanales)
	hora_act = datetime.now().time()

	with open('/home/diego/.dotfiles/trains.json', 'r') as jsonfile:
		trains = json.load(jsonfile)[trip]

	actual_day = int(datetime.today().weekday())
	if (actual_day < 5):
		return tell_train(trains['entreSemana'], hora_act)
	else:
		return tell_train(trains['finDeSemana'], hora_act)


def tell_train(trains, hora_act):
	#Recorre el horario de trenes hasta encontrar el proximo
	for train in trains:
		train = datetime.strptime(train, "%H:%M:%S").time()
		if (train > hora_act):
			#El formato de la hora es "hh:mm:ss" pero solo devuelve "hh:mm"
			return train.strftime("%I:%M %p")


def main():
	# ├
	print 'next trains:'

	print '\nFrom Cordoba to:'
	print '\t└Rabanales at',next_train('Cordoba-Rabanales')

	print '\nFrom Rabanales to:'
	print '\t└Cordoba at',next_train('Rabanales-Cordoba')


if __name__== "__main__":
	main()
