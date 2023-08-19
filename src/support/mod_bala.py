import support.mod_astrodata as data
import support.mod_general as gen
import support.mod_constants as c
import math 
import datetime
import calendar
import copy 

rel2vimshopakratio = {  c.MOOL          : (20/20),
                        c.SWAYAM        : (20/20),
                        c.ATHIMITRA     : (18/20),
                        c.MITRA         : (15/20),
                        c.SAMA          : (10/20),
                        c.SHATRU        : (7/20),
                        c.ATHISHATRU    : (5/20)
                      }

rel2sapthavargajabala = {   c.MOOL          : 45,
                            c.SWAYAM        : 30,
                            c.ATHIMITRA     : 20,
                            c.MITRA         : 15,
                            c.SAMA          : 10,
                            c.SHATRU        : 4,
                            c.ATHISHATRU    : 2
                      }

vimshopak_divisionstrengths = { "shadvarga":{   "D1":6,
                                                "D2":2,
                                                "D3":4,
                                                "D9":5,
                                                "D12":2,
                                                "D30":1
                                            },
                                "saptavarga":{  "D1":5,
                                                "D2":2,
                                                "D3":3,
                                                "D7":2.5,
                                                "D9":4.5,
                                                "D12":2,
                                                "D30":1
                                            },
                                "dashavarga":{  "D1":3,
                                                "D2":1.5,
                                                "D3":1.5,
                                                "D7":1.5,
                                                "D9":1.5,
                                                "D10":1.5,
                                                "D12":1.5,
                                                "D16":1.5,
                                                "D30":1.5,
                                                "D60":5
                                            },
                                "shodashavarga":{   "D1":3.5,
                                                    "D2":1,
                                                    "D3":1,
                                                    "D4":0.5,
                                                    "D7":0.5,
                                                    "D9":3,
                                                    "D10":0.5,
                                                    "D12":0.5,
                                                    "D16":2,
                                                    "D20":0.5,
                                                    "D24":0.5,
                                                    "D27":0.5,
                                                    "D30":1,
                                                    "D40":0.5,
                                                    "D45":0.5,
                                                    "D60":4
                                                }
                               }

Num = 60
ShadbalaMax =  { "Total" : 1110,
              "Sthanabala": { "Total" : 480,
                              "Uchhabala" : 60,
                              "Saptavargajabala" : 315,
                              "Ojhayugmarashiamshabala" : 30,
                              "Kendradhibala" : 60,
                              "Drekshanabala" : 15,
                            },
              "Digbala" : 60,
              "Kaalabala": { "Total" : 390,
                              "Natonnatabala" : 60,
                              "Pakshabala" : 60,
                              "Tribhagabala" : 60,
                              "Varsha-maasa-dina-horabala" : 150,
                              "Yuddhabala" : 60,
                              "Ayanabala" : 60,
                            },
              "Cheshtabala" : 60,
              "Naisargikabala" : 60,
              "Drikbala" : 60
            }
BalaNeededValues = {
                    "Shadbala": {"Sun": 390, "Moon": 360, "Mars": 300, "Mercury": 420, "Jupiter": 390, "Venus": 330, "Saturn": 300},
                    "Sthanabala": {"Sun": 165, "Moon": 133, "Mars": 96, "Mercury": 165, "Jupiter": 165, "Venus": 133, "Saturn": 96},
                    "Digbala": {"Sun": 35, "Moon": 50, "Mars": 30, "Mercury": 35, "Jupiter": 35, "Venus": 50, "Saturn": 30},
                    "Kaalabala": {"Sun": 80, "Moon": 70, "Mars": 60, "Mercury": 80, "Jupiter": 80, "Venus": 70, "Saturn": 60},
                    "Cheshtabala": {"Sun": 112, "Moon": 100, "Mars": 67, "Mercury": 112, "Jupiter": 112, "Venus": 100, "Saturn": 67},
                    "Ayanabala": {"Sun": 30, "Moon": 40, "Mars": 20, "Mercury": 30, "Jupiter": 30, "Venus": 40, "Saturn": 20}                    
                    }

def get_PlanetaryDispositorRelation(planet, division, lagna):
    #Computes the relation of planet with its dispositor in the given divisional chart
    #outputs can be Swayam rashi, athimitra to athishatru
    dispositor = division["planets"][planet]["dispositor"]
    naturalfriends = lagna["planets"][planet]["friends"]
    naturalenemies = lagna["planets"][planet]["enemies"]
    naturalnuetrals = lagna["planets"][planet]["nuetral"]

    planetsts = check_planetPos_OwnMooltrikonExhalt(division["symbol"],planet)
    

    #Getting the natural friendship between planet and dispositor 
    if((planetsts == "EXALT") or (planetsts == "MOOL")):
        naturalrelation = "Mooltrikona"
        return(c.MOOL)  
    elif(planetsts == "OWN"): #first check for own sign
      naturalrelation = "Swarashi"
      return(c.SWAYAM)
    elif(dispositor in naturalfriends): #next check for friend sign       
      naturalrelation = "Mitra"
      n_val = 1
    elif(dispositor in naturalenemies): #next check for enemy sign 
      naturalrelation = "Shatru"
      n_val = -1
    elif(dispositor in naturalnuetrals): #next check for neutral sign       
      naturalrelation = "Sama"
      n_val = 0
    else:
      naturalrelation = "UNKNOWN"
      n_val = 0

    #getting the temporary friendship between planet and dispositor
    temporaryrelation = ""
    planethouse = lagna["planets"][planet]["house-num"]
    dispositorhouse = lagna["planets"][dispositor]["house-num"]
    planet2disp = gen.housediff(planethouse,dispositorhouse)
    if((planet2disp == 2) or 
       (planet2disp == 3) or 
       (planet2disp == 4) or
       (planet2disp == 10) or
       (planet2disp == 11) or
       (planet2disp == 12)):
       temporaryrelation = "Mitra"
       t_val = 1
    else:
        temporaryrelation = "Shatru"
        t_val = -1
    
    final_val = n_val + t_val
    if (final_val == 2):
        return (c.ATHIMITRA)
    elif (final_val == 1):
        return (c.MITRA)
    elif (final_val == 0):
        return (c.SAMA)
    elif (final_val == -1):
        return (c.SHATRU)
    elif (final_val == -2):
        return (c.ATHISHATRU)
    else:
        print("Should not reach here while computing planet to dispositor relation")
        return (c.SAMA)

