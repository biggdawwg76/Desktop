#For loops examples

#print "EXAMPLE 1: We can use for loops to go through a list of strings"
##    count=0
#    for e in U:
#        if e[0] =='U':
#            count = count + 1
#    return count

#print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

#print measure_udacity(['Umika','Umberto'])
#>>> 2

#y loops

#def find_element(p,t):
#    i=0
#    while i< len(p):
#        if p[i]==t:
#            return i
#        i=+1
#        return -1


#for loop

#def find_element(p,t):
#    i=0
#    for e in p:
#    if e == t:
#    i=i+1
#    return -1


#indew Method





#def weekend(day):
 #  if day == 'Saturday' or day == 'Sunday':
#       return True
 #  else:
#       return False
 #return False

#print weekend('Monday')
#>>> False

#print weekend('Saturday')
#>>> True

#print weekend('July')
#>>> False



countDown = 3
while (countDown >= 0):
    if countDown != 0:
        print(countDown)
        countDown = countDown - 1
    else:
        print("Action!")
        break






# madlibs generator test strung

# Write code for the function word_transformer, which takes in a string word as input.
# If word is equal to "NOUN", return a random noun, if word is equal to "VERB",
# return a random verb, else return the first character of word.

from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"

def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == "NOUN":
        return random_noun()
    if word == "VERB":
        return random_verb()
    else:
        return word [0]


# madlibs generator full string
from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"

def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == "NOUN":
        return random_noun()
    elif word == "VERB":
        return random_verb()
    else:
        return word[0]

def process_madlib(mad_lib):
    processed = ""
    index = 0
    box_length = 4
    while index < len (mad_lib):
        frame = mad_lib [index:index+box_length]
        to_add = word_transformer (frame)
        processed += to_add
        if len (to_add) ==1:
            index +=1
        else:
            index += 4
    return processed

    # you may find the built-in len function useful for this quiz
    # documentation: https://docs.python.org/2/library/functions.html#len

test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print process_madlib(test_string_1)
print process_madlib(test_string_2)
