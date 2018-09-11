class Guessing():
    import random
    num= random.randint(0,10)
    stop= False

    def reset(self):
        import random
        self.num= random.randint(0,10)
        self.stop=False
        print(self.num)

    def choice(self):

       x= int(input('psl select number 0-10:'))

       if x== self.num:
           print('congratulation')
           self.stop =True
       elif x>self.num: print('choose smaller number')
       else: print('choose bigger number')

class main():
    game= Guessing()
    print(game.num)
    while True:
        game.choice()
        if game.stop==True:
            ask= input('do want to continue Y or N')
            if ask.lower().startswith('y'):
                game.reset()
                game.choice()
            else:
                print('Goodbye')
                break

main()
