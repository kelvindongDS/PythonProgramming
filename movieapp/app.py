from movie import  Movie
from user import User
import os
import json

#add testing data and save it to jsonFile.txt
user= User('Kelvin')
my_movie = Movie('Star','xxx',True)

user.movie.append(my_movie)
print(user)
user.add_movie('superman','x')
user.add_movie('batman','x')
print(user.movie)

#save to json
with open('kelvin.txt','w') as f:
    json.dump(user.save_json(),f)
#stop the app to have new file created


def file_exist(filename):
    return os.path.isfile(filename)

def menu():
    name= input('pls input username:')
    filename = '{}.txt'.format(name)
    if file_exist(filename):
        user= User.load_from_json(filename)
        print('welcome back {}'.format(name))
        print(user.movie)
    else:
        user= User(name)
    while True:
        print('---------')
        print('Add new movie: 1')
        print('See movies 2')
        print('See list movies watched 3')
        print('Delete movie 4')
        print('quit 5')
        select= input('select option')
        while select != '1' and select != '2' and select != '3' and select != '4' and select != '5':
            select = input('select option')

        if select=='1':
            while True:
                movieName= input('insert movie name: ')
                movieGenre= input('insert movie genre: ')
                user.add_movie(movieName,movieGenre)
                print('u inserted successfully')
                print(user.movie)
                c= input('do you want to continue ?')
                if c.lower().startswith('n'): break

        elif select=='2':
            print(user.movie)

        elif select=='3':
            print(user.wached_movie())

        elif select=='4':
            delnum = 0
            delName= input('input deleted movie:')
            for movie in user.movie:
                if movie.name == delName:
                    delnum +=1
            if delnum==0:
                print('this movie name does not exist')
            else:
                 user.del_movie(delName)
                 print('you delete movie {}, number of movie deleted {}'.format(movie.name,delnum))


        else:
            with open('{}.txt'.format(user.name),'w') as f:
                json.dump(user.save_json(),f)
                print('you save data')
                break

menu()
