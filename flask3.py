from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def form():
    # هذا يرجع نموذج HTML بسيط عند زيارة الصفحة الرئيسية
    return '''
    <html>
       <body>
          <form action="/login" method="post">
             <p>Enter Name:</p>
             <p><input type="text" name="nm" /></p>
             <p><input type="submit" value="submit" /></p>
          </form>
       </body>
    </html>
    '''

@app.route('/login', methods=['POST'])
def login():
    # الحصول على البيانات المُرسلة من النموذج
    name = request.form['nm']
    return f'<h1>Hello {name}!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
