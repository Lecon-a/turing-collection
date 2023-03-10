# Date: March 10, 2023

# My Solution for Turing Practical Challenge

# This program collects input from user to check if brackets are properly opened and closed.

If properly opened and closed accordingly, the program prints out success message, else, the program prints out failure message

# SPAlgo'23

Step 1: Input text

Step 2: Initialize dictionary for brackets and maps values appropriately to the brackets { => 1, } => -1, [ => 2, ] => -2, ( => 3, and ) => -3

Step 3: Initialize an empty list to keep track of bracket opening and closing

Step 4: Check if the length of the entered string is 0 i.e. user has entered an empty string, program return True i.e the text is closed

Step 5: If closing bracket if found before opening bracket program return False and halt the program with not closed message

Step 6: Iterate through the entered text/string
- Indicate open bracket character and keep track of it
- Check if opposite i.e. close bracket is found pop the current track of the open bracket from behind

[Sunday P. Afolabi](https://bit.ly/31Av5Ei)

` Copyright 2023



