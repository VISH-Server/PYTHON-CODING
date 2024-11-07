class PrimeArray:
    def __init__(self, m1, n1):
        self.arr = [[0 for _ in range(n1)] for _ in range(m1)]
        self.m = m1
        self.n = n1
        self.fill()

    def is_prime(self, p):
        if p <= 1:
            return False 

        for i in range(2, int(p**0.5) + 1):
            if p % i == 0:
                return False  

        return True  

    def fill(self):
        num = 2  

        for i in range(self.m):
            for j in range(self.n):
                while not self.is_prime(num):
                    num += 1  
                self.arr[i][j] = num
                num += 1

    def display(self):
        for row in self.arr:
            print("\t".join(map(str, row)))

def main():
    rows = int(input("Enter rows : "))
    cols = int(input("Enter columns: "))

    if rows <= 20 and cols <= 20:
        prime_matrix = PrimeArray(rows, cols)
        print("Prime Array:")
        prime_matrix.display()
    else:
        print("Invalid input.")

if __name__ == "__main__":
    main()
