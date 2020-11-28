from networkgame import NetworkGame


if __name__ == "__main__":

    print("Do you want to load the previous game? (Y or N)")
    load_ans = input("-->")
    load = False
    num_players=0
    if load_ans.lower == "y":
        load = True
    else:
        print("How many players?")
        num_players = int(input("-->"))

    game = NetworkGame("NetworkingGameQandA.csv", num_players, load)
    game.run()

