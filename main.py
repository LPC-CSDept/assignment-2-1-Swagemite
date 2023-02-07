def main():
    ##################################################
    # Comlete your code here
    num_males = int(input("Enter number of males: "))
    num_females = int(input("Enter number of females: "))
    total = num_males + num_females
    print(total)
    print(num_males, num_females)
    print(f'Percentage of males: \t {num_males:.2f}%')
    print(f'Percentage of females: \t {num_females:.2f}%')
    ##################################################
    pass


if __name__ == '__main__':
    main()
