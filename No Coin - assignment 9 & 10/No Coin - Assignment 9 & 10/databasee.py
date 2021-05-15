def add_user(user_db):

    uname = input('Please enter a username: ')

    while uname in user_db:
        uname = input('That username is already taken, please choose another: ')
    password = input("Please enter a password: ")
    user_db[uname] = password
    print('Added!')



def login(user_db):
    uname = input('Enter your username: ')
    if uname not in user_db:
        uname = input('Invalid username so try it again.')
        if uname not in user_db:
            print('Invalid data! please contact to your admin.')
            return
    for i in range(3):
        password = input("Enter your password: ")
        if user_db[uname] == password:
            print('Login successfully!')
            return
        else:
            print('Invalid password!')
    print('Temporarily blocked. Please try afterwards or contact to your admin.')



def main():
    user_db = {'param': "123", 'hesam': "1102", 'gagan': '2345', 'john': "a123", 'joe': '453'}
    print('Database:', user_db)
    print('Please add three new users:')
    add_user(user_db)
    print('Database:', user_db)
    add_user(user_db)
    print('Database:', user_db)
    add_user(user_db)
    print('Database:', user_db)
    # simulating login of three users
    print('Please logging-in two users to verify:')
    login(user_db)
    login(user_db)
    print('Database:', user_db)


main()