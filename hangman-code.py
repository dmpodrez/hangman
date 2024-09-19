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
  word = random.choice(word_list)
  return word.upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
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


get_word()
