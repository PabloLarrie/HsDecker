class mago:
    	def __init__(self, **kwargs):
		self.name = kwargs.get("name")
		self.health = kwargs.get("health")
		self.damage = kwargs.get("damage")
		self.tipo = kwargs.get("tipo")
		self.dead = kwargs.get("dead", False)
		self.protec = kwargs.get("protec", False)
		self.disarm = kwargs.get("disarm", False)

	def attack(self, enemy): 
		if not self.disarm and not enemy.protec: 
			enemy.health -= self.damage
			enemy.check_life()
		else:
			return "No puedes atacar"


	def avada_kedavra(self, enemy):
		if not self.disarm and not enemy.protec:
			carga = True
			if carga == True:
				enemy.health -= enemy.health
				carga = False
				enemy.check_life()
			else:
				return "No puedes utilizar ese hechizo"
		else:
			return "No puedes atacar"

	def protego(self):
		if not self.disarm:
			self.protec = True
			return "Estás protegido"
		else:
			"Estás desarmado"

	def expelliarmus(self, enemy):
		if not self.disarm and not enemy.protec:
			enemy.disarm = True
			return "Tu enemigo está desarmada"
		else:
			return "No puedes hacer eso"


	def get_type(self):
		if self.__class__.__name__:
			return "inutil"

	def get_flow(self):
		return "0"

	def print_info(self):
		print(f"A {self.name} le quedan {self.health} PV. Es un {self.tipo} con {self.get_flow()} puntos de nivel.")
		if self.dead == True:
			print("Este mago ha muerto")

	def print_type(self):
		print(f"{self.name} es un mago {self.get_type()}.")

	def check_life(self):
		if self.health <= 0:
			self.dead = True

	def command(self):
		orden = input()
		self.orden()


class auror(mago):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.lealtad = kwargs.get("lealtad")
		
	def get_type(self):
		return self.__class__.__name__

	def get_flow(self):
		return self.lealtad

	def check_life(self):
		if self.health <= 0:
			self.dead = True

class mortifago(mago):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.obediencia = kwargs.get("obediencia")

	def get_flow(self):
		return self.obediencia
		
	def get_type(self):
		if self.__class__.__name__:
			return "mortífago"

	def check_life(self):
		if self.health <= 0:
			self.dead = True


c1 = mago(name="Xurxo", health=22, damage=6, tipo="Gryffindor")
c2 = auror(name="Benito", health=30, damage=7, tipo="Ravenclaw", lealtad=9)
c3 = mortifago(name="Xoanxo", health=26, damage=4, tipo="Slytherin", obediencia=6)

c1.attack(c2)
c2.expelliarmus(c3)
c3.attack(c1)

for card in [c1, c2, c3]:
    card.print_type()
    card.print_info()
    print(" ")
