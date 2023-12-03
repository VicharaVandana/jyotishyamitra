
import support.mod_constants as c

################ CHARTS ########################
##  Lagna Ascendant related data
###   LAGNA - ASCENDANT
lagna_ascendant = {"name"        : "Ascendant",
                  "symbol"       : "Asc",
                  "pos"          : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
                  "nakshatra"    : "Ashwini" ,
                  "pada"         : 1,
                  "nak-ruler"    : "Ketu",
                  "nak-diety"    : "Ashwini kumaras",
                  "sign"         : "Aries",
                  "rashi"        : "Mesha",
                  "lagna-lord"   : "Mars",
                  "sign-tatva"   : c.FIRE,
                  "lagnesh-sign" : "Aries",
                  "lagnesh-rashi": "Mesha",
                  "lagnesh-disp" : "Mars",
                  "status"       : c.INIT
                  }
##  Lagna planets related data
###   LAGNA - SUN
lagna_sun = {"name"         : "Sun",
             "symbol"       : "Su",
             "retro"        : 0,    #initialized retro as 0
             "pos"          : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
             "nakshatra"    : "Ashwini" ,
             "pada"         : 1,
             "nak-ruler"    : "Ketu",
             "nak-diety"    : "Ashwini kumaras",
             "sign"         : "Aries",
             "rashi"        : "Mesha",
             "dispositor"   : "Mars",
             "tattva"       : c.FIRE,
             "sign-tatva"   : c.FIRE,
             "house-rel"    : c.EXHALTED,
             "house-nature" : c.DHARMA,
             "planet-nature": c.PAAPAGRAHA,
             "gender"       : c.MALE,
             "category"     : c.DEVA,
             "house-num"    : 1,
             "friends"      : ["Moon", "Mars", "Jupiter"],
             "enemies"      : ["Venus", "Saturn", "Rahu", "Ketu"],
             "nuetral"      : ["Mercury"],
             "varna"        : c.KSHATRIYA,
             "guna"         : c.SATVA,
             "Aspects"      : {"planets":[], "houses":[], "signs":[]},
             "Aspected-by"  : [],
             "conjuncts"    : [],
             "status"       : c.INIT
            }
###   LAGNA - MOON
lagna_moon = {"name"         : "Moon",
             "symbol"       : "Mo",
             "retro"        : 0,    #initialized retro as 0
             "pos"          : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
             "nakshatra"    : "Ashwini" ,
             "pada"         : 1,
             "nak-ruler"    : "Ketu",
             "nak-diety"    : "Ashwini kumaras",
             "sign"         : "Aries",
             "rashi"        : "Mesha",
             "dispositor"   : "Mars",
             "tattva"       : c.WATER,
             "sign-tatva"   : c.FIRE,
             "house-rel"    : c.FRIENDSIGN,
             "house-nature" : c.DHARMA,
             "planet-nature": c.PUNYAGRAHA,
             "gender"       : c.FEMALE,
             "category"     : c.DEVA,
             "house-num"    : 1,
             "friends"      : ["Sun", "Mercury"],
             "enemies"      : [],
             "nuetral"      : ["Mars", "Venus", "Jupiter", "Saturn", "Rahu", "Ketu"],
             "varna"        : c.VAISHYA,
             "guna"         : c.SATVA,
             "Aspects"      : {"planets":[], "houses":[], "signs":[]},
             "Aspected-by"  : [],
             "conjuncts"    : [],
             "status"       : c.INIT
            }
###   LAGNA - MARS
lagna_mars = {"name"        : "Mars",
             "symbol"       : "Ma",
             "retro"        : 0,    #initialized retro as 0
             "pos"          : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
             "nakshatra"    : "Ashwini" ,
             "pada"         : 1,
             "nak-ruler"    : "Ketu",
             "nak-diety"    : "Ashwini kumaras",
             "sign"         : "Aries",
             "rashi"        : "Mesha",
             "dispositor"   : "Mars",
             "tattva"       : c.FIRE,
             "sign-tatva"   : c.FIRE,
             "house-rel"    : c.OWNSIGN,
             "house-nature" : c.DHARMA,
             "planet-nature": c.PAAPAGRAHA,
             "gender"       : c.MALE,
             "category"     : c.DEVA,
             "house-num"    : 1,
             "friends"      : ["Sun", "Moon", "Jupiter"],
             "enemies"      : ["Mercury"],
             "nuetral"      : ["Saturn", "Venus", "Rahu", "Ketu"],
             "varna"        : c.KSHATRIYA,
             "guna"         : c.TAMAS,
             "Aspects"      : {"planets":[], "houses":[], "signs":[]},
             "Aspected-by"  : [],
             "conjuncts"    : [],
             "status"       : c.INIT
            }
