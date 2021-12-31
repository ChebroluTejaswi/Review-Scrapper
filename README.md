### Flipkart Review Scrapper

    Web scraping is a technique using which the webpages from the internet are fetched and parsed 
    to understand and extract specific information similar to a human being. Web scrapping 
    consists of two parts:

    • Web Crawling→ Accessing the webpages over the internet and pulling data from 
    them.
    • HTML Parsing→ Parsing the HTML content of the webpages obtained through web 
    crawling and then extracting specific information from it.

    Hence, web scrappers are applications/bots, which automatically send requests to websites and 
    then extract the desired information from the website output.

How it works?

    1. Form in Index.html takes an input(search key) and posts the value to path '/scrap'.
    2. Python file app.py executes index function on a post request 
      -> Generates a URL to search for a product in flipkart
      -> Scrapes review data from the website for a particular product
      -> Stores the results in Reviews list
    3. Results are sent to results.html file.
    4. Results.html displays the output in a table format.
    
Installation
> Create a virtual Environment

```shell
python -m venv env
```
> Activate virtual Environement

```shell
env\Scripts\activate
```

> Install required libraries

```shell
pip  install -r requirements.txt 
```
> Run the python file

```shell
python app.py
```
> Open the link in browser

```shell
host:127.0.0.1 port:8000 (http://127.0.0.1:8000/)
```
