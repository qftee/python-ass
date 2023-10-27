with open('users.txt', 'r') as read_users:
    for line in read_users:
        line = line.strip().split(':')
        print(line)
        print(f'UserID:{line[0]}     User Name:{line[1]}     User Password:{line[2]}        '
              f'User Type:{line[3]} \n ')
choice = input('1.Main Menu\n2.Exit').strip()