###   LAGNA - MERCURY
lagna_mercury = {"name"     : "Mercury",
             "symbol"       : "Me",
             "retro"        : 0,    #initialized retro as 0
             "pos"          : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
             "nakshatra"    : "Ashwini" ,
             "pada"         : 1,
             "nak-ruler"    : "Ketu",
             "nak-diety"    : "Ashwini kumaras",
             "sign"         : "Aries",
             "rashi"        : "Mesha",
             "dispositor"   : "Mars",
             "tattva"       : c.EARTH,
             "sign-tatva"   : c.FIRE,
             "house-rel"    : c.NEUTRALSIGN,
             "house-nature" : c.DHARMA,
             "planet-nature": c.PAAPAGRAHA,
             "gender"       : c.NEUTER,
             "category"     : c.NEUTRAL,
             "house-num"    : 1,
             "friends"      : ["Sun", "Venus", "Rahu"],
             "enemies"      : ["Moon", "Ketu"],
             "nuetral"      : ["Saturn", "Mars", "Jupiter"],
             "varna"        : c.SHUDRA,
             "guna"         : c.RAJAS,
             "Aspects"      : {"planets":[], "houses":[], "signs":[]},
             "Aspected-by"  : [],
             "conjuncts"    : [],
             "status"       : c.INIT
            }
###   LAGNA - JUPITER
lagna_jupiter = {"name"     : "Jupiter",
             "symbol"       : "Ju",
             "retro"        : 0,    #initialized retro as 0
             "pos"          : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
             "nakshatra"    : "Ashwini" ,
             "pada"         : 1,
             "nak-ruler"    : "Ketu",
             "nak-diety"    : "Ashwini kumaras",
             "sign"         : "Aries",
             "rashi"        : "Mesha",
             "dispositor"   : "Mars",
             "tattva"       : c.FIRE,
             "sign-tatva"   : c.FIRE,
             "house-rel"    : c.FRIENDSIGN,
             "house-nature" : c.DHARMA,
             "planet-nature": c.PUNYAGRAHA,
             "gender"       : c.MALE,
             "category"     : c.DEVA,
             "house-num"    : 1,
             "friends"      : ["Moon", "Mars", "Sun", "Ketu"],
             "enemies"      : ["Venus", "Mercury", "Rahu"],
             "nuetral"      : ["Saturn"],
             "varna"        : c.BRAHMIN,
             "guna"         : c.SATVA,
             "Aspects"      : {"planets":[], "houses":[], "signs":[]},
             "Aspected-by"  : [],
             "conjuncts"    : [],
             "status"       : c.INIT
            }
###   LAGNA - VENUS
lagna_venus = {"name"       : "Venus",
             "symbol"       : "Ve",
             "retro"        : 0,    #initialized retro as 0
             "pos"          : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
             "nakshatra"    : "Ashwini" ,
             "pada"         : 1,
             "nak-ruler"    : "Ketu",
             "nak-diety"    : "Ashwini kumaras",
             "sign"         : "Aries",
             "rashi"        : "Mesha",
             "dispositor"   : "Mars",
             "tattva"       : c.AIR,
             "sign-tatva"   : c.FIRE,
             "house-rel"    : c.NEUTRALSIGN,
             "house-nature" : c.DHARMA,
             "planet-nature": c.PUNYAGRAHA,
             "gender"       : c.FEMALE,
             "category"     : c.DANAVA,
             "house-num"    : 1,
             "friends"      : ["Saturn", "Mercury", "Rahu", "Ketu"],
             "enemies"      : ["Sun", "Moon"],
             "nuetral"      : ["Mars", "Jupiter"],
             "varna"        : c.BRAHMIN,
             "guna"         : c.RAJAS,
             "Aspects"      : {"planets":[], "houses":[], "signs":[]},
             "Aspected-by"  : [],
             "conjuncts"    : [],
             "status"       : c.INIT
            }
