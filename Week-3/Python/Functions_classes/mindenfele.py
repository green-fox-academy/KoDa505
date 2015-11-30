class MySuperString():
    def __init__(self, textfield):
        self.textfield = textfield


    def snake_case(self):
        replaced = ''
        for i in self.textfield:
            if i == ' ':
                replaced = replaced + '_'
            replaced = replaced + i
        return replaced


snake_case('asg asg wigo')
