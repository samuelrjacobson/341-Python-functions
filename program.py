import math

# compute pi using first n terms of infinite sum
def compute_pi(n):
    sum = 0
    denom = 1
    for i in range(1, n + 1, 1):
        val = 4 / denom # calculate value of term i
        if i % 2 == 0: val *= -1 # flip sign for every other term
        sum += val # add value to sum
        denom += 2 # increment denominator for next term
    return sum

# computer square root of number x
def compute_sqrt(x):
    last = 1
    for i in range(0, 10, 1): # repeatedly approximate closer
        next = 0.5 * (last + x / last)
        last = next
    return next # return approximation of sqrt(x)

# determine whether n is prime
def is_prime(n):
    prime = True
    for i in range(2, n // 2 + 1, 1): # check each number 2 to n/2
        if n % i == 0: # if it's a factor of n, prime = false
            prime = False
            break
    return prime # return true/false (prime or not)

# display all prime numbers less than or equal to n
def display_primes(n):
    for i in range(2, n + 1, 1):
        if is_prime(i): print(i) # print if prime

# receive test scores and display summary data
def process_scores():
    min_name = ''
    max_name = ''
    min_score = 0
    max_score = 0
    avg_score = 0
    count_students = 0

    while (True):
        # receive name and score input
        name = input('Enter a name: ')

        if name == 'q' or name == 'Q': break # quit when user inputs q

        score = int(input('Enter a score: '))

        # set variables in first iteration
        if count_students == 0:
            min_name = name
            max_name = name
            min_score = score
            max_score = score
        else:
            if score < min_score: # Find minimum score
                min_score = score
                min_name = name
            if score > max_score: # Find maximum score
                max_score = score
                max_name = name
        avg_score += score # calculate sum of scores
        count_students += 1
    avg_score /= count_students # calculate average

    # display summary data
    print('Average:', avg_score)
    print('Minimum:', min_score)
    print('Maximum:', max_score)
    print('Student with lowest score:', min_name)
    print('Student with highest score:', max_name)

# calculate tax amount
def compute_tax(income, status, state):
    tax_rate = 0
    # calculate base rate (instate)
    if state == 'I' or state == 'O':
        if status == 'SINGLE': # Single
            if income < 30000: tax_rate = 0.20 # Income
            else: tax_rate = 0.25
        elif status == 'MARRIED': # Married
            if income < 50000: tax_rate = 0.10 # Income
            else: tax_rate = 0.15
    # adjust for out-of-state
    if state == 'O':
        tax_rate -= .03
    return tax_rate

# perform quadratric formula given coefficients
def solve_quadratic(a, b, c):
    discriminant = b*b - 4 * a * c # calculate discriminant
    if discriminant < 0: # check whether there are solutions
        return 0, 0
    else: # calculate two solutions
        solution1 = (-b + math.sqrt(discriminant)) / (2 * a)
        solution2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return solution1, solution2

# perform selection sort on a list
def sort(list):
    for i in range(len(list)): # each time through list, put smallest at top
        min = i
        for j in range (i + 1, len(list)): # each time, find smallest remaining
            if list[j] < list[min]: min = j
        if min != i:
            temp = list[min]
            list[min] = list[i]
            list[i] = temp
    return list

# generate user ID and password based on name
def id_password(first, last):
    fn = first.upper() # convert name to uppercase
    ln = last.upper()
    id = fn[0] + ln # set user id
    pw = fn[0] + fn[len(fn) - 1] + ln[0:3] + str(len(fn)) + str(len(ln)) # set password
    return id, pw

# read student information from file, sort and output to file
def file_sort(infile, outfile):
    in_reader = open(infile, 'r') # open file for reading
    m = int(in_reader.readline()) # get number of students

    # create lists to store data in
    id_list = []
    name_list = []
    gpa_list = []
    iterator = 0 # to access elements of lists

    # read values to lists
    line = in_reader.readline()
    while line != '':
        line = line.strip()
        line = line.split()
        id_list.insert(iterator, int(line[0]))
        name_list.insert(iterator, line[1])
        gpa_list.insert(iterator, float(line[2]))

        # set up for next iteration
        line = in_reader.readline()
        iterator += 1

    in_reader.close()

    # selection sort by id#
    for i in range(len(id_list)): #each time through list, put smallest at top
        min = i
        for j in range (i + 1, len(id_list)): # each time, find smallest remaining
            if id_list[j] < id_list[min]: min = j
        if min != i:
            temp = id_list[min]
            id_list[min] = id_list[i]
            id_list[i] = temp

            temp = name_list[min]
            name_list[min] = name_list[i]
            name_list[i] = temp

            temp = gpa_list[min]
            gpa_list[min] = gpa_list[i]
            gpa_list[i] = temp

    # write student data to file
    out_writer = open(outfile, 'w')
    for j in range(len(id_list)):
        out_writer.write((str(id_list[j])) + ' ' + name_list[j] + ' ' + str((gpa_list[j])) + '\n')
    
    out_writer.close()

# main
while (True): # let user execute multiple options until terminating program
    # display menu
    print('\nSelect an option:\n1-computing pi\n2-computing square root')
    print('3-displaying primes\n4-processing grades\n5-computing tax')
    print('6-solving quadratic\n7-sorting list\n8-generate id and password')
    print('9-sorting file\n10-quit')

    # get option number from user
    option = int(input(''))

    # execute corresponding option based on user selection
    if option == 1: # pi calculation
        n = int(input('Enter an integer to use as the number of terms in the infinite sum calculation: '))
        pi = compute_pi(n)
        print('Pi is approximately equal to', pi)

    elif option == 2: # sqrt calculation
        x = float(input('Enter a number to find out its square root: '))
        root = compute_sqrt(x);
        print('The square root of ' + str(x) + ' is ' + str(root))

    elif option == 3: # prime numbers
        n = int(input('Enter a number to see all prime numbers less than or equal to it: '))
        display_primes(n)

    elif option == 4: # process grades
        process_scores()

    elif option == 5: # tax computation
        # get input
        income = int(input('Enter income: '))
        status = input('Enter married/single status: ').upper()
        state = input('Enter i for instate or o for out-of-state: ').upper()

        #calculate and print
        tax_amount = compute_tax(income, status, state)
        print('Your tax amount is', tax_amount)

    elif option == 6: # quadratic forumla
        # get input
        a = int(input('Enter coefficient a: '))
        b = int(input('Enter coefficient b: '))
        c = int(input('Enter coefficient c: '))

        # if there are solutions, print them */
        solution1, solution2 = solve_quadratic(a, b, c)
        if solution1 == 0 and solution2 == 0:
            print('There is no solution.')
        else:
            print('Solutions:', solution1, solution2)

    elif option == 7: # sort list
        list = []
        i = 0 # use to access list elements

        # add numbers to list until user stops entering more
        next_element = input('Enter a number to add to list, or Q to quit: ')
        while next_element != 'q' and next_element != 'Q':
            list.insert(i, float(next_element))
            next_element = input('Enter a number to add to list, or Q to quit: ')
        
        sort(list)
        print(list)

    elif option == 8: # generate user id and password
        first_name = input('Enter a first name: ')
        last_name = input('Enter a last name: ')
        print(id_password(first_name, last_name))

    elif option == 9: # sort file
        input_file = input('Enter a filename with type extension: ')
        output_file = input('Enter an output file with type extension: ')
        file_sort(input_file, output_file)

    elif option == 10: # quit
        print('Have a nice day!')
        break
# end of program