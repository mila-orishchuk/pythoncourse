'''
Create a simple function called favorite_movie, which takes a string containing the name
of your favorite movie. The function should then print “My favorite movie is named {name}”.

'''


def favorite_movie():
    movie = input("Enter a name of your favorite movie: ")
    print(f'My favorite movie is named {movie}')    

if __name__ == '__main__':
    favorite_movie()