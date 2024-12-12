import random

#iterate through each letter of the country's name, replaces them with "_" and display them one by one if the player doesn't get it right

#word=country; x=number of letters revealed
def displayClue(word,x):
   clue = ""
   for i in range (0, len(word)):
      if i<x:
         clue = clue + word[i]
         #skips the white space and reveals the next letter after it
         if word[i] == " ":
         	x = x + 1
      #replaces the white space with another white space to prevent it from becoming a "_"
      else:
         if " " in word[i]:
         	clue = clue + " "
         else:
         	#replace letters with "_"
         	clue = clue + "_"
       #leave a space after the "_" so everything doesn't get stuck together'
      clue = clue + " "   
   print("Name the country: " + clue.upper())

#function that chooses a random country from the "countries" list
def choice():
				 countries = ["Afghanistan","Albania","Algeria","Andorra","Angola","Antigua And Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan","The Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","Bosnia And Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Canada","Cape Verde","Central African Republic","Chad","Chile","China","Colombia","Comoros","Democratic Republic Of The Congo","Republic Of The Congo","Costa Rica","Croatia","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","East Timor","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Eswatini","Ethiopia","Fiji","Finland","France","Gabon","The Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea Bissau","Guyana","Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iran","Iraq","Republic Of Ireland","Islamic Republic Of Afghanistan","Italy","Ivory Coast","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Federated States Of Micronesia","Moldova","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar","Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","North Korea","North Macedonia","Norway","Oman","Pakistan","Palau","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Romania","Russia","Rwanda","Saint Kitts And Nevis","Saint Lucia","Saint Vincent And The Grenadines","Samoa","San Marino","São Tomé And Príncipe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Korea","South Sudan","Spain","Sri Lanka","Sudan","Suriname","Sweden","Switzerland","Syria","Tajikistan","Tanzania","Thailand","Togo","Tonga","Trinidad And Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States","Uruguay","Uzbekistan","Vanuatu","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"]
				 country = random.choice(countries)
				 return country
				 

turns = 1
#variable to store the points of each round
score = 0
#creates a list of all countries that have already been chosen
chosen = [ ]
#creates ten rounds of the game
while turns <=10:
	turns += 1
	country = choice()
	#prevent a country that has already been chosen from being chosen again (checking if it is in the "chosen" list) and calls the choice() function until a country that has not yet been chosen is selected
	while country in chosen:
		country = None
		country = choice()
	#adds the selected country to the "chosen" list	
	chosen.append(country)
	#reveals the first letter
	x = 1
	#counts how many white spaces the country name has
	y = country.count(" ")
	#s(small),m(medium),b(big). Part of the expression that calculates the game points. Countries with 5 letters or less are worth a maximum of 100 points, from 6 to 10 = 300, above 10 = 500. substracts whitespaces(y) so that it is not counted as characters
	s = 100/(len(country)-y)
	m = 300/(len(country)-y)
	b = 500/(len(country)-y)
	
	#adds the number of blank spaces to the revealed letters (x+y) because the displayClue() function skips the blank spaces but they are still counted as characters outside it, so the game would not end after the last letter revealed
	
	#It reveals the letters while the player doesn't get it right or moves on to the next round if the player gets the name of the country right
	
	while x + y <len(country):
		displayClue(country,x)
		guess = input("Your guess? ").title()
		
		#divide the maximum number of points by the number of letters in the country's name, each new letter revealed subtracts a number of points from the maximum value
		if len(country)<=5:
			points = round(100-(s*x)+s,1)
		elif 5<len(country)<=10:
			points = round(300-(m*x)+m,1)
		else:
			points = round(500-(b*x)+b,1)
		if guess==country:
		   print("\nWELL DONE!","\nPOINTS:",points,"\n")
		   score += points
		   break
		else:
		   #reveals the next letter
		   x = x + 1
		   if x + y == len(country):
		   	print("\nYOU LOSE\nCORRECT ANSWER:",country.upper(),"\nPOINTS: 0\n")
		   	score += 0

print("GAME OVER\nSCORE:",round(score,1))