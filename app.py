import os
from bs4 import BeautifulSoup
import requests
from flask import Flask, request, render_template, redirect, jsonify


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])

def home():
    return render_template('index.html')


@app.route('/result', methods = ['GET', 'POST'])

def result():
    if request.method == 'POST':
        searchString = request.form['quote'].replace(' ', '')
        print(searchString)

        url = 'https://www.brainyquote.com/search_results?q=' + searchString
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup.prettify())

        quotes = soup.find_all('div', {'class':'clearfix'})
       
        

        filename = 'happy' + '.csv'
        fw = open(filename, 'w+')
        headers = 'Quote, Written by \n'
        fw.write(headers)

        list_of_quotes = []
        # my_dict={}


        for quote in quotes:
            # Quotess = quote.div.a.text
            # print(Quotess)
            try:
                Quote = quote.find('a',{'class':'b-qt'}).text
            
                    # print(author.text)
                # my_dict['Quote']

                try:
                    author = quote.find('a',{'class':'oncl_a'}).text     
                    myDict = {'Quote': Quote, 'Writer': author}
                    list_of_quotes.append(myDict)
                except:
                    author = None
            except:
                pass
        return render_template('result.html', list_of_quotes = list_of_quotes)
    else:
        return render_template('index.html')


# port = int(os.getenv("PORT"))
if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=port)
