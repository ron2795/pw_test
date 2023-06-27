def first_unique_char(s):
    char_count = {}
    for i, char in enumerate(s):
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    

    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
        
    return -1


if __name__ == "__main__":
    string = "leetcode"
    print(first_unique_char(string))  

    string = "loveleetcode"
    print(first_unique_char(string))  

    string = "aabbcc"
    print(first_unique_char(string)) 
