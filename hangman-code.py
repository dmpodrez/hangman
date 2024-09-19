import random

word_list = {
    "Animals": ["alligator", "antelope", "baboon", "butterfly", "cheetah", "crocodile", "dolphin", 
                "elephant", "flamingo", "giraffe", "kangaroo", "octopus", "rhinoceros", "squirrel", "tarantula"],
    "Countries": ["Australia", "Argentina", "Belgium", "Brazil", "Cambodia", "Denmark", "Ethiopia", 
                  "Finland", "Germany", "Honduras", "Indonesia", "Jamaica", "Kazakhstan", "Luxembourg", "Madagascar"],
    "Professions": ["architect", "astronomer", "biologist", "carpenter", "detective", "engineer", 
                    "firefighter", "geologist", "journalist", "lawyer", "musician", "pharmacist", "pilot", 
                    "psychologist", "veterinarian"],
    "Colors": ["aquamarine", "burgundy", "chartreuse", "cyan", "emerald", "fuchsia", "indigo", 
               "lavender", "magenta", "maroon", "navy", "olive", "periwinkle", "turquoise", "violet"],
    "Food": ["avocado", "broccoli", "cappuccino", "chocolate", "croissant", "doughnut", "espresso", 
             "grapefruit", "lasagna", "mozzarella", "pancake", "quesadilla", "ravioli", "strawberry", "zucchini"],
    "Technology": ["algorithm", "bandwidth", "calculator", "database", "encryption", "firewall", 
                   "keyboard", "microchip", "network", "processor", "quantum", "robotics", "software", 
                   "transistor", "wireless"],
    "Nature": ["avalanche", "canyon", "desert", "earthquake", "glacier", "hurricane", "jungle", 
               "lightning", "monsoon", "ocean", "rainforest", "tornado", "volcano", "waterfall", "wildfire"],
    "Space": ["asteroid", "blackhole", "comet", "galaxy", "meteorite", "nebula", "orbit", 
              "planet", "satellite", "spacecraft", "stardust", "supernova", "telescope", "universe", "wormhole"],
    "Hard Words": ["bureaucracy", "cacophony", "dichotomy", "exacerbate", "facetious", "juxtaposition"]
}

def get_word_and_category():
    category = random.choice(list(word_list.keys()))
    word = random.choice(word_list[category]).upper()
    return word, category

def display_hangman(tries, extended=False):
    stages = [  
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        ''',
        '''
           
           |      
           |      
           |      
           |      
           |      
           -
        ''',
        '''
           
                 
           -
        '''
    ]
    return stages[tries]

def display_word_completion(word_completion, word, show_ends):
    if show_ends:
        first_letter = word[0]
        last_letter = word[-1]
        hidden_part = ' '.join(word_completion)
        return f"{first_letter} {hidden_part[1:-2]} {last_letter}"
    else:
        return ' '.join(word_completion)

def play():
    print("Welcome to Hangman!")
    
    # Choose game settings
    extended_hangman = input("Do you want the extended version of the hangman (with 8 parts)? (yes/no) ").lower() == 'yes'
    show_ends = input("Do you want to see the first and last letter of the word? (yes/no) ").lower() == 'yes'
    
    while True:
        word, category = get_word_and_category()
        word_completion = ['_'] * len(word)
        guessed_letters = []
        tries = 8 if extended_hangman else 6
        guessed = False
        
        print(f"\nCategory: {category}")
        print(f"Hint: {display_word_completion(word_completion, word, show_ends)}")
        print(display_hangman(tries, extended_hangman))
        
        while not guessed and tries > 0:
            letter_try = input("Guess a letter: ").upper()
            
            if len(letter_try) != 1 or not letter_try.isalpha():
                print("Please enter a single letter.")
                continue
            
            if letter_try in guessed_letters:
                print("You've already guessed that letter.")
                continue
            
            if letter_try in word:
                for index, letter in enumerate(word):
                    if letter == letter_try:
                        word_completion[index] = letter_try
                if '_' not in word_completion:
                    guessed = True
                    print(f"Congratulations! You've guessed the word: {word}.")
            else:
                guessed_letters.append(letter_try)
                tries -= 1
                print(f"Wrong guess. You have {tries} tries left.")
            
            print(display_hangman(tries, extended_hangman))
            print(f"Hint: {display_word_completion(word_completion, word, show_ends)}")
        
        if guessed:
            print('You won! Do you want to play again? (yes/no)')
        else:
            print(f"You've run out of tries. The word was '{word}'.")
            print('Do you want to play again? (yes/no)')
        
        answer = input().lower()
        if answer == 'yes':
            continue
        else:
            print('Thank you for playing!')
            break

play()
