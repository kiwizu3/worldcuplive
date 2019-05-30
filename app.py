from flask import Flask, render_template,request,jsonify,json
import hotstar
from datetime import date

app = Flask(__name__)
app.secret_key = 'iknowyoucanseethis'

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
   return render_template("index.html")

@app.route('/details', methods=['GET', 'POST'])
def details():
    if request.method == 'POST':
        button_clicked=request.form['submit_button']
        button_clicked=button_clicked.split(':')
        quality,language=button_clicked[0],button_clicked[1]
        today = date.today()
        todaydate = today.strftime("%d%B%Y").lower()
        hotstar_url=hotstar.getLink(quality,language,todaydate,"01")

    return render_template("streaming.html",hotstar_url=hotstar_url)
    #return render_template("display.html",dp_url=dp_url,username=username,fullname=fullname,private_profile=private_profile,is_verified=is_verified,anonymous_profile_pic=anonymous_profile_pic,total_posts=total_posts,followers=followers,following=following,bio=bio,external_url=external_url,report_fraud=report_fraud,hd_dp_url=hd_dp_url)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000,use_reloader=True)
