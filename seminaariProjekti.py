import pandas as pd


filePath = 'sahkonHintaData.xlsx'

dataFrame = pd.read_excel(filePath)

#dataFrame on nimennyt automaattisesti Headerit/ column namet excel tiedoston ensimmäisen rivin tietojen mukaan
#Niihin päästää käsiksi esim -> dataFrame['Aika'] tämä sisältää Aika columnin datat.

#jotta pandas osaa ymmärtää dataFrame['Aika'] datan oikein, pitää sille kertoa missä muodossa data on. Se tehdään format lauseessa, esim day = %d
#kun datamme on muodossa 01/01/2021  1.00.00 eli day, month, year, hour, min ,sec on format lause format='%d/%m/%Y %H.%M.%S'

#Muutetaan data muotoon jossa pandas/python voi käyttää sitä
dataFrame['Aika'] = pd.to_datetime(dataFrame['Aika'], format='%d/%m/%Y %H.%M.%S')
print(dataFrame['Aika'])
print(dataFrame['Hinta (snt/kWh)'])
# Hinta columnin sisältämästä datasta pitää pilkut muuttaa pisteiksi, jotta python / pandas voi tulkita ne desimaali lukuina. Pythonissa desimaalierottaja on piste eikä pilkku. 
dataFrame['Hinta (snt/kWh)'] = dataFrame['Hinta (snt/kWh)'].astype(str).replace(',', '.').astype(float)
#\n 
#Luodaan uusi columni "Year" johon asetetaan dataksi "Aika" columnin vuosi luvut. Niihin päästään käsiksi .dt.year metodeilla. 
dataFrame['Year'] = dataFrame['Aika'].dt.year
#sama homma kuukausilla
dataFrame['Month'] = dataFrame['Aika'].dt.month


def welcome():
    print("Welcome to my project! ")
    print("Here you can analyze data of finnish exchange electricity prices between 2021-2024.")
    options()

def options():    
    print("For average price type 1")
    print("For average price of each year type 2")
    print("For averages of years months type 3")
    print("For max value type 4")
    print("For min value type 5")
    print("To quit type x")
    userInput = input("Type a number and press enter \n")

    if userInput == "1":
        print("\n")
        getAverage()
        print("\n")
        options()
    elif userInput == "2":
        print("\n")
        getAverageOfYears()
        print("\n")
        options()
    elif userInput == "3":
        print("\n")
        getAverageOfMonth()
        print("\n")
        options()
    elif userInput == "4":
        print("\n")
        getMax()
        print("\n")
        options()
    elif userInput == "5":
        print("\n")
        getMin()
        print("\n")
        options()
    elif userInput == "x":
        return
    else:
        print("\n")
        print("Please type 1, 2, 3, 4, 5 or x")
        print("\n")
        options()

#lasketaan keskiarvo koko hinta datasta ja printataan se. 
def getAverage():
    #pandasin methodilla .mean() saamme dataFrame['Hinta (snt/kWh)'] sisältämästä datasta keskiarvon.
    averagePrice = dataFrame['Hinta (snt/kWh)'].mean()
    print("Average price between 2021-2024 is:", round(averagePrice, 2), "snt / kWh")

def getAverageOfYears():
    #järjestetään dataFrame['Hinta (snt/kWh)'] data Year columnin mukaan, niin että jokainen rivi, jossa on sama Year arvo kuuluu yhteen "ryhmään". Sitten näiden ryhmien datasta lasketaan keskiarvo .mean() metodilla.
    averagePricePerYear = dataFrame.groupby('Year')['Hinta (snt/kWh)'].mean()
    #pyöristetään tulos 2 desimaaliin ja muutetaan objekti toString muotoon printatessa. 
    print(round(averagePricePerYear, 2).to_string())
 

def getAverageOfMonth():
    year = int(input("Which year? "))
    
    #suodatetaan dataFramesta tiedot pois joissa vuosi ei ole sama kuin käyttäjän syöttämä.
    filteredDataFrame = dataFrame[(dataFrame['Year'] == year)]
    
    #Järjestetään data "Month" columnin mukaan, jotta saadaan laskettua keskiarvo kaikista arvoista, joissa kuukausi on sama .mean() metodilla. 
    averagePricePerMonth = filteredDataFrame.groupby(['Month'])['Hinta (snt/kWh)'].mean()
    #pyöristetään tulos 2 desimaaliin ja muutetaan objekti toString muotoon printatessa. 
    print(round(averagePricePerMonth, 2).to_string())  

def getMax():
    #haetaan suurin hinta tieto dataFramesta, joka löydetään max() methodilla. 
    maxPriceHinta = dataFrame['Hinta (snt/kWh)'].max()
    #printataan tulos pyöristettynä 2 desimaaliin.
    print("Max price between 2021-2024 is:", round(maxPriceHinta, 2), "snt / kWh")

def getMin():
    #haetaan pienin hinta tieto dataFramesta, joka löydetään max() methodilla. 
    minPriceHinta = dataFrame['Hinta (snt/kWh)'].min()
    #printataan tulos pyöristettynä 2 desimaaliin.
    print("Min price between 2021-2024 is:", round(minPriceHinta, 2), "snt / kWh")

welcome()



