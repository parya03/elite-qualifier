import random
import unittest
from requests import get
import json

###################################
#Pranit Arya                      #
#Chatbot Project                  #
###################################

#The basis of my code was taken from the Code2College Chatbot starter code

#The code can be expanded to have more responses by adding or editing relevant
#response arrays/lists and setting what type of response they are in
#generate_response(), then adding more ifs to handle_input() to check for what words
#and phrases to map to which response

#Global variables
name = ""
useName = 0

#Initialize APIs and variables
publicIP = get("https://api.ipify.org").text
#print(publicIP)
geolocation = get("http://ip-api.com/json/").json() #Get location of the system where this script is being ran, for future reference
#geolocationDict = json.loads(geolocationJSON) #Get geolocation JSON and parse it into a Python dictionary, NOT NECESSARY
#print(geolocation["city"] + ", " + geolocation["regionName"] + ", " + geolocation["country"])
with open("trivia.json") as trivia_file: #Open trivia JSON file
  trivia = json.load(trivia_file)
  #print(trivia)

def introduction():
  global name
  global useName
  name = input("What is your name?")
  useName = 1 #Tell generateResponse() to address user by name
  return "Nice to meet you, " + name


def generate_response(responseType): #Pass types of responses to return
  stringToReturn = ""
  genericResponses = [ #Type 0
    "How interesting",
    "You don't say",
    "Very cool",
    "Programming is fun",
    "That's really nice"
  ]
  yesNoResponses = [ #Type 1
    "Yes",
    "No"
  ]
  if(responseType == 0):
    stringToReturn = random.choice(genericResponses)
  if(responseType == 1):
    stringToReturn = random.choice(yesNoResponses)
  if(responseType == 2):
    stringToReturn = "I am currently running on a system in " + geolocation["city"] + ", " + geolocation["regionName"] + ", " + geolocation["country"]
  if(responseType == 3):
    z = list(trivia["Capitals"].keys())
    zindex = random.randrange(0, len(z))
    response = input("What is the capital of " + z[zindex] + "? ")
    if(response == trivia["Capitals"][z[zindex]]):
      stringToReturn = "You are correct"
    else:
      stringToReturn = "Try again"
    #print(trivia["Capitals"])
  if(responseType == 4):
    z = list(trivia["Jokes"].keys())
    zindex = random.randrange(0, len(z))
    response = input(z[zindex])
    stringToReturn = trivia["Jokes"][z[zindex]]
  
  global useName
  global name
  if(useName == 1): #If user has introduced themself, use their name
    stringToReturn += (", " + name)
  
  return stringToReturn

def init_chat():
  quit_character = 'quit'

  user_input = input("Hello, how are you? Type help for help! \n")

  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    user_input = input(handle_input(user_input) + "\n")

def handle_input(input):
  if input.find("Can") != -1 or input.find("can") != -1 or input.find("Is") != -1 or input.find("is") != -1:
    return generate_response(1)
  if input.find("help") != -1:
    return "Type quit to quit, introduce to tell the Chatbot your name, trivia to find country capitals, and skip to have the Chatbot ask you something"
  if input.find("skip") != -1:
    return "Tell me something about yourself!"
  if input.find("introduce") != -1:
    return introduction()
  if input.find("where are you") != -1:
    return generate_response(2)
  if input.find("trivia") != -1:
    return generate_response(3)
  if input.find("jokes") != -1:
    return generate_response(4)

  else:
    return generate_response(0)


if __name__ == "__main__":
  init_chat()