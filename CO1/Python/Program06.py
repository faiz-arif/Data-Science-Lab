def occurance_of_substring(wordlist,name):
    count=0
    index_list=[]
    for word in wordlist:
        if name in word:
            count+=1
            index_list.append(word.index(name))  
        else:
            index_list.append(0)  
    
    return (count, index_list)
"""wordlist = ["apple", "banana", "pineapple", "orange"]
name = "an"
result = occurance_of_substring(wordlist, name)
print("Number of words with 'name' as a substring:", result[0])
print("Indices of 'name' in each word:", result[1])"""

wordlist = input("Enter a list of words separated by spaces: ").split()
name = input("Enter the name to search for: ")
result = occurance_of_substring(wordlist, name)
print("Number of words with '{}' as a substring: {}".format(name, result[0]))
print("Indices of '{}' in each word: {}".format(name, result[1]))
