from application import app                                                 #this is importing the app function from the application folder - should be saved outwith the application folder

if __name__ == '__main__':                                                  #this is means it will run if the file is the main folder and will debug and host it on an open i.p. address
    app.run(debug=True, host='0.0.0.0')                                     #make sure you run your create file first to create the database