from flask import Flask, redirect, url_for

todos = {}                                              #defining an empty dictionary list
i = 0                                                   #defining our first variable as i - this will be our primary key for the dictionary

app = Flask(__name__)

@app.route('/')                                         #this route is just /
def home():                                             #all this function does is return the dictionary list todos
    return todos

@app.route('/create/<task>')                            #this route allows you to create a task - the input possible is denoted by <task>
def create(task):                                       #this function is create a task and asks for one parameter - the task input
    global i                                            #need to understand global i
    todos[i] = {"task":task, "status":"todo"}           #todos is the dictionary and i is the  key i.e. 0 for the beginning and it is adding two values to the key - the task and the status
    i += 1                                              #this is increasing the variable of i each time
    return redirect(url_for('home'))                    #this is going to return you to the homepage which will show you the updated dictionary - using the the url_for function

@app.route('/update/<int:i>/<newstatus>')               #this route allows you to update your task status - it is asking for the key number i.e. 0, 1, etc as an integer and then the new status
@app.route('/update/<int:i>/<newtask>/<newstatus>')     #this route allows you to update your key number with a new task and status. Both routes lead to the same function.
def update(i, newstatus, newtask = None):               #defining multiple routes and setting default val in function def allows the user to either update just the status, or update the task description and status
    if not newtask:                                     #this is saying, if there no new task, the newtask variable = the previous task input
        newtask = todos[i]["task"]                      
    todos[i] = {"task":newtask, "status":newstatus}     #and so then, update the todos list with the task and the status
    return redirect(url_for('home'))                    #this is again returning you to the home url to see the new list    

@app.route('/delete/<int:i>')                           #this route allows you to delete a value and key - it is asking for the input of an integer
def delete(i):                                          #this function is called delete and is asking for one parameter, the number of the task
    todos.pop(i)                                        #this removes the key and it's values
    return redirect(url_for('home'))                    #this is again returning you to the home url to see the new list 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')