import random

class NetworkPlayer():
    def __init__(self, name, sites=["Github", "Imgur", "Spotify", "YouTube"]):
        # 0Name, 1Letter, 2Pos, 3Score, 4destination, 5skip_flag, 6last_location, 7page to load, 8cache
        self.name= name #0 #1
        self.position=0 #2
        self.score=0 #3
        self.destination="DNS" #4
        self.skip_flag=0 #5
        self.last_location="Home" #6
        self.page_to_load = random.choice(sites) #7
        self.cache=[] #8

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    @property
    def destination(self):
        return self.__destination

    @destination.setter
    def destination(self, destination):
        self.__destination = destination

    @property
    def skip_flag(self):
        return self.__skip_flag

    @skip_flag.setter
    def skip_flag(self, skip_flag):
        self.__skip_flag = skip_flag

    @property
    def page_to_load(self):
        return self.__page_to_load

    @page_to_load.setter
    def page_to_load(self, page_to_load):
        self.__page_to_load = page_to_load

    @property
    def last_location(self):
        return self.__last_location

    @last_location.setter
    def last_location(self, last_location):
        self.__last_location = last_location

    @property
    def cache(self):
        return self.__cache

    @cache.setter
    def cache(self, cache):
        self.__cache = cache