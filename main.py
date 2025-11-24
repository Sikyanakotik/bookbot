import sys
from stats import wordcount, charcount

def main():
     
    try:
        filepath = sys.argv[1]
    except IndexError:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
        
    print('============ BOOKBOT ============')
    print('Analyzing book found at {filepath}...')
    
    print('----------- Word Count ----------')
    book = get_book(filepath)
    num_words = wordcount(book)
    print(f'Found {num_words} total words')
    
    print('--------- Character Count -------')
    char_count = charcount(book)
    char_list = list(char_count)
    char_list = [char for char in char_list if char.isalpha()]
    char_list.sort(key=(lambda x: char_count[x]), reverse=True)
    for char in char_list:
        print(f'{char}: {char_count[char]}')
        
    print('============= END ===============')


def get_book_test(filepath):
    with open(filepath) as file:
        print(file.read())

def get_book(filepath):
    with open(filepath) as file:
        return file.read()
    
main()