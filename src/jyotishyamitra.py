######################################################################
######################### Module imports #############################
######################################################################
from input.birthdata import birthdata,birthdatastr
import support.mod_astrodata as data
import support.mod_json as js
import support.mod_lagna as lagna
import support.dashas as dashas
import support.mod_divisional as varga
import support.mod_bala as bala
import support.mod_ashtakavarga as ashtaka
import support.mod_specialpoints as sp
import os


######################################################################
############################# Constants  #############################
######################################################################

#Month constants
January = "1"
February = "2"
March = "3"
April = "4"
May = "5"
June = "6"
July = "7"
August = "8"
September = "9"
October = "10"
November = "11"
December = "12"

######################################################################
######################### Global Variables  ##########################
######################################################################

is_InputBirthdata_Validated = False
is_OutputPathSet = False

outputpath = ""
outputfilename = ""
outputfilenamefull = ""


######################################################################
######################## General Functions  ##########################
######################################################################

#if the striong is not a float then returns False. else returns the string as float number
def isfloat(num):
    try:
        float(num)
        return float(num)
    except ValueError:
        return False
    

######################################################################
################ Functions related to input ##########################
######################################################################

def input_birthdata(name = "", gender = "", place = "", longitude = "", lattitude = "", timezone = "", year = "", month = "", day = "", hour = "", min = "", sec="0"):
    global is_InputBirthdata_Validated

    if (name != ""):
        birthdatastr["name"] = str(name)
    
    if (gender != ""):
        birthdatastr["Gender"] = str(gender)
    
    if (place != ""):
        birthdatastr["POB"]["name"] = str(place)

    if (timezone != ""):
        birthdatastr["POB"]["timezone"] = str(timezone)

    if (longitude != ""):
        birthdatastr["POB"]["lon"] = str(longitude)

    if (lattitude != ""):
        birthdatastr["POB"]["lat"] = str(lattitude)
    
    if (year != ""):
        birthdatastr["DOB"]["year"] = str(year)
    
    if (month != ""):
        birthdatastr["DOB"]["month"] = str(month)

    if (day != ""):
        birthdatastr["DOB"]["day"] = str(day)

    if (hour != ""):
        birthdatastr["TOB"]["hour"] = str(hour)

    if (min != ""):
        birthdatastr["TOB"]["min"] = str(min)

    if (sec != ""):
        birthdatastr["TOB"]["sec"] = str(sec)

    is_InputBirthdata_Validated = False

    return(birthdatastr.copy())   


