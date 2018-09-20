from movie import Movie

class User:
    def __init__(self,name):
        self.name= name
        self.movie= []

    def __repr__(self):
        return 'User : {}'.format(self.name)

    def wached_movie(self):

        watch_list= list(filter(lambda movie: movie.watched,self.movie))
        return watch_list

    def add_movie(self,name,genre):
        movie= Movie(name,genre,False)
        self.movie.append((movie))

    def del_movie(self,name):
        self.movie= list(filter(lambda movie: movie.name !=name,self.movie))


    #save to json
    def save_json(self):
        return {
                'name': self.name,
                'movie': [movie.json() for movie in self.movie]
            }

    @classmethod
    #load from json
    def load_from_json(cls,filename):
        import json
        with open(filename,'r') as f:
            content = json.load(f)
            username= content['name']
            movie=[]
            for m in content['movie']:
                movie.append(Movie(m['name'],m['genre'],m['watched']))
            user= User(username)
            user.movie= movie
            return user