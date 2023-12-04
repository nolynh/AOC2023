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

def d2color(color, number):
    if (color == 'red' and int(number) > 12) or (color == 'green' and int(number) > 13) or (color == 'blue' and int(number) > 14):
        return True
    else:
        return False
    

def dayTwo():
    data = getData('2').readlines(-1)
    sum = 0
    impossible = []
    for line in data:
        game = line.split(':')
        gameNum = game[0].split(' ')[1]
        draws = game[1].split(';')
        include = True
        for draw in draws:
            if include == False:
                break
            cubes = draw.split(',')
            for cube in cubes:
                if include == False:
                    break
                values = cube.split(' ')
                if d2color(values[2].strip(),values[1].strip()) == True:
                    include = False
                    break
        if include == True:
            sum += int(gameNum)
            include == False
    return sum

print(dayTwo())
#print(dayOne_b())
