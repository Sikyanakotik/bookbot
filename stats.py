def wordcount(text):
    return len(text.split())

def charcount(text):
    count_dict = {}
    for char in text:
        char = char.lower()
        try:
            count_dict[char] += 1
        except KeyError:
            count_dict[char] = 1
    return count_dict