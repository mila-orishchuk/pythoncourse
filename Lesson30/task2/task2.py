'''
Extend the echo server, which returns to client the data, encrypted using
the Caesar cipher algorithm by a specific shift obtained from the client.
'''
from string import ascii_letters


def encrypt_caesar(message: str, shift: int = 3):
    encrypted_message = []
    
    for letter in message:
        if letter in ascii_letters:
            index = ascii_letters.index(letter) + shift
            encrypted_letter = ascii_letters[index % len(ascii_letters)]
        else:
            encrypted_letter = letter
            
        encrypted_message.append(encrypted_letter)
        
    return ''.join(encrypted_message)


if __name__ == '__main__':
    print(encrypt_caesar('erwrew'))
