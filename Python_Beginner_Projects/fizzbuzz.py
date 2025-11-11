class FizzBuzz:
    def display(self):
        print("Welcome to the FizzBuzz: \t")
        for i in range(1, 101):
            if i % 5 == 0 and i % 3 == 0:
                print("FizzBuzz")
            elif i % 5 == 0:
                print("Fizz")
            elif i % 3 == 0:
                print("Buzz")
            else:
                print(i)

    def main(self):
        self.display()


if __name__ == "__main__":
    fizzbuzz = FizzBuzz()
    fizzbuzz.main()
