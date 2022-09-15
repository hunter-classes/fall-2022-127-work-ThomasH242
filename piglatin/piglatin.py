
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
    if( l== 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u'):
        w = word+'yay'
        return w
    else:
        i = word[1:99] + word[0:1] + 'ay'
        return i
"""
input: a string representing a word
returns: a new string with the word converted to piglatin

Rules:
if the first letter is a consonent, move it from the start to the end and add "ay"
so "hello" becomes "ellohay"

If the first letter is a vowel, just add "yay" to the end

try to also handle upper case words

"""
print(piglatin("hello"))
print(bondify("thomas huang"))