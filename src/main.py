from flask import Flask, render_template, request #imports Flask; render_template() allows us to use html
                                                  #in another file; request takes info from form

app = Flask(__name__) #build a variable from our Flask object

#now we are going to start building routes, which are ways that we interact
@app.route('/') #'/' indicates the home page of our flask application
def index(): #declaring a function
    return render_template("index.html") #connects whatever is in our index.html file to the return statement here

@app.route("/AddNew", methods=["POST"]) #if we have a url that contains /AddNew, then we route to this page
def AddNew(): #this function tells us what will happen if the url contains /AddNew
    name = request.form["Name"] #comes from request import
    email = request.form["Email"] #comes from request import

    with open("src/data.csv", "a") as f: #a = append, so appending to data.csv; f is just a placeholder name for an object
        f.write(f"{name}, {email}\n") #write these attributes to object f and then add to data.csv file


    print(name, email) #print to screen to check and see if name and email were added
    return "Added"

app.run(debug=True) #runs the web server; debug command provides info on what is going on whenever something occurs