#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# mod_divisional.py -- module Divisional. All computations for Divisional chart [D2 to D60 chart - Total 15 divisional charts]
#
# Copyright (C) 2023 Shyam Bhat  <vicharavandana@gmail.com>
# Downloaded from "https://github.com/VicharaVandana/jyotishyam.git"
#
# This file is part of the "jyotishyam" Python library
# for computing Hindu jataka with sidereal lahiri ayanamsha technique 
# using swiss ephemeries
#
#Computed divisional charts with logic given in https://jothishi.com/divisional-charts/
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

import support.mod_astrodata as data
import support.mod_constants as c
import support.mod_general as gen
from support.mod_lagna import *

#Below function computes Navamsa longitude from lagna longitude
def navamsa_from_long(sign, pos_deg, pos_min, pos_sec):
    #sign as 1:Aries, 2:Taurus ... 12:Pisces
    #pos_x is position of planet in sign in degree minute and seconds
    #this function computes navamsha position in sign and degree minute and seconds format only in tuple
    longi_sec = (((sign - 1) * 30 * 3600) +
                (pos_deg * 3600) + (pos_min * 60) + pos_sec)
    amsa = ((3 * 3600) + (20 * 60)) #one navamsa is 3 degree 20 minutes
    #check which navamsha does our planet falls in
    navSign = 1 + int(longi_sec/amsa) % 12
    longi_pending_sec = (longi_sec % amsa)
    longi_pending_sec_normalized = ((longi_pending_sec*30*3600)/amsa)   #pending is for 3deg20min so normalized is for 30deg
    navDeg = int(longi_pending_sec_normalized / 3600)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 3600)
    navMin = int(longi_pending_sec_normalized / 60)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 60)
    navSec = round(longi_pending_sec_normalized,2)
    longi_nav_sec = (((navSign - 1) * 30 * 3600) +
                (navDeg * 3600) + (navMin * 60) + navSec)
    return(longi_nav_sec, navSign, navDeg, navMin, navSec)

#Below function computes Dasamsa longitude from lagna longitude
def dasamsa_from_long(sign, pos_deg, pos_min, pos_sec):
    #sign as 1:Aries, 2:Taurus ... 12:Pisces
    #pos_x is position of planet in sign in degree minute and seconds
    #this function computes navamsha position in sign and degree minute and seconds format only in tuple
    longi_sec = ((pos_deg * 3600) + (pos_min * 60) + pos_sec)
    amsa = (3 * 3600) #one dasamsa is 3 degree 
    #check which dasamsa compartment does our planet falls in
    dasamsaCompartment = 1 + int(longi_sec/amsa) % 12
    #if lagna sign is even then dasamsa sign starts from 9th sign from lagna sign else from same sign
    if(sign % 2 == 0):  #even sign
        baseSign = gen.compute_nthsign(sign,9)
    else:
        baseSign = sign
    dasSign = gen.compute_nthsign(baseSign,dasamsaCompartment)
    longi_pending_sec = (longi_sec % amsa)
    longi_pending_sec_normalized = ((longi_pending_sec*30*3600)/amsa)   #pending is for 3deg20min so normalized is for 30deg
    dasDeg = int(longi_pending_sec_normalized / 3600)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 3600)
    dasMin = int(longi_pending_sec_normalized / 60)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 60)
    dasSec = round(longi_pending_sec_normalized,2)
    longi_nav_sec = (((dasSign - 1) * 30 * 3600) +
                (dasDeg * 3600) + (dasMin * 60) + dasSec)
    return(longi_nav_sec, dasSign, dasDeg, dasMin, dasSec)

#Below function computes Dasamsa longitude from lagna longitude
def hora_from_long(sign, pos_deg, pos_min, pos_sec):
    #sign as 1:Aries, 2:Taurus ... 12:Pisces
    #pos_x is position of planet in sign in degree minute and seconds
    #this function computes navamsha position in sign and degree minute and seconds format only in tuple
    longi_sec = (((sign - 1) * 30 * 3600) +
                (pos_deg * 3600) + (pos_min * 60) + pos_sec)
    amsa = (15 * 3600) #one hora amsa is 15 degree 
    horSign = 1 + int(longi_sec/amsa) % 12
    longi_pending_sec = (longi_sec % amsa)
    longi_pending_sec_normalized = ((longi_pending_sec*30*3600)/amsa)   #pending is for 3deg20min so normalized is for 30deg
    horDeg = int(longi_pending_sec_normalized / 3600)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 3600)
    horMin = int(longi_pending_sec_normalized / 60)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 60)
    horSec = round(longi_pending_sec_normalized,2)
    longi_hora_sec = (((horSign - 1) * 30 * 3600) +
                (horDeg * 3600) + (horMin * 60) + horSec)
    return(longi_hora_sec, horSign, horDeg, horMin, horSec)

