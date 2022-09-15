def initialize(name):
    """
    input: a string in the form "first last"
    returns: a string in the form "F. Last"
    """
    l = name.find(" ")
    print(l)
    na = name[0].upper() + '.' + name[l + 1:99].capitalize()
    return na


def bondify(name):
    """
    input: a string in the form "first last"
    returns: a string in the form "Last, First Last"
    """
    l = name.find(" ")
    na = name[l + 1:99].capitalize() + ',' + name[0:l].capitalize() + " " + name[l + 1:99].capitalize()
    return na


print(initialize("thomas huang"))
print(bondify("thomas huang"))
