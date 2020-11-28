import csv
import random
from termcolor import colored
import pickle
from networkplayer import NetworkPlayer

double = False


class NetworkGame:

    def __init__(self, question_csv, no_of_players, load_game=False):
        self.diceroll = 0
        self.contents = []
        self.sites = ['Home', "Github", "Imgur", "DNS", "Spotify", "YouTube"]
        self.SSP = [
            "0. Not in use",
            "1.	Database request needed - Miss next turn",
            "2.	Cache prize - Store all DNS entries",
            "3.	Gigabit Ethernet - make your next roll now"]
        with open(question_csv) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.contents.append(row)

        self.size_of_board = 10

        if load_game:
            self.players = pickle.load(open("save.p", 'rb'))
            self.current_player = int(input("Current player (INTEGER): ")) - 1
        else:
            self.players = []
            for i in range(no_of_players):
                print("What is the name of player ", i + 1)
                name = input("-->")
                self.players.append(NetworkPlayer(name))
            self.current_player = -1

    def display_board(self):
        # Clear screen
        # system('clear')
        boardline_1 = ["->\t" for i in range(self.size_of_board)]

        boardline_1[-1] = 'YouTube'
        boardline_1[-2] = 'Spotify'
        boardline_1[-3] = 'DNS\t'
        boardline_1[-4] = 'Imgur\t'
        boardline_1[-5] = 'Github\t'

        print("\t|".join(boardline_1))

        for i in range(len(self.players)):
            boardline_1 = ["__" for i in range(self.size_of_board)]
            boardline_1[self.players[i].position] = self.players[i].name
            string_to_print = "\t\t|".join(boardline_1)
            if i == self.current_player:

                print(colored(string_to_print, "red"))
            else:
                print("\t\t|".join(boardline_1))
        print("\n")

    def display_information(self):
        # Name, Letter, Pos, Score, destination, packets_remain, last_location, page to load, cache
        print("Player: ", self.players[self.current_player].name)
        print("Packet Destination: ", self.players[self.current_player].destination)
        print("Loading site: ", self.players[self.current_player].page_to_load)
        print("Cache: ", self.players[self.current_player].cache, "\n")
        print("Score: ", self.players[self.current_player].score)

    def ask_hard(self):
        random_number = random.randint(0, len(self.contents) - 1)

        print("What is this defining?  --> " + self.contents[random_number][1])

        input('\nReturn to reveal answer\n\n')
        print("Correct definition -->  ", self.contents[random_number][0], "\n")
        correct = input("Type anything here if the answer was correct (leave blank if wrong --> ")
        if correct:
            return self.diceroll * 2
        else:
            return 0

    def ask_mcq(self):
        """
        If the game only allows multiple choice questions...
        """
        random_number = random.randint(0, len(self.contents) - 1)
        print("What is this defining?  --> " + self.contents[random_number][1])

        possanswers = []
        for i in range(3):
            possanswers.append(self.contents[random.randint(0, len(self.contents) - 1)][0])
        possanswers.append(self.contents[random_number][0])
        possanswers.sort()
        for i, possanswer in enumerate(possanswers):
            if possanswer == self.contents[random_number][0]:
                correct_answer_number = i
            print(i + 1, "-", possanswer)

        print("Enter answer NUMBER: ")

        answer = input('-->')
        print("Correct definition -->  ", self.contents[random_number][0], "\n")
        if int(answer) == correct_answer_number + 1:
            return self.diceroll
        else:
            return 0

    def check_distance(self):
        """
        Look for the player destination and work out how far they have got left to go...
        """
        if self.players[self.current_player].destination == "Github":
            return (self.size_of_board - 4) - self.players[self.current_player].position
        elif self.players[self.current_player].destination == "Imgur":
            return (self.size_of_board - 3) - self.players[self.current_player].position
        elif self.players[self.current_player].destination == "DNS":
            return (self.size_of_board - 2) - self.players[self.current_player].position
        elif self.players[self.current_player].destination == "Spotify":
            return (self.size_of_board - 2) - self.players[self.current_player].position
        elif self.players[self.current_player].destination == "YouTube":
            return (self.size_of_board - 1) - self.players[self.current_player].position
        elif self.players[self.current_player].destination == "Home":
            return self.players[self.current_player].position
        else:
            return self.players[self.current_player].position

    def start_round(self):
        if self.current_player >= len(self.players) - 1:
            self.current_player = 0
        else:
            self.current_player += 1


    def player_go(self) -> bool:
        pickle.dump(self.players, open("save.p", "wb"))
        self.display_board()
        self.display_information()
        self.diceroll = random.randint(1, 6)

        print("'A' - Multiple choice roll - Move ", self.diceroll)
        print("'B' - No help - Move ", self.diceroll * 2)
        print("What difficulty do you want? (A or B")
        letter = input("-->")
        if letter.lower() == "b":
            return True
        else:
            return False

    def server_side_processing(self):
        self.players[self.current_player].destination = 'Home'
        self.display_board()

        random_number = random.randint(1, len(self.SSP) - 1)
        print(self.SSP[random_number])

        if random_number == 1:
            self.players[self.current_player].skip_flag = 1
            input("OK")
        if random_number == 2:
            self.players[self.current_player].cache = ["Github", "Imgur", "Spotify", "YouTube"]
            self.display_information()
            input("OK")
        if random_number == 3:
            self.current_player -= 1
            input("OK")

    def arrived_at_destination(self):
        """
        Add site to cache if at DNS
        Change destination if at destination
        Display server side processing wildcard if they are at the server.
        """
        if self.players[self.current_player].position == self.size_of_board - (
                len(self.sites) - self.sites.index("DNS")):
            self.players[self.current_player].last_location = self.players[self.current_player].destination
            self.players[self.current_player].destination = self.players[self.current_player].page_to_load
            self.players[self.current_player].cache.append(self.players[self.current_player].page_to_load)
        elif self.players[self.current_player].position == 0:
            self.players[self.current_player].last_location = self.players[self.current_player].destination
            random_site = random.choice(["Github", "Imgur", "Spotify", "YouTube"])
            self.players[self.current_player].page_to_load = random_site
            self.players[self.current_player].score += 1
            if random_site in self.players[self.current_player].cache:
                self.players[self.current_player].destination = random_site
            else:
                self.players[self.current_player].destination = "DNS"
        else:
            self.server_side_processing()

    def move_player(self, distance_to_go):
        """
        Move the player and work out if they have arrived or not
        BUG: IF THEY ARRIVE AT THE DNS WITH NO MOVE LEFT, THE DESTINATION WILL NOT CHANGE.
        """
        arrived = False
        if abs(distance_to_go) <= self.diceroll and "Home" == self.players[self.current_player].destination:
            self.players[self.current_player].position = 0
            arrived = True
        elif abs(distance_to_go) <= self.diceroll:
            self.players[self.current_player].position = self.size_of_board - (
                    len(self.sites) - self.sites.index(self.players[self.current_player].destination))
            arrived = True
        elif self.players[self.current_player].destination == 'Home' or self.size_of_board - (
                len(self.sites) - self.sites.index(self.players[self.current_player].destination)) < self.players[
            self.current_player].position:
            self.players[self.current_player].position -= self.diceroll
        else:
            self.players[self.current_player].position += self.diceroll

        if arrived:
            self.arrived_at_destination()

    def run(self):
        while True:
            """
            Check to see if player should miss a turn
            """
            self.start_round()
            if not (self.players[self.current_player].skip_flag):
                double = self.player_go()
                if double:
                    move = self.ask_hard()
                else:
                    move = self.ask_mcq()
                distance_to_go = self.check_distance()
                if move:
                    self.move_player(distance_to_go)
            else:
                self.players[self.current_player].skip_flag = 0
                print("PLAYER ", self.players[self.current_player].name, "SKIPPED")
