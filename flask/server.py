from flask import Flask

app = Flask(__name__)

@app.route('/evo_id')
def evo_id():
    with open("evo_id/evo_id.txt","r") as file:
        sess_id = file.read()
        file.close()
    return sess_id

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')