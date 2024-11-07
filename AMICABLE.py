class AMICABLE:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def SD(self, n, d):
        if d > n / 2:
            return 0
        if n % d == 0:
            return d + self.SD(n, d + 1)
        else:
            return self.SD(n, d + 1)

    def isAmicable(self):
        sum_x = self.SD(self.x, 1)
        sum_y = self.SD(self.y, 1)

        if sum_x == self.y and sum_y == self.x:
            print(f"{self.x} and {self.y} are amicable numbers.")
        else:
            print(f"{self.x} and {self.y} are not amicable numbers.")


if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    obj = AMICABLE(num1, num2)
    obj.isAmicable()
