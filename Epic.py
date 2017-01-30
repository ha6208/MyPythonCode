def userInt(prompt):    # def = define function
    print prompt,
    num = int(raw_input())
    return num          # return will return a value (num in this case)

def kmToMi(km):
    return 0.62 * km
    
def userString(prompt):
    print prompt,
    s = raw_input()
    return s
    
def userFloat(prompt):
    print prompt,
    f = float(raw_input())
    return f