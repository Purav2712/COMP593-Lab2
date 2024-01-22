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
    return                           
    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(data_struct):
    full_name = data_struct['full_name']
    first_name = (full_name.split(' '))[0]
    student_id = data_struct['student_id']

    print(f"My name is {full_name}, but you can call me Mr {first_name}.")

    print(f"My student ID is {student_id}.")

    print()

    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()