#Below function computes Drekkana longitude from lagna longitude
def Drekkana_from_long(sign, pos_deg, pos_min, pos_sec):
    #sign as 1:Aries, 2:Taurus ... 12:Pisces
    #pos_x is position of planet in sign in degree minute and seconds
    #this function computes Drekkana position in sign and degree minute and seconds format only in tuple
    longi_sec = ((pos_deg * 3600) + (pos_min * 60) + pos_sec)
    amsa = (10 * 3600) #one Drekkana amsa is 10 degree 
    drekkanaCompartment = 1 + int(longi_sec/amsa) 
    if(drekkanaCompartment == 1):  #even sign
        DrekkanaSign = gen.compute_nthsign(sign,1)
    elif(drekkanaCompartment == 2):  #even sign
        DrekkanaSign = gen.compute_nthsign(sign,5)
    else:
        DrekkanaSign = gen.compute_nthsign(sign,9)
    longi_pending_sec = (longi_sec % amsa)
    longi_pending_sec_normalized = ((longi_pending_sec*30*3600)/amsa)   #pending is for 10degree so normalized is for 30deg
    DrekkanaDeg = int(longi_pending_sec_normalized / 3600)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 3600)
    DrekkanaMin = int(longi_pending_sec_normalized / 60)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 60)
    DrekkanaSec = round(longi_pending_sec_normalized,2)
    longi_Drekkana_sec = (((DrekkanaSign - 1) * 30 * 3600) +
                (DrekkanaDeg * 3600) + (DrekkanaMin * 60) + DrekkanaSec)
    return(longi_Drekkana_sec, DrekkanaSign, DrekkanaDeg, DrekkanaMin, DrekkanaSec)

#Below function computes Chaturtamsa longitude from lagna longitude
def Chaturtamsa_from_long(sign, pos_deg, pos_min, pos_sec):
    #sign as 1:Aries, 2:Taurus ... 12:Pisces
    #pos_x is position of planet in sign in degree minute and seconds
    #this function computes Chaturtamsa position in sign and degree minute and seconds format only in tuple
    longi_sec = ((pos_deg * 3600) + (pos_min * 60) + pos_sec)
    amsa = (30 * 3600) / 4 #one Chaturtamsa amsa is 30degree/4 
    ChaturtamsaCompartment = 1 + int(longi_sec/amsa) 
    if(ChaturtamsaCompartment == 1):  #even sign
        ChaturtamsaSign = gen.compute_nthsign(sign,1)
    elif(ChaturtamsaCompartment == 2):  #even sign
        ChaturtamsaSign = gen.compute_nthsign(sign,4)
    elif(ChaturtamsaCompartment == 3):  #even sign
        ChaturtamsaSign = gen.compute_nthsign(sign,7)
    else:
        ChaturtamsaSign = gen.compute_nthsign(sign,10)
    longi_pending_sec = (longi_sec % amsa)
    longi_pending_sec_normalized = ((longi_pending_sec*30*3600)/amsa)   #pending is for 10degree so normalized is for 30deg
    ChaturtamsaDeg = int(longi_pending_sec_normalized / 3600)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 3600)
    ChaturtamsaMin = int(longi_pending_sec_normalized / 60)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 60)
    ChaturtamsaSec = round(longi_pending_sec_normalized,2)
    longi_Chaturtamsa_sec = (((ChaturtamsaSign - 1) * 30 * 3600) +
                (ChaturtamsaDeg * 3600) + (ChaturtamsaMin * 60) + ChaturtamsaSec)
    return(longi_Chaturtamsa_sec, ChaturtamsaSign, ChaturtamsaDeg, ChaturtamsaMin, ChaturtamsaSec)

#Below function computes Saptamsa longitude from lagna longitude
def Saptamsa_from_long(sign, pos_deg, pos_min, pos_sec):
    #sign as 1:Aries, 2:Taurus ... 12:Pisces
    #pos_x is position of planet in sign in degree minute and seconds
    #this function computes Saptamsa position in sign and degree minute and seconds format only in tuple
    longi_sec = ((pos_deg * 3600) + (pos_min * 60) + pos_sec)
    amsa = (30 * 3600) / 7 #one Saptamsa amsa is 30degree/4 
    SaptamsaCompartment = 1 + int(longi_sec/amsa) 
    if(sign % 2 == 1):  #odd sign
        SaptamsaSign = gen.compute_nthsign(sign,SaptamsaCompartment)
    else:   #odd sign
        SaptamsaSign = gen.compute_nthsign(sign,SaptamsaCompartment + 6)
    longi_pending_sec = (longi_sec % amsa)
    longi_pending_sec_normalized = ((longi_pending_sec*30*3600)/amsa)   #pending is for 10degree so normalized is for 30deg
    SaptamsaDeg = int(longi_pending_sec_normalized / 3600)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 3600)
    SaptamsaMin = int(longi_pending_sec_normalized / 60)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 60)
    SaptamsaSec = round(longi_pending_sec_normalized,2)
    longi_Saptamsa_sec = (((SaptamsaSign - 1) * 30 * 3600) +
                (SaptamsaDeg * 3600) + (SaptamsaMin * 60) + SaptamsaSec)
    return(longi_Saptamsa_sec, SaptamsaSign, SaptamsaDeg, SaptamsaMin, SaptamsaSec)

