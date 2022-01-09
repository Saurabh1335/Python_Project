from flask import Flask,render_template,request,redirect
import pymysql
app=Flask(__name__)

@app.route('/')
def index():
    try:
        db=pymysql.connect(host="localhost",user="root",password="",db="wct")
        cu=db.cursor()
        sql="select * from records"
        cu.execute(sql)
        data=cu.fetchall()
        #return "All records fetched"
        return render_template('self_dashboard.html',d=data)
    except Exception:
        return "Error inconnection"


@app.route('/form')
def form():
    return render_template("self_form.html")

@app.route('/insert',methods=['POST','GET'])
def insert():
    ot=request.form['opposition_team']
    r=request.form['runs']
    w=request.form['wickets']
    dt=request.form['match_date']
    
    # return t+det+dt
    try:
        db=pymysql.connect(host="localhost",user="root",password="",db="wct")
        cu=db.cursor()
        sql="insert into records(opposition_team,runs,wickets,match_date)values('{}','{}','{}','{}')".format(ot,r,w,dt)
        cu.execute(sql)
        db.commit()
        return redirect('/')
    except Exception:
        return "Error in connectionn"
    
@app.route('/delete/<rid>')
def delete(rid):
    try:
        db=pymysql.connect(host="localhost",user="root",password="",db="wct")
        cu=db.cursor()
        sql="delete from records where id='{}'".format(rid)
        cu.execute(sql)
        db.commit()
        return redirect('/')
        # return "Record deleted"
    except Exception:
        return "Error"

@app.route('/edit/<rid>')
def edit(rid):
     try:
        db=pymysql.connect(host="localhost",user="root",password="",db="wct")
        cu=db.cursor()
        sql="select * from records where id='{}'".format(rid)
        cu.execute(sql)
        data=cu.fetchone()
        
        return render_template('edit_self_form.html',d=data) 
     except Exception:
        return "Error in connectionnn"
    
@app.route('/update',methods=['POST','GET'])
def update():
    rid=request.form['rid']
    ot=request.form['opposition_team']
    r=request.form['runs']
    w=request.form['wickets']
    dt=request.form['match_date']
    
    try:
        db=pymysql.connect(host="localhost",user="root",password="",db="wct")
        cu=db.cursor()
        sql="UPDATE records SET opposition_team='{}',runs='{}',wickets='{}',match_date='{}' where id='{}'".format(ot,r,w,dt,rid)
        cu.execute(sql)
        db.commit()
        return redirect('/') 
    except Exception:
        return "Error in connectionnnn"
if __name__=='__main__':
    
    app.run(debug=True)
