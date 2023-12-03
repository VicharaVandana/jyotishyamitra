#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# mod_general.py -- module General. All general computations for any chart [D1-D60 charts]
#
# Copyright (C) 2022 Shyam Bhat  <vicharavandana@gmail.com>
# Downloaded from "https://github.com/VicharaVandana/jyotishyam.git"
#
# This file is part of the "jyotishyam" Python library
# for computing Hindu jataka with sidereal lahiri ayanamsha technique 
# using swiss ephemeries
#

import support.mod_constants as c
import support.panchanga as panchanga

###############################################################################
##                                  DATA                                     ##
###############################################################################
nakshatras = [  "Ashwini", "Bharani", "Kritika", 
                "Rohini", "Mrigashira", "Ardra", 
                "Punarvasu", "Pushya", "Ashlesha", 
                "Magha", "Purva Phalguni", "Uttara Phalguni", 
                "Hasta", "Chitra", "Swati", 
                "Vishaka", "Anurada", "Jyeshta", 
                "Mula", "Purva Ashadha", "Uttara Ashadha", 
                "Shravana", "Dhanishta", "Shatabhishak", 
                "Purva Bhadrapada", "Uttara Bhadrapada", "Revati" ]

nakshatra_rulers = [    "Ketu", "Venus", "Sun", 
                        "Moon", "Mars", "Rahu", 
                        "Jupiter", "Saturn", "Mercury", 
                        "Ketu", "Venus", "Sun", 
                        "Moon", "Mars", "Rahu", 
                        "Jupiter", "Saturn", "Mercury", 
                        "Ketu", "Venus", "Sun", 
                        "Moon", "Mars", "Rahu", 
                        "Jupiter", "Saturn", "Mercury", ]

nakshatra_dieties = [   "Ashwini kumaras", "Yama", "Agni", 
                        "Bramha", "Soma", "Rudra", 
                        "Aditi", "Brihaspathi", "Nagas", 
                        "Pitris", "Aryaman", "Bhaga", 
                        "Surya", "Vishwakarma", "Vaayu", 
                        "Indra - Agni", "Mitra", "Indra", 
                        "Niriti", "Apah", "Vishwe Devatas", 
                        "Vishnu", "Ashta Vasu", "Varuna", 
                        "Ajikapada", "Ahir Budhyana", "Pushan" ]

signs = [ "Aries",       "Taurus",    "Gemini",   "Cancer",
          "Leo",         "Virgo",     "Libra",    "Scorpio",
          "Saggitarius", "Capricorn", "Aquarius", "Pisces"
        ]

rashis = ["Mesha",       "Vrushaba",  "Mithuna",  "Karka",
          "Simha",       "Kanya",     "Tula",     "Vruschika",
          "Dhanu",       "Makara",    "Kumbha",   "Meena",
         ]

signlords = [ "Mars",    "Venus",     "Mercury",  "Moon",
              "Sun",     "Mercury",   "Venus",    "Mars",
              "Jupiter", "Saturn",    "Saturn",   "Jupiter",
            ]

signtatvas = [  c.FIRE, c.EARTH, c.AIR, c.WATER,
                c.FIRE, c.EARTH, c.AIR, c.WATER,
                c.FIRE, c.EARTH, c.AIR, c.WATER,
             ]

planets = [ "Sun",      "Moon",     "Mars",
            "Mercury",  "Jupiter",  "Venus",
            "Saturn",   "Rahu",     "Ketu"
          ]

exhaltation_signs = [   "Aries",        "Taurus",       "Capricorn",
                        "Virgo",        "Cancer",       "Pisces",
                        "Libra",        "Taurus",       "Scorpio"
                    ]

#in format (x,y) x is sign number and y is degrees
deep_ExaltationPoints =    [    (1,10),     (2,3),  (10,28),
                                (6,15),     (4,5),  (12,27),
                                (7,20),     (2,27),  (8,27),
                            ]

deep_DebilitationPoints =   [   (7,10),     (8,3),  (4,28),
                                (12,15),    (10,5), (6,27),
                                (1,20),     (8,27), (2,27),
                            ]

debilitation_signs = [  "Libra",        "Scorpio",      "Cancer",
                        "Pisces",       "Capricorn",    "Virgo",
                        "Aries",        "Scorpio",      "Taurus"
                     ]

