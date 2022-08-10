from flask import Flask 
import dnssorgu 
import sys

app = Flask ( __name__)

@app.route ("/")
def index () :
    return "İSTEDİĞİNİZ DNS SORGUSU YAPILMIŞTIR , İSTENİLEN IP ADRESİ --->  "

@app.route ("/query")
def query () :
    return dnssorgu.query("firat.edu.tr")

if __name__ == "__main__" :
    app.run(debug=True) 
