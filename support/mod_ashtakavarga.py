#The AshtakaVarga calculation is made using method provided in below webpage:
# Webpage: https://www.thevedichoroscope.com/asthvarga-lessons/asthvarga-lessons-1/

import support.mod_astrodata as data
import support.mod_general as gen

#Bhinna ashtaka varga mappings 
BAV_BinduMatrix = {
    "Sun": { "Sun" : [1,2,4,7,8,9,10,11],   #Sun is benefic from suns 1st, 2nd, 4th, ... 11th houses
             "Moon" : [3,6,10,11],   #Sun is benefic from Moon in following positions 3,6,10,11.
             "Mars" : [1,2,4,7,8,9,10,11],
             "Mercury" : [3,5,6,9,10,11,12],
             "Jupiter" : [5,6,9,11],
             "Venus" : [6,7,12],
             "Saturn" : [1,2,4,7,8,9,10,11],
             "Ascendant" : [3,4,6,10,11,12]
            },
    "Moon": { "Sun" : [3,6,7,8,10,11],   
             "Moon" : [1,3,6,7,10,11],   
             "Mars" : [2,3,5,6,9,10,11],
             "Mercury" : [1,3,5,6,9,10,11],
             "Jupiter" : [1,4,7,8,10,11,12],
             "Venus" : [3,4,5,7,9,10,11],
             "Saturn" : [3,5,6,11],
             "Ascendant" : [3,6,10,11]
            },
    "Mars": { "Sun" : [3,5,6,10,11],   
             "Moon" : [3,6,11],   
             "Mars" : [1,2,4,7,8,10,11],
             "Mercury" : [3,5,6,11],
             "Jupiter" : [6,10,11,12],
             "Venus" : [6,8,11,12],
             "Saturn" : [1,7,8,9,10,11],
             "Ascendant" : [1,3,6,10,11]
            },
    "Mercury": { "Sun" : [5,6,9,11,12],   
             "Moon" : [2,4,6,8,10,11],   
             "Mars" : [1,2,4,7,8,9,10,12],
             "Mercury" : [1,3,5,6,9,10,11,12],
             "Jupiter" : [6,8,11,12],
             "Venus" : [1,2,3,4,5,8,9,11],
             "Saturn" : [1,2,4,7,8,9,10,12],
             "Ascendant" : [1,2,4,6,8,10,11]
            },
    "Jupiter": { "Sun" : [1,2,3,4,7,8,9,10,11],   
             "Moon" : [2,5,7,9,11],   
             "Mars" : [1,2,4,7,8,10,11],
             "Mercury" : [1,2,4,5,6,9,10,11],
             "Jupiter" : [1,2,3,4,7,8,10,11],
             "Venus" : [2,5,6,9,10,11],
             "Saturn" : [3,5,6,12],
             "Ascendant" : [1,2,4,5,6,7,9,10,11]
            },
    "Venus": { "Sun" : [8,11,12],   
             "Moon" : [1,2,3,4,5,8,9,11,12],   
             "Mars" : [3,4,6,9,11,12],
             "Mercury" : [3,5,6,9,11],
             "Jupiter" : [5,8,9,10,11],
             "Venus" : [1,2,3,4,5,8,9,10,11],
             "Saturn" : [3,4,5,8,9,10,11],
             "Ascendant" : [1,2,3,4,5,8,9,11]
            },
    "Saturn": { "Sun" : [1,2,4,7,8,10,11],   
             "Moon" : [3,6,11],   
             "Mars" : [3,5,6,10,11,12],
             "Mercury" : [6,8,9,10,11,12],
             "Jupiter" : [5,6,11,12],
             "Venus" : [6,11,12],
             "Saturn" : [3,5,6,11],
             "Ascendant" : [1,3,4,10,11]
            }
        }
BhinnaAshtakaVargaPoints = {"Sun" : [0,0,0,0,0,0,0,0,0,0,0,0],   
                            "Moon" : [0,0,0,0,0,0,0,0,0,0,0,0],   
                            "Mars" : [0,0,0,0,0,0,0,0,0,0,0,0],
                            "Mercury" : [0,0,0,0,0,0,0,0,0,0,0,0],
                            "Jupiter" : [0,0,0,0,0,0,0,0,0,0,0,0],
                            "Venus" : [0,0,0,0,0,0,0,0,0,0,0,0],
                            "Saturn" : [0,0,0,0,0,0,0,0,0,0,0,0],
                            "Total" : [0,0,0,0,0,0,0,0,0,0,0,0]
                            }

def compute_AshtakaVargas():
    for planet in BAV_BinduMatrix:
        for refPlanet in BAV_BinduMatrix[planet]:
            planet_BAV_points = BhinnaAshtakaVargaPoints[planet]
            if (refPlanet == "Ascendant"):
                refplanet_housenum = 1
            else:
                refplanet_housenum = data.charts["D1"]["planets"][refPlanet]["house-num"]
            for nth in BAV_BinduMatrix[planet][refPlanet]:
                index = gen.compute_nthsign(refplanet_housenum,nth) - 1
                planet_BAV_points[index] = planet_BAV_points[index] + 1
                #print(f'''planet[{planet}] - refplanet[{refPlanet} in {nth}th house {refplanet_housenum}] - adding 1 point to house {index+1} \nto make the new matrix is {planet_BAV_points}''')
    for hno in range(12):
        BhinnaAshtakaVargaPoints["Total"][hno] = (  BhinnaAshtakaVargaPoints["Sun"][hno] +
                                                    BhinnaAshtakaVargaPoints["Moon"][hno] +
                                                    BhinnaAshtakaVargaPoints["Mars"][hno] +
                                                    BhinnaAshtakaVargaPoints["Mercury"][hno] + 
                                                    BhinnaAshtakaVargaPoints["Jupiter"][hno] +
                                                    BhinnaAshtakaVargaPoints["Venus"][hno] +
                                                    BhinnaAshtakaVargaPoints["Saturn"][hno])
    data.charts["AshtakaVarga"] = BhinnaAshtakaVargaPoints.copy()
    return


if __name__ == '__main__':
    compute_AshtakaVargas()
    print(BhinnaAshtakaVargaPoints["Sun"])
        