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
        line = line.replace('one','one1one')
        line = line.replace('two','two2two')
        line = line.replace('three','three3three')
        line = line.replace('four','four4four')
        line = line.replace('five','five5five')
        line = line.replace('six','six6six')
        line = line.replace('seven','seven7seven')
        line = line.replace('eight','eight8eight')
        line = line.replace('nine','nine9nine')
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