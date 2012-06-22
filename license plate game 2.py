def license_plate_game():
    plate = raw_input('Enter a license plate: ')
    plate = plate.lower()
    dictionary = open('5desk.txt', 'r')
    words = []
    # creates a list of non-proper words that are at least 3 characters in length
    for word in dictionary:
        str.splitlines(word)
        if str.islower(word) and len(word) >= 3:
            words.append(str.strip(word))

    #finds words with the plate letters in proper order; returns a list of options
    def find_words(plate):
        possible_words = []
        for word in words:
            if plate[0] in word:
                index1 = word.index(plate[0])
                if plate[1] in word[(index1 + 1):]:
                    index2 = word.index(plate[1])
                    if plate[2] in word[(index2 + 1):]:
                        possible_words.append(word)
        return possible_words
        
    print find_words(plate)
            
license_plate_game()
