class Equipo(object):
	"""docstring for Equipo"""
	def __init__(self, nombre,ciudad,campeonatos,numJugadores):
		self.nombre=nombre
		self.ciudad=ciudad
		self.campeonatos=int(campeonatos)
		self.numJugadores=int(numJugadores)
	"""
	Creamos los metodos GET y SET para cada atributo
	"""
	def setNombre(self,nombre):
		self.nombre=nombre
	def getNombre(self):
		return self.nombre

	def setCiudad(self,ciudad):
		self.ciudad=ciudad
	def getCiudad(self):
		return self.ciudad

	def setCampeonatos(self,campeonatos):
		self.campeonatos=int(campeonatos)
	def getCampeonatos(self):
		return self.campeonatos

	def setNumJugadores(self,numJugadores):
		self.numJugadores=int(numJugadores)
	def getNumJugadores(self):
		return self.numJugadores
	"""
	Metodo __str__ y __repr__ para personalziar al rpesentacion de nuestro objeto
	"""
	def __str__(self):
		cadena="Nombre: %s|Ciudad: %s|Partidos Ganados: %d|Partidos Jugados: %d\n"%(self.nombre,self.ciudad,self.campeonatos,self.numJugadores)
		return cadena
	def __repr__(self):
		cadena="Nombre: %s|Ciudad: %s|Partidos Ganados: %d|Partidos Jugados: %d\n"%(self.nombre,self.ciudad,self.campeonatos,self.numJugadores)
		return cadena


class Operaciones(object):
	
	def __init__(self, listado):
		self.listado_equipos=listado

	def ordenar(self, opcion):	
		"""
			https://docs.python.org/3/howto/sorting.html
            >>> sorted(student_objects, key=lambda student: student.age)   # sort by age
		"""
		if opcion=="Nombre":
			return sorted(self.listado_equipos, key=lambda equipo: equipo.nombre)
		elif opcion=="Campeonatos":
			return sorted(self.listado_equipos, key=lambda equipo: equipo.campeonatos)	


		