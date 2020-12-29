class Card:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.cost = kwargs.get("cost")
        self.rarity = kwargs.get("rarity")
        self.description = kwargs.get("description")
        self.golden = kwargs.get("golden", False)
        self.own = kwargs.get("own", False)

    def print_type(self):
        print(f"{self.name} es una carta de tipo: {self.get_type()}")

    def print_info(self):
    	print(f"'{self.name}' es una '{self.get_type()}' de la colección: '{self.colection}', de la expansion: '{self.expansion}', del año: {self.year}.")
    	print(f"Es una carta {self.rarity} de coste {self.cost}.")
    	if self.__class__ == Criatura:
    		print(f"Su fuerza es: {self.strength}, y su resistencia es: {self.endurance}.")
    	print(f'el texto de esta carta dice: "{self.description}".')
    	if self.golden and self.own:
    		print("Tienes esta carta Dorada!")
    	elif self.own:
    		print("Tienes esta carta!")
    	
    	print("")

    def get_type(self):
        return self.__class__.__name__

class Colection(Card):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.colection = kwargs.get("colection")
		self.year = kwargs.get("year")

	def get_type(self):
		return self.__class__.__name__

class Expansion(Colection, Card):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.expansion = kwargs.get("expansion")
		self.colection = kwargs.get("colection")

	def get_type(self):
		return self.__class__.__name__
        
class Criatura(Expansion, Colection, Card):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.strength = kwargs.get("strength")
        self.endurance = kwargs.get("endurance")

    def get_type(self):
        return self.__class__.__name__
        

class Hechizo(Expansion, Colection, Card):
    pass

class Arma(Expansion, Colection, Card):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.attack = kwargs.get("attack")
        self.durability = kwargs.get("durability")

carta_normal2 = Expansion(expansion="Hola")
carta_normal1 = Colection(colection="aaa", year="1992")
carta_normal = Card(name="Hola")
leeroy_creature = Criatura(name="Leeroy Jenkins", cost=5, rarity="Legendary", description="Tiene dos dragoncitos", golden=True, strength=6, endurance=2)
brain_freeze = Hechizo(name="Brain Freeze", cost=1, rarity="Uncommon", description="Comí mucho helado")
carta_prueba = Criatura(name="Pedo", cost=8, rarity="Legendaria", description="Te tirah un peo y te vah", golden=True, 
	colection="Año del Fenix", year="2020", expansion="Cenizas de Terrallende", strength=8, endurance=8, own=True)
carta_prueba2 = Hechizo(name="Casa", cost=9, rarity="Común", description="vai durmir", golden=False, 
	colection="Año del Mamut", year="2017", expansion="El proyecto Armagebum", own=True)
carta_prueba3 = Arma(name="Salchipapa", cost=10, rarity="Legendaria", description="Te vas a comer una...", golden=True, 
	colection="Año del Fenix", year="2020", expansion="Cenizas de Terrallende", attack=8, durability=8)

carta_prueba.print_info()
carta_prueba2.print_info()
carta_prueba3.print_info()
#for card in [carta_normal, leeroy_creature, brain_freeze, carta_normal1, carta_normal2, carta_prueba]:
    #card.print_type()