#validate the birthdatastr contents are proper or not. If any error then report it. 
# If all fine then update birthdata
def validate_birthdata():
    
    global is_InputBirthdata_Validated
    #check for name -> must be a non empty string
    l_name = birthdatastr["name"]
    if (len(l_name.strip()) == 0):
      return ("Name field cant be empty")
    #check for DOB:Year -> must be a number and less than 5000
    l_year = (birthdatastr["DOB"]["year"]).strip()
    if (len(l_year) == 0):
      return ("BirthYear field cant be empty")
    if (l_year.isnumeric() == False):
      return ("BirthYear field must have numerical value.")
    if (int(l_year) > 5000):
      return ("BirthYear field must in range of 0 to 5000 only.")
    #check for DOB:month -> must be a number and in range 1 to 12
    l_month = (birthdatastr["DOB"]["month"]).strip()
    if (len(l_month) == 0):
      return ("BirthMonth field cant be empty")
    if (l_month.isnumeric() == False):
      return ("BirthMonth field must have numerical value.")
    if ((int(l_month) < 1) or (int(l_month) > 12)):
      return ("BirthMonth field must in range of 1 to 12 only.")
    #check for DOB:day -> must be a number and  in range 1 to 31 -consideration of 30 days and leap year etc not done
    l_day = (birthdatastr["DOB"]["day"]).strip()
    if (len(l_day) == 0):
      return ("BirthDay field cant be empty")
    if (l_day.isnumeric() == False):
      return ("BirthDay field must have numerical value.")
    if ((int(l_day) < 1) or (int(l_day) > 31)):
      return ("BirthDay field must in range of 1 to 31 only.")
    #check for TOB:hour -> must be a number and in range 0 to 23
    l_hr = (birthdatastr["TOB"]["hour"]).strip()
    if (len(l_hr) == 0):
      return ("BirthHour field cant be empty")
    if (l_hr.isnumeric() == False):
      return ("BirthHour field must have numerical value.")
    if ((int(l_hr) < 0) or (int(l_hr) > 23)):
      return ("BirthHour field must in range of 0 to 23 only.")
    #check for TOB:minute -> must be a number and in range 0 to 59
    l_mn = (birthdatastr["TOB"]["min"]).strip()
    if (len(l_mn) == 0):
      return ("BirthMinute field cant be empty")
    if (l_mn.isnumeric() == False):
      return ("BirthMinute field must have numerical value.")
    if ((int(l_mn) < 0) or (int(l_mn) > 59)):
      return ("BirthMinute field must in range of 0 to 59 only.")
    #check for TOB:second -> must be a number and in range 0 to 59
    l_ss = (birthdatastr["TOB"]["sec"]).strip()
    if (len(l_ss) == 0):
      return ("BirthSecond field cant be empty")
    if (l_ss.isnumeric() == False):
      return ("BirthSecond field must have numerical value.")
    if ((int(l_ss) < 0) or (int(l_ss) > 59)):
      return ("BirthSecond field must in range of 0 to 59 only.")
    #check for POB:name -> must be a non empty string
    l_placename = birthdatastr["POB"]["name"]
    if (len(l_placename.strip()) == 0):
      return ("Place name field cant be empty")
    #check for POB:longitude -> must be a floatnumber 
    l_lonstr = (birthdatastr["POB"]["lon"]).strip()
    if (len(l_lonstr) == 0):
      return ("Longitude field cant be empty")
    l_lon = isfloat(l_lonstr) 
    if (l_lon == False):
      return ("Longitude field must be a number (+ve or -ve with or without decimal point)")
    #check for POB:lattitude -> must be a floatnumber 
    l_latstr = (birthdatastr["POB"]["lat"]).strip()
    if (len(l_latstr) == 0):
      return ("Lattitude field cant be empty")
    l_lat = isfloat(l_latstr) 
    if (l_lat == False):
      return ("Lattitude field must be a number (+ve or -ve with or without decimal point)")
    #check for POB:timezone -> must be a float number and divisible by 0.5
    l_tzstr = (birthdatastr["POB"]["timezone"]).strip()
    if (len(l_tzstr) == 0):
      return ("Timezone field cant be empty")
    l_tz = isfloat(l_tzstr) 
    if (l_tz == False):
      return ("Timezone field must be a number (+ve or -ve with or without decimal point)")
    if (((l_tz%0.5)==0) == False):
      return ("Timezone field must be in hour format with steps of 30 min (30 min would be 0.5 hours)")
    #check for Gender -> must be a non empty string
    l_gender = birthdatastr["Gender"]
    if (len(l_gender.strip()) == 0):
      return ("Gender field cant be empty")
    #All fields are proper. So update birthdata
    birthdata["name"] = l_name.strip()
    birthdata["Gender"] = l_gender.strip()
    birthdata["DOB"]["year"] = int(l_year)
    birthdata["DOB"]["month"] = int(l_month) 
    birthdata["DOB"]["day"] = int(l_day)
    birthdata["TOB"]["hour"] = int(l_hr)
    birthdata["TOB"]["min"] = int(l_mn)
    birthdata["TOB"]["sec"] = int(l_ss)
    birthdata["POB"]["name"] = l_placename.strip()
    birthdata["POB"]["lon"] = l_lon
    birthdata["POB"]["lat"] = l_lat
    birthdata["POB"]["timezone"] = l_tz
    is_InputBirthdata_Validated = True
    return("SUCCESS")

def clear_birthdata():
   global is_InputBirthdata_Validated
   global is_OutputPathSet
   birthdatastr = { "DOB"  : { "year"     : "",
                            "month"    : "",
                            "day"      : ""
                          },
              "TOB"     : { "hour"     : "",  #in 24 hour format
                            "min"      : "",
                            "sec"      : ""
                          }, 
              "POB"     : { "name"     : "",
                            "lat"      : "",     #+ve for North and -ve for south
                            "lon"      : "",     #+ve for East and -ve for West
                            "timezone" : ""
                          },
              "name"    : "",
              "Gender"  : ""
            }
   is_InputBirthdata_Validated = False
   is_OutputPathSet = False
   return(birthdatastr.copy())