############################# Vimshopaka Related Computations ###############################################
def compute_VimshopakaBalas():
    #this function computes vimshopaka balas for all varga levels for all 9 planets
    #and updates it in data structure Balas -> Vimshopaka
    for level in ["shadvarga", "saptavarga", "dashavarga", "shodashavarga"]:
        for planet in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn", "Rahu", "Ketu"]:
            planet_vimshopakaBala = 0.0
            #for each planet go through each division
            for div in vimshopak_divisionstrengths[level]:
                planetDispositor_relationInDiv = get_PlanetaryDispositorRelation(planet, data.charts[div], data.charts["D1"])
                planetStrengthInDiv = rel2vimshopakratio[planetDispositor_relationInDiv]
                divisionWeightage = vimshopak_divisionstrengths[level][div]
                planet_vimshopakaBala = planet_vimshopakaBala + (planetStrengthInDiv * divisionWeightage)
            
            #Update the Vimshopaka Bala for the planet in given level
            data.charts["Balas"]["Vimshopaka"][level][planet] = round(planet_vimshopakaBala, 3)
    return

############################# Shadbala Related Computations ###############################################
#Get if planets mooltrikon or own sign is present
def check_planetPos_OwnMooltrikonExhalt(div, planet, varga_degreesConsidered = False):
    if(div == "D1") or (varga_degreesConsidered == True):
        #for D1 chart the degrees also need to be considered for classification of placement
        signno = gen.signnum(data.charts[div]["planets"][planet]["sign"])
        deg = (data.charts[div]["planets"][planet]["pos"]["dec_deg"])
        if(planet == "Sun"):
            if(signno == 5):
                if(deg <=20.0):
                    return ("MOOL")
                else:
                    return ("OWN")
            else:
                return ("NONE")
        elif(planet == "Moon"):
            if(signno == 2):
                if(deg <=3.0):
                    return ("EXALT")
                else:
                    return ("MOOL")
            elif(signno == 4):
                return ("OWN")
            else:
                return ("NONE")
        elif(planet == "Mars"):
            if(signno == 1):
                if(deg <=12.0):
                    return ("MOOL")
                else:
                    return ("OWN")
            elif(signno == 8):
                return ("OWN")
            else:
                return ("NONE")
        elif(planet == "Mercury"):
            if(signno == 6):
                if(deg <=15.0):
                    return ("EXALT")
                elif(deg <=20.0):
                    return ("MOOL")
                else:
                    return ("OWN")
            elif(signno == 3):
                return ("OWN")
            else:
                return ("NONE")
        elif(planet == "Jupiter"):
            if(signno == 9):
                if(deg <=10.0):
                    return ("MOOL")
                else:
                    return ("OWN")
            elif(signno == 12):
                return ("OWN")
            else:
                return ("NONE")
        elif(planet == "Venus"):
            if(signno == 7):
                if(deg <=15.0):
                    return ("MOOL")
                else:
                    return ("OWN")
            elif(signno == 2):
                return ("OWN")
            else:
                return ("NONE")
        elif(planet == "Saturn"):
            if(signno == 11):
                if(deg <=20.0):
                    return ("MOOL")
                else:
                    return ("OWN")
            elif(signno == 10):
                return ("OWN")
            else:
                return ("NONE")
        else:
            pass
    else:   #In divisional charts degrees are not valid and so just with sign number we decide
        signno = gen.signnum(data.charts[div]["planets"][planet]["sign"])
        if(planet == "Sun"):
            if(signno == 5):
                return ("MOOL")
            else:
                return ("NONE")
        elif(planet == "Moon"):
            if(signno == 2):
                return ("MOOL")
            elif(signno == 4):
                return ("OWN")
            else:
                return ("NONE")
        elif(planet == "Mars"):
            if(signno == 1):
                return ("MOOL")
            elif(signno == 8):
                return ("OWN")
            else:
                return ("NONE")
        elif(planet == "Mercury"):
            if(signno == 6):
                return ("MOOL")
            elif(signno == 3):
                return ("OWN")
            else:
                return ("NONE")
        elif(planet == "Jupiter"):
            if(signno == 9):
                return ("MOOL")
            elif(signno == 12):
                return ("OWN")
            else:
                return ("NONE")
        elif(planet == "Venus"):
            if(signno == 7):
                return ("MOOL")
            elif(signno == 2):
                return ("OWN")
            else:
                return ("NONE")
        elif(planet == "Saturn"):
            if(signno == 11):
                return ("MOOL")
            elif(signno == 10):
                return ("OWN")
            else:
                return ("NONE")
        else:
            pass



