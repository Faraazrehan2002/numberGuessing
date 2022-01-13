from flask import Flask, render_template, request
import random
app = Flask(__name__)
counter = 0
comp_num = random.randint(1,10)
# Make the WSGI interface available at the top level so wfastcgi can get it
#wsgi_app = app.wsgi_app

@app.route('/',methods = ['GET','POST'])
def guess():
    global counter,comp_num
    message = ""
    if request.method == 'POST':
        counter += 1
        form = request.form
        user_guess = int(form['guess'])
        if comp_num == user_guess:
            message =  "Well done, you got it."
            return render_template("game_over.html",message = message)
        elif comp_num>user_guess:
            message = "Too Low!"
        else:
            message = "Too High!"
        if counter == 3:
            message = "You Failed!"
            return render_template("game_over.html",message = message)
    return render_template("guess.html",message = message)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST','localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT','5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug = True)