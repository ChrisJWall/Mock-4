def get_n():
    n = int(input('How many lines?'))
    return n

def get_lines(n):
    lines = []
    for i in range(n):
        lines.append(input('Input line:'))
    return lines

def find_frequencies(lines):
    collection = {}
    for line in lines:
        temp_lst = line.split()
        for word in temp_lst:
            if word not in collection:
                collection[word] = 1
            else:
                collection[word] += 1
    return collection

# might be wrong from here

def print_words(collection):
    finished = False
    while len(collection) > 0:
        temp_lst = []
        maxi = max(collection.values())
        for key, value in collection.items():
            if value == maxi:
                temp_lst.append(key)
        temp_lst = sorted(temp_lst)
        for word in temp_lst:
            print(word)
            collection.pop(word)


def main():
    n = get_n()
    lines = get_lines(n)
    collection = find_frequencies(lines)
    print_words(collection)

if __name__ == '__main__':
    main()


        
    
    
        
                
    
    