###   LAGNA - SATURN
lagna_saturn = {"name"      : "Saturn",
             "symbol"       : "Sa",
             "retro"        : 0,    #initialized retro as 0
             "pos"          : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
             "nakshatra"    : "Ashwini" ,
             "pada"         : 1,
             "nak-ruler"    : "Ketu",
             "nak-diety"    : "Ashwini kumaras",
             "sign"         : "Aries",
             "rashi"        : "Mesha",
             "dispositor"   : "Mars",
             "tattva"       : c.AIR,
             "sign-tatva"   : c.FIRE,
             "house-rel"    : c.DEBILITATED,
             "house-nature" : c.DHARMA,
             "planet-nature": c.PAAPAGRAHA,
             "gender"       : c.FEMALE,
             "category"     : c.DANAVA,
             "house-num"    : 1,
             "friends"      : ["Venus", "Mercury", "Rahu", "Ketu"],
             "enemies"      : ["Sun", "Moon", "Mars"],
             "nuetral"      : ["Jupiter"],
             "varna"        : c.SHUDRA,
             "guna"         : c.TAMAS,
             "Aspects"      : {"planets":[], "houses":[], "signs":[]},
             "Aspected-by"  : [],
             "conjuncts"    : [],
             "status"       : c.INIT
            }
###   LAGNA - RAHU
lagna_rahu = {"name"        : "Rahu",
             "symbol"       : "Ra",
             "retro"        : 1,    #initialized retro as 1
             "pos"          : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
             "nakshatra"    : "Ashwini" ,
             "pada"         : 1,
             "nak-ruler"    : "Ketu",
             "nak-diety"    : "Ashwini kumaras",
             "sign"         : "Aries",
             "rashi"        : "Mesha",
             "dispositor"   : "Mars",
             "tattva"       : c.AIR,
             "sign-tatva"   : c.FIRE,
             "house-rel"    : c.OWNSIGN,
             "house-nature" : c.DHARMA,
             "planet-nature": c.PAAPAGRAHA,
             "gender"       : c.MALE,
             "category"     : c.DANAVA,
             "house-num"    : 1,
             "friends"      : ["Venus", "Mercury", "Ketu", "Saturn"],
             "enemies"      : ["Sun", "Moon", "Mars"],
             "nuetral"      : ["Jupiter"],
             "varna"        : c.SHUDRA,
             "guna"         : c.TAMAS,
             "Aspects"      : {"planets":[], "houses":[], "signs":[]},
             "Aspected-by"  : [],
             "conjuncts"    : [],
             "status"       : c.INIT
            }
###   LAGNA - KETU
lagna_ketu = {"name"        : "Ketu",
             "symbol"       : "Ke",
             "retro"        : 1,    #initialized retro as 1
             "pos"          : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
             "nakshatra"    : "Ashwini" ,
             "pada"         : 1,
             "nak-ruler"    : "Ketu",
             "nak-diety"    : "Ashwini kumaras",
             "sign"         : "Aries",
             "rashi"        : "Mesha",
             "dispositor"   : "Mars",
             "tattva"       : c.AIR,
             "sign-tatva"   : c.FIRE,
             "house-rel"    : c.OWNSIGN,
             "house-nature" : c.DHARMA,
             "planet-nature": c.PAAPAGRAHA,
             "gender"       : c.FEMALE,
             "category"     : c.DANAVA,
             "house-num"    : 1,
             "friends"      : ["Venus", "Mercury", "Rahu", "Saturn"],
             "enemies"      : ["Sun", "Moon", "Mars"],
             "nuetral"      : ["Jupiter"],
             "varna"        : c.SHUDRA,
             "guna"         : c.TAMAS,
             "Aspects"      : {"planets":[], "houses":[], "signs":[]},
             "Aspected-by"  : [],
             "conjuncts"    : [],
             "status"       : c.INIT
            }
lagna_planets = {"Sun"      : lagna_sun,
                 "Moon"     : lagna_moon,
                 "Mars"     : lagna_mars,
                 "Mercury"  : lagna_mercury,
                 "Jupiter"  : lagna_jupiter,
                 "Venus"    : lagna_venus,
                 "Saturn"   : lagna_saturn,
                 "Rahu"     : lagna_rahu,
                 "Ketu"     : lagna_ketu
                 }
