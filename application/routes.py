from datetime import timedelta                                                      #save this file within applications
from flask import redirect, url_for, render_template                                               #this file basically is here to separate all the routes into a different file
from application import app, db                                                     #this is importing the app file and the db (the db is imported from the init file but that basically means that it is being imported from the application folder)
from application.models import Project, Todo                                        #this is importing from the models file, the todo class (which is basically the definition of our table)
from datetime import date, timedelta                                                #this is importing the time/date rules that we need


@app.route('/')                                                                         #this is the basic route of /
def home():
    return render_template ('index.html')
    #return f"{Todo.query.count()} todos: " + '<br>'.join(str(t.project) + " ," + str(t) for t in Todo.query.all())    #this is bringing back all the queries for the "Todo" class but you can limit them too i.e. query.limit(5).all()) would bring back 5 
                                                                                                #the first part is counting the number of queries so this will show everything in the table. The str(t.project) bit is referring back to the project name
                                                                                                #this string is joined by a line-break('<br>') for ever line in the todo class
@app.route('/search=<keyword>')                                                 #this is an example that he couldn't finish 
def search(keyword):
    data = db.session.execute(f"SELECT * FROM todo WHERE desc LIKE '%{keyword}%'")
    return '<br>'.join([str(res) for res in data])

@app.route('/done')                                                                             #this route will now filter out all the done todos because of the below filter
def done():                                                                                                     
    return '<br>'.join(str(t) for t in Todo.query.filter_by(status = 'done').order_by(Todo.title.desc()).all())   #this will take us to a route where the filter is status = done, you can also add a couple of filters using a comma as a separator
                                                                                            #this will order it by title - you need to put the class.attribute name and .desc gives it descending order           
                                                                                            # we are not allowed to return a query object in flask, so we need to loop it through to return the answer as a string - i.e. for t in Todo

@app.route('/create/<int:pnum>/<title>/<desc>')                    #this route is called create and it allows you to update the title and the description - denoted by <>. These have been defined in the models file
def create(pnum, title, desc):                                #this function is called create and it requires a title and desc parameter and project number (which will be input as above)
    todo = Todo(title=title, desc=desc, status='todo', proj_id = pnum)  #this is defining the variable todo which pulls from the Todo class - the default for status is todo - this creating a new record
    db.session.add(todo)                                #this is adding the todo variable that we just created to the database - the db.session is a scoped connection to the db - we don't need a session for queries but we need it if we want to change anything in the tables
    db.session.commit()                                 #this db.session saves it to the table so this will always go hand in hand with the above
    return redirect(url_for('home'))                    #this will return us to home which shows all the todos


@app.route('/create-proj/<name>')
def create_project(name):
    new_proj = Project(project_name = name, due_date = date.today() + timedelta(30))  #we don't need to define the proj_id because it is a primary key, so it will be set automatically
    db.session.add(new_proj)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/update/<int:i>/<newstatus>')               #this route updates the status - it is asking for a number <int:i> (this i could be anything, we're just defining it now) and a new status
@app.route('/update/<int:i>/<newtask>/<newstatus>')     #this routes updates the status and the task title - both these routes are going to lead to the same function
def update(i, newstatus, newtask = None):               #defining multiple routes and setting default val in function def allows the user to either update just the status, or update the task description and status
    todo = Todo.query.get(i)                            #defining the todo variable as a query and pull out the record that corresponds to the i number, which is the primary key
    if newtask:                                         #if there is a new task title
        todo.title = newtask                            #set title to new task title
    todo.status = newstatus                             #otherise just set status to new status
    db.session.commit()                                 #save it to the database 
    return redirect(url_for('home'))                    #return the home url

@app.route('/delete/<int:i>')                           #this route allows you to delete the task by asking for the task number
def delete(i):                                          #delete function just needs one parameter - the task number which we have defined as i (could be anything)
    todo = Todo.query.get(i)                            #defining the todo variable as the record associated with the number
    db.session.delete(todo)                             #allows you to delete the variable
    db.session.commit()                                 #saves it to the database
    return redirect(url_for('home'))