ben_mal_neut_bylagna = [ {  #Aries lagna
                            "benefics" : ["Sun", "Moon", "Mars", "Jupiter", "Venus"],
                            "malefics" : ["Mercury", "Saturn"],
                            "neutral"  : [],
                         },
                         {  #Taurus lagna
                            "benefics" : ["Sun", "Moon", "Mars", "Mercury", "Venus", "Saturn"],
                            "malefics" : ["Jupiter"],
                            "neutral"  : [],
                         },
                         {  #Gemini lagna
                            "benefics" : ["Moon", "Mercury", "Jupiter", "Venus", "Saturn"],
                            "malefics" : ["Mars"],
                            "neutral"  : ["Sun"],
                         },
                         {  #Cancer lagna
                            "benefics" : ["Moon", "Mars", "Jupiter"],
                            "malefics" : ["Mercury", "Venus", "Saturn"],
                            "neutral"  : ["Sun"],
                         },
                         {  #Leo lagna
                            "benefics" : ["Sun", "Mars", "Jupiter", "Venus"],
                            "malefics" : ["Moon", "Mercury", "Saturn"],
                            "neutral"  : [],
                         },
                         {  #Virgo lagna
                            "benefics" : ["Mercury", "Jupiter", "Venus"],
                            "malefics" : ["Sun", "Moon", "Mars"],
                            "neutral"  : ["Saturn"],
                         },
                         {  #Libra lagna
                            "benefics" : ["Moon", "Mars", "Mercury", "Venus", "Saturn"],
                            "malefics" : ["Sun", "Jupiter"],
                            "neutral"  : [],
                         },
                         {  #Scorpio lagna
                            "benefics" : ["Sun", "Moon", "Mars", "Jupiter"],
                            "malefics" : ["Mercury", "Venus"],
                            "neutral"  : ["Saturn"],
                         },
                         {  #Saggitarius lagna
                            "benefics" : ["Sun", "Mars", "Mercury", "Jupiter"],
                            "malefics" : ["Moon", "Venus", "Saturn"],
                            "neutral"  : [],
                         },
                         {  #Capricorn lagna
                            "benefics" : ["Moon", "Mercury", "Venus", "Saturn"],
                            "malefics" : ["Sun", "Jupiter"],
                            "neutral"  : ["Mars"],
                         },
                         {  #Aquarius lagna
                            "benefics" : ["Sun", "Mars", "Venus", "Saturn"],
                            "malefics" : ["Moon", "Mercury", "Jupiter"],
                            "neutral"  : [],
                         },
                         {  #Pisces lagna
                            "benefics" : ["Moon", "Mars", "Mercury", "Jupiter"],
                            "malefics" : ["Sun", "Venus", "Saturn"],
                            "neutral"  : [],
                         },                         
                       ]

maasa_names = [ "Chaitra", "Vaisakha", "Jyestha", "Ashadha", "Sravana", "Bhadrapada", 
                "Ashwayuja", "Kartika", "Margashira", "Pushya", "Magha", "Phalguna"]