#charts consists of Divisional charts
D1 = {"name"            : "Lagna",
      "symbol"          : "D1",
      "ascendant"       : lagna_ascendant,
      "planets"         : lagna_planets,
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }



D9 = {"name"            : "Navamsa",
      "symbol"          : "D9",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D10 = {"name"            : "Dasamsa",
      "symbol"          : "D10",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D2 = {"name"            : "Hora",
      "symbol"          : "D2",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D3 = {"name"            : "Drekkana",
      "symbol"          : "D3",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D4 = {"name"            : "Chaturtamsa",
      "symbol"          : "D4",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D7 = {"name"            : "Saptamsa",
      "symbol"          : "D7",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D12 = {"name"            : "Dwadasamsa",
      "symbol"          : "D12",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D16 = {"name"            : "Shodasamsa",
      "symbol"          : "D16",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D20 = {"name"            : "Vimsamsa",
      "symbol"          : "D20",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D24 = {"name"            : "Chaturvimsamsa",
      "symbol"          : "D24",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D27 = {"name"            : "Saptavimsamsa",
      "symbol"          : "D27",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D30 = {"name"            : "Trimsamsa",
      "symbol"          : "D30",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D40 = {"name"            : "Khavedamsa",
      "symbol"          : "D40",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D45 = {"name"            : "Akshavedamsa",
      "symbol"          : "D45",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

D60 = {"name"            : "Shashtiamsa",
      "symbol"          : "D60",
      "houses"          : [],
      "classifications" : { "benefics"    : [],
                            "malefics"    : [],
                            "neutral"     : [],
                            "natural-benefics" : [],
                            "natural-malefics" : [],
                            "kendra"      : [],
                            "trikona"     : [],
                            "trik"        : [],
                            "upachaya"    : [],
                            "dharma"      : [],
                            "artha"       : [],
                            "kama"        : [],
                            "moksha"      : []
                          }
      }

isAstroDataComputed = False

charts = {"D1": D1,
          "D9": D9,
          "D10":D10,
          "D2":D2,
          "D3":D3,
          "D4":D4,
          "D7":D7,
          "D12":D12,
          "D16":D16,
          "D20":D20,
          "D24":D24,
          "D27":D27,
          "D30":D30,
          "D40":D40,
          "D45":D45,
          "D60":D60,
          #"yogadoshas":[],
          "Balas":{"Vimshopaka":{ "shadvarga": {  "Sun": 0,
                                                  "Moon": 0,
                                                  "Mars": 0,
                                                  "Mercury": 0,
                                                  "Jupiter": 0,
                                                  "Venus": 0,
                                                  "Saturn": 0,
                                                  "Rahu": 0,
                                                  "Ketu": 0
                                                },
                                  "saptavarga": { "Sun": 0,
                                                  "Moon": 0,
                                                  "Mars": 0,
                                                  "Mercury": 0,
                                                  "Jupiter": 0,
                                                  "Venus": 0,
                                                  "Saturn": 0,
                                                  "Rahu": 0,
                                                  "Ketu": 0
                                                },
                                  "dashavarga": { "Sun": 0,
                                                  "Moon": 0,
                                                  "Mars": 0,
                                                  "Mercury": 0,
                                                  "Jupiter": 0,
                                                  "Venus": 0,
                                                  "Saturn": 0,
                                                  "Rahu": 0,
                                                  "Ketu": 0
                                                },
                                  "shodashavarga": { "Sun": 0,
                                                  "Moon": 0,
                                                  "Mars": 0,
                                                  "Mercury": 0,
                                                  "Jupiter": 0,
                                                  "Venus": 0,
                                                  "Saturn": 0,
                                                  "Rahu": 0,
                                                  "Ketu": 0
                                                },
                                },
"Shadbala": { "Total" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
              "Rupas" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
              "Sthanabala": { "Total" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                              "Uchhabala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                              "Saptavargajabala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                              "Ojhayugmarashiamshabala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                              "Kendradhibala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                              "Drekshanabala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                            },
              "Digbala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
              "Kaalabala": { "Total" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                              "Natonnatabala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                              "Pakshabala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                              "Tribhagabala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                              "Varsha-maasa-dina-horabala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                              "Yuddhabala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                              "Ayanabala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
                            },
              "Cheshtabala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
              "Naisargikabala" : {"Sun": 60, "Moon": 51.4, "Mars": 17.1 , "Mercury": 25.7, "Jupiter": 34.3, "Venus": 42.9, "Saturn": 8.6},
              "Drikbala" : {"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0}
            },
"Ishtabala":{"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
"Kashtabala":{"Sun": 0, "Moon": 0, "Mars": 0, "Mercury": 0, "Jupiter": 0, "Venus": 0, "Saturn": 0},
"BhavaBala": {  "BhavaAdhipathibala" : [0,0,0,0,0,0,0,0,0,0,0,0],
                "BhavaDigbala" : [0,0,0,0,0,0,0,0,0,0,0,0],
                "BhavaDrishtibala" : [0,0,0,0,0,0,0,0,0,0,0,0],
                "Total" : [0,0,0,0,0,0,0,0,0,0,0,0]
},
                  },
          "AshtakaVarga" : {},
          "Dashas":{ "Vimshottari":{  "mahadashas" : {},
                                      "antardashas": {},
                                      "paryantardashas": {},
                                      "current":{
                                                  "date": "",
                                                  "dasha": "",
                                                  "bhukti": "",
                                                  "paryantardasha": "",
                                                 }
                                    }
                    },
        "special_points" : {
          "sphuta" : {
                        "type" : "", #Beeja for males and Kshetra for females
                        "symbol" : "",
                        "D1" : {
                                  "sign" : "",
                                  "pos"  : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
                                  "signlord" : "",
                                  "nakshatra" : "",
                                  "pada" : 0,
                                  "nak-ruler" : "",
                                  "house-num" : 0
                        },
                        "D3" : {
                                  "sign" : "",
                                  "pos"  : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
                                  "signlord" : "",
                                  "nakshatra" : "",
                                  "pada" : 0,
                                  "nak-ruler" : "",
                                  "house-num" : 0
                        },
                        "D7" : {
                                  "sign" : "",
                                  "pos"  : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
                                  "signlord" : "",
                                  "nakshatra" : "",
                                  "pada" : 0,
                                  "nak-ruler" : "",
                                  "house-num" : 0
                        },
                        "D9" : {
                                  "sign" : "",
                                  "pos"  : {"deg" : 0, "min" : 0, "sec" : 0, "dec_deg": 0.0}, #initioalized to zero
                                  "signlord" : "",
                                  "nakshatra" : "",
                                  "pada" : 0,
                                  "nak-ruler" : "",
                                  "house-num" : 0
                        },                        
                },
        },
          "user_details" : {"name"  :"Shyam Bhat",
                            "birthdetails": {   "DOB"     : {   "year"     : 0,
                                                                "month"    : 0,
                                                                "day"      : 0
                                                            },
                                                "TOB"     : {   "hour"     : 0,  #in 24 hour format
                                                                "min"      : 0,
                                                                "sec"      : 0
                                                            }, 
                                                "POB"     : {   "name"     : "",
                                                                "lat"      : 0,     #+ve for North and -ve for south
                                                                "lon"      : 0,     #+ve for East and -ve for West
                                                                "timezone" : 0
                                                            },
                                                "name"    : "",
                                                "Gender"  : ""
                                                },
                            "maasa" :"",
                            "vaara" : "",
                            "tithi" : "",
                            "karana" : "",
                            "nakshatra" : "",
                            "yoga" : "",
                            "rashi" : ""}
          }

def clearAstroData(charts):
  charts["D1"]["classifications"] = { "benefics"    : [],
                                      "malefics"    : [],
                                      "neutral"     : [],
                                      "kendra"      : [],
                                      "trikona"     : [],
                                      "trik"        : [],
                                      "upachaya"    : [],
                                      "dharma"      : [],
                                      "artha"       : [],
                                      "kama"        : [],
                                      "moksha"      : []
                                    }.copy()
  charts["D1"]["houses"] = []
  #charts["yogadoshas"] = []

  for key in lagna_planets:
    lagna_planets[key]["Aspects"] = {"planets":[], "houses":[], "signs":[]}.copy()
    lagna_planets[key]["Aspected-by"] = []
    lagna_planets[key]["conjuncts"] = []
  return(True)