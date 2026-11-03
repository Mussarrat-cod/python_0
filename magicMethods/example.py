class Counter:
    def __init__(self):
        self.value=1

    def count_up(self):
        self.value+=1

    def count_down(self):
        self.value-=1


    def __str__(self):
        return f"Count= {self.value}"

    def __repr__(self):
        return f"Count= {self.value}"


count1=Counter()
count2=Counter()

print(count1)

print(count1)