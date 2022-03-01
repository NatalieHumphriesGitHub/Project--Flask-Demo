from application import db                                      #db is the database - we have things defined in init it is considered the folder i.e. application which is why it imports from there
                                                                #save this file within applications
class Todo(db.Model):                                           #creating a class db.model contains the functionality to create the tables
    pk = db.Column(db.Integer, primary_key = True)              #we just always need to define it as db.whatever it is 
    title = db.Column(db.String(30))
    desc = db.Column(db.String(100))
    status = db.Column(db.String(4))
    proj_id = db.Column(db.Integer, db.ForeignKey('project.pk'))#this is saying that the project id is referencing the primary key of the Project class
    def __str__(self):                                          #this function means that it is going to return a string
        return f"{self.title}:\n{self.desc}: {self.status}"     #this is the sentence that it will return when you reference it in the routes     




class Project(db.Model):                                        #we're making another table here which also inherits from db.Model
    pk = db.Column(db.Integer, primary_key = True)              #these are the columns that we need 
    project_name = db.Column(db.String(30))
    due_date = db.Column(db.Date)
    proj_items = db.relationship('Todo', backref='project')         #relationship doesn't have a capital, everything else after db. does!
    def __str__(self):
        return f"{self.project_name}, due {self.due_date}"


#one to many relationship - one project will have many todos so that makes that the project primary key is going to be the foreign key in the todo class