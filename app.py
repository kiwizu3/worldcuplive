from flask import Flask, render_template,request,jsonify,json
import hotstar
from datetime import date

app = Flask(__name__)
app.secret_key = 'iknowyoucanseethis'

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    today=date.today()
    d1=today.strftime("%d%B%Y").lower()
    print(d1)
    match_number_1=hotstar.getMatchNumber(d1)
    if d1 in hotstar.double_match_dates:
        return render_template("index.html",multiple_match=True,match_number_1=hotstar.getMatchDetails(match_number_1),match_number_2=hotstar.getMatchDetails(match_number_1+1))
    return render_template("index.html",multiple_match=False,match_number_1=hotstar.getMatchDetails(match_number_1))

@app.route('/details', methods=['GET', 'POST'])
def details():
    hotstar_url='https://cyberboysumanjay.github.io/comingsoon.html'
    if request.method == 'POST':
        button_clicked=request.form['submit_button']
        button_clicked=button_clicked.split(':')
        quality,language,match=button_clicked[0],button_clicked[1],button_clicked[2]
        today = date.today()
        todaydate = today.strftime("%d%B%Y").lower()
        hotstar_url=hotstar.getLink(quality,language,todaydate,match)
        print(hotstar_url)
    return render_template("streaming.html",hotstar_url=hotstar_url)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000,use_reloader=True)