#Compute Uccha bala (shad-->sthana-->uccha) of planets from sun to saturn in virupas
def compute_uchhabala():
    # Find out the distance between a planet an its debilation point (max is 180). 
    # Uchcha Bala (in Virupas) will be one third of this value.
    for planet in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        #Get planets deep debilitation point
        DebilitPoint = [gen.deepDebilitPoint[planet][0], gen.deepDebilitPoint[planet][1], 0,0]
        
        #get distance of planet from deep debilitation point
        dist_sec = gen.get_point2planetdistance(data.charts["D1"], DebilitPoint, planet)
        if(dist_sec > (180*3600)):
            dist_sec = (360*3600) - dist_sec
        
        #compute uchha bala and update in structure
        uchhabala_virupa = dist_sec/(3600*3)
        data.charts["Balas"]["Shadbala"]["Sthanabala"]["Uchhabala"][planet] = round(uchhabala_virupa, 3)

    return

def compute_saptavargajabala():
    for planet in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        planet_saptavargajabala = 0.0
        #for each planet go through each division
        for div in ["D1", "D2", "D3", "D7", "D9", "D12", "D30"]:
            planetDispositor_relationInDiv = get_PlanetaryDispositorRelation(planet, data.charts[div], data.charts["D1"])
            planetStrengthInDiv = rel2sapthavargajabala[planetDispositor_relationInDiv]
            planet_saptavargajabala = planet_saptavargajabala + planetStrengthInDiv
        
        data.charts["Balas"]["Shadbala"]["Sthanabala"]["Saptavargajabala"][planet] = round(planet_saptavargajabala, 3)
    
    return

def compute_ojhayugmarashiamsabala():
    for planet in ["Sun", "Mars", "Mercury", "Jupiter", "Saturn"]:
        planet_ojhayugmarashiamsabala = 0.0
        planet_lagnasignnum = gen.signnum(data.charts["D1"]["planets"][planet]["sign"])
        planet_navamsasignnum = gen.signnum(data.charts["D9"]["planets"][planet]["sign"])
        if((planet_lagnasignnum % 2) == 1):
            planet_ojhayugmarashiamsabala = planet_ojhayugmarashiamsabala + 15
        if((planet_navamsasignnum % 2) == 1):
            planet_ojhayugmarashiamsabala = planet_ojhayugmarashiamsabala + 15
        data.charts["Balas"]["Shadbala"]["Sthanabala"]["Ojhayugmarashiamshabala"][planet] = planet_ojhayugmarashiamsabala

    for planet in ["Moon", "Venus"]:
        planet_ojhayugmarashiamsabala = 0.0
        planet_lagnasignnum = gen.signnum(data.charts["D1"]["planets"][planet]["sign"])
        planet_navamsasignnum = gen.signnum(data.charts["D9"]["planets"][planet]["sign"])
        if((planet_lagnasignnum % 2) == 0):
            planet_ojhayugmarashiamsabala = planet_ojhayugmarashiamsabala + 15
        if((planet_navamsasignnum % 2) == 0):
            planet_ojhayugmarashiamsabala = planet_ojhayugmarashiamsabala + 15
        data.charts["Balas"]["Shadbala"]["Sthanabala"]["Ojhayugmarashiamshabala"][planet] = planet_ojhayugmarashiamsabala
    
    return

def compute_Kendradhibala():
    for planet in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        planet_kendradhibala = 0
        hno = data.charts["D1"]["planets"][planet]["house-num"]
        if (hno in [1,4,7,10]):
            planet_kendradhibala = 60
        elif (hno in [2,5,8,11]):
            planet_kendradhibala = 30
        else:
            planet_kendradhibala = 15
        data.charts["Balas"]["Shadbala"]["Sthanabala"]["Kendradhibala"][planet] = planet_kendradhibala
    
    return

def compute_Drekkanabala():
    for planet in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        planet_drekkanabala = 0
        deg = (data.charts["D1"]["planets"][planet]["pos"]["dec_deg"])
        if ((deg <= 10.0) and (planet in ["Sun", "Jupiter", "Mars"])):
            planet_drekkanabala = 15
        elif ((deg > 10.0) and (deg <= 20.0) and (planet in ["Moon", "Venus"])):
            planet_drekkanabala = 15
        elif ((deg > 20.0) and (planet in ["Mercury", "Saturn"])):
            planet_drekkanabala = 15
        else:
            planet_drekkanabala = 0
        data.charts["Balas"]["Shadbala"]["Sthanabala"]["Drekshanabala"][planet] = planet_drekkanabala
    
    return

def compute_sthanabala():
    #sthanabala is sum of all sub balas
    #first compute all sub balas
    compute_uchhabala()
    compute_Drekkanabala()
    compute_ojhayugmarashiamsabala()
    compute_Kendradhibala()
    compute_saptavargajabala()
    #Now add all balas
    for planet in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        planet_sthanabala = 0
        planet_sthanabala = planet_sthanabala + data.charts["Balas"]["Shadbala"]["Sthanabala"]["Uchhabala"][planet]
        planet_sthanabala = planet_sthanabala + data.charts["Balas"]["Shadbala"]["Sthanabala"]["Saptavargajabala"][planet]
        planet_sthanabala = planet_sthanabala + data.charts["Balas"]["Shadbala"]["Sthanabala"]["Ojhayugmarashiamshabala"][planet]
        planet_sthanabala = planet_sthanabala + data.charts["Balas"]["Shadbala"]["Sthanabala"]["Kendradhibala"][planet]
        planet_sthanabala = planet_sthanabala + data.charts["Balas"]["Shadbala"]["Sthanabala"]["Drekshanabala"][planet]

        data.charts["Balas"]["Shadbala"]["Sthanabala"]["Total"][planet] = round(planet_sthanabala, 3)        

    return

