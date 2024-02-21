class Character:
  def __init__(self, name, life, lvl) -> None:
    self.__name = name
    self.__life = life
    self.__lvl = lvl
    
  def get_name(self):
    return self.__name

  def get_life(self):
    return self.__life

  def get_lvl(self):
    return self.__lvl

  def attack_normal(self, target):
    print(f"{self.__name} atacou com um ataque normal, causou {int(self.__lvl)} de dano ao {target.get_name()}")
    
    return int(self.__lvl) * 1.3    

  def decrease_life(self, damage):
    self.__life -= damage

  def show_attributes(self):
    return f"Nome: {self.get_name()}\nVida: {self.get_life()}\nNvl: {self.get_lvl()}"