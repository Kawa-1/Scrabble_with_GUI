from enum import Enum

# Not implemented Enum; JUST IDEA YET
class LevelAI(Enum):
    HARD = "hard"
    MEDIUM = "hard"
    EASY = "easy"

class Player:
    """This class will hold information involved with information of user
    who has logged in to play the game
    """
    # Empty string mean player, EASY means AI as well as HARD means AI as well as MEDIUM; considering difficulty parameter
    def __init__(self, name: str, rack: list, bot=False, difficulty=""):
        self._name = name
        if bot is True:
            self._name = name + "_AI"
        self._rack = rack
        self._score = 0
        self._fails = 0
        self._bot = bot
        self._difficulty = difficulty
        self._tiles_put = 0
        self._word_best = ""
        #self.tiles_put_statistics = ""
        #self._swapped = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def rack(self) -> list:
        return self._rack

    @property
    def score(self) -> int:
        return self._score

    @property
    def fails(self):
        return self._fails

    @property
    def bot(self):
        return self._bot

    @property
    def difficulty(self):
        return self._difficulty

    @property
    def tiles_put(self):
        return self._tiles_put

    @property
    def word_best(self):
        return self._word_best

    #@property
    #def swapped(self):
    #    return self._swapped

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @rack.setter
    def rack(self, init_rack: list):
        self._rack = init_rack

    @score.setter
    def score(self, points_add: int):
        self._score += points_add

    @fails.setter
    def fails(self, add_one: int):
        self._fails += add_one

    #@swapped.setter
    #def swapped(self, add_one: int):
    #    self._swapped += add_one

    @bot.setter
    def bot(self, flag):
        self._bot = flag

    @difficulty.setter
    def difficulty(self, level):
        self._difficulty = level

    @tiles_put.setter
    def tiles_put(self, tiles_put):
        self._tiles_put += tiles_put

    @word_best.setter
    def word_best(self, best_word):
        self._word_best = best_word

    @fails.deleter
    def fails(self):
        self._fails = 0

    #@swapped.deleter
    #def swapped(self):
    #    self._swapped = 0




