# count-lines-python
# Count Lines Starting With 'A' or 'a' in Python

This repository contains a simple Python program that demonstrates
basic file handling concepts.

## Problem
Count the number of lines in a text file that start with the
character 'A' or 'a'.

## Approach
- Open the file in read mode
- Read all lines using readlines()
- Traverse each line
- Check the first character
- Maintain a counter
- Display the final count

## Program
```python
def COUNTLINES():
    file = open('STORY.TXT', 'r')
    lines = file.readlines()
    count = 0

    for w in lines:
        if w != "" and (w[0] == 'A' or w[0] == 'a'):
            count += 1

    print("Total lines started with 'A' or 'a':", count)
    file.close()

COUNTLINES()
