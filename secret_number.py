def get_numbers_list(number_length, digit):
    table = []
    for i in range(0, 2**number_length):
        if '{0:0{1}b}'.format(i, number_length)[digit] == '1':
            table.append(i)
    return table


def is_binary_one(i, table):
    while True:
        print "\n\nTable {0}: {1}".format(i, table)
        answer = raw_input('Is your number in the above table?   ')
        if answer in ('y', 'ye', 'yes'):
            return True
        if answer in ('n', 'no', 'nop', 'nope'):
            return False
        print """\nAnswer must be 'yes' or 'no'!"""


def main():
    binary_length = int(raw_input("\nThink of a secret number. Please provide the number of digits of this number in binary: "))
    secret_number_list = [1 for i in range(binary_length)]
    for i in range(1, binary_length + 1):
        numbers_list = get_numbers_list(binary_length, -i)
        is_binary = is_binary_one(i, numbers_list)
        secret_number_list[-i] = '1' if is_binary else '0'
        print "secret_number_list:", secret_number_list
    secret_number = ''.join(secret_number_list)
    print "\nYou have selected number {}".format(int(secret_number, 2))
    raw_input("\nPress any key to exit.")


if __name__ == '__main__':
    main()