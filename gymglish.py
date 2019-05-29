# Gymglish test
# Vitor Vilela
# Last revision: 1-February-2017

def CountOccurencesInText(word, text):

    occurrences = 0

    # Ghost chars
    text = '  ' + text.lower() + '  '
    t = len(text)

    # Sought word
    word = word.lower()
    w = len(word)

    # Neighbors
    right_neighbor = {" ", "\n", "!", "?", ".", ",", ":", ")", "_", "\"", u"\xbb", u"\u201d"}
    left_neighbor = {" ", "\n", "!", "?", ".", ",", ":", "(", "_", u"\xab", u"\u201c"}

    # Counting occurrences
    i = 2
    while i < t - 2:
      
        i = text.find(word, i)
        if i != -1:
            # Checking neighborhood
            if text[i + w] in right_neighbor and text[i - 1] in left_neighbor:
                occurrences += 1
                i += w + 1
            elif (text[i + w] == "'" and text[i + w + 1] == "'") or (text[i - 1] == "'" and text[i - 2] == "'"):
                occurrences += 1
                i += w
            else:
                i += w
        else:
            break
	          
    return occurrences



# text = """Georges is my name and I like python. Oh ! your name is georges? And you like Python!
# Yes it is true, I like PYTHON
# and my name is GEORGES"""
# #
# # text = "John O'maley is my friend"
# counter = CountOccurencesInText("georges", text)
# print counter


text = """
A Suggestion Box Entry from Bob Carter

Dear Anonymous,

I'm not quite sure I understand the concept of this 'Anonymous' Suggestion Box. If no one reads what we write, then how will anything ever
change?

But in the spirit of good will, I've decided to offer my two cents, and hopefully Kevin won't steal it! (ha, ha). I would really like to
see more varieties of coffee in the coffee machine in the break room. 'Milk and sugar', 'black with sugar', 'extra sugar' and 'cream and su
gar' don't offer much diversity. Also, the selection of drinks seems heavily weighted in favor of 'sugar'. What if we don't want any suga
r?

But all this is beside the point because I quite like sugar, to be honest. In fact, that's my second suggestion: more sugar in the office.
Cakes, candy, insulin, aspartame... I'm not picky. I'll take it by mouth or inject it intravenously, if I have to.

Also, if someone could please fix the lock on the men's room stall, that would be helpful. Yesterday I was doing my business when Icarus ne
arly climbed into my lap.

So, have a great day!

Anonymously,
 Bob Carter
"""


def doit():
    """Run CountOccurencesInText on a few examples"""
    i = 0
    for x in range(400):
        i += CountOccurencesInText("word", text)
        i += CountOccurencesInText("sugar", text)
        i += CountOccurencesInText("help", text)
        i += CountOccurencesInText("heavily", text)
        i += CountOccurencesInText("witfull", text)
        i += CountOccurencesInText("dog", text)
        i += CountOccurencesInText("almost", text)
        i += CountOccurencesInText("insulin", text)
        i += CountOccurencesInText("attaching", text)
        i += CountOccurencesInText("asma", text)
        i += CountOccurencesInText("neither", text)
        i += CountOccurencesInText("won't", text)
        i += CountOccurencesInText("green", text)
        i += CountOccurencesInText("parabole", text)
    print(i)

# Start profiling - I need to be fast as well
if __name__ == '__main__':
    import profile
    profile.run('doit()')

