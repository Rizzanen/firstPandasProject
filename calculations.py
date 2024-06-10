import pandas as pd
from tabulate import tabulate

filePath = 'sahkonHintaData.xlsx'

dataFrame = pd.read_excel(filePath)

#Muutetaan data muotoon jossa pandas voi käyttää sitä
dataFrame['Aika'] = pd.to_datetime(dataFrame['Aika'], format='%d/%m/%Y %H.%M.%S')

# Hinta columnin sisältämästä datasta pitää pilkut muuttaa pisteiksi, jotta python / pandas voi tulkita ne desimaali lukuina. Pythonissa desimaalierottaja on piste eikä pilkku. 
dataFrame['Hinta (snt/kWh)'] = dataFrame['Hinta (snt/kWh)'].astype(str).replace(',', '.').astype(float)

#Luodaan uusi columni "Year" johon asetetaan dataksi "Aika" columnin vuosi luvut. Niihin päästään käsiksi .dt.year metodeilla. 
dataFrame['Year'] = dataFrame['Aika'].dt.year
dataFrame['Hour'] = dataFrame['Aika'].dt.hour
#sama homma kuukausilla
dataFrame['Month'] = dataFrame['Aika'].dt.month

#lasketaan keskiarvo koko hinta datasta ja printataan se. 
def getAverage():
    #pandasin methodilla .mean() saamme dataFrame['Hinta (snt/kWh)'] sisältämästä datasta keskiarvon.
    averagePrice = dataFrame['Hinta (snt/kWh)'].mean()
    print("Average price between 2021-2024 is:", round(averagePrice, 2), "snt / kWh")


def getAverageOfYears():
    #järjestetään dataFrame['Hinta (snt/kWh)'] data Year columnin mukaan, niin että jokainen rivi, jossa on sama Year arvo kuuluu yhteen "ryhmään". Sitten näiden ryhmien datasta lasketaan keskiarvo .mean() metodilla.
    averagePricePerYear = dataFrame.groupby('Year')['Hinta (snt/kWh)'].mean()
    #pyöristetään data 2 desimaalin tarkkuuteen. groupby  lause tekee "Year" columnista indexi columnin. Jotta saadaan Year takaisin normi columniksi pitää
    #kutsua .reset_index() metodia, joka luo taas uuden indeksi rivin ja "Year" column käyttäytyy taas normaalisti.
    roundedAveragePrices = round(averagePricePerYear, 2).reset_index() 
    #Käytetään tabulate kirjastoa, joka tekee roundedAveragePrices columnista silmälle miellyttävämmän ja helpommin luettavamman.
    print(tabulate(roundedAveragePrices, headers=['Year', 'Hinta (snt/kWh)'] , tablefmt="fancy_grid", showindex=False))
   

def getAverageOfMonth():
    year = int(input("Which year? "))
    #suodatetaan dataFramesta tiedot pois joissa vuosi ei ole sama kuin käyttäjän syöttämä.
    filteredDataFrame = dataFrame[(dataFrame['Year'] == year)]
    
    #Järjestetään data "Month" columnin mukaan, jotta saadaan laskettua keskiarvo kaikista arvoista, joissa kuukausi on sama .mean() metodilla. 
    averagePricePerMonth = filteredDataFrame.groupby(['Month'])['Hinta (snt/kWh)'].mean().reset_index()
    #pyöristetään tulos 2 desimaaliin ja groupby  lause tekee "Month" columnista indexi columnin. Jotta saadaan "Month" takaisin normi columniksi pitää
    #kutsua .reset_index() metodia, joka luo taas uuden indeksi rivin ja "Year" column käyttäytyy taas normaalisti. 
    #Käytetään tabulate kirjastoa, joka tekee averagePricePerMonth columnista silmälle miellyttävämmän ja helpommin luettavamman.
    print(tabulate(round(averagePricePerMonth , 2) , headers=['Month', 'Hinta (snt/kWh)'], tablefmt="fancy_grid",showindex=False))  

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

def getBelowAverageTimes():
    average = dataFrame['Hinta (snt/kWh)'].mean()
    cheapestHour = dataFrame.groupby("Hour")["Hinta (snt/kWh)"].mean().reset_index()
    filteredDataFrame = cheapestHour[(cheapestHour['Hinta (snt/kWh)'] < average)]
    print("The following hours has a lower price than the average. The average price of every hour also displayed. ")
    print(tabulate(round(filteredDataFrame , 2) , headers=['Hours', 'Hinta (snt/kWh)'], tablefmt="fancy_grid",showindex=False))