#Below function computes Dwadasamsa longitude from lagna longitude
def Dwadasamsa_from_long(sign, pos_deg, pos_min, pos_sec):
    #sign as 1:Aries, 2:Taurus ... 12:Pisces
    #pos_x is position of planet in sign in degree minute and seconds
    #this function computes Dwadasamsa position in sign and degree minute and seconds format only in tuple
    longi_sec = ((pos_deg * 3600) + (pos_min * 60) + pos_sec)
    amsa = (30 * 3600) / 12 #one Dwadasamsa amsa is 30degree/12 
    DwadasamsaCompartment = 1 + int(longi_sec/amsa) % 12   
    DwadasamsaSign = gen.compute_nthsign(sign,DwadasamsaCompartment)
    
    longi_pending_sec = (longi_sec % amsa)
    longi_pending_sec_normalized = ((longi_pending_sec*30*3600)/amsa)   #pending is for 10degree so normalized is for 30deg
    DwadasamsaDeg = int(longi_pending_sec_normalized / 3600)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 3600)
    DwadasamsaMin = int(longi_pending_sec_normalized / 60)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 60)
    DwadasamsaSec = round(longi_pending_sec_normalized,2)
    longi_Dwadasamsa_sec = (((DwadasamsaSign - 1) * 30 * 3600) +
                (DwadasamsaDeg * 3600) + (DwadasamsaMin * 60) + DwadasamsaSec)
    return(longi_Dwadasamsa_sec, DwadasamsaSign, DwadasamsaDeg, DwadasamsaMin, DwadasamsaSec)

#Below function computes Shodasamsa longitude from lagna longitude
def Shodasamsa_from_long(sign, pos_deg, pos_min, pos_sec):
    #sign as 1:Aries, 2:Taurus ... 12:Pisces
    #pos_x is position of planet in sign in degree minute and seconds
    #this function computes Shodasamsa position in sign and degree minute and seconds format only in tuple
    longi_sec = ((pos_deg * 3600) + (pos_min * 60) + pos_sec)
    amsa = (30 * 3600) / 16 #one Shodasamsa amsa is 30degree/16
    ShodasamsaCompartment = 1 + int(longi_sec/amsa) 
    if(sign in [1,4,7,10]):  #Movable sign
        ShodasamsaSign = gen.compute_nthsign(1,ShodasamsaCompartment)
    elif(sign in [2,5,8,11]):  #Fixed sign
        ShodasamsaSign = gen.compute_nthsign(5,ShodasamsaCompartment)
    else:   #Dual sign
        ShodasamsaSign = gen.compute_nthsign(9,ShodasamsaCompartment)
    longi_pending_sec = (longi_sec % amsa)
    longi_pending_sec_normalized = ((longi_pending_sec*30*3600)/amsa)   #pending is for 10degree so normalized is for 30deg
    ShodasamsaDeg = int(longi_pending_sec_normalized / 3600)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 3600)
    ShodasamsaMin = int(longi_pending_sec_normalized / 60)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 60)
    ShodasamsaSec = round(longi_pending_sec_normalized,2)
    longi_Shodasamsa_sec = (((ShodasamsaSign - 1) * 30 * 3600) +
                (ShodasamsaDeg * 3600) + (ShodasamsaMin * 60) + ShodasamsaSec)
    return(longi_Shodasamsa_sec, ShodasamsaSign, ShodasamsaDeg, ShodasamsaMin, ShodasamsaSec)

#Below function computes Vimsamsa longitude from lagna longitude
def Vimsamsa_from_long(sign, pos_deg, pos_min, pos_sec):
    #sign as 1:Aries, 2:Taurus ... 12:Pisces
    #pos_x is position of planet in sign in degree minute and seconds
    #this function computes Vimsamsa position in sign and degree minute and seconds format only in tuple
    longi_sec = ((pos_deg * 3600) + (pos_min * 60) + pos_sec)
    amsa = (30 * 3600) / 20 #one Vimsamsa amsa is 30degree/30
    VimsamsaCompartment = 1 + int(longi_sec/amsa) 
    if(sign in [1,4,7,10]):  #Movable sign
        VimsamsaSign = gen.compute_nthsign(1,VimsamsaCompartment)
    elif(sign in [2,5,8,11]):  #Fixed sign
        VimsamsaSign = gen.compute_nthsign(9,VimsamsaCompartment)
    else:   #Dual sign
        VimsamsaSign = gen.compute_nthsign(5,VimsamsaCompartment)
    longi_pending_sec = (longi_sec % amsa)
    longi_pending_sec_normalized = ((longi_pending_sec*30*3600)/amsa)   #pending is for 10degree so normalized is for 30deg
    VimsamsaDeg = int(longi_pending_sec_normalized / 3600)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 3600)
    VimsamsaMin = int(longi_pending_sec_normalized / 60)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 60)
    VimsamsaSec = round(longi_pending_sec_normalized,2)
    longi_Vimsamsa_sec = (((VimsamsaSign - 1) * 30 * 3600) +
                (VimsamsaDeg * 3600) + (VimsamsaMin * 60) + VimsamsaSec)
    return(longi_Vimsamsa_sec, VimsamsaSign, VimsamsaDeg, VimsamsaMin, VimsamsaSec)

