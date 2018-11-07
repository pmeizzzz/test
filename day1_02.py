import string
 
def checkio(text):
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)

if __name__ == "__main__":
    str_1 = "Hello world!!!"
    str_2 = "How do you do"
    print(checkio(str_2))
