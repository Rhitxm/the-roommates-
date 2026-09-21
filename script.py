from flask import Flask , render_template , abort #importing things
from data import roommates ,education_data, skills_data
from github import get_repo_data
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

#routing page for skills
@app.route("/skills/<name>")
def skills(name):
    selected_skills = skills_data.get(name)
    name = name.capitalize()
    if selected_skills is None:
        return abort(404)
    return render_template("skills.html", skills = selected_skills , name = name)

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
    projects = [] #creating a list to store projects 
    for project in selected_person["projects"]: #iterates thru the dicts inside the list projects which is inside roommates (main list) (which is inside the data.py)
        data = get_repo_data(project["owner"], project["repo"]) # keep in mind - data is a dictionary
        if data is not None:
            projects.append(data) #appending those dictionaries inside our projects
    return render_template("projects.html",person=selected_person,projects=projects)
    # passing selected_person as the variable person and projects as projects in projects.html

@app.errorhandler(404)  #this is what runs whenever this certain error occurs anywhere in our page
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
