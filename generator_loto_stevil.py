from random import randint

def lottery_number_generator(length):
    loto_list = []
    while True:
        loto_number = randint(1, 50)
        if loto_number not in loto_list:
            loto_list.append(loto_number)

        if len(loto_list) == length:
            break
    return loto_list

def main():
    print("Welcome to the Lottery numbers generator.")
    number = int(input("Please enter how many random numbers would you like to have: "))
    print(lottery_number_generator(number))

main()