#Below function computes ChaturVimsamsa longitude from lagna longitude
def ChaturVimsamsa_from_long(sign, pos_deg, pos_min, pos_sec):
    #sign as 1:Aries, 2:Taurus ... 12:Pisces
    #pos_x is position of planet in sign in degree minute and seconds
    #this function computes ChaturVimsamsa position in sign and degree minute and seconds format only in tuple
    longi_sec = ((pos_deg * 3600) + (pos_min * 60) + pos_sec)
    amsa = (30 * 3600) / 24 #one ChaturVimsamsa amsa is 30degree/24
    ChaturVimsamsaCompartment = 1 + int(longi_sec/amsa) 
    if(sign % 2 == 0):  #Even sign
        ChaturVimsamsaSign = gen.compute_nthsign(4,ChaturVimsamsaCompartment)
    else:   #Odd sign
        ChaturVimsamsaSign = gen.compute_nthsign(5,ChaturVimsamsaCompartment)
    longi_pending_sec = (longi_sec % amsa)
    longi_pending_sec_normalized = ((longi_pending_sec*30*3600)/amsa)   #pending is for 10degree so normalized is for 30deg
    ChaturVimsamsaDeg = int(longi_pending_sec_normalized / 3600)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 3600)
    ChaturVimsamsaMin = int(longi_pending_sec_normalized / 60)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 60)
    ChaturVimsamsaSec = round(longi_pending_sec_normalized,2)
    longi_ChaturVimsamsa_sec = (((ChaturVimsamsaSign - 1) * 30 * 3600) +
                (ChaturVimsamsaDeg * 3600) + (ChaturVimsamsaMin * 60) + ChaturVimsamsaSec)
    return(longi_ChaturVimsamsa_sec, ChaturVimsamsaSign, ChaturVimsamsaDeg, ChaturVimsamsaMin, ChaturVimsamsaSec)

#Below function computes SaptaVimsamsa longitude from lagna longitude
def SaptaVimsamsa_from_long(sign, pos_deg, pos_min, pos_sec):
    #sign as 1:Aries, 2:Taurus ... 12:Pisces
    #pos_x is position of planet in sign in degree minute and seconds
    #this function computes SaptaVimsamsa position in sign and degree minute and seconds format only in tuple
    longi_sec = ((pos_deg * 3600) + (pos_min * 60) + pos_sec)
    amsa = (30 * 3600) / 27 #one SaptaVimsamsa amsa is 30degree/27
    SaptaVimsamsaCompartment = 1 + int(longi_sec/amsa) 
    if(sign in [1,5,9]):  #Fiery sign
        SaptaVimsamsaSign = gen.compute_nthsign(1,SaptaVimsamsaCompartment)
    elif(sign in [2,6,10]):  #Earthy sign
        SaptaVimsamsaSign = gen.compute_nthsign(4,SaptaVimsamsaCompartment)
    elif(sign in [3,7,11]):  #Airy sign
        SaptaVimsamsaSign = gen.compute_nthsign(7,SaptaVimsamsaCompartment)
    else:   #Watery sign
        SaptaVimsamsaSign = gen.compute_nthsign(10,SaptaVimsamsaCompartment)

    longi_pending_sec = (longi_sec % amsa)
    longi_pending_sec_normalized = ((longi_pending_sec*30*3600)/amsa)   #pending is for 10degree so normalized is for 30deg
    SaptaVimsamsaDeg = int(longi_pending_sec_normalized / 3600)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 3600)
    SaptaVimsamsaMin = int(longi_pending_sec_normalized / 60)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 60)
    SaptaVimsamsaSec = round(longi_pending_sec_normalized,2)
    longi_SaptaVimsamsa_sec = (((SaptaVimsamsaSign - 1) * 30 * 3600) +
                (SaptaVimsamsaDeg * 3600) + (SaptaVimsamsaMin * 60) + SaptaVimsamsaSec)
    return(longi_SaptaVimsamsa_sec, SaptaVimsamsaSign, SaptaVimsamsaDeg, SaptaVimsamsaMin, SaptaVimsamsaSec)

#Below function computes Trimsamsa longitude from lagna longitude
def Trimsamsa_from_long(sign, pos_deg, pos_min, pos_sec):
    #sign as 1:Aries, 2:Taurus ... 12:Pisces
    #pos_x is position of planet in sign in degree minute and seconds
    #this function computes Trimsamsa position in sign and degree minute and seconds format only in tuple
    longi_sec = ((pos_deg * 3600) + (pos_min * 60) + pos_sec)
    amsa = (30 * 3600) / 30 #one Trimsamsa amsa is 30degree/30
    #TrimsamsaCompartment = 1 + int(longi_sec/amsa) 
    if(sign % 2 == 0):  #Even Lagna in Rasi chart
        if(longi_sec <= 5 * 3600):
            TrimsamsaSign = 2
        elif(longi_sec <= 12 * 3600):
            TrimsamsaSign = 6
        elif(longi_sec <= 20 * 3600):
            TrimsamsaSign = 12
        elif(longi_sec <= 25 * 3600):
            TrimsamsaSign = 10
        else:
            TrimsamsaSign = 8
    else:   #Odd Lagna in Rasi chart
        if(longi_sec <= 5 * 3600):
            TrimsamsaSign = 1
        elif(longi_sec <= 10 * 3600):
            TrimsamsaSign = 11
        elif(longi_sec <= 18 * 3600):
            TrimsamsaSign = 9
        elif(longi_sec <= 25 * 3600):
            TrimsamsaSign = 3
        else:
            TrimsamsaSign = 7

    longi_pending_sec = (longi_sec % amsa)
    longi_pending_sec_normalized = ((longi_pending_sec*30*3600)/amsa)   #pending is for 10degree so normalized is for 30deg
    TrimsamsaDeg = int(longi_pending_sec_normalized / 3600)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 3600)
    TrimsamsaMin = int(longi_pending_sec_normalized / 60)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 60)
    TrimsamsaSec = round(longi_pending_sec_normalized,2)
    longi_Trimsamsa_sec = (((TrimsamsaSign - 1) * 30 * 3600) +
                (TrimsamsaDeg * 3600) + (TrimsamsaMin * 60) + TrimsamsaSec)
    return(longi_Trimsamsa_sec, TrimsamsaSign, TrimsamsaDeg, TrimsamsaMin, TrimsamsaSec)

