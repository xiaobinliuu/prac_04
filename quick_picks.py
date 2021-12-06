import random


def main():
    quick_picks()


def quick_picks():
    number = int(input("Enter number: "))

    for i in range(number):
        random_num = []
        for y in range(6):
            random_num.append(random.randint(1, 45))
        random_num.sort()

        print(
            f"{random_num[0]:2} {random_num[1]:2} {random_num[2]:2} {random_num[3]:2} {random_num[4]:2} {random_num[5]:2}")


main()
