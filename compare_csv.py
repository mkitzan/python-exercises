#!/usr/bin/python3.2

import sys

def csv_to_dictionary(argn, index):
    """Reads csv file line by line and processes it by assigning the element at the
    index specified by 'index' var as the key, and the remaining elements of the 
    line are the data"""
    #initializes empty dictionary container
    processed = {}
    
    #reads in file by line converting it to key:value form
    with open(sys.argv[argn], 'r') as infile:
        for line in infile:
            line = line.strip('\n')
            line = line.split(',')
            #draws out data at key index, then removes it from the list
            key_data = line[index]
            del line[index]
            #adds data to the final dictionary
            if key_data not in list(processed.keys()):
                processed[key_data] = line
            #catch case where multiple of the same key are present in one csv
            else:
                processed[key_data] = processed[key_data] + line
    return processed


def filter_dict(inpt, filtr):
    """Removes all key:value pairs from inpt if, in the data, the filtr variable 
    exists"""
    #pops all key:value pairs where filter was found in value section
    for el in list(inpt.keys()):
        if filtr in inpt[el]:
            inpt.pop(el, None)
    return inpt

def error():
    """User input errors caught in main() divert here. A generic error message is printed,
    then the porgram exits"""
    print("Not enough arguments entered.\nRequired: --base *file* --comp *file* --outfile *file*\nOptional: --column *integer* --filter *string* *number*\nFilter can take any number of filters, but if the filter string is multiple words use underscore instead of spaces\nShorter flags: -b -c -o -cl -fl\nNote: remove all column headers from your input csv files")
    exit()


def process_flow(base, comp, out, index, filters):
    """Mediates all the file processing with variables passed from main()"""
    #converts csv files to dictionaries using the element at specified index as the key
    base = csv_to_dictionary(base, index)
    comp = csv_to_dictionary(comp, index)
    
    #applies filters to base dictionary weeding out superfluous key:value pairs
    for fil in filters:
        base = filter_dict(base, fil)
    
    #performs set difference to find unique keys in the comp dictionary
    key_set = set(comp.keys()) - set(base.keys())
    
    #clears out the outfile
    open(sys.argv[out], 'w').close()
    
    #writes into the outfile all csv rows from comp where the key was not found in base
    with open(sys.argv[out], 'a') as outfile:
        for el in key_set:
            inp_str = str(el)
            for item in comp[el]:
                inp_str += ',' + str(item)
            inp_str += '\n'
            outfile.write(inp_str)


def main():
    """Processes arguments for filenames, and comparison column index"""
    #initializes all variables drawn from sys.argv
    base = 0
    comp = 0
    out = 0
    index = 0
    filters = []
    
    #catches error if user input too few args
    if len(sys.argv) < 9:
        error()
    
    #processes args with a flag checking loop
    for argn in range(len(sys.argv)):
        if sys.argv[argn] == '--base' or sys.argv[argn] == '-b':
            base = argn+1
        elif sys.argv[argn] == '--comp' or sys.argv[argn] == '-c':
            comp = argn+1
        elif sys.argv[argn] == '--outfile' or sys.argv[argn] == '-o':
            out = argn+1
        elif sys.argv[argn] == '--column' or sys.argv[argn] == '-cl':
            index = int(sys.argv[argn+1])
        elif sys.argv[argn] == '--filter' or sys.argv[argn] == '-fl':
            #filter can take multiple args, so reads until next flag or ends of sys.argv
            while argn+1 < len(sys.argv) and sys.argv[argn+1][0] == '-' and sys.argv[argn+1][1] == '-':
                temp = sys.argv[argn].replace('_', ' ')
                filters.append(temp)
                argn += 1
    
    #catches error where required arguments (base, comp, outfile) were not passed
    if base == 0 or comp == 0 or out == 0:
          error()  

    process_flow(base, comp, out, index, filters)
    exit()
    

if __name__ == '__main__':
    main()
