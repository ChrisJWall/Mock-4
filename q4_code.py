def student_number():
    '''returns the number of students input from by the user'''
    return int(input('How many students? '))

def student_languages(num_students):
    '''returns the number of and details of the languages spoken by each student as a list'''
    language_list = []
    for student in range(num_students):
        data = input('Enter student language info: ').split()
        language_list.append(data)
    return language_list

def common_languages(language_list):
    '''prints the number of common languages among the students and what they are in alphabetical order'''
    language_set = set(language_list[0][1:]) # sets up the set to start taking the union of
    for student in language_list[1:]:       # starting from 2nd student
        language_set = language_set.intersection(set(student[1:]))
    print(language_set)
    print('There are ', len(language_set), ' common languages among the students. These are: ')
    for language in sorted(list(language_set)):
        print(language)

def total_languages(language_list):
    '''Prints the number of languages in total spoken by the students and what they are'''
    s = set([])
    for student in language_list:
        s = s.union(set(student[1:]))
    print('There are ', len(s), ' total languages spoken among the students. These are: ')
    for language in sorted(list(s)):
        print(language)

def main():
    n = student_number()
    language_list = student_languages(n)
    print(language_list)
    common_languages(language_list)
    total_languages(language_list)

if __name__ == '__main__':
    main()
    
        