def compute_nathonnatabala(birthdata):
    planet_nathonnatabala = 0
    birthtime = birthdata["TOB"]
    bt_sec = (birthtime["hour"]*3600) + (birthtime["min"]*60) + (birthtime["sec"])
    if (bt_sec > (12*3600)):
        bt_gap = (24*3600) - bt_sec
    else:
        bt_gap =  bt_sec
    planet_nathonnatabala = bt_gap/720
    for planet in [ "Moon", "Mars", "Saturn"]:  #60 virupas at midnight        
        data.charts["Balas"]["Shadbala"]["Kaalabala"]["Natonnatabala"][planet] = round(planet_nathonnatabala, 3)
    for planet in [ "Sun", "Jupiter", "Venus"]:  #60 virupas at noon
        data.charts["Balas"]["Shadbala"]["Kaalabala"]["Natonnatabala"][planet] = round((60.0-planet_nathonnatabala), 3)

    data.charts["Balas"]["Shadbala"]["Kaalabala"]["Natonnatabala"]["Mercury"] = 60.0

    return

def compute_ayanabala():
    PI = 3.14159265358979
    for planet in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        planet_ayanabala = 0
        signno = gen.signnum(data.charts["D1"]["planets"][planet]["sign"])
        deg = (data.charts["D1"]["planets"][planet]["pos"]["dec_deg"])
        planet_longifull = (signno * 30) + deg

        if (signno in [1,2,3,4,5,6]):
            kranti = "North"
        else:
            kranti = "South"
        
        if (planet in ["Moon", "Saturn"]):
            if (kranti == "North"):
                planet_ayanabala = 30*(1-(abs(math.sin(math.radians(planet_longifull)))))
            else:
                planet_ayanabala = 30*(1+(abs(math.sin(math.radians(planet_longifull)))))
        elif (planet in ["Sun", "Mars", "Jupiter", "Venus"]):
            if (kranti == "South"):
                planet_ayanabala = 30*(1-(abs(math.sin(math.radians(planet_longifull)))))
            else:
                planet_ayanabala = 30*(1+(abs(math.sin(math.radians(planet_longifull)))))
        else:   #For Mercury
            planet_ayanabala = 30*(1+(abs(math.sin(math.radians(planet_longifull)))))

        data.charts["Balas"]["Shadbala"]["Kaalabala"]["Ayanabala"][planet] = round((planet_ayanabala), 3)
        #print(f'''{planet} ayanabala is :{planet_ayanabala}.''')
    return

def compute_pakshabala():
    planet_pakshabala = 0
    sun_moon_gap = gen.get_distancebetweenplanets(data.charts["D1"],"Sun","Moon")
    if(sun_moon_gap > (180*3600)):
        sun_moon_gap = (360*3600) - sun_moon_gap
    naturalbenefics = data.charts["D1"]["classifications"]["natural-benefics"].copy()
    naturalmalefics = data.charts["D1"]["classifications"]["natural-malefics"].copy()
    naturalmalefics.remove("Rahu")
    naturalmalefics.remove("Ketu")
    
    planet_pakshabala = sun_moon_gap/(3*3600)
    for planet in naturalbenefics:          
        data.charts["Balas"]["Shadbala"]["Kaalabala"]["Pakshabala"][planet] = round(planet_pakshabala, 3)
    for planet in naturalmalefics:  
        data.charts["Balas"]["Shadbala"]["Kaalabala"]["Pakshabala"][planet] = round((60.0-planet_pakshabala), 3)

    return

def compute_tribhagabala():
    for planet in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        data.charts["Balas"]["Shadbala"]["Kaalabala"]["Tribhagabala"][planet] = 0.0

    #Jupiter always gets 60 virupas
    data.charts["Balas"]["Shadbala"]["Kaalabala"]["Tribhagabala"]["Jupiter"] = 60.0

    #Compute part of the day by distace between Sun and lagna
    lagnaPoint = [  gen.signnum(data.charts["D1"]["ascendant"]["sign"]),
                    data.charts["D1"]["ascendant"]["pos"]["deg"],
                    data.charts["D1"]["ascendant"]["pos"]["min"],
                    data.charts["D1"]["ascendant"]["pos"]["sec"]  ]
    lagna2sun_dist = gen.get_point2planetdistance(data.charts["D1"],lagnaPoint,"Sun")
    sun2lagna_dist = (360*3600) - lagna2sun_dist

    if sun2lagna_dist <= (60*3600):
        data.charts["Balas"]["Shadbala"]["Kaalabala"]["Tribhagabala"]["Mercury"] = 60.0
    elif sun2lagna_dist <= (120*3600):
        data.charts["Balas"]["Shadbala"]["Kaalabala"]["Tribhagabala"]["Sun"] = 60.0
    elif sun2lagna_dist <= (180*3600):
        data.charts["Balas"]["Shadbala"]["Kaalabala"]["Tribhagabala"]["Saturn"] = 60.0
    elif sun2lagna_dist <= (240*3600):
        data.charts["Balas"]["Shadbala"]["Kaalabala"]["Tribhagabala"]["Moon"] = 60.0
    elif sun2lagna_dist <= (300*3600):
        data.charts["Balas"]["Shadbala"]["Kaalabala"]["Tribhagabala"]["Venus"] = 60.0
    elif sun2lagna_dist <= (360*3600):
        data.charts["Balas"]["Shadbala"]["Kaalabala"]["Tribhagabala"]["Mars"] = 60.0
    else:
        pass

    return

