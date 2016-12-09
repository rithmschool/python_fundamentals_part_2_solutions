# Using the requests module and the OMDB API, build an application that prompts 
# the user for two pieces of information, the name of an actor/actress and a movie. 
# Your program should tell the user if that actor or actress was in that movie 
# (this will only work for leading actors and actresses). 

# As a bonus, add functionality to tell users who the director and writer of a movie were.

import requests

# if you are using python 2 make sure you use raw_input and not input

movie = input('What movie would you like to search? ')
actor = input('What actor/actress would you like to search for? ')

r = requests.get('https://omdbapi.com?t={}'.format(movie))

if actor.lower() in r.json()['Actors'].lower():
    print('Yes! {} was in {}'.format(actor,movie))
else:
    print("Nope!")