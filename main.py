with open('transcript.txt', 'r') as file:
    content = file.read()
    words = content.split()
    word_count = len(words)
    print(f"The word count of my text file is {word_count} words")

    # replace spaces with nothing
    characters = content.replace("","")
    # Get the length of the data
    number_of_characters = len(content)
    print(f"Number of characters in my text file is {number_of_characters}")

    # Get the average word length in the file
    average_word_length = word_count/number_of_characters
    print(f"The average word length is {average_word_length}")

    # Get the frequency of each word in the file
    for word in words:
        freq = words.count(word)
        print(word, freq)