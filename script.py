from flask import Flask , render_template , abort #importing things

app = Flask(__name__) #assigning the variable app

@app.route("/") #routing - /  means home page basically 
def home():
    roommates =[
    {
        "name": "Sumedh",
        "instagram": "https://www.instagram.com/sumedhg.69/",
        "linkedin": "https://www.linkedin.com/in/sumedh-ghule-790617342/",
        "profile_image": "https://avatars.githubusercontent.com/u/190742018?v=4",
        "github": "https://github.com/Sumedh2509"
    },
    {
        "name": "Rhitam",
        "instagram": "https://www.instagram.com/rhitxm.exe/",
        "linkedin": "https://www.linkedin.com/in/rhitam-paul-4a58021b4/",
        "profile_image": "https://avatars.githubusercontent.com/u/293724039?v=4",
        "github": "https://github.com/Rhitxm"
    } ]#creating a list of people
    return render_template("index1.html", people= roommates ) #people= roommates , basically tells that use the strings in roommates list for the variable 'people'in our html file
        #remember - the variable for html --> people , the variable that it is acessing from python-->roommates

    

@app.route("/about") #routing to another page
def about_us():
    return "We are roommates at VESIT"

@app.route("/education/<name>") #<name> is a placeholder here  
# so if we do education/sumedh - it will return - Education page for sumedh
def education(name):
    education_data = {
                        "rhitam":{"name":"Rhitam",
                                  "college":"VESIT",
                                  "course": "Automation and robotics",
                                  "10year" : "2023-2024",
                                  "12year": "2025-2026",
                                  "clgyear": "2026-2030"},
                        "sumedh":{"name":"Sumedh", 
                                  "college":"VESIT", 
                                  "course":"Computer engineering",
                                  "10year": "2022-2023",
                                  "12year": "2024-2025",
                                  "clgyear": "2026-2030"} }
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