#Below function computes Khavedamsa longitude from lagna longitude
def Khavedamsa_from_long(sign, pos_deg, pos_min, pos_sec):
    #sign as 1:Aries, 2:Taurus ... 12:Pisces
    #pos_x is position of planet in sign in degree minute and seconds
    #this function computes Khavedamsa position in sign and degree minute and seconds format only in tuple
    longi_sec = ((pos_deg * 3600) + (pos_min * 60) + pos_sec)
    amsa = (30 * 3600) / 40 #one Khavedamsa amsa is 30degree/40
    KhavedamsaCompartment = 1 + int(longi_sec/amsa) 
    if(sign % 2 == 0):  #Even sign
        KhavedamsaSign = gen.compute_nthsign(7,KhavedamsaCompartment)
    else:   #Odd sign
        KhavedamsaSign = gen.compute_nthsign(1,KhavedamsaCompartment)
    longi_pending_sec = (longi_sec % amsa)
    longi_pending_sec_normalized = ((longi_pending_sec*30*3600)/amsa)   #pending is for 10degree so normalized is for 30deg
    KhavedamsaDeg = int(longi_pending_sec_normalized / 3600)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 3600)
    KhavedamsaMin = int(longi_pending_sec_normalized / 60)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 60)
    KhavedamsaSec = round(longi_pending_sec_normalized,2)
    longi_Khavedamsa_sec = (((KhavedamsaSign - 1) * 30 * 3600) +
                (KhavedamsaDeg * 3600) + (KhavedamsaMin * 60) + KhavedamsaSec)
    return(longi_Khavedamsa_sec, KhavedamsaSign, KhavedamsaDeg, KhavedamsaMin, KhavedamsaSec)

#Below function computes Akshavedamsa longitude from lagna longitude
def Akshavedamsa_from_long(sign, pos_deg, pos_min, pos_sec):
    #sign as 1:Aries, 2:Taurus ... 12:Pisces
    #pos_x is position of planet in sign in degree minute and seconds
    #this function computes Akshavedamsa position in sign and degree minute and seconds format only in tuple
    longi_sec = ((pos_deg * 3600) + (pos_min * 60) + pos_sec)
    amsa = (30 * 3600) / 45 #one Akshavedamsa amsa is 30degree/45
    AkshavedamsaCompartment = 1 + int(longi_sec/amsa) 
    if(sign in [1,4,7,10]):  #Movable sign
        AkshavedamsaSign = gen.compute_nthsign(1,AkshavedamsaCompartment)
    elif(sign in [2,5,8,11]):  #Fixed sign
        AkshavedamsaSign = gen.compute_nthsign(5,AkshavedamsaCompartment)
    else:   #Dual sign
        AkshavedamsaSign = gen.compute_nthsign(9,AkshavedamsaCompartment)
    longi_pending_sec = (longi_sec % amsa)
    longi_pending_sec_normalized = ((longi_pending_sec*30*3600)/amsa)   #pending is for 10degree so normalized is for 30deg
    AkshavedamsaDeg = int(longi_pending_sec_normalized / 3600)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 3600)
    AkshavedamsaMin = int(longi_pending_sec_normalized / 60)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 60)
    AkshavedamsaSec = round(longi_pending_sec_normalized,2)
    longi_Akshavedamsa_sec = (((AkshavedamsaSign - 1) * 30 * 3600) +
                (AkshavedamsaDeg * 3600) + (AkshavedamsaMin * 60) + AkshavedamsaSec)
    return(longi_Akshavedamsa_sec, AkshavedamsaSign, AkshavedamsaDeg, AkshavedamsaMin, AkshavedamsaSec)

#Below function computes Shashtiamsa longitude from lagna longitude
def Shashtiamsa_from_long(sign, pos_deg, pos_min, pos_sec):
    #sign as 1:Aries, 2:Taurus ... 12:Pisces
    #pos_x is position of planet in sign in degree minute and seconds
    #this function computes Shashtiamsa position in sign and degree minute and seconds format only in tuple
    longi_sec = ((pos_deg * 3600) + (pos_min * 60) + pos_sec)
    amsa = (30 * 3600) / 60 #one Shashtiamsa amsa is 30degree/60 
    ShashtiamsaCompartment = 1 + int(longi_sec/amsa) % 12   
    ShashtiamsaSign = gen.compute_nthsign(sign,ShashtiamsaCompartment)
    
    longi_pending_sec = (longi_sec % amsa)
    longi_pending_sec_normalized = ((longi_pending_sec*30*3600)/amsa)   #pending is for 10degree so normalized is for 30deg
    ShashtiamsaDeg = int(longi_pending_sec_normalized / 3600)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 3600)
    ShashtiamsaMin = int(longi_pending_sec_normalized / 60)
    longi_pending_sec_normalized = (longi_pending_sec_normalized % 60)
    ShashtiamsaSec = round(longi_pending_sec_normalized,2)
    longi_Shashtiamsa_sec = (((ShashtiamsaSign - 1) * 30 * 3600) +
                (ShashtiamsaDeg * 3600) + (ShashtiamsaMin * 60) + ShashtiamsaSec)
    return(longi_Shashtiamsa_sec, ShashtiamsaSign, ShashtiamsaDeg, ShashtiamsaMin, ShashtiamsaSec)

