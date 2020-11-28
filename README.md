# Networking-Board-Game
A digital board game that covers the computer science vocabulary in a network inspired board game.

## What is the game?
The game is played on a linear board where they must retrieve packets from the websites to obtain a point.

Players choose their name and will be initial positioned on 127.0.0.1 (or 'home').

The aim is to get a packet from the correct site and return it to your 'home'.

## Game objectives
1. Start at your home square and you will be assigned a site to get to.
2. Get to the DNS server to resolve the IP address before you go to the site.
3. Get to the correct server.
4. Collect the packet and return it home to get a point.
5. When you get home you will be given a new site to go to.
7. Win by doing this three times.

## Rules
You move by rolling a d6 dice and then answering a correct question. 
	• Multiple choice questions allow you to move the full dice distance. 
	• Challenge questions allow you to move double the value on the dice.

You will be randomly given a site - You will have get a single packet to the root DNS unless you have it cached i.e. you have already been to that site.

When entering a site you will be given one of three server side actions:
1.Database request needed - Miss next turn.
2.Cache prize - Store all DNS entries.
3.Gigabit Ethernet - make your next roll now.

The cache:
To get to a site, its IP must be stored in your cache. If your assigned site is not in the cache, you will have to visit the DNS first.

Over-rolls:
If you roll enough to get to your destination, you will arrive and travel no further.

Questions:
The questions are taken from a range of glossarys that range from GCSE, A-LEVEL and PROFESSIONAL levels of knowledge. You can edit them by editing the 'NetworkingGameQandA.csv' file.

## How to start
Play the game by running 'play_game.py' with python 3.X.