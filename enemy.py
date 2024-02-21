from character import Character


class Enemy(Character):
  def __init__(self, name, life, lvl, type) -> None:
    super().__init__(name, life, lvl)
    self.__type = type
    
    
  def get_type(self):
    return self.__type

  def show_attributes(self):
    return f"{super().show_attributes()}\nTipo: {self.get_type()}"