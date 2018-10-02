STOPLIST_FILENAME = "SmartStoplist.txt"

def get_stoplist():
    with open(STOPLIST_FILENAME, 'r') as f:
        return f.readlines()

def add_to_stoplist(word):
    with open(STOPLIST_FILENAME, 'a+') as f:
        if word not in get_stoplist():
            f.write("\n" + word)
            return True
    return False
