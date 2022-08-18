
class Boss:
    def __init__(self, name: str, damage: int, puzzle_FEN: str, move_list: list) -> None:
        self.name = name
        self.damage = damage
        self.move_list = move_list
        self.boss_moves = move_list[::2]
        self.player_moves = move_list[1::2]
        self.puzzle_FEN = puzzle_FEN
    def __str__(self) -> str:
        return f"Boss Name: {self.name} -- Boss Damage {self.damage}"
    def __repr__(self) -> str:
        return f'Boss({self.name}, {self.damage}, {self.puzzle_FEN}, {self.move_list})'
    def attack(self, hero):
        hero.hp -= self.damage
    def battle(self, hero):
        pass
