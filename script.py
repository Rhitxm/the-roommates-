from flask import Flask , render_template , abort #importing things
from data import roommates ,education_data

app = Flask(__name__) #assigning the variable app

@app.route("/") #routing - /  means home page basically 
def home():
    #creating a list of people
    return render_template("index1.html", people= roommates ) #people= roommates , basically tells that use the strings in roommates list for the variable 'people'in our html file
        #remember - the variable for html --> people , the variable that it is acessing from python-->roommates

    

@app.route("/about") #routing to another page
def about_us():
    return "We are roommates at VESIT"

@app.route("/education/<name>") #<name> is a placeholder here  
# so if we do education/sumedh - it will return - Education page for sumedh
def education(name):
     
    # data_of = education_data[name] --this can throw a key error when we don't use the keys that we have already established
    data_of = education_data.get(name) #this is better, as we know - if we don't have the key established it returns none
    if data_of is None:
        abort(404)
    return render_template("education.html", person= data_of)

# @app.route("/temp")
# def temporary():
#     return render_template("/Rhitameducation.html")

if __name__ == "__main__":
    app.run(debug=True)

