from django.db import models

class Adventure(models.Model): #Primer menú
    announcement = models.CharField(max_length=50, unique=True) #Chapter unlocked! Chapter I:Dalaran Bank
    name = models.CharField(max_length=50, unique=True)  #Dalaran 
    message = models.CharField(max_length=150, unique=True) # Dalaran! A splendid, floating city of...
    menus = models.ForeignKey('adventure.Chapter', through='adventure.AdventureChapters', on_delete=models.CASCADE) #Selección de capítulo (I, II, III, IV o V)


class Chapter(models.Model): #Segundo menú
    number = models.PositiveIntegerField() #I
    name = models.CharField(max_length=50, unique=True) #Dalaran Bank
    message = models.CharField(max_length=150, unique=True) #Everyone, split up. For this plan to work, we must each do our part.
    info = models.CharField(max_length=100, unique=True) #Break into the Bank of Dalaran to loot its most precious artifacts.
    rewards = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100) #Enseña una imagen del reward.
    description = models.CharField(max_length=50, unique=True) #First Chapter, bank of Dalaran... (Accesible desde el menú anterior)  
    adventure = models.ForeignKey('adventure.Adventure', through='adventure.AdventureChapters', on_delete=models.CASCADE)
    anomaly_get = models.ManyToManyField('adventure.Anomaly', related_name='chapters', on_delete=models.CASCADE) #relación chapter/anomaly
    new = models.BooleanField() #Indica si se trata de un Challenge nuevo con "New"
    #para avanzar al siguiente menú solo hay que darle a "GO!"
    

class AdventureChapter(models.Model): #Tabla de relación
    adventure = models.ForeignKey('adventure.Adventure', on_delete=models.CASCADE) #Indica la aventura
    chapter = models.ForeignKey('adventure.Chapter', on_delete=models.CASCADE) #Indica el capítulo
    info = models.CharField(max_length=50, unique=True) #Dalaran. 0/5 Chapters Completed
    unlocked = models.BooleanField() #Indica si el chapter es accesible
    unlocked_info = models.CharField(max_length=50) #Opens week 2 / Still unlocked
    new = models.BooleanField() #Indica si se trata de un Challenge nuevo con un contorno brillante.
    reward_status = models.BooleanField() #Indica si se ha conseguido el reward
    anomaly = models.BooleanField() #Indica si se juega con o sin Anomaly.

class Anomaly(models.Model): #subtrama del segundo menú
    name = models.CharField(max_length=50, unique=True) #Anomaly- Arcane
    description = models.CharField(max_length=50, unique=True) #All spells cost (2) less.
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100) #imagen de la anomalía
    info = models.CharField(max_length=50, unique=True)  #Anomaly Mode: Gain a random effect this turn.

class Champion(models.Model): #Tercer menú
    message = models.CharField(max_length=200, unique=True) #We have recruited an elite band of disenfranchised miscreantes. Each have their own strengths.     
    unlocked = models.BooleanField() #Indica si el Hero es accesible
    unlocked_info = models.CharField(max_length=100) #Opens week 2 / Still unlocked
    new = models.BooleanField() #Indica si se trata de un Champion nuevo con "New"
    hero = models.ManyToManyField('adventure.Hero', related_name='champions', on_delete=models.CASCADE) #Selección del hero.
    hero = models.ManyToManyField('cards.Hero', related_name='champions', on_delete=models.CASCADE) #Selección del hero.


"""class Hero(models.Model): #heroes
    name = models.CharField(max_length=30, unique=True) #Rakanishu
    description = models.TextField(max_length=200) #The mischievous fire elemental from Togwaggle's lantern.
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100) #imagen del hero
    hero_class = models.ForeignKey('cards.HeroClass', related_name='adventure heros', on_delete=models.CASCADE) #clase del hero
    health = models.PositiveIntegerField(default=30) #salud del hero
    armor = models.PositiveIntegerField(default=0) #armadura del hero"""


class Power(models.Model): #Cuarto menú
    message = models.CharField(max_length=200, unique=True) #As we plunder the riches of Dalaran...
    unlocked = models.BooleanField() #Indica si el power es accesible
    unlocked_info = models.CharField(max_length=100) #Summon Totems 0/25 | Overload Mana 0/25
    new = models.BooleanField() #Indica si se trata de un Power nuevo con "New"
    hero_power = models.ManyToManyField('cards.Power', related_name='abbilities', on_delete=models.CASCADE) #Selección del Power.
    #bosses = models.PositiveIntegerField(default=0) #indica el número de bosses derrotados


class Deck(models.Model): #Quinto menú
    message = models.CharField(max_length=200, unique=True) #You will begin with a modest deck...
    unlocked = models.BooleanField() #Indica si el Deck es accesible
    unlocked_info = models.CharField(max_length=100) #Defeat Bosses 0/5 | 0/10 | 0/15
    new = models.BooleanField() #Indica si se trata de un Deck nuevo con "New"
    hero_decks = models.ManyToManyField('decks.Deck', related_name='adventure decks', on_delete=models.CASCADE) #Selección del Deck.
    #bosses = models.PositiveIntegerField(default=0) #indica el número de bosses derrotados
    

class Challenge(models.Model): #Sexto menú
    message = models.CharField(max_length=200, unique=True) #The guards and citizens of Dalaran will rise against you...
    round_ind = models.PositiveIntegerField(default=1) #Indica la ronda en la que se encuentra el jugador.
    hero_enemy = models.ManyToManyField('cards.Hero', related_name='adventure bosses', on_delete=models.CASCADE) #Indicador del Boss.
    bosses = models.PositiveIntegerField(default=0) #indica el número de bosses derrotados    