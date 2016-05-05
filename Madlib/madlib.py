first_name = raw_input("Enter your name:  ")
fav_color = raw_input("Enter your favorite color:  ")
fav_tvshow = raw_input("Enter your favorite TV show:  ")

story = ["Donald Trump", "Jimmy Fallon"]


for i in range(0,3):
	story.append(raw_input("Enter a number between 1 and 10:  "))
	i = i+1

tvshows = dict()
tvshows = {story[0]:"The Apprentice", story[1]:"The Tonight Show"}

trump_wallet = story[2] * 1000000
fallon_wallet = story[3] * 100000
wallet = story[4] * 100 - 50