import support.mod_constants as c
import support.mod_astrodata as data
import json

# astrodata.json related functions
def dump_astrodata_injson(filefullname):
    with open(filefullname, 'w') as json_astrodatafile:
        json.dump(dict(data.charts), json_astrodatafile, indent=4)
    return




if __name__ == "__main__":
    #print("Section1")
    #load_birthdatas()
    #print(data.birthdatas)
    print("Section2")
    #load_yogadoshas()
    #yd.yogadoshas
    #print(yd.yogadoshas["yogadoshas"])
    print("Section End")