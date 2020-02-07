while True:
    user_input = input('Ask question to Mr. Miyagi: \n').strip().lower()

    if 'sensei' not in user_input :
        print('You are smart, but not wise - address me as Sensei please')
    elif 'block' in user_input or 'blocking' in user_input:
        print('Remember, best block, not to be there..')
    elif '?' in user_input:
        print('questions are wise, but for now. Wax on, and Wax off!')
    elif user_input == 'sensei i am at peace':
        print('Sometimes, what heart know, head forget')
        break
    else:
        print('do not lose focus. Wax on. Wax off.')