def compute_VarshaMaasaDinaHoraBala(birthdata):
    #Make all planets varshamaasadinahorabala as 0 initially.
    for planet in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        data.charts["Balas"]["Shadbala"]["Kaalabala"]["Varsha-maasa-dina-horabala"][planet] = 0.0
    
    #Day lords
    daylord = { "Sunday": "Sun",
                "Monday": "Moon",
                "Tuesday": "Mars",
                "Wednesday": "Mercury",
                "Thursday": "Jupiter",
                "Friday": "Venus",
                "Saturday": "Saturn" }
    
    bd = birthdata["DOB"]

    #Varsha lord is the lord of first day of birth year. he gets 15 virupas
    date = f'''01 01 {bd["year"]}'''
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    bornvarsha_firstday =  (calendar.day_name[born])
    varshalord = daylord[bornvarsha_firstday]
    data.charts["Balas"]["Shadbala"]["Kaalabala"]["Varsha-maasa-dina-horabala"][varshalord] = 15.0

    #Maasa lord is the lord of first day of birth month. he gets 30 virupas
    date = f'''01 {bd["month"]} {bd["year"]}'''
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    bornmaasa_firstday =  (calendar.day_name[born])
    maasalord = daylord[bornmaasa_firstday]
    data.charts["Balas"]["Shadbala"]["Kaalabala"]["Varsha-maasa-dina-horabala"][maasalord] = 30.0 + data.charts["Balas"]["Shadbala"]["Kaalabala"]["Varsha-maasa-dina-horabala"][maasalord]

    #Vaara lord is the lord of day of birth date. he gets 45 virupas
    date = f'''{bd["day"]} {bd["month"]} {bd["year"]}'''
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    bornvaara =  (calendar.day_name[born])
    vaaralord = daylord[bornvaara]
    data.charts["Balas"]["Shadbala"]["Kaalabala"]["Varsha-maasa-dina-horabala"][vaaralord] = 45.0 + data.charts["Balas"]["Shadbala"]["Kaalabala"]["Varsha-maasa-dina-horabala"][vaaralord]

    #Compute hora of the day by distace between Sun and lagna
    lagnaPoint = [  gen.signnum(data.charts["D1"]["ascendant"]["sign"]),
                    data.charts["D1"]["ascendant"]["pos"]["deg"],
                    data.charts["D1"]["ascendant"]["pos"]["min"],
                    data.charts["D1"]["ascendant"]["pos"]["sec"]  ]
    lagna2sun_dist = gen.get_point2planetdistance(data.charts["D1"],lagnaPoint,"Sun")
    sun2lagna_dist = (360*3600) - lagna2sun_dist

    hora_num = sun2lagna_dist // (15*3600)
    if((sun2lagna_dist % (15*3600))>0):
        hora_num = hora_num + 1
    horalords = [   "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
                    "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
                    "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
                    "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
                    "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
                ]
    dinaidx = horalords.index(bornvaara)
    horalord = daylord[horalords[dinaidx+hora_num]]
    data.charts["Balas"]["Shadbala"]["Kaalabala"]["Varsha-maasa-dina-horabala"][horalord] = 60.0 + data.charts["Balas"]["Shadbala"]["Kaalabala"]["Varsha-maasa-dina-horabala"][horalord]

    return

def compute_digbala():
    #Get lowest point of digbala for planets
    planet_zeroDigbalaPoints = {    "Sun": [data.charts["D1"]["houses"][4-1]["sign-num"], 15,0,0],
                                    "Moon": [data.charts["D1"]["houses"][10-1]["sign-num"], 15,0,0],
                                    "Mars": [data.charts["D1"]["houses"][4-1]["sign-num"], 15,0,0],
                                    "Mercury": [data.charts["D1"]["houses"][7-1]["sign-num"], 15,0,0],
                                    "Jupiter": [data.charts["D1"]["houses"][7-1]["sign-num"], 15,0,0],
                                    "Venus": [data.charts["D1"]["houses"][10-1]["sign-num"], 15,0,0],
                                    "Saturn": [data.charts["D1"]["houses"][1-1]["sign-num"], 15,0,0],
                                }
    for planet in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        planet_dist4mzeropoint = gen.get_point2planetdistance(data.charts["D1"],planet_zeroDigbalaPoints[planet], planet)
        if(planet_dist4mzeropoint > (180*3600)):
            planet_dist4mzeropoint = (360*3600) - planet_dist4mzeropoint
        planet_digbala = planet_dist4mzeropoint / (3*3600)  #in virupas
        data.charts["Balas"]["Shadbala"]["Digbala"][planet] = round(planet_digbala, 3)

    return

