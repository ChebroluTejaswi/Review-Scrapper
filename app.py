# Importing necessary libraries

from flask import Flask, render_template, request,jsonify
# from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

app = Flask(__name__)  # initialising the flask app with the name 'app'


@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')


# base url + /
#http://localhost:8000 + /
@app.route('/scrap',methods=['POST']) # route with allowed methods as POST and GET
def index():
    if request.method == 'POST':
        print("post recieved")
        searchString = request.form['content'].replace(" ","") # obtaining the entered search string
        try:
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString # preparing the URL to search the product on flipkart
            print(flipkart_url)
            # Code to open the url(website)
            uClient = uReq(flipkart_url) # requesting the webpage from the internet (returns a HTTP respose)
            flipkartPage = uClient.read() # reading the webpage (page source of the website)
            uClient.close() # closing the connection to the web server
            
            flipkart_html = bs(flipkartPage, "html.parser") # parsing the webpage as HTML
            # searching for appropriate tag to redirect to the product link
            bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
            del bigboxes[0:3] # the first 3 members of the list do not contain relevant information, hence deleting them.
            box = bigboxes[0] # taking the first iteration/product
            productLink = "https://www.flipkart.com" + box.div.div.a['href'] # extracting the actual product link
            
            prodRes = requests.get(productLink) # getting the product page from server
            prod_html = bs(prodRes.text, "html.parser") # parsing the product page as HTML
            commentboxes = prod_html.find_all('div', {'class': "_16PBlm"}) # finding the HTML section containing the customer comments
           
            reviews = [] # initializing an empty list for reviews
            #  iterating over the comment section to get the details of customer and their comments
            for commentbox in commentboxes:
                try:
                    name=commentbox.find_all('p',{'class':'_2sc7ZR _2V5EHH'})[0].text
                    print(name)
                except:
                    name = 'No Name'
                try:
                    rating = commentbox.div.div.div.div.text

                except:
                    rating = 'No Rating'
                try:
                    commentHead = commentbox.div.div.div.p.text
                except:
                    commentHead = 'No Comment Heading'
                try:
                    comtag = commentbox.div.div.find_all('div', {'class': ''})
                    custComment = comtag[0].div.text
                except:
                    custComment = 'No Customer Comment'
                    
                mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
                          "Comment": custComment} # saving that detail to a dictionary
                reviews.append(mydict) #  appending the comments to the review list
                
            return render_template('results.html', reviews=reviews) # showing the review to the user
        
        except:
            return 'OOPS! Something is wrong.'



if __name__ == "__main__":
    app.run(port=8000,debug=True) # running the app on the local machine on port 8000