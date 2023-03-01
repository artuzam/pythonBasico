from datetime import datetime


def get_users():
    f = open('users.txt', 'r')
    userlist = []
    for line in f:
        userlist.append(line.rstrip('\n'))
    f.close()
    return userlist


def add_user_stat(username, result):
    filename = username.replace(' ', '').lower()
    # write in new file
    f = open(f'{filename}-stats.txt', 'a')
    dt = datetime.now()
    strdate = dt.strftime("%d %B, %Y")
    f.write(f'{strdate} : {username} {result}\n')
    f.close()