def compute_chestabala_kurmamethod():
    #Chestabala of Sun is same as Ayana bala
    data.charts["Balas"]["Shadbala"]["Cheshtabala"]["Sun"] = data.charts["Balas"]["Shadbala"]["Kaalabala"]["Ayanabala"]["Sun"]
    
    #Chesta bala of moon is same as its paksha bala
    data.charts["Balas"]["Shadbala"]["Cheshtabala"]["Moon"] = data.charts["Balas"]["Shadbala"]["Kaalabala"]["Pakshabala"]["Moon"]

    #ChestaBala for Exterior planets - Mars, Jupiter, Saturn using Kurma method (Approximation upto 3 virupas)
    planet_chestapoints = { "Jupiter": [7, 5, 3, 1, 2, 2, 0],
                            "Saturn": [6, 5, 3, 1, 2, 3, 0],
                            "Mars": [7, 6, 4, 2, 0, 1, 0]  }
    for planet in planet_chestapoints:
        #Get the distance between sun and planet
        dist_planet2sun = gen.get_distancebetweenplanets(data.charts["D1"], planet,"Sun")
        dist_sun2planet = gen.get_distancebetweenplanets(data.charts["D1"], "Sun", planet)
        #Get the gap only (whichever is smaller)
        gap_planet2sun = min(dist_planet2sun,dist_sun2planet)

        #classify the gap in terms of how many signs and extra degrees
        gap_signs = gap_planet2sun//(30*3600)
        gap_degrees = (gap_planet2sun % (30*3600)) / 3600

        
        # now compute chestabal in below steps
        # Counting the least signs forwards between the Sun and planet add that many digits its chestapoints array
        # Multiply the sum by 3 to get the product
        # Multiply 1/10th of the balance degrees by the next digit in array and add it on to product to get chestabal
        list = planet_chestapoints[planet].copy()
        cheshtabal_signpart =  (sum(list[0:gap_signs]))*3
        chestabal_degreepart = ((0.1*gap_degrees)*list[gap_signs])
        planet_cheshtabala = cheshtabal_signpart + chestabal_degreepart
        data.charts["Balas"]["Shadbala"]["Cheshtabala"][planet] = round(planet_cheshtabala,3)

    #For venus:
    #Get the distance between sun and venus
    dist_venus2sun = gen.get_distancebetweenplanets(data.charts["D1"], "Venus","Sun")
    dist_sun2venus = gen.get_distancebetweenplanets(data.charts["D1"], "Sun", "Venus")
    #Get the gap only (whichever is smaller)
    gap_venus2sun = min(dist_venus2sun,dist_sun2venus)/3600
    venus_retroSts = data.charts["D1"]["planets"]["Venus"]["retro"]

    #Compute chestabala based on retro status
    if (venus_retroSts == True):
        venus_cheshtabala = 60 - (gap_venus2sun/(10))
    else:   #non retrograde
        if(gap_venus2sun <=40.0):
            venus_cheshtabala = gap_venus2sun
        else:
            venus_cheshtabala = (2*gap_venus2sun) - 41
    data.charts["Balas"]["Shadbala"]["Cheshtabala"]["Venus"] = round(venus_cheshtabala,3)

    #For Mercury
    #Get the distance between sun and mercury
    dist_mercury2sun = gen.get_distancebetweenplanets(data.charts["D1"], "Mercury","Sun")
    dist_sun2mercury = gen.get_distancebetweenplanets(data.charts["D1"], "Sun", "Mercury")
    #Get the gap only (whichever is smaller)
    gap_mercury2sun = min(dist_mercury2sun,dist_sun2mercury)/3600
    mercury_retroSts = data.charts["D1"]["planets"]["Mercury"]["retro"]

    #Compute chestabala based on retro status
    if (mercury_retroSts == True):
        mercury_cheshtabala = 60 - (gap_mercury2sun/(2))
    else:   #non retrograde
        mercury_cheshtabala = (2*gap_mercury2sun) 
    data.charts["Balas"]["Shadbala"]["Cheshtabala"]["Mercury"] = round(mercury_cheshtabala,3)

    return

def get_sputadrishti(degree, aspectingplanet):
    if(degree <=30):
        return(0)
    elif(degree <=60):
        if(aspectingplanet == "Saturn"):
            return((degree - 30 ) * 2)
        else:
            return((degree - 30 ) / 2)
    elif(degree <=90):
        if(aspectingplanet == "Saturn"):
            return(45 + (90 - degree) / 2)
        else:
            return(degree - 45)
    elif(degree <=120):
        if((aspectingplanet == "Mars") or (aspectingplanet == "Jupiter")):
            return(45 + (degree - 90) / 2)
        else:
            return(30 + (120 - degree) / 2)
    elif(degree <=150):
        if((aspectingplanet == "Mars") or (aspectingplanet == "Jupiter")):
            return((150 - degree) * 2)
        else:
            return(150 - degree)
    elif(degree <=180):
        return((abs(150 - degree)) * 2)
    elif(degree <=210):
        if(aspectingplanet == "Mars"):
            return(60)
        else:
            return((300 - degree) / 2)
    elif(degree <=240):
        if(aspectingplanet == "Mars"):
            return(270 - degree)
        elif(aspectingplanet == "Jupiter"):
            return(45 + (degree - 210 ) / 2)
        else:
            return((300 - degree) / 2)
    elif(degree <=270):
        if(aspectingplanet == "Saturn"):
            return(degree - 210)
        elif(aspectingplanet == "Jupiter"):
            return(15 + 2 * ( 270 - degree ) / 3)
        else:
            return((300 - degree) / 2)
    elif(degree <=300):
        if(aspectingplanet == "Saturn"):
            return((300 - degree) * 2)
        else:
            return((300 - degree) / 2)
    else:
        return(0)
        


