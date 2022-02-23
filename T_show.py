# Basic Shows and tickets
print("""Book-It-Up""")
print('ADMINISTRATOR INPUT')
shows = int(input('Enter the Number of shows today: '))
show = {}
bookings = {}
for i in range(shows):
    x = input(f'Show {i+1} Name: ')
    y = int(input(f'Enter Total Number of tickets for {x} show: '))
    show[x.lower()] = y
recommend = {}
print('''
'''*50)
count = 0
while True:
    print('''-------------
Show Names: ''')
    print('\n'.join(show.keys()))
    query = input('Which Show do you want to book (Enter Name): ')
    if query.lower() in show:
        name = input("Please Enter Your Name: ")
        booked_tickets = int(input('Please Enter The Number Of Tickets You Wan To Get: '))
        if show[query.lower()] >= booked_tickets:
            if str(name) in bookings:
                bookings[str(name)+f'({str(count)})'] = [query.lower(), booked_tickets]
                count +=1
            else:
                bookings[str(name)] = [query.lower(), booked_tickets]
            show[query.lower()] = show[query.lower()] - booked_tickets
            print(f'Thank you for booking, {booked_tickets} Tickets have been booked under {name}.')
            input('Press Enter: ')
            print('''
                                ''' * 50)
        else:
            print(f'Sorry, But there Are Not Enough Tickets Left. Tickets Left = '
                  f'{show[query.lower()]}. ')
            input('Press Enter: ')
            print('''
                    ''' * 50)
    elif query.upper() == 'EXIT':
        print('Exiting')
        print(show)
        print(bookings)
        print(recommend)
        break

    else:
        print('Sorry But That Show is Not Playing Today :(')
        if query.lower() in recommend:
            recommend[query.lower()] = recommend[query.lower()] + 1
        else:
            recommend[query.lower()] = 1
        input('Please Press Enter: ')
        print('''
        ''' * 50)
    tickets_total = 0
    for i in show:
        tickets_total += show[i]
    if tickets_total == 0:
        print(
            'No Show Tickets Are Left. Sorry For the Inconvenience... :(')
        input()
        print('Exiting')
        print(f'Show Tickets Left:')
        for i in show:
            print(f'    {i}: {show[i]}')
        print(f'Show Bookings:')
        for i in bookings:
            print(f'    Name: {i} (Booked Show: {bookings[i][0]}, Tickets Booked:'
                  f' {bookings[i][1]})')
        print(f'Show Recommendations:')
        for i in recommend:
            print(f'    Show Name: {i} (No. of people recommended = {recommend[i]})')
        break
