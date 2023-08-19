#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# mod_lagna.py -- module lagna. All computations for lagna chart [D1 chart]
#
# Copyright (C) 2022 Shyam Bhat  <vicharavandana@gmail.com>
# Downloaded from "https://github.com/VicharaVandana/jyotishyam.git"
#
# This file is part of the "jyotishyam" Python library
# for computing Hindu jataka with sidereal lahiri ayanamsha technique 
# using swiss ephemeries
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Use Swiss ephemeris to calculate planetery position of 9 vedic astrology planets 
and lagna(Ascendant)
"""

from collections import namedtuple as struct
import swisseph as swe
import support.mod_astrodata as data
import support.mod_constants as c
import support.mod_general as gen
#from support.mod_astrodata import birthdata as bd



Date = struct("Date", ["year", "month", "day"])
Place = struct("Place", ["latitude", "longitude", "timezone"])

sidereal_year = 365.256360417   # From 


# namah suryaya chandraya mangalaya ... rahuve ketuve namah
swe.KETU = swe.PLUTO  # I've mapped Pluto to Ketu
planet_list = [swe.SUN, swe.MOON, swe.MARS, swe.MERCURY, swe.JUPITER,
               swe.VENUS, swe.SATURN, swe.MEAN_NODE, # Rahu = MEAN_NODE
               swe.KETU]

set_ayanamsa_mode = lambda: swe.set_sid_mode(swe.SIDM_LAHIRI)           #Vedic astrology uses Lahiri ayanamsa 
reset_ayanamsa_mode = lambda: swe.set_sid_mode(swe.SIDM_FAGAN_BRADLEY)  #Default is FAGAN_BRADLEY ayanamsa in swiss ephemeries

################################# FUNCTIONS #############################
def get_planet_name(planet):
  names = { swe.SUN: "Sun", swe.MOON: "Moon", swe.MARS: "Mars",
            swe.MERCURY: "Mercury", swe.JUPITER: "Jupiter", swe.VENUS: "Venus",
            swe.SATURN: "Saturn", swe.MEAN_NODE: "Rahu", swe.KETU: "Ketu"}
  return names[planet]

def get_planet_symbol(planet):
  symbols = { swe.SUN: "Su", swe.MOON: "Mo", swe.MARS: "Ma",
              swe.MERCURY: "Me", swe.JUPITER: "Ju", swe.VENUS: "Ve",
              swe.SATURN: "Sa", swe.MEAN_NODE: "Ra", swe.KETU: "Ke"}
  return symbols[planet]

# Convert 23d 30' 30" to 23.508333 degrees
from_dms = lambda degs, mins, secs: degs + mins/60 + secs/3600

# the inverse
def to_dms_prec(deg):
  d = int(deg)
  mins = (deg - d) * 60
  m = int(mins)
  s = round((mins - m) * 60, 6)
  return [d, m, s]

def to_dms(deg):
  d, m, s = to_dms_prec(deg)
  return [d, m, int(s)]

# Make angle lie between [-180, 180) instead of [0, 360)
norm180 = lambda angle: (angle - 360) if angle >= 180 else angle;

# Make angle lie between [0, 360)
norm360 = lambda angle: angle % 360

# Ketu is always 180° after Rahu, so same coordinates but different constellations
# i.e if Rahu is in Pisces, Ketu is in Virgo etc
ketu = lambda rahu: (rahu + 180) % 360

# Julian Day number as on (year, month, day) at 00:00 UTC
gregorian_to_jd = lambda date: swe.julday(date.year, date.month, date.day, 0.0)
jd_to_gregorian = lambda jd: swe.revjul(jd, swe.GREG_CAL)   # returns (y, m, d, h, min, s)

get_nakshatra_name = [  "Ashwini", "Bharani", "Kritika", 
                        "Rohini", "Mrigashira", "Ardra", 
                        "Punarvasu", "Pushya", "Ashlesha", 
                        "Magha", "Purva Phalguni", "Uttara Phalguni", 
                        "Hasta", "Chitra", "Swati", 
                        "Vishaka", "Anurada", "Jyeshta", 
                        "Mula", "Purva Ashadha", "Uttara Ashadha", 
                        "Shravana", "Dhanishta", "Shatabhishak", 
                        "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"]

def nakshatra_pada(longitude):
  """Gives nakshatra (0..26) and paada (1..4) in which given longitude lies"""
  # 27 nakshatras span 360°
  one_star = (360 / 27)  # = 13°20'
  # Each nakshatra has 4 padas, so 27 x 4 = 108 padas in 360°
  one_pada = (360 / 108) # = 3°20'
  quotient = int(longitude / one_star)
  reminder = (longitude - quotient * one_star)
  pada = int(reminder / one_pada)
  # convert 0..26 to 1..27 and 0..3 to 1..4
  return [get_nakshatra_name[quotient], 1 + pada]

def sidereal_longitude(jd, planet):
  """Computes nirayana (sidereal) longitude of given planet on jd"""
  set_ayanamsa_mode()
  (longi,myflags) = swe.calc_ut(jd, planet, flag = swe.FLG_SWIEPH | swe.FLG_SIDEREAL)
  reset_ayanamsa_mode()
  return norm360(longi[0]) # degrees

def Is_Retrograde(jd, planet):
  """Checks if given planet is in retrograde motion on jd"""
  set_ayanamsa_mode()
  (longi,myflags) = swe.calc_ut(jd, planet, flag = swe.FLG_SWIEPH | swe.FLG_SPEED | swe.FLG_SIDEREAL)
  reset_ayanamsa_mode()
  return (longi[3] < 0) # if speed is negative then its in retro




def update_ascendant(jd, place):
  """Lagna (=ascendant) calculation at any given time & place
     It also updates most of lagna elements data, 
     except lagnesh_sign, lagnesh rashi and lagnesh dispositor"""
  lat, lon, tz = place
  jd_utc = jd - (tz / 24.)
  set_ayanamsa_mode() # needed for swe.houses_ex()
  # returns two arrays, cusps and ascmc, where ascmc[0] = Ascendant
  nirayana_lagna = swe.houses_ex(jd_utc, lat, lon, flag = swe.FLG_SIDEREAL)[1][0]
  # 12 zodiac signs span 360°, so each one takes 30°
  # 0 = Mesha, 1 = Vrishabha, ..., 11 = Meena
  constellation = int(nirayana_lagna / 30)
  coordinates = to_dms(nirayana_lagna % 30)
  reset_ayanamsa_mode()
  #Updating the data from computed values
  #update position of ascendant
  data.lagna_ascendant["pos"]["deg"] = coordinates[0]
  data.lagna_ascendant["pos"]["min"] = coordinates[1]
  data.lagna_ascendant["pos"]["sec"] = coordinates[2]
  data.lagna_ascendant["pos"]["dec_deg"] = (nirayana_lagna % 30)

  #update nakshatra related data for ascendant
  nak_pad = nakshatra_pada(nirayana_lagna)
  data.lagna_ascendant["nakshatra"] = nak_pad[0]
  data.lagna_ascendant["pada"] = nak_pad[1]
  data.lagna_ascendant["nak-ruler"] = gen.ruler_of_nakshatra[nak_pad[0]]
  data.lagna_ascendant["nak-diety"] = gen.diety_of_nakshatra[nak_pad[0]]

  #update sign related data for ascendant
  data.lagna_ascendant["sign"]       = gen.signs[constellation]
  data.lagna_ascendant["rashi"]      = gen.rashis[constellation]
  data.lagna_ascendant["lagna-lord"] = gen.signlords[constellation]
  data.lagna_ascendant["sign-tatva"] = gen.signtatvas[constellation]

  #updating Status of Ascendant
  data.lagna_ascendant["status"] = c.PARTIAL

  return (1 + constellation)

def update_planetaryData(jd, place):
  """Computes instantaneous planetary positions
     (i.e., which celestial object lies in which constellation)
     Also gives the nakshatra-pada division
     And updates the birth chart data for all the planets except those dependant on ascendant
   """
  jd_ut = jd - place.timezone / 24.

  for planet in planet_list:
    if planet != swe.KETU:
      nirayana_long = sidereal_longitude(jd_ut, planet)
      retro = Is_Retrograde(jd_ut, planet)
    else: # Ketu
      #nirayana_long = ketu(sidereal_longitude(jd_ut, swe.RAHU))
      nirayana_long = ketu(sidereal_longitude(jd_ut, swe.MEAN_NODE))
      retro = True  #ketu is always in retrograde

    # 12 zodiac signs span 360°, so each one takes 30°
    # 0 = Mesha, 1 = Vrishabha, ..., 11 = Meena
    constellation = int(nirayana_long / 30)
    coordinates = to_dms(nirayana_long % 30)
    
    #Update the data properly for the planet
    db_planet = data.lagna_planets[get_planet_name(planet)] #get the proper planet container
    db_planet["retro"] = retro  #retrograde property

    #update position of the planet
    db_planet["pos"]["deg"] = coordinates[0]
    db_planet["pos"]["min"] = coordinates[1]
    db_planet["pos"]["sec"] = coordinates[2]
    db_planet["pos"]["dec_deg"] = (nirayana_long % 30)

    #update nakshatra related data for the planet
    nak_pad = nakshatra_pada(nirayana_long)
    db_planet["nakshatra"] = nak_pad[0]
    db_planet["pada"] = nak_pad[1]
    db_planet["nak-ruler"] = gen.ruler_of_nakshatra[nak_pad[0]]
    db_planet["nak-diety"] = gen.diety_of_nakshatra[nak_pad[0]]

    #update sign related data for the planet
    currentsign = gen.signs[constellation]
    db_planet["sign"]       = currentsign
    db_planet["rashi"]      = gen.rashis[constellation]
    dispositor = gen.signlords[constellation]
    db_planet["dispositor"] = dispositor
    db_planet["sign-tatva"] = gen.signtatvas[constellation]

    #Compute the house relation for the planet
    
    exhaltsign = gen.exhaltationSign_of_planet[db_planet["name"]] 
    debilitsign = gen.debilitationSign_of_planet[db_planet["name"]]
    friends = db_planet["friends"]
    enemies = db_planet["enemies"]
    neutral = db_planet["nuetral"]  

    if(currentsign == exhaltsign):  #first check for exhaltation
      db_planet["house-rel"] = c.EXHALTED
    elif(currentsign == debilitsign): #next check for debilitated 
      db_planet["house-rel"] = c.DEBILITATED
    elif(db_planet["name"] == dispositor): #next check for own sign 
      db_planet["house-rel"] = c.OWNSIGN
    elif(dispositor in friends): #next check for friend sign 
      db_planet["house-rel"] = c.FRIENDSIGN
    elif(dispositor in enemies): #next check for enemy sign 
      db_planet["house-rel"] = c.ENEMYSIGN
    elif(dispositor in neutral): #next check for neutral sign 
      db_planet["house-rel"] = c.NEUTRALSIGN
    else:
      db_planet["house-rel"] = "UNKNOWN"
    
    #Planet with dispositor relation

    
    #updating Status of planet
    db_planet["status"] = c.PARTIAL

  return



def compute_lagnaChart_custom(UserBirthData):
  birthday_julien = swe.julday( UserBirthData["DOB"]["year"],  #birth year
                                UserBirthData["DOB"]["month"],  #birth month
                                UserBirthData["DOB"]["day"],  #birth day
                                ((UserBirthData["TOB"]["hour"])+ (UserBirthData["TOB"]["min"])/60. + (UserBirthData["TOB"]["sec"])/3600),  #birth time in float
                              )   #yyyy,mm,dd,time_24hr_format(hh + mm/60 + ss/3600)
  
  birth_place = Place( UserBirthData["POB"]["lat"], #lattitude
                       UserBirthData["POB"]["lon"], #longitude
                       UserBirthData["POB"]["timezone"]  #Timezone
                      )
  lagna = update_ascendant(birthday_julien, birth_place)  #Compute ascendant related data
  update_planetaryData(birthday_julien, birth_place)  #Compute navagraha related data

  #update miscdata like name maasa vaara tithi etc
  data.charts["user_details"]["name"] = UserBirthData["name"]
  gen.update_miscdata(birthday_julien, birth_place, data.charts["user_details"])

  #computing benefics, malefics and neutral planets for given lagna
  gen.compute_BenMalNeu4lagna(lagna,data.D1["classifications"])

  #computing lagnesh related data for ascendant - not updated by update_ascendant()
  lagnesh = data.lagna_ascendant["lagna-lord"]  #get lagnesh
  data.lagna_ascendant["lagnesh-sign"]  = data.lagna_planets[lagnesh]["sign"]  #check the sign of lagnesh
  data.lagna_ascendant["lagnesh-rashi"] = data.lagna_planets[lagnesh]["rashi"] 
  data.lagna_ascendant["lagnesh-disp"]  = data.lagna_planets[lagnesh]["dispositor"] 
  #updating Status of Ascendant
  data.lagna_ascendant["status"] = c.COMPUTED

  #computing house related data for planets - not updated by update_planetaryData()
  for planetname in data.lagna_planets:
    planet = data.lagna_planets[planetname]
    planet["house-num"] = gen.housediff(lagna, gen.signnum(planet["sign"]))
    #updating Status of the planet
    planet["status"] = c.COMPUTED

  gen.update_houses(data.D1)

  #computing aspects and conjunction planets
  gen.compute_aspects(data.D1)
  gen.compute_aspectedby(data.D1)  
  gen.compute_conjuncts(data.D1) 

  #populating the classification part of divisional chart
  gen.populate_Natural_BeneficsMalefics(data.D1)  #Natural benefics and malefics
  gen.populate_kendraplanets(data.D1) #kendra planets
  gen.populate_trikonaplanets(data.D1) #trikona planets
  gen.populate_trikplanets(data.D1) #trik planets
  gen.populate_upachayaplanets(data.D1) #upachaya planets
  gen.populate_dharmaplanets(data.D1) #dharma planets
  gen.populate_arthaplanets(data.D1) #artha planets
  gen.populate_kamaplanets(data.D1) #kama planets
  gen.populate_mokshaplanets(data.D1) #moksha planets

  data.charts["user_details"]["nakshatra"] = data.lagna_moon["nakshatra"]
  data.charts["user_details"]["rashi"] = data.lagna_moon["sign"]
  data.charts["user_details"]["birthdetails"] = UserBirthData.copy()

  data.isAstroDataComputed = True
  return

if __name__ == "__main__":
    #compute_lagnaChart()
    print("GOOD")



