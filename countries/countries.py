#Create a class called as CountryCapital 
# which has a list that contains names of countries and a list that stores names of their respective capitals. 
# It also has a variable score set to 0 in the init method. 
# In the init method set both the lists to empty. 
# Create a function called as load_data which opens a file country.txt and reads all data from it and loads both the lists. 
# The file contains names of countries and their capitals separated by a '-'. 
# The country names need to be stored in the country list and capitals in the capital list. 
# Position of county in county list and its capital in capital list should be the same. 
# Create another function called as quiz which prints each country from the list and asks user to input its capital. 
# If there is a match increase the score. Create a third function which displays score. Test the application 
#Save score with username in result file.
#Print highest score till now.
#If player is playing again and his username exists in the result file then compare his score. 
# If existing score is lesser than current score then put this score in the file else let that score be

class CountryCapital:
    def __init__(self):
        self.score = 0
        self.countries = []
        self.capitals = []
    
    def appendCC(self, country, capital):
        self.countries.append(country)
        self.capitals.append(capital.replace("\n",""))
        

def load_data(cc):
    f=open("country2.txt","r")
    countrydata = f.readlines()

    for line in countrydata:
        lst=line.split("-")
        cc.appendCC(lst[0],lst[1])

    f.close()
    r=open("results.txt","r")
    resultdata = r.readlines()
    
    myscore = 0
    for line in resultdata:
        lst=line.split("-")
        if lst[0]==name:
             myscore = int(lst[1])
    r.close()
    return myscore

def save_data(name,cc):
    r=open("results.txt","r")
    resultdata = r.readlines()

    user_exist=False
    for i in range(len(resultdata)):
        lst=resultdata[i].split("-")
        if lst[0]==name:
            user_exist=True
            if cc.score > int(lst[1]):
                resultdata[i]=name+"-"+str(cc.score)+"\n"
            break
    if user_exist==False:
        resultdata.append(name+"-"+str(cc.score)+"\n")
        
    w=open("results.txt","w")
    w.writelines(resultdata)
    w.close()


def quiz(country, capital):
    capital_in = input("What is the capital of "+country)
    if capital_in == capital:
        return True
    else:
        return False

# main
cc = CountryCapital()
name = input("Type your name:")
highestscore=load_data(cc)

for i in range(len(cc.countries)):
    if quiz(cc.countries[i],cc.capitals[i]) :
        print("Correct!")
        cc.score+=1
    else:
        print("Not Correct. Answer is "+cc.capitals[i])

save_data(name,cc)

