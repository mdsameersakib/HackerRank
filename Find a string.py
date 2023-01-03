def count_substring(string, sub_string):
    s1 = string
    s2 = sub_string
    c = 0
    while s1.count(s2)!=0:
        c+=1
        s1 = s1[s1.index(s2)+1::]      
    return c

if __name__ == '__main__':
    string = input("Enter First Sentence:").strip()
    sub_string = input("Find the number of repetition:").strip()
    
    count = count_substring(string, sub_string)
    print(count)
