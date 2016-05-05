#User input obtained and stored in variables
first_name = raw_input("Enter your name:  ")
fav_color = raw_input("Enter your favorite color:  ")
fav_tvshow = raw_input("Enter your favorite TV show:  ")

#Create an array
story = ["Donald Trump", "Jimmy Fallon"]

#Loop the the user input qustion "Enter a number between 1 and 10:  " 3 times and store each value in the story array
for i in range(0,3):
	story.append(raw_input("Enter a number between 1 and 10:  "))
	i = i+1

#Create dictionary
tvshows = dict()
#Populate dictionary with info
tvshows = {story[0]:"The Apprentice", story[1]:"The Tonight Show"}


#Calculate how much Trump and Fallon are each willing to pay
trump_wallet = int(story[2]) * 100000
fallon_wallet = int(story[3]) * 100000


#Calculate who is willing to pay the most
if trump_wallet > fallon_wallet:
	a = "Donald Trump is willing to pay more than Jimmy Fallon for you to guest star in his TV show. "
elif fallon_wallet > trump_wallet:
	a = "Jimmy Fallon is willing to pay more than Donald Trump for you to guest star in his TV show. "
else:
	a = "Both Donald Trump and Jimmy Fallon have offered to pay $" + str(trump_wallet) + " for you to guest star in their TV show. "


#Check if the users favorite TV show matches any in the dictionary
if fav_tvshow == tvshows[story[0]]:
	b = "Donald Trump and you have something in common. "
elif fav_tvshow == tvshows[story[1]]:
	b = "Jimmy Fallon and you have something in common. "
else:
	b = "You dont have anything in common with Trump or Fallon. "


#Create intro sentence to story using user input

def story_sentence(y, z):
	make_sentence = "Hi " + y + "!" + " The " + z + " socks you are wearing defiantly don't go unnoticed. "
	return make_sentence

#Return function value to variable to be used later
d = story_sentence(first_name, fav_color);

#Print story
print d + "Tonight Donald Trump and Jimmy Fallon want you to guest star in their TV show they host. " + a + b