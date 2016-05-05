first_name = raw_input("Enter your name:  ")
fav_color = raw_input("Enter your favorite color:  ")
fav_tvshow = raw_input("Enter your favorite TV show:  ")

story = ["Donald Trump", "Jimmy Fallon"]


for i in range(0,3):
	story.append(raw_input("Enter a number between 1 and 10:  "))
	i = i+1

tvshows = dict()
tvshows = {story[0]:"The Apprentice", story[1]:"The Tonight Show"}

trump_wallet = int(story[2]) * 100000
fallon_wallet = int(story[3]) * 100000

if trump_wallet > fallon_wallet:
	a = "Donald Trump is willing to pay more than Jimmy Fallon for you to guest star in his TV show. "
elif fallon_wallet > trump_wallet:
	a = "Jimmy Fallon is willing to pay more than Donald Trump for you to guest star in his TV show. "
else:
	a = "Both Donald Trump and Jimmy Fallon have offered to pay $" + str(trump_wallet) + " for you to guest star in their TV show."

if fav_tvshow == tvshows[story[0]]:
	b = "Donald Trump and you have something in common."
elif fav_tvshow == tvshows[story[1]]:
	b = "Jimmy Fallon and you have something in common."

def story_sentence(y, z):
	make_sentence = "Hi " + y + "!" + " The " + z + " socks you are wearing defiantly wont go unnoticed."
	return make_sentence

d = story_sentence(first_name, fav_color);
#print d