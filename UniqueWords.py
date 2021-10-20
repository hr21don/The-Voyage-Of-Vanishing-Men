import re #extract individual words from a txt file
from collections import Counter # keeping track of unique words

def unique_words(path):
    with open(path, encoding='utf-8') as file: #opening the input file using a context manager
        total_words = re.findall(r"[0-9a-zA-Z-']+", file.read())# finding all the words within the text using search-pattern that looks for letters, hyphens, apostrophes
        total_words = [word.upper() for word in total_words]#Convert the list to uppercase
        print('\nTotal Worlds:' , len(total_words))#print the length of the list

        word_counts = Counter() #new counter object
        for word in total_words: # iterating through the entire list, incrementing corresponding entries within the counter's dictionary
            word_counts[word] += 1
        print ('\n Top 20 words:')
        for word in word_counts.most_common(20):# using the counters most_common method to retrieve a list of the 20 most common words along with their count values to display
            print(word[0], '\t', word[1])

