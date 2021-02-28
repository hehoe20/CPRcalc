count=0
birthdate ="030779"
male=True
serial=[0,1,2,3,4,9] #0-3 = 1900-1999, #4 = 2000-2036 or 1937-1999, #5-8 2000-2057 or 1858-1899, #9 = 2000-2036 or 1937-1999
for x in serial:
    initialcpr=birthdate+str(x)
    for y in range(1000):
        validcpr=initialcpr+str(y).zfill(3)
        check=int(validcpr[0:1])*4+int(validcpr[1:2])*3+int(validcpr[2:3])*2+int(validcpr[3:4])*7+int(validcpr[4:5])*6+int(validcpr[5:6])*5+int(validcpr[6:7])*4+int(validcpr[7:8])*3+int(validcpr[8:9])*2+int(validcpr[9:10])*1
        if check % 11 == 0:
            if ((male) & (int(validcpr[9:10]) % 2 == 1)):
                print(validcpr)
                count += 1
            if ((not male) & (int(validcpr[9:10]) % 2 == 0)):
                print(validcpr)
                count +=1
print(count)
