from flask import Flask, redirect, url_for                  #here we are importing from flask - this isn't working right now but I am not sure why

data = {}                                                   #this is an empty dictionary list called data
i = 0                                                       # i is a variable which equals 0 at the moment

app = Flask(__name__)                                       #this is basically defining the app and where the functionality is saved - get more info on this

@app.route('/')                                             #app route is a decorator - this is basically defining the different routes that you can have on your webpage. Within them you can define functions and responses
def home():
    return data                                             #currently this function is returning 'data', which is the empty dictionary list. i.e. when you go to the homepage, you will see the dictionary

@app.route('/create/<message>')                             #these<> marks mean that you can input your own message in the search bar of your browser
def create(message):                                        #this function is called create, and the input message above is called as it's value
    global i                                                #what does global i mean?
    data[i] = message                                       #this is adding for each i variable, the message input. i.e. at 0 key, the value will be the first message
    i += 1                                                  #this is adding 1 to the i variable each time the method is run, so that now the next message will be 1
    return message + " added to dict"                       #each time the function is run, it will return the input message and the phrase "added to dict"

@app.route('/update/<int:i>/<newmessage>')                  #this is another route which we will use to update the message - because we are asking for a number i.e. the index number for the dict, we need to make this an int as demonstrated
def update(i, newmessage):                                  #this is the update function with 2 parameters - the number, and the updated message
    data[i] = newmessage                                    #this finds the number within the 'data' list and updates it with the new message
    return "Updated entry"                                  #this shows the message "updated entry"

@app.route('/delete/<int:i>')                               #this is another route - delete - again it is asking for a number because we want to delete the key associated with that number
def delete(i):                                              #this delete function just looks for one parameter - the number of the key to be deleted
    data.pop(i)                                             #this is removing from the 'data' dictionary the corresponding key
    return "Deleted entry"                                  #this shows the message 'deleted entry'

if __name__ == '__main__':                                  #this tells the python interpreter that if the name is the main file, then it should be run, with the debugging option and the host is public on the internet
    app.run(debug=True, host='0.0.0.0')