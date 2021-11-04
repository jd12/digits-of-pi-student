import sys
import random

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            for c in line:
                if random.random() < .1:
                    c = chr(random.randint(0, 127))
                    print(c, end="")
                else:
                    print(c, end="")

if __name__ == "__main__":
    main()