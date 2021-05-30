from flask import Flask, render_template, request, redirect, url_for, session, jsonify, make_response
import os
from werkzeug.utils import secure_filename
from flaskext.mysql import MySQL

app = Flask(__name__)

@app.route("/")
def main():
    # # Connecting to mysql server
    conn = myMysqlApp.connect()
    cursor = conn.cursor()
    # # getting data
    cursor.execute("SELECT * FROM `products__info`")
    fetchAllProductsData = cursor.fetchall()

    data = { "prodctData" : fetchAllProductsData, "lenght" : len(fetchAllProductsData)}
    template = 'index.html'
    return render_template(template, productsDataForAdding=data)


@app.route("/admin")
def admin():
    if 'admin' in session:
        if 'productAddedMsg' in session:
            # it will delete specifed session that's done
            session.pop('productAddedMsg')
            return render_template('admin.html', vari="Product Added")
        return render_template('admin.html')
    else:
        return render_template('login.html')


@app.route('/productdata', methods=['POST', 'GET'])
def product_data_save():
    if request.method == 'POST':
        form_data = request.form
        prductName = form_data['producName']
        productDescription = form_data['discription']
        priceProduct = form_data['price']
        file_form = request.files['productFile']

        # Connecting to mysql
        conn = myMysqlApp.connect()
        cursor = conn.cursor()

        # secure filename for on space and no error while saving
        fileSeries = 0
        cursor.execute("SELECT * FROM `products__info`")
        product_info_data = cursor.fetchall()
    

        if product_info_data != ():
            print(product_info_data)
            # product_info_data
            fileSeries = len(product_info_data)
            fileSeries+=1
        
        procductFileName = 'static/products/'+secure_filename(f'productImage_{str(fileSeries)}')
        cursor.execute(f"INSERT INTO `products__info` (`Sn.`, `Products Name`, `Description`, `Price`, `Filename`) VALUES (NULL, '{prductName}', '{productDescription}', '{priceProduct}', '{procductFileName}');")

        file_form.save(procductFileName)
        session['productAddedMsg'] = 'productadded'
        return redirect(url_for('admin'))
    else:
        return "Get Method Not Allowed"


@app.route("/login")
def login():
    print(session)
    if 'admin' in session:
        return redirect(url_for('admin'))
    elif 'logoutSuccessfully' in session:
        session['logoutSuccessfully'] = ''
        vari = 'Logout Successfully'
        app.secret_key = 'SeSsIoNkEyFoRLoginR'
        session.clear()
        return render_template('login.html', vari=vari)
    elif 'wrongPass' in session:
        print("ehree")
        session.clear()
        return render_template('login.html', vari="Wrong Username and Password Combination. Try Again")
    else:
        return render_template('login.html')


@app.route("/checkLogin", methods=['POST'])
def checkLogin():
    data = request.form
    print(data['username'])
    if data['username'] == 'admin':
        session.clear()
        session['admin'] = data['username']
        return redirect("/admin")
    else:
        session['wrongPass'] = 'wrongPass'
        return redirect(url_for('login'))


@app.route("/adminsignout")
def adminSignOut():
    if 'admin' in session:
        session.clear()
        session['logoutSuccessfully'] = 'logoutSuccessfully'
        return redirect(url_for('login'))
    else:
        return "There is no any problem"


@app.route("/signup")
def signup():
    return "Coming Soon"


if __name__ == '__main__':
    myMysqlApp = MySQL()
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = ''
    app.config['MYSQL_DATABASE_PORT'] = 3308
    app.config['MYSQL_DATABASE_DB'] = "mydatabase"
    myMysqlApp.init_app(app)
    app.secret_key = 'SeSsIoNkEyFoRLogin'
    app.config['SESSION_TYPE'] = 'login'
    app.config['UPLOAD_FOLDER'] = 'static/products'
    app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024

    app.run(debug=True)
 
