import jyotishyamitra as jsm

print("START")

#For input related functions
jsm.clear_birthdata()

################ Providing input birth data ####################
#providing Name and Gender
inputdata = jsm.input_birthdata(name="Shyam Bhat", gender="male")

#providing Date of birth details
inputdata = jsm.input_birthdata(year="1991", month=jsm.October, day="8")

#Providing Place of birth details
inputdata = jsm.input_birthdata(place="Honavar", longitude="+74.4439", lattitude="+14.2798", timezone="+5.5")

#Providing Time of birth details
inputdata = jsm.input_birthdata(hour="14", min="47", sec="9")

################### Lets Validate Birthdata ######################
jsm.validate_birthdata()

#If Birthdata is valid then get birthdata
if(jsm.IsBirthdataValid()):
    birthdata = jsm.get_birthdata()


########### Set the output folder and name of file to save generated astrological data
if("SUCCESS" == jsm.set_output(path="C:\\Users\sbb925582\Downloads", filename="astroOutput")):
    print(f'The output is : {jsm.get_output()}')
else:
    print("Given folder path doesnt exist")

############# Computing Astrological data ###############

if(jsm.reset_astrologicalData() == "SUCCESS"):  #Resetting the astrological data to clear history
    jsm.generate_astrologicalData(birthdata)    #Compute the astrological data based on new set.


print("END")
