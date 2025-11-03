def name_bagde(first_name, last_name):
    if ' ' in first_name:
        return first_name
    else:
        last_word = last_name.split(' ')[-1]

        complete_name = f'{first_name} {last_word}'
        return complete_name
