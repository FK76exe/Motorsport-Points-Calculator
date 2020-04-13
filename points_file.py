import csv

def create_points():
    try:
        name = input("Name your system: ")

        pos = int(input("How many positions are awarded points? "))
        
        f = open("points/"+name,"w")
        f.write("Position" + '\n')
        if pos >= 0:
            for x in range(1,pos+1):
                points = int(input("Enter points for position {} ".format(x)))
                f.write(str(x) + '\t' + str(points) + '\n')
        else:
            print("Error reached: please enter postive integer")

        qual = int(input("How many qualifying positions are awarded points? "))
        f.write("Qualifying" + '\n')
        if qual >= 0:
            for x in range(1,qual+1):
                points = int(input("Enter points for position {} ".format(x)))
                f.write(str(x) + '\t' + str(points) + '\n')
        else:
            print("Error reached: please enter postive integer")

        lap = int(input("How many points for leading a lap? "))
        f.write("Lap Led" + '\n')
        if lap > 0:
            f.write(str(points) + '\n')
        elif lap == 0:
            f.write('0'+'\n')
        else:
            print("Error reached: please enter postive integer")

        most = int(input("How many points for leading the most laps? "))
        f.write("Most Laps Led" + '\n')
        if most > 0:
            f.write(str(most) + '\n')
        else:
            f.write('0' + '\n')
    except ValueError:
        print("please enter valid integer")


def open_points(name):
    file = open('points/'+name,"r")
    points_reader = csv.reader(file,delimiter='\t')
    return list(points_reader)

def dictmaker(x):
    lod = [] #lod = list of dicts (pos, qual, lap, most lap)
    pos_d = {}
    i = 1
    
    while len(x[i]) == 2:
        pos_d[x[i][0]] = int(x[i][1]) #for position
        i += 1
    lod.append(pos_d)

    qual_d = {}
    i += 1
    while len(x[i]) == 2:
        qual_d[x[i][0]] = int(x[i][1]) #for position
        i += 1
    lod.append(qual_d)
    

    for row in x[i+1:]:
        if row[0].isdigit():
            lod.append(int(row[0]))

    return lod

    


#print(dictmaker(open_points('Faris')))
