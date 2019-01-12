	#!/usr/bin/python

from datetime import datetime
import json


def next_class():
	actual_time = datetime.now().time()
	actual_day = str(datetime.today().weekday())
	# actual_day = '1'
	# actual_time = datetime.strptime("9:00:00","%H:%M:%S").time()
	with open('/home/diego/.dotfiles/horario.json', 'r') as jsonfile:
		classes = json.load(jsonfile)['calendar']
		classes = classes[actual_day]

	return tell_class(classes, actual_time)

def tell_class(classes, actual_time):
	#Recorre el horario de trenes hasta encontrar el proximo
	for clas in classes:
		clas_time = datetime.strptime(clas, "%X").time()
		if (clas_time > actual_time):
			#El formato de la hora es "hh:mm:ss" pero solo devuelve "hh:mm"
			return classes[clas], clas[:-3]
	return None

def print_class(next, class_time):
	with open('/home/diego/.dotfiles/horario.json', 'r') as jsonfile:
		asignaturas = json.load(jsonfile)['class'][next['name']]
		print ('Siguiente clase:\n\n',asignaturas['long'])
		print ('\tA las',class_time)
		print ('\tEn',asignaturas['where'])
		print ('\tLa clase dura',asignaturas['duration'])
		print ('\tGrupo',asignaturas['group'])
		print ('\tCurso',asignaturas['course'])

	pass

def main():
	if next_class()!=None:
		next, class_time=next_class()
		print_class (next, class_time)
	else:
		print ('Hoy no hay mas clases!')


if __name__== "__main__":
	main()