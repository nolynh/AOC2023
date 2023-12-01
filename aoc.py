def getData(day):
    file = open(day + '.txt')
    return file

def dayOne():
    data = getData('1').readlines(-1)
    c = 0
    for line in data:
        line.replace("\n","")
        a = None
        b = None
        for char1 in line:
            if char1 in ['0','1','2','3','4','5','6','7','8','9']:
                a = char1
                break
        for char2 in reversed(line):
            if char2 in  ['0','1','2','3','4','5','6','7','8','9']:
                b = char2
                break
        c += int(str(a) + str(b))
    return c

def dayOne_b():
    data = getData('1').readlines(-1)
    c = 0
    for line in data:
        line = line.replace("\n","")        
        line = line.replace('one','o1e')
        line = line.replace('two','t2o')
        line = line.replace('three','t3e')
        line = line.replace('four','f4r')
        line = line.replace('five','f5e')
        line = line.replace('six','s6x')
        line = line.replace('seven','s7n')
        line = line.replace('eight','e8t')
        line = line.replace('nine','n9e')
        a = None
        b = None
        for char1 in line:
            if char1 in ['0','1','2','3','4','5','6','7','8','9']:
                a = char1
                break
        for char2 in reversed(line):
            if char2 in  ['0','1','2','3','4','5','6','7','8','9']:
                b = char2
                break
        c += int(str(a) + str(b))
    return c

print(dayOne())
print(dayOne_b())