vaara_names = [ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

tithi_names = [ "shukla padyami", "shukla dwitiya", "shukla tritiya", "shukla chauti", "shukla panchami",
                "shukla shashti", "shukla sapthami", "shukla ashtami", "shukla navami", "shukla dashami",
                "shukla ekadashi", "shukla dwadashi", "shukla trayodashi", "shukla chaturdashi", "poornima",
                "krishna padyami", "krishna dwitiya", "krishna tritiya", "krishna chauti", "krishna panchami",
                "krishna shashti", "krishna sapthami", "krishna ashtami", "krishna navami", "krishna dashami",
                "krishna ekadashi", "krishna dwadashi", "krishna trayodashi", "krishna chaturdashi", "amavasya"]

karana_names = ["Kintughna", "Bava", "Balava", "Kaulava", "Taitila", "Gara", "Vanija", "Vishti", "Bava", "Balava", 
                "Kaulava", "Taitila", "Gara", "Vanija", "Vishti", "Bava", "Balava", "Kaulava", "Taitila", "Gara", 
                "Vanija", "Vishti", "Bava", "Balava", "Kaulava", "Taitila", "Gara", "Vanija", "Vishti", "Bava", "Balava", 
                "Gara", "Taitila", "Kaulava", "Vanija", "Vishti", "Bava", "Balava", "Kaulava", "Taitila", "Gara", 
                "Vanija", "Vishti", "Bava", "Balava", "Kaulava", "Taitila", "Gara", "Vanija", "Vishti", "Bava", 
                "Balava", "Kaulava", "Taitila", "Gara", "Vanija", "Vishti", "Shakuni", "Chatushpada", "Naga"]

yoga_names = [  "Vaidhriti", "Vishkambha", "Priti", "Ayushman", "Saubhagya", "Shobhana", "Atiganda", "Sukarma", "Dhriti", "Soola", 
                "Ganda", "Vriddhi", "Dhruva", "Vyaghata", "Harshana", "Vajra", "Siddhi", "Vyatipata", "Variyana", "Parigha", 
                "Siva", "Siddha", "Sadhya", "Shubha", "Shukla", "Brahma", "Indra" ]

sign_natures =  [   "Movable",       "Fixed",    "Dual",
                    "Movable",       "Fixed",    "Dual",
                    "Movable",       "Fixed",    "Dual",
                    "Movable",       "Fixed",    "Dual",
                ]

diety_of_nakshatra = dict(zip(nakshatras, nakshatra_dieties))
ruler_of_nakshatra = dict(zip(nakshatras, nakshatra_rulers))
lord_of_sign       = dict(zip(signs, signlords))
lord_of_rashi      = dict(zip(rashis, signlords))
tatva_of_sign      = dict(zip(signs, signtatvas))
tatva_of_rashi     = dict(zip(rashis, signtatvas))
exhaltationSign_of_planet  = dict(zip(planets, exhaltation_signs))
debilitationSign_of_planet = dict(zip(planets, debilitation_signs))
deepExaltPoint =  dict(zip(planets, deep_ExaltationPoints))
deepDebilitPoint =  dict(zip(planets, deep_DebilitationPoints))
sign_nature = dict(zip(signs, sign_natures))

###############################################################################
##                              lamda functions                              ##
###############################################################################

signnum = lambda signstr: signs.index(signstr) + 1

###############################################################################
##                                 APIs                                      ##
###############################################################################

def update_miscdata(jd, place, miscdata):
    #update maasa
    (maasanum, leap) = panchanga.masa(jd,place)
    if(leap == True):
        miscdata["maasa"] = "adhikamaasa - " + maasa_names[maasanum - 1]
    else:
         miscdata["maasa"] = maasa_names[maasanum - 1]

    miscdata["vaara"] = vaara_names[panchanga.vaara(jd)-1]

    miscdata["tithi"] = tithi_names[panchanga.tithi(jd,place)[0] - 2]

    miscdata["karana"] = karana_names[panchanga.karana(jd,place)[0] - 2]

    miscdata["yoga"] = yoga_names[panchanga.yoga(jd,place)[0] - 1]

    #print(panchanga.jd_to_gregorian(jd))
    #print(place)
    #print(panchanga.tithi(jd,place))
    #print(panchanga.karana(jd,place))

    return

def housediff(fromsign, tosign):
  ''' Computes how many houses is difference between from fromsign to tosign
      This function is used to compute housenumber for planets too '''
  if(tosign > fromsign):
    house = tosign - fromsign + 1
  elif(tosign < fromsign):
    house = 12 + tosign - fromsign + 1
  else: #same signs
    house = 1 #first house
  return house

def compute_nthsign(fromsign, n):
    s = (fromsign + n - 1) % 12
    if (s == 0):
        s = 12
    return (s)

def compute_nthsign_backwards(fromsign, n):
    s =  (12 + fromsign - n + 1) % 12
    if (s == 0):
        s = 12
    return (s)

def compute_aspects4planet(planetname,aspectnum,division):
    ''' Computes the aspects of each planet in planet group and 
        updates its Aspects elements - planets, signs and houses '''
    planetgroup = division["planets"]
    planet = planetgroup.get(planetname, "NOT_FOUND")
    if (planet != "NOT_FOUND"):
        #if planet is present. Compute its aspects
        houseno = planet["house-num"]
        signno = signnum(planet["sign"])
        aspecthousenum = compute_nthsign(houseno, aspectnum)
        planet["Aspects"]["houses"].append(aspecthousenum) #nth house aspect
        planet["Aspects"]["signs"].append(signs[compute_nthsign(signno, aspectnum)-1]) #nth sign aspect
        planets = get_planets_in_house(aspecthousenum, division["planets"])
        for p in planets:    
            planet["Aspects"]["planets"].append(p)
    else:
        print(planetname + " Not found in planet group.")
    return

def compute_aspects(division):
    ''' Computes the aspects of each planet in planet group and 
        updates its Aspects elements - planets, signs and houses '''
    # Sun aspects 7th house
    compute_aspects4planet("Sun", 7, division)
    # Moon aspects 7th house
    compute_aspects4planet("Moon", 7, division)
    # Mars aspects 4th house
    compute_aspects4planet("Mars", 4, division)
    # Mars aspects 7th house
    compute_aspects4planet("Mars", 7, division)
    # Mars aspects 8th house
    compute_aspects4planet("Mars", 8, division)
    # Mercury aspects 7th house
    compute_aspects4planet("Mercury", 7, division)
    # Jupiter aspects 5th house
    compute_aspects4planet("Jupiter", 5, division)
    # Jupiter aspects 7th house
    compute_aspects4planet("Jupiter", 7, division)
    # Jupiter aspects 9th house
    compute_aspects4planet("Jupiter", 9, division)
    # Venus aspects 7th house
    compute_aspects4planet("Venus", 7, division)
    # Saturn aspects 3rd house
    compute_aspects4planet("Saturn", 3, division)
    # Saturn aspects 7th house
    compute_aspects4planet("Saturn", 7, division)
    # Saturn aspects 10th house
    compute_aspects4planet("Saturn", 10, division)
    # Rahu aspects 5th house
    compute_aspects4planet("Rahu", 5, division)
    # Rahu aspects 7th house
    compute_aspects4planet("Rahu", 7, division)
    # Rahu aspects 9th house
    compute_aspects4planet("Rahu", 9, division)
    # Ketu aspects 5th house
    compute_aspects4planet("Ketu", 5, division)
    # Ketu aspects 7th house
    compute_aspects4planet("Ketu", 7, division)
    # Ketu aspects 9th house
    compute_aspects4planet("Ketu", 9, division)
    return

def compute_aspectedby(division):
    ''' Computes the aspects on each planet in planet group '''
    planetgroup = division["planets"]
    for planetname in planetgroup:
        planet = planetgroup[planetname]    #geteach planet sturcuture
        house_no = planet["house-num"]
        for p in division["houses"][house_no - 1]["aspect-planets"]:
            planet["Aspected-by"].append(p)
    return

def compute_conjuncts(division):
    ''' Computes the conjuncted planets of each planet in planet group '''
    planetgroup = division["planets"]
    for planetname in planetgroup:
        planet = planetgroup[planetname]    #get each planet sturcuture
        house_no = planet["house-num"]
        for p in division["houses"][house_no - 1]["planets"]:
            planet["conjuncts"].append(p)
        try:
            planet["conjuncts"].remove(planetname)
        except:
            print(f"An exception occurred to remove {planetname}")
    
    return

def compute_BenMalNeu4lagna(lagna, cls):
    #computes the benefics, malefics and neutral planets for given lagna of a divisional chart
    pset = ben_mal_neut_bylagna[lagna - 1]
    for bp in pset["benefics"]:
        cls["benefics"].append(bp)
    for mp in pset["malefics"]:
        cls["malefics"].append(mp)
    for np in pset["neutral"]:
        cls["neutral"].append(np)
    return

def populate_Natural_BeneficsMalefics(division):
    division["classifications"]["natural-benefics"] = []
    division["classifications"]["natural-malefics"] = []
    #Fixed Natural Benefics
    division["classifications"]["natural-benefics"].append("Jupiter")
    division["classifications"]["natural-benefics"].append("Venus")

    #Fixed Natural Malefics
    division["classifications"]["natural-malefics"].append("Sun")
    division["classifications"]["natural-malefics"].append("Saturn")
    division["classifications"]["natural-malefics"].append("Mars")
    division["classifications"]["natural-malefics"].append("Rahu")
    division["classifications"]["natural-malefics"].append("Ketu")

    #Shukla Paksha moon is Benefic and Krishna Paksha moon is malefic
    distSunToMoon_sec = get_distancebetweenplanets(division,"Sun", "Moon")
    if(distSunToMoon_sec < (180*3600)): #shukla paksha
        division["classifications"]["natural-benefics"].append("Moon")
    else:   #Krishna Paksha
        division["classifications"]["natural-malefics"].append("Moon")

    #If Mercury is conjunct with any malefic then he is malefic. Else he is Benefic
    for malefic in division["classifications"]["natural-malefics"]:
        if(division["planets"][malefic]["house-num"] == division["planets"]["Mercury"]["house-num"]):
            division["classifications"]["natural-malefics"].append("Mercury")
            break
    if ("Mercury" not in division["classifications"]["natural-malefics"]):
        division["classifications"]["natural-benefics"].append("Mercury")
    
    return



def populate_kendraplanets(division):
    #populates the kendra planets in the given chart. Kendra are house 1,4,7,10
    #1st House planets
    for p in division["houses"][0]["planets"]:
        division["classifications"]["kendra"].append(p)
    #4th House planets
    for p in division["houses"][3]["planets"]:
        division["classifications"]["kendra"].append(p)
    #7th House planets
    for p in division["houses"][6]["planets"]:
        division["classifications"]["kendra"].append(p)
    #10th House planets
    for p in division["houses"][9]["planets"]:
        division["classifications"]["kendra"].append(p)
    return

def populate_trikonaplanets(division):
    #populates the trikona planets in the given chart. trikona are house 1,5,9
    #1st House planets
    for p in division["houses"][0]["planets"]:
        division["classifications"]["trikona"].append(p)
    #5th House planets
    for p in division["houses"][4]["planets"]:
        division["classifications"]["trikona"].append(p)
    #9th House planets
    for p in division["houses"][8]["planets"]:
        division["classifications"]["trikona"].append(p)
    return

def populate_trikplanets(division):
    #populates the trik planets in the given chart. trik are house 6,8,12
    #6th House planets
    for p in division["houses"][5]["planets"]:
        division["classifications"]["trik"].append(p)
    #8th House planets
    for p in division["houses"][7]["planets"]:
        division["classifications"]["trik"].append(p)
    #12th House planets
    for p in division["houses"][11]["planets"]:
        division["classifications"]["trik"].append(p)
    return

def populate_upachayaplanets(division):
    #populates the Upachaya planets in the given chart. Upachaya are house 3,6,11
    #3rd House planets
    for p in division["houses"][2]["planets"]:
        division["classifications"]["upachaya"].append(p)
    #6th House planets
    for p in division["houses"][5]["planets"]:
        division["classifications"]["upachaya"].append(p)
    #11th House planets
    for p in division["houses"][10]["planets"]:
        division["classifications"]["upachaya"].append(p)
    return

def populate_dharmaplanets(division):
    #populates the dharma planets in the given chart. dharma are house 1,5,9
    #1st House planets
    for p in division["houses"][0]["planets"]:
        division["classifications"]["dharma"].append(p)
    #5th House planets
    for p in division["houses"][4]["planets"]:
        division["classifications"]["dharma"].append(p)
    #9th House planets
    for p in division["houses"][8]["planets"]:
        division["classifications"]["dharma"].append(p)
    return

def populate_arthaplanets(division):
    #populates the artha planets in the given chart. artha are house 2,6,10
    #2nd House planets
    for p in division["houses"][1]["planets"]:
        division["classifications"]["artha"].append(p)
    #6th House planets
    for p in division["houses"][5]["planets"]:
        division["classifications"]["artha"].append(p)
    #10th House planets
    for p in division["houses"][9]["planets"]:
        division["classifications"]["artha"].append(p)
    return

def populate_kamaplanets(division):
    #populates the kama planets in the given chart. kama are house 3,7,11
    #3rd House planets
    for p in division["houses"][2]["planets"]:
        division["classifications"]["kama"].append(p)
    #7th House planets
    for p in division["houses"][6]["planets"]:
        division["classifications"]["kama"].append(p)
    #11th House planets
    for p in division["houses"][10]["planets"]:
        division["classifications"]["kama"].append(p)
    return

def populate_mokshaplanets(division):
    #populates the moksha planets in the given chart. moksha are house 4,8,12
    #4th House planets
    for p in division["houses"][3]["planets"]:
        division["classifications"]["moksha"].append(p)
    #8th House planets
    for p in division["houses"][7]["planets"]:
        division["classifications"]["moksha"].append(p)
    #12th House planets
    for p in division["houses"][11]["planets"]:
        division["classifications"]["moksha"].append(p)
    return

def get_planets_in_house(houseno, planetgroup):
    houseplanets = []
    for planetname in planetgroup:
        planet = planetgroup[planetname]
        if (planet["house-num"] == houseno):
            houseplanets.append(planet["name"])
    return houseplanets


def update_houses(division):
    ''' Computes the houses properties for each house like
        planets in house
        house sign and sign number with rashi
    '''
    
    for housenum in range(1, 13):   #house 1 to 12
        house = {"planets"       : [],
                 #"planet-symbols": [],
                 #"retro-status"  : [],
                 "house-num"     : 0,
                 "sign-num"      : 0,
                 "sign"          : "Aries",
                 "sign-lord"     : "Aries",
                 "rashi"         : "Mesha",
                 "aspect-planets" : []
                }        

        #get planets sitting in that house
        planets = get_planets_in_house(housenum, division["planets"])
        for planet in planets:    
            house["planets"].append(planet)
            #house["planet-symbols"].append(division["planets"][planet]["symbol"])
            #house["retro-status"].append(division["planets"][planet]["retro"])
            

        #put house number
        house["house-num"] = housenum

        #get sign of the house
        mysignnum = compute_nthsign(signnum(division["ascendant"]["sign"]),housenum)
        house["sign-num"] = mysignnum
        house["sign"] = signs[mysignnum - 1]
        house["sign-lord"] = signlords[mysignnum - 1]
        house["rashi"] = rashis[mysignnum - 1]

        #compute planets which are aspecting this house
        #all planets will have 7th aspect.So add planets in 7th from it
        planets = get_planets_in_house(compute_nthsign_backwards(housenum,7), division["planets"])
        for planet in planets:    
            house["aspect-planets"].append(planet)
        #Mars has 4th aspect. so check if mars is present in 4 house backwards
        planets = get_planets_in_house(compute_nthsign_backwards(housenum,4), division["planets"])
        if ("Mars" in planets):
            house["aspect-planets"].append("Mars")
        #Mars has 8th aspect. so check if mars is present in 8 house backwards
        planets = get_planets_in_house(compute_nthsign_backwards(housenum,8), division["planets"])
        if ("Mars" in planets):
            house["aspect-planets"].append("Mars")
        #Saturn has 3rd aspect. so check if saturn is present in 3 house backwards
        planets = get_planets_in_house(compute_nthsign_backwards(housenum,3), division["planets"])
        if ("Saturn" in planets):
            house["aspect-planets"].append("Saturn")
        #Saturn has 10th aspect. so check if saturn is present in 10 house backwards
        planets = get_planets_in_house(compute_nthsign_backwards(housenum,10), division["planets"])
        if ("Saturn" in planets):
            house["aspect-planets"].append("Saturn")
        #Jupiter has 5th aspect. so check if jupiter is present in 5 house backwards
        planets = get_planets_in_house(compute_nthsign_backwards(housenum,5), division["planets"])
        if ("Jupiter" in planets):
            house["aspect-planets"].append("Jupiter")
        #Jupiter has 9th aspect. so check if jupiter is present in 9 house backwards
        planets = get_planets_in_house(compute_nthsign_backwards(housenum,9), division["planets"])
        if ("Jupiter" in planets):
            house["aspect-planets"].append("Jupiter")
        #Rahu has 5th aspect. so check if Rahu is present in 5 house backwards
        planets = get_planets_in_house(compute_nthsign_backwards(housenum,5), division["planets"])
        if ("Rahu" in planets):
            house["aspect-planets"].append("Rahu")
        #Rahu has 9th aspect. so check if Rahu is present in 9 house backwards
        planets = get_planets_in_house(compute_nthsign_backwards(housenum,9), division["planets"])
        if ("Rahu" in planets):
            house["aspect-planets"].append("Rahu")
        #Ketu has 5th aspect. so check if Ketu is present in 5 house backwards
        planets = get_planets_in_house(compute_nthsign_backwards(housenum,5), division["planets"])
        if ("Ketu" in planets):
            house["aspect-planets"].append("Ketu")
        #Ketu has 9th aspect. so check if Ketu is present in 9 house backwards
        planets = get_planets_in_house(compute_nthsign_backwards(housenum,9), division["planets"])
        if ("Ketu" in planets):
            house["aspect-planets"].append("Ketu")
        division["houses"].append(house)
    return

def iterativeReplace(string, substring, newstring):
    while(substring in string):
        string = string.replace(substring,newstring)
    return string

def get_nthLord(division,n):
    #Gets house-number(n)'s sign lord (who owns the sign in that housein division)
    signlord = division["houses"][n-1]["sign-lord"]
    return signlord

def get_planetPlacedHousenum(division, planet):
    #Gets in which house is the requested planet placed in that housein division
    housenum = division["planets"][planet]["house-num"]
    return housenum

def get_distancebetweenplanets(division, fromplanet, toplanet):
    #Computes whats the distance between from planet to toplanet in given divisional chart in seconds(deg and minutes also converted to seconds)
    fp = division["planets"][fromplanet]
    tp = division["planets"][toplanet]
    #compute distance from start of lagna to from and to planets in seconds.
    sec_fp = (((fp["house-num"]-1)*30*3600) + (fp["pos"]["deg"]*3600) + (fp["pos"]["min"]*60) + (fp["pos"]["sec"]))
    sec_tp = (((tp["house-num"]-1)*30*3600) + (tp["pos"]["deg"]*3600) + (tp["pos"]["min"]*60) + (tp["pos"]["sec"]))

    if(sec_tp >= sec_fp):   #if toplanet is ahead of fromplanet
        dist = sec_tp - sec_fp
    else:   #if toplanet is behind of fromplanet
        gap = sec_fp - sec_tp
        dist = (360*3600) - gap

    return dist

def get_point2planetdistance(division, point, toplanet):
    #Computes whats the distance between the point [sign,deg,min,sec] to toplanet in given divisional chart in seconds(deg and minutes also converted to seconds)
    tp = division["planets"][toplanet]
    tp_signnum = signnum(tp["sign"])
    #compute distance from start of Aries to from and to planets in seconds.
    sec_fp = (((point[0]-1)*30*3600) + (point[1]*3600) + (point[2]*60) + (point[3]))
    sec_tp = (((tp_signnum-1)*30*3600) + (tp["pos"]["deg"]*3600) + (tp["pos"]["min"]*60) + (tp["pos"]["sec"]))

    if(sec_tp >= sec_fp):   #if toplanet is ahead of fromplanet
        dist = sec_tp - sec_fp
    else:   #if toplanet is behind of fromplanet
        gap = sec_fp - sec_tp
        dist = (360*3600) - gap

    return dist

def isPushkaraNavamsha(nak, paada):
    PushkaraNavamshas = [   "Bharani3", "Kritika1", "Kritika4", "Rohini2", "Ardra4", 
                            "Punarvasu2", "Pushya2", "Purva Phalguni3", "Uttara Phalguni1", "Uttara Phalguni4",
                            "Hasta2", "Swati4", "Punarvasu4", "Vishaka4", "Vishaka2", "Anurada2", 
                            "Uttara Ashadha4", "Purva Ashadha3", "Uttara Ashadha1", "Shravana2", "Shatabhishak4", 
                            "Purva Bhadrapada4", "Purva Bhadrapada2", "Uttara Bhadrapada2" ]
    if(f'{nak}{paada}' in PushkaraNavamshas):
        return True
    else:
        return False

def isPushkaraBhaga(SignTatva, Degree):
    #For Fire signs (Aries, Leo and Sagittarius) - 21st degree is the Pushkara bhaga
    #For Earth signs (Taurus, Virgo and Capricorn) - 14th degree is the Pushkara bhaga
    #For Airy signs (Gemini, Libra and Aquarius) - 24th degree is the Pushkara bhaga
    #For Water signs (Cancer, Scorpio and Pisces) - 7th degree is the Pushkara bhaga 
    if (SignTatva == c.FIRE) and (Degree == 21):
        return True
    if (SignTatva == c.EARTH) and (Degree == 14):
        return True
    if (SignTatva == c.AIR) and (Degree == 24):
        return True
    if (SignTatva == c.WATER) and (Degree == 7):
        return True
    return False

def check_ifAllNumInSetA_in_SetB(SetA,SetB):
    SetA_Copy = SetA.copy()
    SetB_Copy = SetB.copy()
    for item in SetB_Copy:
        while(item in SetA_Copy):
            SetA_Copy.remove(item)
    if(len(SetA_Copy) == 0):
        return True
    else:
        return False

def list_intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

if __name__ == "__main__":
    print(signnum("Aries"))
    print(check_ifAllNumInSetA_in_SetB([1,4,4,10,7,1,1], [1,4,7,10]))
    #print(debilitationSign_of_planet)