from enemy import Enemy
from hero import Hero


class Game:
  """
  Classe responsável por gerenciar o jogo.
  """

  def __init__(self) -> None:
    self.hero = Hero("Teste", 10, 5, "Guerreiro")
    self.enemy = Enemy("Teste", 10, 5, "Voador") 
    
  def play_game(self):
    while(self.hero.get_life() > 0 and self.enemy.get_life() > 0):
      print("Detalhes dos personagens:\n")
      print(self.hero.show_attributes())
      print("--------------------------------")
      print(self.enemy.show_attributes())
      
      input("Presione ENTER para atacar")
      
      choice = input("Pressione 1 para ataque normal e 2 para ataque especial: ")
      if(choice == "1"):
        get_value_attack_hero = self.hero.attack_normal(self.enemy)
        
        self.enemy.decrease_life(get_value_attack_hero)
        
      elif(choice == "2"):
        self.hero.special_attack(self.enemy)
      else:
        print("Opção inválida")
      
      get_value_attack_enemy = self.enemy.attack_normal(self.hero)
      
      self.hero.decrease_life(get_value_attack_enemy)
      
      print("\nFim da rodada!!\n")
      