import random as rd

class RandomGen:
    def __init__(self):
        self.letters = [x for x in 'abcdefghijklmnopqrstuvwxyz']
        self.nums = [str(x) for x in range(0,10)]
    
    def _n_check(self, n) -> bool:
        if n < 1 or not isinstance(n, int):
            raise ValueError('must be positive whole number')

    
    def string_gen(self, n: int = rd.randint(1,5)) -> str:
        res = []
        self._n_check(n)
        
        for i in range(n):
            res.append(self.letters[rd.randint(0,25)])

        return ''.join(x for x in res)

    
    def num_gen(self, n: int = rd.randint(0,5)) -> str:
        self._n_check(n)
        return ''.join([self.nums[rd.randint(0,n)]])
        
    def email_gen(self) -> str:
        name = self.string_gen(4)
        email = ['gmail', 'yahoo', 'aol', 'wiredog', 'comcast'][rd.randint(0,4)]
        tld = ['com', 'net', 'edu'][rd.randint(0,2)]
        return f'{name}@{email}.{tld}'

    def password_gen(self, n: int = rd.randint(8,16)) -> str:
        self._n_check(n)
        ls = self.letters + self.nums
        i = [rd.randint(0,(len(ls)-1)) for x in range(n)]
        return ''.join([ls[x] for x in i])
        