import math
import csv

# Combinatoric function
def nCr(n,r):
    f = math.factorial
    return float(f(n) / f(r) / f(n-r))

# Hypergeometric function
def hypergeo(N,x,n,k):
    return nCr(x,k) * nCr(N-k,n-x) / nCr(N,n)

# format a float as a string percentage
def format_as_percent(float):
    float *= 100
    return str(float) + "%"



# set these all up as lists from 1 to 41
max = 101
file_shards = range(1,max)

# open a csvfile to dump the results into
with open('results'+ str(max-1) + '.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')

    # the number of shards in a file is fixed for a table
    # it varies between tables
    for x in file_shards:

        # set up a network size
        # set up a number of draws
        # they can't be less than x
        network_size = range(x, max)
        number_of_draws = range(x, max)

        # set up each table with a header 
        writer.writerow(["shards in the file:", x])
        writer.writerow([""])
        writer.writerow(["\\"] + network_size)

        # create a row for each n
        # preface it with the n
        for n in number_of_draws:
            output_row = [n]
            
            # compute each entry for that row
            for N in network_size:

                # if n > N, then it's an impossible case 
                if n > N:
                    output_row += "-"
                else:
                    next = [format_as_percent(hypergeo(N,x,n,x))]
                    output_row += next

            # when it's done, write the row
            writer.writerow(output_row)

        # when you've written the whole table for a given x, 
        # write 2 blank lines, then another table
        writer.writerow([""])
        writer.writerow([""])
