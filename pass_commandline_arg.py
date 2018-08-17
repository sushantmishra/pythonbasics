#Execute the program as below :
#1. pythonbasics>python pass_commandline_arg.py http://sixty-north.com/c/t.txt
#2. >>> from pass_commandline_arg import *
#   >>> main("http://sixty-north.com/c/t.txt")
import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from a URL.
	Args: 
		url: The uRL of a UTF-8 document
	Returns:
		A list of strings contaiing the words from the document
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for words in line_words:
                story_words.append(words)
    return story_words

	
def print_words(story_words):    			
    for word in story_words:
        print(word)

		
def main(url):
    words = fetch_words(url)
    print_words(words)
	
	
if __name__ == '__main__':
    url = sys.argv[1]
    main(url)