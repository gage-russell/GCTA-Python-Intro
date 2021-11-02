# This is an expansion of the math test example. This was written as a group effort live, in-class

# for random number generation:
# import the python library, random
# use the function randint() from the random library to generate a random number between 0 and 10
# random.randint(0, 10)
# https://docs.python.org/3/library/random.html#random.randint

import random


def modulo_test_question(a, b):
    answer = a%b
    question = f'{a} % {b} = '
    return (question, answer)


def floor_division_test_question(a, b):
    answer = a//b
    question = f'{a} // {b} = '
    return (question, answer)


def division_test_question(a, b):
    answer = a/b
    question = f'{a} / {b} = '
    return (question, answer)


def multiplication_test_question(a, b):
    answer = a*b
    question = f'{a} * {b} = '
    return (question, answer)


def division_test_question(a, b):
    answer = a/b
    question = f'{a} / {b} = '
    return (question, answer)


def addition_test_question(a, b):
    answer = a+b
    question = f'{a} + {b} = '
    return (question, answer)


def subtraction_test_question(a, b):
    answer = a+b
    question = f'{a} + {b} = '
    return (question, answer)


def get_random_numbers():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    
    return (a, b)


def get_test_type():
    test_types = ('//', '%', '/', '*', '+', '-')
    user_input = input(f'select a test type from {test_types}: ')
    
    if user_input not in test_types:
        raise ValueError(f'not a valid test type: {user_input}')
        
    return user_input


def ask_question(question, answer):
    user_answer = input(question)
    
    return user_answer == str(answer)


def proctor(question_function, true_incrementor=0):
    
    nums = get_random_numbers()
    question, answer = question_function(nums[0], nums[1])
    right_or_wrong = ask_question(question, answer) 
    
    if right_or_wrong:
        true_incrementor += 1
    
    return true_incrementor


def check_user_playing():
    
    options = ('y', 'n')
    user_playing = input(f'Still playing {options}: ')

    if user_playing not in options:
            raise ValueError(f'not a valid response: {user_playing}') 
            
    if user_playing == 'y':
        return True
    else:
        return False


user_playing = True

test = get_test_type()

question_counter = 0
correct_answer_counter = 0
scores = []

while user_playing:
    
    for i in range(3):
        
        question_counter += 1

        if test == '%':
            correct_answer_counter = proctor(modulo_test_question, true_incrementor=correct_answer_counter)

        if test == '//':
            correct_answer_counter = proctor(floor_division_test_question, true_incrementor=correct_answer_counter)

        if test == '/':
            correct_answer_counter = proctor(division_test_question, true_incrementor=correct_answer_counter)

        if test == '*':
            correct_answer_counter = proctor(multiplication_test_question, true_incrementor=correct_answer_counter)

        if test == '+':
            correct_answer_counter = proctor(addition_test_question, true_incrementor=correct_answer_counter)      

        if test == '-':
            correct_answer_counter = proctor(subtraction_test_question, true_incrementor=correct_answer_counter)  
            
    score = round(correct_answer_counter/question_counter*100, 2)
    
    print(f'You scored: {score}% \n\n')
    
    scores.append(score)
    
    user_playing = check_user_playing()

else:
    num_plays = len(scores)
    avg_score = round(sum(scores)/len(scores), 2)
    string_scores = [str(i) + '%' for i in scores]
    print(f'\n\n\nYou took {num_plays} tests \nYour average score was {avg_score}% \nYour individual scores were {string_scores}')
