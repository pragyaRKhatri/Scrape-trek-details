import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

base_url = 'https://www.bikatadventures.com/#one'

#Following is the Dictionary in which the final information will be stored about the category and URL

trek_type_dict = {
    'Trek_Category' : [],
    'Trek_Category_Link' : []
}

# Following function will find the tags and return dataframe, this will contain 6 rows

def get_trek_category(doc):
    selection_class = 'dropdown-item'     #This is the class_name use to find the tags
    tag = doc.find_all('a',{'class':selection_class})      #Finding "a" tags with particular class_name

    #Since there are 17 "a" tags in total but we want contents of only top 6
    for i in tag[:6]:       
        trek_type_dict['Trek_Category'].append( i.text.strip())  #storing the category name in list
        trek_type_dict['Trek_Category_Link'].append( 'https://www.bikatadventures.com/' + i.get('href'))  #Storing category URL in the list
    
    #putting above lists as value in the dictionary

    
    #creating DataFrame using Panda Libraries
    trek_cat_df = pd.DataFrame(trek_type_dict)
    #creating CSV with the name "Trek_Categories"
    trek_cat_df.to_csv('Trek_Categories.csv', index = None)

    #returning DataFrame for further use
    return trek_cat_df

#scrape_trek_category() will scrape the Base_Url and return Dataframes 

def scrape_trek_category():
    #Using Request Library and checking if request status is successful or not
    response = requests.get(base_url)
    if response.status_code != 200:
        print('Status code:',response.status_code)
        raise Exception('Failed to fetch webpage {}'.format(source_url))

    #Parsing HTML with the help of BeautifulSoup and getting the object    
    doc = BeautifulSoup(response.text, 'html.parser')
    #print(doc.prettify())   #Use this print, In case if you want to see the contents of BeautifulSoup Object
    
    #calling get_trek_category(doc) to get the DataFrames
    return get_trek_category(doc)

#Created an empty Dictionary which will store the details of the treks

trek_details_dict = {'Trek_Name':[],
                    'Trek_Duration':[],
                    'Trek_Amount':[],
                    'Trek_Level':[],
                    'Trek_URL':[]}



#This function is just like above get_trek_category(), only difference it will give further details about each trek and will return DataFrames 
def get_trek_details(doc):
    selection_class = 'col-lg-3 col-md-3 col-sm-4 col-xs-12'  #Class_Name to be searched
    trek_title_tags = doc.find_all('div', {'class':selection_class}) #Finding all the "Div" tags and storing
    print('Total Number of Treks : ',len(trek_title_tags))  #printing the total no.  of treks by counting total no. of "Div" tags
    
    base_url="https://www.bikatadventures.com/"
    #Executing Loop to get content of each trek from a particular category and storing data in the lists
    for tag in trek_title_tags :
        trek_details_dict['Trek_Name'].append(tag.strong.text)
        trek_details_dict['Trek_Duration'].append(tag.span.contents[0].replace('|','').strip())
        trek_details_dict['Trek_Amount'].append(tag.span.span.contents[0])
        trek_details_dict['Trek_Level'].append(tag.find('span', class_='gauge-text').text)
        trek_details_dict['Trek_URL'].append(base_url+tag.a['href'])
    
    #Returning dictionary as Dataframe
    return pd.DataFrame(trek_details_dict)


#Here is how the DataFrames will look
pd.DataFrame(trek_details_dict)

#Following function is scraping each category URL
def get_category_details(url):
    #Using Request Library and checking request status is success or not 
    response = requests.get(url)
    if response.status_code != 200:
        print('Status code:',response.status_code)
        raise Exception('Failed to fetch webpage {}'.format(source_url))

    #using BeautifulSoup to parse    
    doc = BeautifulSoup(response.text, 'html.parser')
    #calling get_trek_details(doc) to get DataFrames
    return get_trek_details(doc)

#Following function is using get_category_details() to get Dataframes and creating separate CSV's

def scrape_treks(trek_type, trek_type_url):
    trek_df = get_category_details(trek_type_url)
    trek_df.to_csv(trek_type+ '.csv', index = None)
    
def scrape_each_category():
    treks_df = scrape_trek_category()
    print(treks_df)
    for index, row in treks_df.iterrows():
        print('\n')
        print('Scraping Treks '+ row['Trek_Category'])
        scrape_treks(row['Trek_Category'], row['Trek_Category_Link'])

#Finally calling the Main Function which will give the final OutPut in form of CSV
scrape_each_category()


