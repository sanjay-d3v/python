class Prime:
    def __init__(self, number):
        self.num = number

    def check(self):
        for i in range(2, int(num**(1/2))+1):
            if num % i == 0:
                return False
        return True


__name__ == "__main__"
num = 11
check_prime = Prime(num)
print(check_prime.check())
