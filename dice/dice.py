import random

class Dice:
    def __init__(self,str):
        str = str.lower()
        d = str.find('d')
        if d > 0:
            i = str.find('d')
            if ('-' in str) or ('+' in str):
                pm = str.find('+')
                if pm == -1:
                    pm = str.find('-')
                self.n=int(str[0:i])
                self.d=int(str[i+1:pm])
                self.p=int(str[pm:])
    def __str__(self):
        if self.p>=0:
            return(f"{self.n}d{self.d} + {self.p}")
        else:
            return(f"{self.n}d{self.d} - {self.p}")
    def roll(self):
        result = 0
        for i in range(self.n):
            result += random.randint(1,self.d)
        result += self.p
        return(result)
    def expected(self):
        return(self.n*(self.d*(self.d+1)/2) + self.p)
    def max(self):
        return(self.n*self.d + self.p)
    def min(self):
        return(self.n + self.p)

####====================================

def roll_dice_list(l):
    if l:
        result = 0
        for i in l:
            result += i.roll()
        return(result)

####====================================

if __name__ == "__main__":
    d = Dice("2d6+0")
    l = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(1000):
        r = d.roll()
        l[r] += 1
    print(l)        

