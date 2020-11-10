import re
# in this file data checking / validating functions are shown
valid_mail = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
valid_word = '[a-zA-Z]+'

# is this value an email address
def isMail(value):
    return re.match(valid_mail, value)

def isWord(value):
    # need to check if the object that is returned is equal to the input TODO
    return re.match(valid_word, value)