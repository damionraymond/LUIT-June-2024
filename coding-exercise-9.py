# Sample dictionary containing English to German translations
sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

# Main loop to accept user input and provide translations
while True:
    user_answer: str = input('Enter a word in English or EXIT: ')
    
    if user_answer == 'EXIT':
        break
    
    if user_answer in sample_dict:
        print('Translation:', sample_dict[user_answer])
    else:
        print('No match!')
    
print('Bye!')
