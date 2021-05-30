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
        ## this will fetch only one from starting
        # product_info_data = cursor.fetchone()
        # # this will all 
        product_info_data = cursor.fetchall()
    
        # # it was for only one fetchone
        # if product_info_data != None:
        #     print(product_info_data)
        #     print('fdgfd')
        # # it is for all
        if product_info_data != ():
            print(product_info_data)
            # product_info_data
            fileSeries = len(product_info_data)
            fileSeries+=1
            # for sd in product_info_data:
            #     # str(sd).index()
            #     print(str(sd))
        
        procductFileName = 'static/products/'+secure_filename(f'productImage_{str(fileSeries)}')
        cursor.execute(f"INSERT INTO `products__info` (`Sn.`, `Products Name`, `Description`, `Price`, `Filename`) VALUES (NULL, '{prductName}', '{productDescription}', '{priceProduct}', '{procductFileName}');")
        # data = cursor.fetchone()
        # #saving files to product file names
        file_form.save(procductFileName)
        session['productAddedMsg'] = 'productadded'
        return redirect(url_for('admin'))
        # return "data"
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
        # and clearing all here to logout
        app.secret_key = 'SeSsIoNkEyFoRLoginR'
        session.clear()
        return render_template('login.html', vari=vari)
    elif 'wrongPass' in session:
        print("ehree")
        # session['wrongPass'] = 'DothisStuff'
        session.clear()
        return render_template('login.html', vari="Wrong Username and Password Combination. Try Again")
    else:
        return render_template('login.html')


@app.route("/checkLogin", methods=['POST'])
def checkLogin():
    data = request.form
    print(data['username'])
    # for now I'm only testing no database iahev used here
    if data['username'] == 'admin':
        # firstly clear all other session
        session.clear()
        # then creating a new session
        session['admin'] = data['username']
        return redirect("/admin")
    else:
        session['wrongPass'] = 'wrongPass'
        return redirect(url_for('login'))


@app.route("/adminsignout")
def adminSignOut():
    if 'admin' in session:
        # i am not clearing all sessoin because i need it to clean two times when logout msg will show after that
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
    # app configuration
    app.config['SESSION_TYPE'] = 'login'
    # # it's configuration for upload file
    app.config['UPLOAD_FOLDER'] = 'static/products'
    # maximum size of uploading file
    app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024

    app.run(debug=True)
    # Quick test configuration. Please use proper Flask configuration options
    # in production settings, and use a separate file or environment variables
    # to manage the secret key!

#     from datetime import timedelta
# from flask import session, app

# @app.before_request
# def make_session_permanent():
#     session.permanent = True
#     app.permanent_session_lifetime = timedelta(minutes=5)

    # for uploaded_file in request.files.getlist('file'):
    #     if uploaded_file.filename != '':
    #         uploaded_file.save(uploaded_file.filename)

# @app.route('/', methods=['POST'])
# def upload_file():
#     uploaded_file = request.files['file']
#     if uploaded_file.filename != '':
#         uploaded_file.save(uploaded_file.filename)
#     return redirect(url_for('index'))
