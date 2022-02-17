# Basic Shows and tickets
print("""██████╗░░█████╗░░█████╗░██╗░░██╗░░░░░░██╗████████╗░░░░░░██╗░░░██╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝░░░░░░██║╚══██╔══╝░░░░░░██║░░░██║██╔══██╗
██████╦╝██║░░██║██║░░██║█████═╝░█████╗██║░░░██║░░░█████╗██║░░░██║██████╔╝
██╔══██╗██║░░██║██║░░██║██╔═██╗░╚════╝██║░░░██║░░░╚════╝██║░░░██║██╔═══╝░
██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗░░░░░░██║░░░██║░░░░░░░░░╚██████╔╝██║░░░░░
╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝░░░░░░╚═╝░░░╚═╝░░░░░░░░░░╚═════╝░╚═╝░░░░░""")
print('ADMINISTRATOR INPUT')
shows = int(input('Enter the Number of shows today: '))
show = {}
bookings = {}
for i in range(shows):
    x = input(f'Show {i+1} Name: ')
    y = int(input(f'Enter Total Number of tickets for {x} show: '))
    show[x] = y
recommend = {}
print('''
'''*50)
while True:
    print('''-------------
Show Names: ''')
    print('\n'.join(show.keys()))
    query = input('Which Show do you want to book (Enter Name): ')
    if query in show:
        name = input("Please Enter Your Name: ")
        booked_tickets = int(input('Please Enter The Number Of Tickets You Wan To Get: '))
        if show[query] >= booked_tickets:
            bookings[str(name)] = [query, booked_tickets]
            show[query] = show[query] - booked_tickets
            print(f'Thank you for booking, {booked_tickets} Tickets have been booked under {name}.')
            input('Press Enter: ')
            print('''
                                ''' * 50)
        else:
            print(f'Sorry, But there Are Not Enough Tickets Left. Tickets Left = '
                  f'{show[query]}. ')
            input('Press Enter: ')
            print('''
                    ''' * 50)
    elif query == 'EXIT':
        print('Exiting')
        print(show)
        print(bookings)
        print(recommend)
        break

    else:
        print('Sorry But That Show is Not Playing Today :(')
        recommend.setdefault(f'{query}', query)
        input('Please Press Enter: ')
        print('''
        ''' * 50)
    tickets_total = 0
    for i in show:
        tickets_total += show[i]
    if tickets_total == 0:
        print(
            'No Show Tickets Are Left. Sorry For the Inconvenience... :(')
        break
