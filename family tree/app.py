# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/" , endpoint='home')
def home():

    name = "Ishika" # write your name
    age = "13" # write your age  

    return render_template('index.html' , name = name , age = age)

@app.route("/father" , endpoint='fatherpage')
def fatherpage():

    name = "Dad" # write your name
    age = "49" # write your age  

    return render_template('father.html' , name = name , age = age)

@app.route("/mother" , endpoint='motherpage')
def motherpage():

    name = "Mom" # write your name
    age = "48" # write your age  

    return render_template('mother.html' , name = name , age = age)

@app.route("/friend", endpoint='friendpage')
def friendpage():

    name = "Friend" # write your name
    age = "13" # write your age  

    return render_template('friend.html' , name = name , age = age)


# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
