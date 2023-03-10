# Sunday P. Afolabi's solution to turing practical programming challenge
# Date: March 10, 2023

# Dynamic entering of user's text
string = input("Enter the string: ")


def isStringClosed(text):
    # initiate character mapping
    brackets = {"{": 1, "[": 2, "(": 3,  "}": -1, "]": -2, ")": -3}

    # creating an empty list
    track_bracket = []

    # length of the string
    string_length = len(text)

    # check if a user has supplied empty string
    if string_length == 0:
        return True

    # check if the first entry is either of the closing brackets
    if string_length == 1 and text in brackets:
        if brackets[text] < 1:
            return False

    # initiate counter with 0
    index = 0

    while index < string_length:
        # print(index)
        character = text[index]
        for k, v in brackets.items():
            if character in brackets and character == k:
                if len(track_bracket) != 0:
                    # compare if there are element already in the track bracket list
                    if track_bracket[-1] == -v:
                        # remove the last element of the track bracket
                        track_bracket.pop()
                        # print(track_bracket)
                    else:
                        # push element at the last index of the track bracket list
                        track_bracket.append(v)
                else:
                    track_bracket.append(v)
        # increment index by 1
        index += 1

    if len(track_bracket) == 0:
        return True
    else:
        False


if isStringClosed(string):
    print("Yes")
else:
    print("No")