def IsBirthdataValid():
   global is_InputBirthdata_Validated
   return(is_InputBirthdata_Validated)

def get_birthdata():
   global is_InputBirthdata_Validated
   if(is_InputBirthdata_Validated == True):
    return(birthdata.copy())
   else:
      return(None)
      

######################################################################
################ Functions related to output #########################
######################################################################

def set_output(path, filename = "astrodata"):
  global outputfilenamefull
  global outputfilename
  global outputpath
  global is_OutputPathSet

  if(os.path.isdir(path)):
      outputpath = path
  else:
   is_OutputPathSet = False
   return(f'''Error: The given path parameter{path} is not a valid path innthis system.''')
  
  outputfilename = filename
  outputfilenamefull = f'''{outputpath}\{outputfilename}.json'''
  is_OutputPathSet = True
  return("SUCCESS")
    

def get_output():
  global outputfilenamefull
  if(is_OutputPathSet == True):
    return(outputfilenamefull)
  else:
    return(None)

######################################################################
################ Functions related to processing #####################
######################################################################
def reset_astrologicalData():
  if((data.clearAstroData(data.charts) == True) and (dashas.clearDashaDetails() == True)):
    return("SUCCESS")
  return("FAILURE")

def generate_astrologicalData(birthdata, returnval = "JSON_FILE_LOCATION"):
  global outputfilenamefull
  global is_InputBirthdata_Validated
  global is_OutputPathSet

  if(is_InputBirthdata_Validated == False):
    print("Error: Input birthdata is not validated successfully")
    return("INPUT_ERROR")
  
  if((is_OutputPathSet == False) and (returnval == "JSON_FILE_LOCATION")):
    print("Error: No proper Output Path provided for saving file generated")
    return("OUTPUTPATH_ERROR")

  reset_astrologicalData()
  #Compute Lagna(D1) Related astrological data
  lagna.compute_lagnaChart_custom(birthdata)

  #Compute Divisional charts astrological data
  varga.compute_Dx_4m_D1(data.charts,"D9")
  varga.compute_Dx_4m_D1(data.charts,"D10")
  varga.compute_Dx_4m_D1(data.charts,"D2")
  varga.compute_Dx_4m_D1(data.charts,"D3")
  varga.compute_Dx_4m_D1(data.charts,"D4")
  varga.compute_Dx_4m_D1(data.charts,"D7")
  varga.compute_Dx_4m_D1(data.charts,"D12")
  varga.compute_Dx_4m_D1(data.charts,"D16")
  varga.compute_Dx_4m_D1(data.charts,"D20")
  varga.compute_Dx_4m_D1(data.charts,"D24")
  varga.compute_Dx_4m_D1(data.charts,"D27")
  varga.compute_Dx_4m_D1(data.charts,"D30")
  varga.compute_Dx_4m_D1(data.charts,"D40")
  varga.compute_Dx_4m_D1(data.charts,"D45")
  varga.compute_Dx_4m_D1(data.charts,"D60")

  #COMPUTE BALAS FOR PLANETS
  bala.compute_VimshopakaBalas()
  bala.compute_shadbala(birthdata)
  bala.compute_ishtakashtabalas()
  bala.compute_bhavabala()

  #Compute AshtakaVarga
  ashtaka.compute_AshtakaVargas()

  #Compute Vimshottari dasha
  dashas.Vimshottari(data.charts["D1"], birthdata)

  #Compute special points
  sp.compute_sphuta(data.charts)

  if(returnval == "JSON_FILE_LOCATION"):
    #Dump the astrological computed data in output json file
    js.dump_astrodata_injson(outputfilenamefull)
    return (outputfilenamefull)
  elif (returnval == "ASTRODATA_DICTIONARY"):
     return(data.charts.copy())
  else:
     return("Invalid parameter returnval")


if __name__ == "__main__":
  print("START")
  print(reset_astrologicalData())
  generate_astrologicalData()
  print("END")