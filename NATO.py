import pandas
def nato():
    data = pandas.read_csv("projects/pandas/nato_phonetic_alphabet.csv")
    phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
    # print(phonetic_dict)

    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except:
        print("please enter only letters")
        nato()
    else:
        print(output_list)

nato()