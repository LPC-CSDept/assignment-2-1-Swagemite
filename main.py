def main():
    ##################################################
    # Comlete your code here
    num_males = int(input("Enter number of males: "))
    num_females = int(input("Enter number of females: "))
    percM = num_males / (num_males + num_females) *100
    percF = num_females / (num_males + num_females) * 100
    total = num_males + num_females
    print(total)
    print(num_males, num_females)
    print(f'Percentage of males: \t {percM:.2f}%')
    print(f'Percentage of females: \t {percF:.2f}%')
    ##################################################
    pass


if __name__ == '__main__':
    main()
