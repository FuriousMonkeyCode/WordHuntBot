#Calculates Score Based on Word (Used for deugging, currently commented out of main.py)
#When debugging, it will output the total score of a given word.
def calculateScore(word):

    scoreMapping = {
        3: 100,
        4: 400,
        5: 800,
        6: 1400,
        7: 1800,
        8: 2200,
        9: 2600,
        10: 3000,
        11: 3400,
        12: 3800,
        13: 4200,
        14: 4600,
        15: 5000,
        16: 5400,
    }

    # Return the score based on the word length
    return scoreMapping.get(len(word), 0)