while True:
    python_year = int(input('When was Python 1.0 released? '))
 
    if python_year >1994:
        print('It was earlier than that!')
    elif python_year < 1994:
        print('It was later than that!')
    else:
        print('Correct!')
        break
    