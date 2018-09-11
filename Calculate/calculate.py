class Cal:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b


    def minus(self):
        return self.a - self.b

    def mul(self):
        return self.a*self.b

    def div(self):
        try:
            return self.a/self.b
        except:
            print('cannot div by 0')

    def p(self):
        return ('haha')

    def choose(self,func):
        if func=='+': print(self.add())
        elif func=='-':   print(self.minus())
        elif func == '*':  print(self.mul())
        elif func == '/':  print(self.div())



def main():
    while True:

        a = float(input('pls input:'))
        func = input('choose method need:').strip()
        b = float(input('pls input the second:').strip())
        x = Cal(a, b)
        x.choose(func)
        con = input('do u want to continue: ').strip()
        if con[0].lower().startswith('y'):
            continue
        else:
            break

if __name__=='__main__': main()


