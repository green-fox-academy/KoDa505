class MyMath():
    def __init__(self, num_list):
        self.num_list = num_list

    def average(self):
        res = 0
        for i in self.num_list:
            res = res + i
        return res / len(self.num_list)
