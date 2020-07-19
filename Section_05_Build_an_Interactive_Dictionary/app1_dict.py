##############################################################################
# WHAT:
# Build an interactive dictionary
# from Section 5 of https://www.udemy.com/the-python-mega-course
#
# DESCRIPTION:
# This program is executed from the command line.
# It reads a JSON file, data.json which is a dictionary of English
# words and definitions into memory. Then it prompts the user for a word
# and returns the definition(s).
# It matches exact case and exact spelling but will suggest matches when it
# finds matches that do not match case or exact spelling.
#
#-----------------------------------------------------------------------------
# DATE         WHO                   DESCRIPTION
# ----------   --------------------  -----------------------------------------
# 2019-03-13   Maurice Johnson       Created
##############################################################################
import json

# module that returns imprecise word matches
from difflib import get_close_matches

# Dictionary of words with one or more definitions
data = json.load(open("data.json"))

# Word match function
def translate(w):
    w = w.lower()                     # First attempt case insensitive match
    if w in data:
        return data[w]
    elif w.title() in data:           # Then attempt to match proper nouns
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]        # Then attempt acronymn or all caps match
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("did you mean %s instead ? Enter Y if yes, or N if no." % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word does not exist - please double check it"
        else:
            return "I did not understand your entry"
    else:
        return "The word does not exist - please double check it"


# Prompt user to enter a word
word = input("enter word: ")


# This cleanup the output which is in Python dictionary form
# e.g., Mississippi has two definitions in the Dictionary
#        ['The 20th state of the United States of America, located in the South.','The longest river in the United States.']
# But they are cleaned up and display as
#       The 20th state of the United States of America, located in the South.
#       The longest river in the United States.
output = translate(word)

if type(output) == list:
    for item in output:  # This only applies to the output from the dictionary
        print(item)
else:
    print(output)      # The error messages are strings and do not need to be parsed and printed on separate lines
