from flask import Flask, render_template, request, url_for, redirect,flash
from flask_mysqldb import MySQL
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'remaja'
mysql = MySQL(app)

@app.route('/')
def index():
            return render_template('index.html')
            
@app.route('/home')
def home():
        cur=mysql.connection.cursor()
        sql="SELECT * from data"
        cur.execute(sql)
        results=cur.fetchall()
        cur.close()
        return render_template('home.html',Data=results)

@app.route('/tambah', methods=['GET','POST'])
def tambah():
         if request.method == 'POST':
            nama=request.form['nama']
            kelamin=request.form['kelamin']
            ttl=request.form['ttl']
            alamat=request.form['alamat']
            notelp=request.form['notelp']
            status=request.form['status']
            keterangan=request.form['keterangan']
            cur=mysql.connection.cursor()    
            sql='INSERT into data (nama,kelamin,ttl,alamat,notelp,status,keterangan) values(%s,%s,%s,%s,%s,%s,%s)'
            val=(nama,kelamin,ttl,alamat,notelp,status,keterangan)
            cur.execute(sql,val)
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('home'))



@app.route('/tambah2', methods=['GET','POST'])
def tambah2():
         row=[]
         if request.method == 'POST':
            nama=request.form['nama']
            kelamin=request.form['kelamin']
            ttl=request.form['ttl']
            alamat=request.form['alamat']
            notelp=request.form['notelp']
            status=request.form['status']
            keterangan=request.form['keterangan']
            cur=mysql.connection.cursor()    
            sql='INSERT into data (nama,kelamin,ttl,alamat,notelp,status,keterangan) values(%s,%s,%s,%s,%s,%s,%s)'
            val=(nama,kelamin,ttl,alamat,notelp,status,keterangan)
            cur.execute(sql,val)
            for i in val:
                    row.append(i)
            cur.close()
            return render_template('show.html',row=row)
         
                
@app.route('/edit2/<nama>', methods=['get','post'])
def edit2(nama):
       
        if request.method == 'POST':
            nama=request.form['nama']
            kelamin=request.form['kelamin']
            ttl=request.form['ttl']
            alamat=request.form['alamat']
            notelp=request.form['notelp']
            status=request.form['status']
            keterangan=request.form['keterangan']   
            cur=mysql.connection.cursor()
            sql=("update data set nama=%s,kelamin=%s,ttl=%s,alamat=%s,notelp=%s,status=%s,keterangan=%s where nama=%s ")
            val=(nama,kelamin,ttl,alamat,notelp,status,keterangan,nama)
            cur.execute(sql,val)
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('index'))


@app.route('/edit/<no>',methods=['POST','GET'])
def edit(no):
    if request.method == 'POST':
        no = request.form['no']
        nama = request.form['nama']
        kelamin = request.form['kelamin']
        ttl = request.form['ttl']
        alamat = request.form['alamat']
        notelp = request.form['notelp']
        status = request.form['status']
        keterangan = request.form['keterangan']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE data
               SET nama=%s, kelamin=%s, ttl=%s, alamat=%s, notelp=%s, status=%s, keterangan=%s
               WHERE no=%s
            """, (nama, kelamin, ttl, alamat, notelp, status, keterangan, no))
        mysql.connection.commit()
        return redirect(url_for('home'))

             
@app.route('/hapus/<string:no>',methods=['get'])
def hapus(no):
                cur=mysql.connection.cursor()
                cur.execute('DELETE from data where no=%s',(no,))
                mysql.connection.commit()
                cur.close()
                return redirect(url_for('home'))

@app.route('/login',methods=['get','post'])
def login():
        un=request.form['username']
        pas=request.form['pass']

        cur=mysql.connection.cursor()
        cur.execute("SELECT username,pass from admin where username={un} and pass={pas}")
        result=cur.fetchall()
        if len(result)==1:
                return render_template("home.html")
      
if __name__ =='__main__':
                app.run(debug=True)
