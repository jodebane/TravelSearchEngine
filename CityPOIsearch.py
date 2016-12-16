#article,type,title,alt,wikidata,wikipedia,address,directions,phone,tollFree,email,fax,url,hours,checkIn,checkOut,image,price,latitude,longitude,wifi,accessibility,lastEdit,description
#


###____Beginning of Code, Where Data is First written into program
def firstread():
    textopen = open('wikivoyagelistingsen.txt', 'r')
    linesin=textopen.readlines()
    linelistarray = []
    for line in linesin:
        linetext = line
        linelist = linetext.split(",")
        print(linelist)
        linelistarray.append([linelist])
    return linesin
    return textopen
    return linelistarray

def entercityname():
    cityname = input("Enter the name of a city  ")
    return cityname

#####ADD NEXT FUNCTIONS HERE


####//--------------
def startingmenu():
    options = [[1, "Search for Sights"],
               [2, "Search for Activities "],
               [3, "Search for Accomodation"]

               ]
    global linesin
    global textopen
    entercityname()
    global cityname
    print("Options, press the key for the following")
    for n in range(0, len(options)):
        print(options[n][0], ": ", options[n][1])


firstread()
startingmenu()
