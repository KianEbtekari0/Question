total = 0

question1 = input('The first winner of the Best Programmer Award? ')

if question1 == str('alan perlis'):
    total = 1 + 0

question2 = input('Name of the first computer? ')

if question2 == str('eniac'):
    total = 1 + 0

question3 = input('maker of the first computer? ')

if question3 == str('charles babbage'):
    total = 1 + 0

if question1 == str('alan perlis') and question2 == str('eniac') and question3 == str('charles babbage'):
    total = 0 + 3

print('your total is: ' + str(total))