def compute_drikbala():
    naturalbenefics = data.charts["D1"]["classifications"]["natural-benefics"].copy()
    naturalmalefics = data.charts["D1"]["classifications"]["natural-malefics"].copy()
    naturalmalefics.remove("Rahu")
    naturalmalefics.remove("Ketu")
    for planet in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        planet_drikbala = 0
        benefic_sputa = 0
        malefic_sputa = 0
        #for each planet check drishtis from benefics and malefics 
        for aspectingplanet in naturalbenefics:
            if(planet == aspectingplanet):  # A planet doesnt aspect itself so skip the focus planet
                continue
            #compute sputa drishti from benefics
            dist_aspecting2planet = gen.get_distancebetweenplanets(data.charts["D1"], aspectingplanet,planet)/3600
            sputa = get_sputadrishti(dist_aspecting2planet,aspectingplanet)
            benefic_sputa = benefic_sputa + sputa   #beneficDrishtipinda is sum of all sputadrishtis from benefics
        
        for aspectingplanet in naturalmalefics:
            if(planet == aspectingplanet):  # A planet doesnt aspect itself so skip the focus planet
                continue
            #compute sputa drishti from benefics
            dist_aspecting2planet = gen.get_distancebetweenplanets(data.charts["D1"], aspectingplanet,planet)/3600
            sputa = get_sputadrishti(dist_aspecting2planet,aspectingplanet)
            malefic_sputa = malefic_sputa + sputa   #beneficDrishtipinda is sum of all sputadrishtis from benefics

        #Total drishtipinda is beneficdrishtipinda - malefic drishti pinda
        drishtipinda_total = benefic_sputa - malefic_sputa

        #Drik Bala is quarter of this drishti pinda
        planet_drikbala = drishtipinda_total / 4.0   
        data.charts["Balas"]["Shadbala"]["Drikbala"][planet] = round(planet_drikbala, 3)        

    return

def compute_kaalabala(birthdata):  
    #First compute all sub balas of kaala bala
    compute_nathonnatabala(birthdata) 
    compute_ayanabala() 
    compute_pakshabala()
    compute_tribhagabala()
    compute_VarshaMaasaDinaHoraBala(birthdata)

    #Now add all balas
    for planet in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        planet_kaalaabala = 0
        planet_kaalaabala = planet_kaalaabala + data.charts["Balas"]["Shadbala"]["Kaalabala"]["Natonnatabala"][planet]
        planet_kaalaabala = planet_kaalaabala + data.charts["Balas"]["Shadbala"]["Kaalabala"]["Pakshabala"][planet]
        planet_kaalaabala = planet_kaalaabala + data.charts["Balas"]["Shadbala"]["Kaalabala"]["Tribhagabala"][planet]
        planet_kaalaabala = planet_kaalaabala + data.charts["Balas"]["Shadbala"]["Kaalabala"]["Varsha-maasa-dina-horabala"][planet]
        planet_kaalaabala = planet_kaalaabala + data.charts["Balas"]["Shadbala"]["Kaalabala"]["Ayanabala"][planet]

        data.charts["Balas"]["Shadbala"]["Kaalabala"]["Total"][planet] = round(planet_kaalaabala, 3)        

    return  

def compute_yuddhabala():
    #First clear all yuddha balas of planets before fresh computation
    for planet in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        data.charts["Balas"]["Shadbala"]["Kaalabala"]["Yuddhabala"][planet] = 0

    for planet1 in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        for planet2 in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
            #check both planets are not same
            if (planet1 == planet2):
                continue
            #Now check if planet2 is in yuddha with planet1
            dist_planet1to2 = gen.get_distancebetweenplanets(data.charts["D1"],planet2,planet1)
            if(dist_planet1to2 < 3600): #distance is less than 1 degree then war is there
                looserplanet = planet2
                winnerplanet = planet1
                #now get difference in shadbala between winning and loosing planet
                shadbalaGap = (abs(data.charts["Balas"]["Shadbala"]["Total"][looserplanet] - data.charts["Balas"]["Shadbala"]["Total"][winnerplanet]))
                data.charts["Balas"]["Shadbala"]["Kaalabala"]["Yuddhabala"][looserplanet] = (data.charts["Balas"]["Shadbala"]["Kaalabala"]["Yuddhabala"][looserplanet] - shadbalaGap)
                data.charts["Balas"]["Shadbala"]["Kaalabala"]["Yuddhabala"][winnerplanet] = (data.charts["Balas"]["Shadbala"]["Kaalabala"]["Yuddhabala"][winnerplanet] + shadbalaGap)
    
    return

def compute_shadbala(birthdata):  
    #First compute all sub balas of kaala bala
    compute_sthanabala()
    compute_digbala()
    compute_kaalabala(birthdata)
    compute_drikbala()
    compute_chestabala_kurmamethod()

    #Now add all balas
    for planet in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        planet_shadbala = 0
        planet_shadbala = planet_shadbala + data.charts["Balas"]["Shadbala"]["Sthanabala"]["Total"][planet]
        planet_shadbala = planet_shadbala + data.charts["Balas"]["Shadbala"]["Kaalabala"]["Total"][planet]
        planet_shadbala = planet_shadbala + data.charts["Balas"]["Shadbala"]["Digbala"][planet]
        planet_shadbala = planet_shadbala + data.charts["Balas"]["Shadbala"]["Cheshtabala"][planet]
        planet_shadbala = planet_shadbala + data.charts["Balas"]["Shadbala"]["Naisargikabala"][planet]
        planet_shadbala = planet_shadbala + data.charts["Balas"]["Shadbala"]["Drikbala"][planet]

        data.charts["Balas"]["Shadbala"]["Total"][planet] = round(planet_shadbala, 3)
        #data.charts["Balas"]["Shadbala"]["Rupas"][planet] = round((planet_shadbala/60), 3)        

    #now we can check for yuddabala
    compute_yuddhabala()

    #Now rearrange the Shadbala according to Yuddha balas
    for planet in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        planet_shadbala = data.charts["Balas"]["Shadbala"]["Total"][planet]
        planet_shadbala = planet_shadbala + data.charts["Balas"]["Shadbala"]["Kaalabala"]["Yuddhabala"][planet]
        
        data.charts["Balas"]["Shadbala"]["Total"][planet] = round(planet_shadbala, 3)
        data.charts["Balas"]["Shadbala"]["Rupas"][planet] = round((planet_shadbala/60), 3)

    return 

