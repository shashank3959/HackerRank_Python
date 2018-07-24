# Kevin and Stuart want to play the 'The Minion Game'.
#
# Game Rules
#
# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
#
# Scoring
# A player gets +1 point for each occurrence of the substring in the string .
#
# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
#
# For better understanding, see the image below:
#
# banana.png
#
# Your task is to determine the winner of the game and their score.
#
# Input Format
#
# A single line of input containing the string .
# Note: The string  will contain only uppercase letters: .
#
# Constraints
#
#
#
# Output Format
#
# Print one line: the name of the winner and their score separated by a space.
#
# If the game is a draw, print Draw.
#
# Sample Input
#
# BANANA
# Sample Output
#
# Stuart 12
# Note :
# Vowels are only defined as . In this problem,  is not considered a vowel.


# logic is to make all substrings, add to a list and then sort as per vowel or consonant
'''
def minion_game(word):
    word = list(word)
    list_words = []
    stuart = 0
    kevin = 0
    for i in range(len(word)):
        for j in range(i, len(word)):
            # Check if the word is already present in the list
            if word[i:j+1] not in list_words:
                list_words.append("".join(word[i:j+1]))

    for i in range(len(list_words)):
        if list_words[i][0] == 'A' or list_words[i][0] == 'E' or list_words[i][0] == 'I' or list_words[i][0] == 'O' or list_words[i][0] == 'U':
            kevin += 1
        else:
            stuart += 1

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")
'''


def minion_game(string):
    vowels = 'AEIOU'
    kevin = 0
    stuart = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)