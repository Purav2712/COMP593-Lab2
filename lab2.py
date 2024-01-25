def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {'full_name' : 'Purav Panchal' , 
                'student_id' : 10329392,
                'pizza_toppings' : [
                    'MUSHROOMS',
                    'OLIVES',
                    'EXTRA CHEESE'
                ],
                'movies' : [
                    {'title' : 'Avenegrs Endgame',
                     'genre' : 'Friction'},
                    {'title': 'Ironman',
                     'genre' : 'Action'}
                ]
                }

    # TODO: Step 3 - Add another movie to the data structure
    about_me['movies'].append({'title' : 'star wars',
                               'genre' : 'Sci-fi'})
    print_student_name_and_id(about_me)     

    print_pizza_toppings(about_me)

    toppings=["CHICKEN","PANEER"]
    add_pizza_toppings(about_me,toppings)

    print_pizza_toppings(about_me)

    print_movie_genres(about_me)

    print_movie_titles(about_me)

    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(data_struct):
    full_name = data_struct['full_name']
    first_name = (full_name.split(' '))[0]
    student_id = data_struct['student_id']

    print(f"My name is {full_name}, but you can call me Mr {first_name}.")

    print(f"My student ID is {student_id}.")

    print()
    
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me,toppings):
    for a in toppings:
        about_me['pizza_toppings'].append(a)
    about_me['pizza_toppings'].sort()
    about_me['pizza_toppings'] = [topping.lower() for topping in about_me['pizza_toppings']]

    

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("My favourite pizza toppings are:")
    for topping in about_me['pizza_toppings']:
        print(topping)


# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
     genres = [movie['genre'] for movie in about_me['movies']]
     print(f"I like to watch {', '.join(genres)} movies.\n")


# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(about_me):
    titles = (movie['title'].title() for movie in about_me["movies"])
    print(f"Some of my favourite movies are {', '.join(titles)}!\n")


    
if __name__ == '__main__':
    main()