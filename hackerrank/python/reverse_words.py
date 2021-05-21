def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    splitted = sentence.split(" ") 

    new_sentence = ""
    for word in reversed(splitted):
        new_word = ""
        for l in word:
            if l.isupper():
                new_l = l.lower()
                new_word = new_word + new_l
            else:
                new_l = l.upper()
                new_word = new_word + new_l
            
        new_sentence = new_sentence + " " + new_word
    
    # print (new_sentence)
    return new_sentence[1:]

print (reverse_words_order_and_swap_cases("aWESOME is cODING"))