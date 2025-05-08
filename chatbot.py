import google.generativeai as ai
from flask import Flask, request,jsonify
from  flask_cors import CORS
app=Flask(__name__)
CORS(app)
mykey="AIzaSyCgsaeJpuqRZcvu_ZaqhGnCNWYNVjBlscY"
ai.configure(api_key=mykey)

model=ai.GenerativeModel("gemini-1.5-pro")
@app.route('/chat', methods=['Get'])
def chat():
    msg=request.args.get("message")
    if not msg:
        return jsonify({'error': 'Messge text required'}), 400
    chat=model.start_chat()
    result=model.start_chat()
    result=chat.send_message(msg)
    answer=result.text
    return jsonify({'response': answer})


if __name__=='__main__':
    app.run(debug=True)