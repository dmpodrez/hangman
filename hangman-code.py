import random

word_list = [
    # Animals
    "alligator", "antelope", "baboon", "butterfly", "cheetah", "crocodile", "dolphin", 
    "elephant", "flamingo", "giraffe", "kangaroo", "octopus", "rhinoceros", "squirrel", "tarantula",
    
    # Countries
    "Australia", "Argentina", "Belgium", "Brazil", "Cambodia", "Denmark", "Ethiopia", 
    "Finland", "Germany", "Honduras", "Indonesia", "Jamaica", "Kazakhstan", "Luxembourg", "Madagascar",
    
    # Professions
    "architect", "astronomer", "biologist", "carpenter", "detective", "engineer", 
    "firefighter", "geologist", "journalist", "lawyer", "musician", "pharmacist", "pilot", 
    "psychologist", "veterinarian",
    
    # Colors
    "aquamarine", "burgundy", "chartreuse", "cyan", "emerald", "fuchsia", "indigo", 
    "lavender", "magenta", "maroon", "navy", "olive", "periwinkle", "turquoise", "violet",
    
    # Food
    "avocado", "broccoli", "cappuccino", "chocolate", "croissant", "doughnut", "espresso", 
    "grapefruit", "lasagna", "mozzarella", "pancake", "quesadilla", "ravioli", "strawberry", "zucchini",
    
    # Technology
    "algorithm", "bandwidth", "calculator", "database", "encryption", "firewall", 
    "keyboard", "microchip", "network", "processor", "quantum", "robotics", "software", 
    "transistor", "wireless",
    
    # Nature
    "avalanche", "canyon", "desert", "earthquake", "glacier", "hurricane", "jungle", 
    "lightning", "monsoon", "ocean", "rainforest", "tornado", "volcano", "waterfall", "wildfire",
    
    # Space
    "asteroid", "blackhole", "comet", "galaxy", "meteorite", "nebula", "orbit", 
    "planet", "satellite", "spacecraft", "stardust", "supernova", "telescope", "universe", "wormhole",
    
    # Random Hard Words
    "bureaucracy", "cacophony", "dichotomy", "exacerbate", "facetious", "juxtaposition"
]

def get_word():
    return random.choice(word_list).upper()

def display_hangman(tries):
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
        '''
    ]
    return stages[tries]

def play():
    word = get_word()
    word_completion = ['_'] * len(word)
    guessed_letters = []
    tries = 6
    guessed = False
    
    while True:
        print("Let's start the game!")
        print(' '.join(word_completion))
        print(display_hangman(tries))
        
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
                    print("Congratulations! You've guessed the word.")
            else:
                guessed_letters.append(letter_try)
                tries -= 1
                print(f"Wrong guess. You have {tries} tries left.")
            
            print(display_hangman(tries))
            print(' '.join(word_completion))
            
        if guessed:
            print('Do you want to play again? - yes/no')
        else:
            print(f"You've run out of tries. The word was '{word}'.")
            print('Do you want to play again? - yes/no')
        
        answer = input().lower()
        if answer == 'yes':
            word = get_word()  
            word_completion = ['_'] * len(word)
            guessed_letters = []
            tries = 6
            guessed = False
        else:
            print('Thank you for the game!')
            break

play()

