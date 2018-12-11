"""split string"""

s = "2006-02-26T22:31:33.370000Z |  +8.472 | +123.086 | 7.8 MS"

# huhuihuii
list_of_string = s.split(" | ")
new = []
for item in list_of_string:
    new.append(item.strip())

print(new)



