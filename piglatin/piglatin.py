
from tkinter import W


def bondify(name):
    """
    input: a string in the form "first last"
    returns: a string in the form "Last, First Last"
    """
    l = name.find(" ")
    na = name[l + 1:99].capitalize() + ',' + name[0:l].capitalize() + " " + name[l + 1:99].capitalize()
    return na


def piglatin(word):
    l = word[0].lower()
    n = word.find(".")
    if word in 'aeiou':
        w = word+'yay'
        return w
    else:
        if(n > 0):
            w = word[1:n].capitalize() + word[0:1].lower() + 'ay' + word[n].lower()
            return w
        w = word[1:99] + word[0:1] + 'ay'
        return w
"""
input: a string representing a word
returns: a new string with the word converted to piglatin

Rules:
if the first letter is a consonent, move it from the start to the end and add "ay"
so "hello" becomes "ellohay"

If the first letter is a vowel, just add "yay" to the end

try to also handle upper case words

"""
print(piglatin("Hello."))
print(bondify("thomas huang"))