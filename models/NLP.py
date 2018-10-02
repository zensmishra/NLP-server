import rake

def get_keyword_confidence(message):
    rake_object = rake.Rake("SmartStoplist.txt", 3, 3, 1)
    keywords = rake_object.run(message)
    results = {}
    for tuple in keywords:
        if tuple[1] >= 3:
            results[tuple[0]] = round(tuple[1],1)
    return results