from flask import Flask , render_template #importing things

app = Flask(__name__) #assigning the variable app

@app.route("/") #routing - /  means home page basically 
def home():
    roommates =[
    {
        "name": "Sumedh",
        "instagram": "https://www.instagram.com/sumedhg.69/",
        "linkedin": "https://www.linkedin.com/in/sumedh-ghule-790617342/",
        "profile_image": "https://avatars.githubusercontent.com/u/190742018?v=4"
    },
    {
        "name": "Rhitam",
        "instagram": "https://www.instagram.com/rhitxm.exe/",
        "linkedin": "https://www.linkedin.com/in/rhitam-paul-4a58021b4/",
        "profile_image": "https://avatars.githubusercontent.com/u/293724039?v=4"
    } ]#creating a list of people
    return render_template("index.html", people= roommates ) #people= roommates , basically tells that use the strings in roommates list for the variable 'people'in our html file
        #remember - the variable for html --> people , the variable that it is acessing from python-->roommates

    

@app.route("/about") #routing to another page
def about_us():
    return "We are roommates at VESIT"

if __name__ == "__main__":
    app.run(debug=True)