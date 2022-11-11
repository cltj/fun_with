import os

text_path = os.path.join("/mnt/c/dev/cl/fun_with/jupyter/notebooks/demos/",'all_text.txt')

line_count = 0
word_count = 0
azure_count = 0

searching_for = 'Azure'

with open(text_path,'r') as file:
    # print(len(file))
     # reading each line    
    for line in file:
        line_count += 1
        # reading each word        
        for word in line.split():
            word_count += 1
            # displaying the words           
            # print(word) 
            if word == searching_for:
                azure_count += 1


print('Lines: ' + str(line_count) + '\n',
      'Words: ' + str(word_count) + '\n',
      'Found the word: ' + searching_for + ' ' + str(azure_count) + ' times')