import pandas

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(nato_data)

letters_list = [item for item in nato_data.letter]
codes_list = [item for item in nato_data.code]

nato_dict = {letters_list[item]:codes_list[item] for item in range(0, len(letters_list))}
print(nato_dict)

user_input = input("Type in a sencence or word: ").upper()
nato_user_input = []
for character in user_input:
    if character in letters_list:
        nato_user_input.append(nato_dict[character])
    else:
        nato_user_input.append(character)
print(nato_user_input)