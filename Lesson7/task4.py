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

def get_sum(hand):
    score = 0
    # print(hand)
    for card in hand:
        try:
            score += card['cost']
        except:
            print(card)
    return score

def deal(deck: list, hand: list, num_cards: int):
    for i in range(num_cards):
        hand.append(deck.pop())

    return (deck, hand)

def print_hand(hand):
    for card in hand:
        print(f"{card['suit']} {card['value']}")
    print(get_sum(hand))

def check_win(hand) -> bool:
    sum_score = get_sum(hand)

    return len(hand) == 2 and sum_score == 22 or sum_score == 21
    
def game_end(score):
	print(f"21! Final Score Computer: ", str(score['computer']), " You: ", str(score['human']))


if __name__ == '__main__':
    while True:  
        hand = { 
            'computer': [],
            'human': []
        }

        print('\n New game')
        deck = generate_deck()
        deal(deck, hand['human'], 2)
        deal(deck, hand['computer'], 2)
        print_hand(hand['human'])

        if check_win(hand['human']):
            print('You win')
            continue

        while True:
            user_choice = input("(H)it, (S)tand, or (Q)uit: ").upper()
            
            if user_choice == 'H':
                deal(deck, hand['human'], 1)
                print_hand(hand['human'])
                if check_win(hand['human']):
                    print('You win')
                    break
                elif get_sum(hand['human']) > 21:
                    print('You lose')
                    break
            elif user_choice == 'S':
                print(get_sum(hand['human']))
                break
            else:
               break
        
        while True:
            if check_win(hand['computer']):
                print('Computer win')
                break
            elif get_sum(hand['computer']) > 21:
                print('Computer lose')
                break
            elif get_sum(hand['computer']) < 18:
                deal(deck, hand['computer'], 1)
                print_hand(hand['computer'])
                    
        if get_sum(hand['computer']) < get_sum(hand['human']) <= 21:
            print('You win')
        elif get_sum(hand['human']) < get_sum(hand['computer']) <= 21:
            print('computer win')  

        continue
        