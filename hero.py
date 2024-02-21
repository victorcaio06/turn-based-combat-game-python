from character import Character


class Hero(Character):
  def __init__(self, name, life, lvl, skill) -> None:
    super().__init__(name, life, lvl)
    self.__skill = skill

  def get_skill(self):
    return self.__skill
  
  def special_attack(self, target):
    print(f"{self.get_name()} atacou com um ataque normal, causou {int(self.__lvl)} de dano ao {target.get_name()}")

    return int(super().get_lvl()) * 1.5

  def show_attributes(self):
    return f"{super().show_attributes()}\nSkill: {self.get_skill()}"