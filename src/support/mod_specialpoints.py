import support.mod_general as gen
import support.mod_lagna as lagna
import support.mod_divisional as div



def compute_sphuta(charts):
    AriesStartPoint = [ 1,0,0,0 ]
    
    #Beeja Sphuta (BS is for male and Kshetra Sphuta(KS) is for female
    if (charts["user_details"]["birthdetails"]["Gender"] == "male"):
        charts["special_points"]["sphuta"]["type"] = "Beeja"
        charts["special_points"]["sphuta"]["symbol"] = "BS"
        #computing Beeja Sphuta
        #step1 - get longitudes of Jupiter, Venus and Sun from starting of Aries
        longi_Jupiter = gen.get_point2planetdistance(charts["D1"],AriesStartPoint,"Jupiter")
        longi_Venus = gen.get_point2planetdistance(charts["D1"],AriesStartPoint,"Venus")
        longi_Sun = gen.get_point2planetdistance(charts["D1"],AriesStartPoint,"Sun")

        #step2 - add all 3 longitudes and see in which sign it falls in
        longi_sum_sec = longi_Jupiter + longi_Venus + longi_Sun

    else:
        charts["special_points"]["sphuta"]["type"] = "Kshetra"
        charts["special_points"]["sphuta"]["symbol"] = "KS"
        #computing Kshetra Sphuta
        #step1 - get longitudes of Jupiter, Mars and Moon from starting of Aries
        longi_Jupiter = gen.get_point2planetdistance(charts["D1"],AriesStartPoint,"Jupiter")
        longi_Mars = gen.get_point2planetdistance(charts["D1"],AriesStartPoint,"Mars")
        longi_Moon = gen.get_point2planetdistance(charts["D1"],AriesStartPoint,"Moon")

        #step2 - add all 3 longitudes and see in which sign it falls in
        longi_sum_sec = longi_Jupiter + longi_Mars + longi_Moon

    longi_sum_sec_significant = longi_sum_sec % (360*3600)
    amsa = (30 * 3600)  #one amsa is 30 degree
    sphutaSign = 1 + int(longi_sum_sec_significant/amsa) % 12
    longi_pending_sec = (longi_sum_sec_significant % amsa)
    sphutaDeg = int(longi_pending_sec / 3600)
    sphutaDegDec = (longi_pending_sec / 3600)
    longi_pending_sec = (longi_pending_sec % 3600)
    sphutaMin = int(longi_pending_sec / 60)
    longi_pending_sec = (longi_pending_sec % 60)
    sphutaSec = round(longi_pending_sec,2)

    #update details for D1
    charts["special_points"]["sphuta"]["D1"]["sign"] = gen.signs[sphutaSign - 1]
    charts["special_points"]["sphuta"]["D1"]["pos"]["deg"] = sphutaDeg
    charts["special_points"]["sphuta"]["D1"]["pos"]["min"] = sphutaMin
    charts["special_points"]["sphuta"]["D1"]["pos"]["sec"] = sphutaSec
    charts["special_points"]["sphuta"]["D1"]["pos"]["dec_deg"] = round(sphutaDegDec,3)
    
    # sign lord
    charts["special_points"]["sphuta"]["D1"]["signlord"]  = gen.signlords[sphutaSign - 1]

    #update nakshatra related data for sphuta
    nak_pad = lagna.nakshatra_pada(longi_sum_sec_significant / 3600)
    charts["special_points"]["sphuta"]["D1"]["nakshatra"] = nak_pad[0]
    charts["special_points"]["sphuta"]["D1"]["pada"] = nak_pad[1]
    charts["special_points"]["sphuta"]["D1"]["nak-ruler"] = gen.ruler_of_nakshatra[nak_pad[0]]
    
    #House number
    lagnasignnum = gen.signnum(charts["D1"]["ascendant"]["sign"])
    charts["special_points"]["sphuta"]["D1"]["house-num"] = gen.housediff(lagnasignnum, sphutaSign)

    #Update details for D3
    (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = div.Drekkana_from_long(sphutaSign , sphutaDeg, sphutaMin, sphutaSec)
    currentsign = gen.signs[divSign-1]
    charts["special_points"]["sphuta"]["D3"]["sign"] = currentsign
    charts["special_points"]["sphuta"]["D3"]["pos"]["deg"] = divDeg
    charts["special_points"]["sphuta"]["D3"]["pos"]["min"] = divMin
    charts["special_points"]["sphuta"]["D3"]["pos"]["sec"] = divSec
    charts["special_points"]["sphuta"]["D3"]["pos"]["dec_deg"] = ((divDeg*3600) + (divMin*60) + divSec)/3600

    nak_pad = lagna.nakshatra_pada(div_fullLongi_sec / 3600)  #argument must be full longitude in degrees
    charts["special_points"]["sphuta"]["D3"]["nakshatra"] = nak_pad[0]
    charts["special_points"]["sphuta"]["D3"]["pada"] = nak_pad[1]
    charts["special_points"]["sphuta"]["D3"]["nak-ruler"] = gen.ruler_of_nakshatra[nak_pad[0]]

    lagnasignnum = gen.signnum(charts["D3"]["ascendant"]["sign"])
    charts["special_points"]["sphuta"]["D3"]["house-num"] = gen.housediff(lagnasignnum, divSign)

    #Update details for D7
    (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = div.Saptamsa_from_long(sphutaSign , sphutaDeg, sphutaMin, sphutaSec)
    currentsign = gen.signs[divSign-1]
    charts["special_points"]["sphuta"]["D7"]["sign"] = currentsign
    charts["special_points"]["sphuta"]["D7"]["pos"]["deg"] = divDeg
    charts["special_points"]["sphuta"]["D7"]["pos"]["min"] = divMin
    charts["special_points"]["sphuta"]["D7"]["pos"]["sec"] = divSec
    charts["special_points"]["sphuta"]["D7"]["pos"]["dec_deg"] = ((divDeg*3600) + (divMin*60) + divSec)/3600

    nak_pad = lagna.nakshatra_pada(div_fullLongi_sec / 3600)  #argument must be full longitude in degrees
    charts["special_points"]["sphuta"]["D7"]["nakshatra"] = nak_pad[0]
    charts["special_points"]["sphuta"]["D7"]["pada"] = nak_pad[1]
    charts["special_points"]["sphuta"]["D7"]["nak-ruler"] = gen.ruler_of_nakshatra[nak_pad[0]]

    lagnasignnum = gen.signnum(charts["D7"]["ascendant"]["sign"])
    charts["special_points"]["sphuta"]["D7"]["house-num"] = gen.housediff(lagnasignnum, divSign)

    #Update details for D9
    (div_fullLongi_sec, divSign, divDeg, divMin, divSec) = div.navamsa_from_long(sphutaSign , sphutaDeg, sphutaMin, sphutaSec)
    currentsign = gen.signs[divSign-1]
    charts["special_points"]["sphuta"]["D9"]["sign"] = currentsign
    charts["special_points"]["sphuta"]["D9"]["pos"]["deg"] = divDeg
    charts["special_points"]["sphuta"]["D9"]["pos"]["min"] = divMin
    charts["special_points"]["sphuta"]["D9"]["pos"]["sec"] = divSec
    charts["special_points"]["sphuta"]["D9"]["pos"]["dec_deg"] = ((divDeg*3600) + (divMin*60) + divSec)/3600

    nak_pad = lagna.nakshatra_pada(div_fullLongi_sec / 3600)  #argument must be full longitude in degrees
    charts["special_points"]["sphuta"]["D9"]["nakshatra"] = nak_pad[0]
    charts["special_points"]["sphuta"]["D9"]["pada"] = nak_pad[1]
    charts["special_points"]["sphuta"]["D9"]["nak-ruler"] = gen.ruler_of_nakshatra[nak_pad[0]]

    lagnasignnum = gen.signnum(charts["D9"]["ascendant"]["sign"])
    charts["special_points"]["sphuta"]["D9"]["house-num"] = gen.housediff(lagnasignnum, divSign)

    return

         
