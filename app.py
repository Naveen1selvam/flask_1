from flask import Flask

FAI=Flask(__name__)

@FAI.route('/wish')
def wish():
    return 'Hi Naveen'

@FAI.route('/wish2')
def wish2():
    return 'Welcome to Flask Project'

if __name__=='__main__':

    FAI.run(debug=True)