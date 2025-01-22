s = "I love programming with Python"

# give me all the words from s that has more than 5 characters.

words = s.split()
output = []
for word in words:
    if len(word) >5:
        output.append(word)
#print(output)
# --------------------------------------------------------
# find vowels
s1 = "Service Reliability Engineer at Apple"
count=0
vowels = "aeiouAEIOU"

for char in s1:
    if char in vowels:
        count+=1
print(count)
# --------------------------------------------------------
# revers the words in the sentence
sentence = "Hello Apple Engineers"

lists = sentence.split()
output = ""
for ele in lists:
    output+= ele[::-1] + " "
print(output)
# ------------------------------------------
# Remove duplicate words from sentence by preserving the order:
sentence = "apple banana apple orange banana apple"

words = sentence.split()
unique_words = set()
output = ""
for word in words:
    if word not in unique_words:
        unique_words.add(word)
        output+= word + " "
print(output)

# --------------------------------------------------------
s2 = "name=john; age=30; city=San Francisco"
 
output = {}
elements = s2.split(";")

for ele in elements:
    #ele = name=john
    key,value = ele.split("=")
    #output[ele.split("=")[0].strip()] = ele.split("=")[1]
    output[key.strip()] = value.strip()
print(output)

# --------------------------------------------------------
#check if Ipv4 is valid
ip= "192.168.1.256"
est_cases = [
        ("192.168.1.1", True),
        ("255.255.255.255", True),
        ("0.0.0.0", True),
        ("256.256.256.256", False),
        ("192.168.1", False),
        ("192.168.1.01", False),
        ("192.168.1.1.1", False),
        ("192.168.a.1", False),
        ("", False),
        ("1..1.1", False),
        (" 192.168.1.1 ", False),
        ("192.168.1.-1", False),
        ("192.168.1.256", False),
    ]
#rules:
'''
needs to have 4 parts
every part must be a digit
every value should be 0-255
every part should not have leading zero unless the part is 0
'''
def validIp(ip):
    
    parts = ip.split(".")
    
    if len(parts) != 4: 
        return "IP Not valid"
    for part in parts:
        if not part.isdigit():
            return "IP Not valid"
        if int(part) < 0 or int(part) > 255:
            return "IP Not valid"
        if part != str(int(part)):
            return "IP Not valid"

    return "IP is valid"
print(validIp(ip))