from flask import Flask , render_template , abort #importing things
from data import roommates ,education_data
from github import get_github_data
from database import get_views, increment_views

app = Flask(__name__) #assigning the variable app

@app.route("/") #routing - /  means home page basically 
def home():
    increment_views()
    views = get_views()
    return render_template("index1.html", people= roommates, views= views ) #people= roommates , basically tells that use the strings in roommates list for the variable 'people'in our html file
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


#routing page for projects
@app.route("/projects/<name>")  #<name>-  placeholder
def projects(name):

    selected_person = None #setting this up so we can handle the error

    for person in roommates: #going thru our list of roommates in data.py
        if person["name"].lower() == name: #since the names stored in roommates are captial
            selected_person = person #assigning a new variable to contain the dict of a person
            break                    #breaking when we do find our person, otherwise it keeps going thru the next roommates for no reason
        
    if selected_person is None:
        abort(404)
    projects = get_github_data(selected_person["github_username"]) #kim - get_github_data- returns  lists containing dictionaries
    return render_template("projects.html",person=selected_person,projects=projects)
    #passing two things to projects.html --> selecte_person (a dict) as person and project(list of dict) as project

if __name__ == "__main__":
    app.run(debug=True)
