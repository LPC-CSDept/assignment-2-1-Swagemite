def main():
    ##################################################
    # Comlete your code here
    num_males = int(input("Enter number of males: "))
    num_females = int(input("Enter number of females: "))
    percM = num_males / (num_males + num_females) *100
    percF = num_females / (num_males + num_females) * 100
    total = num_males + num_females
    print('The total number of student:', total)
    print('The number of males and femmales:',num_males, num_females)
    print(f'Percentage of males and females: \t {percM:.2f}% \t {percF:.2f}%')
    ##################################################
    pass


if __name__ == '__main__':
    main()
