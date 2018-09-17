class Print():
    students = {'name': '', 'marks': [], 'avg': 0}

    def reset(self):
        self.students['name']=''
        self.students['marks']=[]


    def print(self):
        print('student name: {}'.format(self.students['name']))
        for i, mark in enumerate(self.students['marks']):
            print('mark {} is: {}'.format(i + 1, mark))
        print('student ave mark: {}'.format(self.students['avg']))
        print('--------------------')

class NewStudent(Print):
    def __init__(self):
        Print.__init__(self)

    global x
    li = list()
    def avgMark(self):
        return sum(self.students['marks'])/ len(self.students['marks'])


    def input(self):
        self.students ={}
        add.reset()
        name = input('input student name :')
        self.students['name'] = name
        while True:
            mark = int(input('input mark:'))
            self.students['marks'].append(mark)
            c = input('do u want to continue :')
            if not (c.lower().startswith('y')):
                break
        self.students['avg'] = self.avgMark()
        x.append(self.students)
        print('u input sucessfully')
        self.print()

        print(self.students)

        return x



class Search(Print):
    def __init__(self):
        Print.__init__(self)

    global x

    def search(self):
        print(x)
        name = input('pls insert student name:')
        for self.students in x:
            if (self.students['name']==name):
                self.print()

if __name__== '__main__':

    x = list()

    while True:
        print('-------------------')
        print('add new student :1')
        print('search student info: 2')
        print('quit: 3')
        sel = input('choose option')

        while sel != '1' and sel != '2' and sel != '3':
            sel = input('choose option')

        if sel == '1':

            add = NewStudent()
            while True:

                add.input()
                print(x)
                stop = input('do you want to add new student:')
                if not(stop.lower().startswith('y')):
                   break
            print(x)
        elif sel == '2':
            s = Search()
            s.search()
        else:
            print('Goodbye')
            break


