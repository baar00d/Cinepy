# heyyy there!!!!!
from bs4 import BeautifulSoup
import urllib2 as ur
city=raw_input('enter city : ')
bms="https://www.filmipop.com/{}".format(city)
page=ur.urlopen(bms)
soup=BeautifulSoup(page,'html.parser')

div_list=soup.find_all('div',{'class':'pull-left lh20 fc_333 fs14 proximanova_bold nearesttheatre_title'})

hall_list=[]    # unicode
show_links=[]   # string
database=[]     # final info
for div in div_list:
    a=div.find('a',{'class':'pull-left fc_333 fc_333_hover text-decoration-none fs15'})
    hall_list.append(a.get('href'))

for each in hall_list:
    show_links.append(each.encode('utf-8'))
   
################### regional movies links [list] stored ##############################

for link in show_links:
    page=ur.urlopen(link)
    soup=BeautifulSoup(page,'html.parser')
    
    hall_find=soup.find('span',{'class':'sectionTitle_Sub'})
    hall=hall_find.text.encode('utf-8')
    movie_list=[hall] #first element of list is hall
    a=soup.find_all('a',{'class':'fc_33'})
    
    
    for mov in a:
        movie=mov.text.encode('utf-8')
        data=' '.join(movie.split())
        movie_list.append(data)
    # print movie_list 
    '''
    ['PVR Vinayak - Civil Lines', 'Baadshaho', 'Bareilly Ki Barfi', 'A Gentleman: Sundar Susheel Risky', 'Shubh Mangal Saavdhan', 'Annabelle: Creation', 'Toilet: Ek Prem Katha', 'Babumoshai Bandookbaaz']
    '''
    database.append(movie_list)
print (database)    
    
    
    


