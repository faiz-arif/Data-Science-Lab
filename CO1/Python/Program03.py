def replacevowel(text):
    vowels='aeiouAEIOU'
    result=""
    for char in text:
        if char in vowels:
            result+="*"
        else:
            result+=char
    return result
text=input("enter text:")
output_text=replacevowel(text)
print(output_text)
        