def prepDivisionalchartElements(division):
    #prepare Ascendant
    division["ascendant"] = {   "name"        : "Ascendant",
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
                                }.copy()
    division["planets"] = {}
    division["vargottamas"] = []    #only for non D1 divisional charts
    division["houses"] = []
    division["classifications"] = { "benefics"    : [],
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
    division["planets"]["Sun"] = {  "name"         : "Sun",
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
                                    }.copy()
    division["planets"]["Moon"] = {"name"         : "Moon",
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
            }.copy()
    division["planets"]["Mars"] = {"name"        : "Mars",
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
            }.copy()
    division["planets"]["Mercury"] = {"name"     : "Mercury",
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
            }.copy()
    division["planets"]["Jupiter"] = {"name"     : "Jupiter",
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
            }.copy()
    division["planets"]["Venus"] = {"name"       : "Venus",
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
            }.copy()
    division["planets"]["Saturn"] = {"name"      : "Saturn",
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
            }.copy()
    division["planets"]["Rahu"] = {"name"        : "Rahu",
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
            }.copy()
    division["planets"]["Ketu"] = {"name"        : "Ketu",
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
            }.copy()
    return

#Takes charts as input. For ascendant and all 9 planets, computes Divisional chart.
#input D1 of Charts and updates DX of charts - All the fields (x can be any division like 9 for navamsa, 10 for dasamsa etc)
def compute_Dx_4m_D1(charts, Dx):
    l_D1 = charts["D1"]
    l_Dx = charts[Dx]
    prepDivisionalchartElements(l_Dx)
    
    #for computing Navamsa Lagna
    #Gather inputs
    D1lagnaSign = (gen.signnum(l_D1["ascendant"]["sign"]))
    D1lagnaPosDeg = (l_D1["ascendant"]["pos"]["deg"])
    D1lagnaPosMin = (l_D1["ascendant"]["pos"]["min"])
    D1lagnaPosSec = (l_D1["ascendant"]["pos"]["sec"])
    #compute Navamsa of Ascendant
    if(Dx == "D9"):
        (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = navamsa_from_long(D1lagnaSign, D1lagnaPosDeg, D1lagnaPosMin, D1lagnaPosSec)
    elif(Dx == "D10"):
        (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = dasamsa_from_long(D1lagnaSign, D1lagnaPosDeg, D1lagnaPosMin, D1lagnaPosSec)
    elif(Dx == "D2"):
        (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = hora_from_long(D1lagnaSign, D1lagnaPosDeg, D1lagnaPosMin, D1lagnaPosSec)
    elif(Dx == "D3"):
        (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = Drekkana_from_long(D1lagnaSign, D1lagnaPosDeg, D1lagnaPosMin, D1lagnaPosSec)
    elif(Dx == "D4"):
        (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = Chaturtamsa_from_long(D1lagnaSign, D1lagnaPosDeg, D1lagnaPosMin, D1lagnaPosSec)
    elif(Dx == "D7"):
        (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = Saptamsa_from_long(D1lagnaSign, D1lagnaPosDeg, D1lagnaPosMin, D1lagnaPosSec)
    elif(Dx == "D12"):
        (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = Dwadasamsa_from_long(D1lagnaSign, D1lagnaPosDeg, D1lagnaPosMin, D1lagnaPosSec)
    elif(Dx == "D16"):
        (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = Shodasamsa_from_long(D1lagnaSign, D1lagnaPosDeg, D1lagnaPosMin, D1lagnaPosSec)
    elif(Dx == "D20"):
        (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = Vimsamsa_from_long(D1lagnaSign, D1lagnaPosDeg, D1lagnaPosMin, D1lagnaPosSec)
    elif(Dx == "D24"):
        (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = ChaturVimsamsa_from_long(D1lagnaSign, D1lagnaPosDeg, D1lagnaPosMin, D1lagnaPosSec)
    elif(Dx == "D27"):
        (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = SaptaVimsamsa_from_long(D1lagnaSign, D1lagnaPosDeg, D1lagnaPosMin, D1lagnaPosSec)
    elif(Dx == "D30"):
        (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = Trimsamsa_from_long(D1lagnaSign, D1lagnaPosDeg, D1lagnaPosMin, D1lagnaPosSec)
    elif(Dx == "D40"):
        (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = Khavedamsa_from_long(D1lagnaSign, D1lagnaPosDeg, D1lagnaPosMin, D1lagnaPosSec)
    elif(Dx == "D45"):
        (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = Akshavedamsa_from_long(D1lagnaSign, D1lagnaPosDeg, D1lagnaPosMin, D1lagnaPosSec)
    elif(Dx == "D60"):
        (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = Shashtiamsa_from_long(D1lagnaSign, D1lagnaPosDeg, D1lagnaPosMin, D1lagnaPosSec)
    else:
        div_fullLongi_sec = (((D1lagnaSign - 1) * 30 * 3600) +
                (D1lagnaPosDeg * 3600) + (D1lagnaPosMin * 60) + D1lagnaPosSec)
        (divSign, divDeg, divMin, divSec) = (D1lagnaSign, D1lagnaPosDeg, D1lagnaPosMin, D1lagnaPosSec)

    lagna = divSign
    #update Navamsa lagna in charts
    l_Dx["ascendant"]["sign"] = gen.signs[divSign-1]
    l_Dx["ascendant"]["pos"]["deg"] = divDeg
    l_Dx["ascendant"]["pos"]["min"] = divMin
    l_Dx["ascendant"]["pos"]["sec"] = divSec
    l_Dx["ascendant"]["pos"]["dec_deg"] = ((divDeg*3600) + (divMin*60) + divSec)/3600
    l_Dx["ascendant"]["rashi"]      = gen.rashis[divSign-1]
    l_Dx["ascendant"]["lagna-lord"] = gen.signlords[divSign-1]
    l_Dx["ascendant"]["sign-tatva"] = gen.signtatvas[divSign-1]

    #update nakshatra related data for ascendant
    nak_pad = nakshatra_pada(div_fullLongi_sec / 3600)  #argument must be full longitude in degrees
    l_Dx["ascendant"]["nakshatra"] = nak_pad[0]
    l_Dx["ascendant"]["pada"] = nak_pad[1]
    l_Dx["ascendant"]["nak-ruler"] = gen.ruler_of_nakshatra[nak_pad[0]]
    l_Dx["ascendant"]["nak-diety"] = gen.diety_of_nakshatra[nak_pad[0]]

    #update for every planet
    for planetname in l_Dx["planets"]:
        #Gather inputs
        D1PlanetSign = (gen.signnum(l_D1["planets"][planetname]["sign"]))
        D1PlanetPosDeg = (l_D1["planets"][planetname]["pos"]["deg"])
        D1PlanetPosMin = (l_D1["planets"][planetname]["pos"]["min"])
        D1PlanetPosSec = (l_D1["planets"][planetname]["pos"]["sec"])
        #compute Navamsa of Ascendant
        #(div_fullLongi_sec, divSign, divDeg, divMin, divSec) = navamsa_from_long(D1PlanetSign, D1PlanetPosDeg, D1PlanetPosMin, D1PlanetPosSec)
        if(Dx == "D9"):
            (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = navamsa_from_long(D1PlanetSign, D1PlanetPosDeg, D1PlanetPosMin, D1PlanetPosSec)
        elif(Dx == "D10"):
            (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = dasamsa_from_long(D1PlanetSign, D1PlanetPosDeg, D1PlanetPosMin, D1PlanetPosSec)
        elif(Dx == "D2"):
            (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = hora_from_long(D1PlanetSign, D1PlanetPosDeg, D1PlanetPosMin, D1PlanetPosSec)
        elif(Dx == "D3"):
            (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = Drekkana_from_long(D1PlanetSign, D1PlanetPosDeg, D1PlanetPosMin, D1PlanetPosSec)
        elif(Dx == "D4"):
            (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = Chaturtamsa_from_long(D1PlanetSign, D1PlanetPosDeg, D1PlanetPosMin, D1PlanetPosSec)
        elif(Dx == "D7"):
            (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = Saptamsa_from_long(D1PlanetSign, D1PlanetPosDeg, D1PlanetPosMin, D1PlanetPosSec)
        elif(Dx == "D12"):
            (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = Dwadasamsa_from_long(D1PlanetSign, D1PlanetPosDeg, D1PlanetPosMin, D1PlanetPosSec)
        elif(Dx == "D16"):
            (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = Shodasamsa_from_long(D1PlanetSign, D1PlanetPosDeg, D1PlanetPosMin, D1PlanetPosSec)
        elif(Dx == "D20"):
            (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = Vimsamsa_from_long(D1PlanetSign, D1PlanetPosDeg, D1PlanetPosMin, D1PlanetPosSec)
        elif(Dx == "D24"):
            (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = ChaturVimsamsa_from_long(D1PlanetSign, D1PlanetPosDeg, D1PlanetPosMin, D1PlanetPosSec)
        elif(Dx == "D27"):
            (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = SaptaVimsamsa_from_long(D1PlanetSign, D1PlanetPosDeg, D1PlanetPosMin, D1PlanetPosSec)
        elif(Dx == "D30"):
            (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = Trimsamsa_from_long(D1PlanetSign, D1PlanetPosDeg, D1PlanetPosMin, D1PlanetPosSec)
        elif(Dx == "D40"):
            (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = Khavedamsa_from_long(D1PlanetSign, D1PlanetPosDeg, D1PlanetPosMin, D1PlanetPosSec)
        elif(Dx == "D45"):
            (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = Akshavedamsa_from_long(D1PlanetSign, D1PlanetPosDeg, D1PlanetPosMin, D1PlanetPosSec)
        elif(Dx == "D60"):
            (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = Shashtiamsa_from_long(D1PlanetSign, D1PlanetPosDeg, D1PlanetPosMin, D1PlanetPosSec)
        else:
            div_fullLongi_sec = (((D1PlanetSign - 1) * 30 * 3600) +
                    (D1PlanetPosDeg * 3600) + (D1PlanetPosMin * 60) + D1PlanetPosSec)
            (divSign, divDeg, divMin, divSec) = (D1PlanetSign, D1PlanetPosDeg, D1PlanetPosMin, D1PlanetPosSec)

        #Updating the attributes
        if(D1PlanetSign == divSign):
            l_Dx["vargottamas"].append(planetname)

        l_Dx["planets"][planetname]["retro"] = l_D1["planets"][planetname]["retro"]
        currentsign = gen.signs[divSign-1]
        l_Dx["planets"][planetname]["sign"] = currentsign
        l_Dx["planets"][planetname]["pos"]["deg"] = divDeg
        l_Dx["planets"][planetname]["pos"]["min"] = divMin
        l_Dx["planets"][planetname]["pos"]["sec"] = divSec
        l_Dx["planets"][planetname]["pos"]["dec_deg"] = ((divDeg*3600) + (divMin*60) + divSec)/3600
        l_Dx["planets"][planetname]["rashi"]      = gen.rashis[divSign-1]
        l_Dx["planets"][planetname]["sign-tatva"] = gen.signtatvas[divSign-1]
        dispositor = gen.signlords[divSign-1]
        l_Dx["planets"][planetname]["dispositor"] = dispositor
        housenum = gen.housediff(lagna, divSign)
        l_Dx["planets"][planetname]["house-num"] = housenum
        if (housenum in [1,5,9]):
            l_Dx["planets"][planetname]["house-nature"] = c.DHARMA
        elif (housenum in [2,6,10]):
            l_Dx["planets"][planetname]["house-nature"] = c.ARTHA
        elif (housenum in [3,7,11]):
            l_Dx["planets"][planetname]["house-nature"] = c.KAMA
        else:
            l_Dx["planets"][planetname]["house-nature"] = c.MOKSHA
        #update nakshatra related data for ascendant
        nak_pad = nakshatra_pada(div_fullLongi_sec / 3600)  #argument must be full longitude in degrees
        l_Dx["planets"][planetname]["nakshatra"] = nak_pad[0]
        l_Dx["planets"][planetname]["pada"] = nak_pad[1]
        l_Dx["planets"][planetname]["nak-ruler"] = gen.ruler_of_nakshatra[nak_pad[0]]
        l_Dx["planets"][planetname]["nak-diety"] = gen.diety_of_nakshatra[nak_pad[0]]

        exhaltsign = gen.exhaltationSign_of_planet[planetname] 
        debilitsign = gen.debilitationSign_of_planet[planetname]
        friends = l_Dx["planets"][planetname]["friends"]
        enemies = l_Dx["planets"][planetname]["enemies"]
        neutral = l_Dx["planets"][planetname]["nuetral"]
        if(currentsign == exhaltsign):  #first check for exhaltation
            l_Dx["planets"][planetname]["house-rel"] = c.EXHALTED
        elif(currentsign == debilitsign): #next check for debilitated 
            l_Dx["planets"][planetname]["house-rel"] = c.DEBILITATED
        elif(planetname == dispositor): #next check for own sign 
            l_Dx["planets"][planetname]["house-rel"] = c.OWNSIGN
        elif(dispositor in friends): #next check for friend sign 
            l_Dx["planets"][planetname]["house-rel"] = c.FRIENDSIGN
        elif(dispositor in enemies): #next check for enemy sign 
            l_Dx["planets"][planetname]["house-rel"] = c.ENEMYSIGN
        elif(dispositor in neutral): #next check for neutral sign 
            l_Dx["planets"][planetname]["house-rel"] = c.NEUTRALSIGN
        else:
            l_Dx["planets"][planetname]["house-rel"] = "UNKNOWN"

    lagnesh = l_Dx["ascendant"]["lagna-lord"]  #get lagnesh
    l_Dx["ascendant"]["lagnesh-sign"]  = l_Dx["planets"][lagnesh]["sign"]  #check the sign of lagnesh
    l_Dx["ascendant"]["lagnesh-rashi"] = l_Dx["planets"][lagnesh]["rashi"] 
    l_Dx["ascendant"]["lagnesh-disp"]  = l_Dx["planets"][lagnesh]["dispositor"]
    
    #computing benefics, malefics and neutral planets for given lagna
    gen.compute_BenMalNeu4lagna(lagna,data.charts[Dx]["classifications"])

    gen.update_houses(data.charts[Dx])

    #computing aspects and conjunction planets
    gen.compute_aspects(data.charts[Dx])
    gen.compute_aspectedby(data.charts[Dx])  
    gen.compute_conjuncts(data.charts[Dx]) 

    #populating the classification part of divisional chart
    gen.populate_Natural_BeneficsMalefics(data.charts[Dx])  #Natural benefics and malefics
    gen.populate_kendraplanets(data.charts[Dx]) #kendra planets
    gen.populate_trikonaplanets(data.charts[Dx]) #trikona planets
    gen.populate_trikplanets(data.charts[Dx]) #trik planets
    gen.populate_upachayaplanets(data.charts[Dx]) #upachaya planets
    gen.populate_dharmaplanets(data.charts[Dx]) #dharma planets
    gen.populate_arthaplanets(data.charts[Dx]) #artha planets
    gen.populate_kamaplanets(data.charts[Dx]) #kama planets
    gen.populate_mokshaplanets(data.charts[Dx]) #moksha planets

    return



if __name__ == "__main__":
      print(f'Hora of Ketu is {Shodasamsa_from_long(3, 20, 33, 21.76)}')
