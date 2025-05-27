#2. Write a program to fill in a letter template given below with name and date.
letter = '''
Dear < |Name|>, You are selected!
‹ |Date| >'''
print(letter.replace("< |Name|>","krushna").replace("‹ |Date| >","7 may 2025"))
# replace ki chain bana di 😵.