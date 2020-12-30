import random

def generate_deck():
    suits = ['♠', '♥', '♦', '♣']
    values = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    costs = [6, 7, 8, 9, 10, 2, 3, 4, 11]
    
    deck = []
    for suit in suits:
        for i, value in enumerate(values):
            deck.append({
                'suit': suit,
                'value': value,
                'cost': costs[i]
            })

    random.shuffle(deck)
    return deck

hand = { 
    'computer': [],
    'human': []
}

def get_sum(player):
    score = 0
    for card in hand[player]:
        score += card['cost']
    return score

def deal(deck, player, num_cards):    
    for i in range(0, num_cards):
        hand[player].append(deck.pop())

def print_hand(player):
    for card in hand[player]:
        print(f"{card['suit']} {card['value']}")
    print(get_sum(player))


def game_end(score):
	print(f"21! Final Score Computer: ", str(score['computer']), " You: ", str(score['human']))


while True:  
    deck = generate_deck()
    deal(deck, 'human', 2)
    deal(deck, 'computer', 2)
    print_hand('human')
    while True:
        user_choice = input("(H)it, (S)tand, or (Q)uit: ").upper()

        if user_choice == 'H':
            deal(deck, 'human', 1)
            print_hand('human')
            if get_sum('human') > 21:
                print('You lose')
                break
        elif user_choice == 'S':
            print(get_sum('human'))
            break
        else:
            break
    break

    

    
  
