from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

page_url = "https://www.amazon.in/gp/bestsellers/books/"

uClient = uReq(page_url)

page_soup = soup(uClient.read(), "html.parser")
uClient.close()

out_filename = "in_book.csv"
headers = "Name;URL;Author;Price;Number of Ratings;Average Ratings \n"

f = open(out_filename, "w",encoding="utf-8")
f.write(headers)


containers = page_soup.findAll("span", {"class": "aok-inline-block zg-item"})


#print(len(containers))
for item in containers:
    try:
        book_name = item.a.span.div.img["alt"]
    except AttributeError:
        book_name = "Not available"
        
    try:
        book_url = "https://www.amazon.in" +  item.a["href"]
    except AttributeError:
        book_url = "Not available"
        
    try:
        book_author = item.find('a', {'class':'a-size-small a-link-child'}).text
    except AttributeError:
        book_author = "Not available"
        
    try:    
        book_price = item.find('span', {'class':'p13n-sc-price'}).text
    except AttributeError:
        book_price = "Not available"
        
    try:
        book_user_rating = item.find('a', {'class':'a-size-small a-link-normal'}).text
    except AttributeError:
        book_user_rating = "Not available"
        
    try:
        book_avg_rating = item.find('span', {'class':'a-icon-alt'}).text
    except AttributeError:
        book_avg_rating = "Not available"

    #print(book_price.replace("\u20b9"," "))
    f.write(book_name.replace(";","") + ";" + book_url.replace(";","") + ";" + book_author.replace(";","") + ";" + book_price.replace(";","") + ";" + book_user_rating.replace(";","") + ";" + book_avg_rating.replace(";","") + "\n")


################### for page 2 ##########################################
page_url2 = "https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_2?ie=UTF8&pg=2"
uClient = uReq(page_url2)
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

containers = page_soup.findAll("span", {"class": "aok-inline-block zg-item"})


#print(len(containers))
for item in containers:
    try:
        book_name = item.a.span.div.img["alt"]
    except AttributeError:
        book_name = "Not available"
        
    try:
        book_url = "https://www.amazon.in" +  item.a["href"]
    except AttributeError:
        book_url = "Not available"
        
    try:
        book_author = item.find('a', {'class':'a-size-small a-link-child'}).text
    except AttributeError:
        book_author = "Not available"
        
    try:    
        book_price = item.find('span', {'class':'p13n-sc-price'}).text
    except AttributeError:
        book_price = "Not available"
        
    try:
        book_user_rating = item.find('a', {'class':'a-size-small a-link-normal'}).text
    except AttributeError:
        book_user_rating = "Not available"
        
    try:
        book_avg_rating = item.find('span', {'class':'a-icon-alt'}).text
    except AttributeError:
        book_avg_rating = "Not available"

    #print(book_price.replace("\u20b9"," "))
    f.write(book_name.replace(";","") + ";" + book_url.replace(";","") + ";" + book_author.replace(";","") + ";" + book_price.replace(";","") + ";" + book_user_rating.replace(";","") + ";" + book_avg_rating.replace(";","") + "\n")




f.close()
