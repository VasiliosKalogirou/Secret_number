def get_list_numbers(number_length, digit):
    numbers = []
    for i in range(0, 2**number_length):
        if '{0:0{1}b}'.format(i, number_length)[digit] == '1':
            numbers.append(i)
    return numbers


def main():
    binary_length = int(raw_input("Think of a secret number. Please provide the number of digits of this number in binary: "))
    secret_number_list = [1 for i in range(binary_length)]
    for i in range(1, binary_length + 1):
        print "Table {0}: {1}".format(i, get_list_numbers(binary_length, -i))
        answer = raw_input('Is your number in the above table? ')
        secret_number_list[-i] = '1' if answer == 'y' else '0'
    secret_number = ''.join(secret_number_list)
    print "You have selected number {}".format(int(secret_number, 2))
    raw_input("Press any key to exit.")


if __name__ == '__main__':
    main()