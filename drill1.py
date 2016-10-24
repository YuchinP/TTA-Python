run = 1
print (run)

homesafe = "they scored!"
print (homesafe.title())

battersAL = {
    'josh donaldson' : ['TOR', .417],
    'brock holt' : ['BOS', .400],
    'elvis andrus' : ['TEX', .364],
    'francisco lindor' : ['CLE', .323],
    'ezequiel carrera' : ['TOR', .303]
    }
battersNL = {
    'joe panik' : ['SF', .462],
    'daniel murphy' : ['WSH', .438],
    'conor gillaspie' : ['SF', .421],
    'jayson werth' : ['WSH', .389],
    'ryan zimmerman' : ['WSH', .353]
    }

def atBat(personsName):
    try:
        personsInfo = battersAL[personsName]
        print ('Batter: ' + personsName.title())
        print ('Team: ' + personsInfo[0])
        