def compute_ishtakashtabalas():
    for planet in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        uchhabala = data.charts["Balas"]["Shadbala"]["Sthanabala"]["Uchhabala"][planet]
        cheshtabala = data.charts["Balas"]["Shadbala"]["Cheshtabala"][planet]
        ishtabala = round(math.sqrt(uchhabala*cheshtabala),3)
        kashtabala = 60.0-ishtabala
        data.charts["Balas"]["Ishtabala"][planet] = ishtabala
        data.charts["Balas"]["Kashtabala"][planet] = kashtabala

    return

############################## BHAVA BALAS #################################
def compute_bhavaAdhipthibala():
    for hno in range(12):
        houselord = data.charts["D1"]["houses"][hno]["sign-lord"]
        data.charts["Balas"]["BhavaBala"]["BhavaAdhipathibala"][hno] = data.charts["Balas"]["Shadbala"]["Total"][houselord]
    return

def compute_bhavaDigbala():
    bhavadigbalas = {    "nara" : [60,50,40,30,20,10,0,10,20,30,40,50],
                        "jalachara" : [30,40,50,60,50,40,30,20,10,0,10,20],
                        "chatuspadha" : [30,20,10,0,10,20,30,40,50,60,50,40],
                        "keeta" : [0,10,20,30,40,50,60,50,40,30,20,10],
                        "none" : [0,0,0,0,0,0,0,0,0,0,0,0]
                    }
    sign_nature = { "Aries":"chatuspadha",       
                    "Taurus":"chatuspadha",    
                    "Gemini":"nara",   
                    "Cancer":"jalachara",
                    "Leo":"chatuspadha",         
                    "Virgo":"nara",     
                    "Libra":"nara",    
                    "Scorpio":"keeta",
                    "Saggitarius-1":"nara",         #first half
                    "Saggitarius-2":"chatuspadha",  #second half
                    "Capricorn-1":"chatuspadha",    #first half
                    "Capricorn-2":"jalachara",      #second half
                    "Aquarius":"none", 
                    "Pisces":"jalachara"
                  }
    for hno in range(12):
        sign = data.charts["D1"]["houses"][hno]["sign"]
        lagnadeg = data.charts["D1"]["ascendant"]["pos"]["dec_deg"]
        if (lagnadeg <= 15.0):
            part = 1
        else:
            part = 2
        
        if ((sign == "Saggitarius") or (sign == "Capricorn")):
            sign_part = f'''{sign}-{part}''' 
        else:
            sign_part = sign

        nature = sign_nature[sign_part]
        bhavadigbala = bhavadigbalas[nature][hno]
        data.charts["Balas"]["BhavaBala"]["BhavaDigbala"][hno] = bhavadigbala
    return

def compute_bhavadrishtibala():
    naturalbenefics = data.charts["D1"]["classifications"]["natural-benefics"].copy()
    naturalmalefics = data.charts["D1"]["classifications"]["natural-malefics"].copy()
    naturalmalefics.remove("Rahu")
    naturalmalefics.remove("Ketu")
    for hno in range(12):
        sign_num = data.charts["D1"]["houses"][hno]["sign-num"]
        bhava_drikbala = 0
        benefic_sputa = 0
        malefic_sputa = 0
        #for each planet check drishtis from benefics and malefics 
        for aspectingplanet in naturalbenefics:
            #compute sputa drishti from benefics to bhava madhya
            dist_bhavamadhya2aspecting = gen.get_point2planetdistance(data.charts["D1"], [sign_num,15,0,0], aspectingplanet)/3600
            dist_aspecting2bhavamadhya = 360 - dist_bhavamadhya2aspecting
            sputa = get_sputadrishti(dist_aspecting2bhavamadhya,aspectingplanet)
            benefic_sputa = benefic_sputa + sputa   #beneficDrishtipinda is sum of all sputadrishtis from benefics
        
        for aspectingplanet in naturalmalefics:
            #compute sputa drishti from malefics
            dist_bhavamadhya2aspecting = gen.get_point2planetdistance(data.charts["D1"], [sign_num,15,0,0], aspectingplanet)/3600
            dist_aspecting2bhavamadhya = 360 - dist_bhavamadhya2aspecting
            sputa = get_sputadrishti(dist_aspecting2bhavamadhya,aspectingplanet)
            malefic_sputa = malefic_sputa + sputa   #beneficDrishtipinda is sum of all sputadrishtis from benefics

        #Total drishtipinda is beneficdrishtipinda - malefic drishti pinda
        drishtipinda_total = benefic_sputa - malefic_sputa

        #Drik Bala is quarter of this drishti pinda
        bhava_drikbala = drishtipinda_total / 4.0
        data.charts["Balas"]["BhavaBala"]["BhavaDrishtibala"][hno] = round(bhava_drikbala,3)
    return

def compute_bhavabala():
    #Compute 3 sub balas first for bhava
    compute_bhavaAdhipthibala()
    compute_bhavaDigbala()
    compute_bhavadrishtibala()

    #Now add all 3 balas to get final bhavabala
    for hno in range(12):
        bhavabala = data.charts["Balas"]["BhavaBala"]["BhavaAdhipathibala"][hno]
        bhavabala = bhavabala + data.charts["Balas"]["BhavaBala"]["BhavaDigbala"][hno]
        bhavabala = bhavabala + data.charts["Balas"]["BhavaBala"]["BhavaDrishtibala"][hno]
        data.charts["Balas"]["BhavaBala"]["Total"][hno] = round(bhavabala,3)        
    return

if __name__ == "__main__":
    #compute_uchhabala()
    compute_bhavaAdhipthibala()
