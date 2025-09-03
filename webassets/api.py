from flask import Flask,request,jsonify,render_template,Response,stream_with_context
from gemini import aiResponse 
from SharpText import sharp_text
from datetime import datetime,date
import json
import os

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process',methods=['POST'])
def process_text():
    data = request.get_json()
    user_input = data.get('user','')
    
    if (user_input.lower() == 'exit'):
        exit()
    def generate_stream():
        ai_response = ""
        chat_history = []
        chat_history_dir = "chats/chat_history.json"
        if(os.path.exists(chat_history_dir)) and os.path.getsize(chat_history_dir) > 0:
            with open(chat_history_dir,'r',encoding='utf-8') as ch:
                chat_history = json.load(ch)
        for chunk in aiResponse(user_input,chat_history):
            ai_response += sharp_text(chunk.text)
            yield sharp_text(chunk.text)
        # chat = {
        #     "time": datetime.now().strftime("%H:%M"),
        #     "date": date.today().strftime("%d/%m/%Y"),
        #     "previous conversation":[
        #         {
        #             "user": user_input,
                    
        #         }
        #     ],
        # }
        chat = {
            "time": datetime.now().strftime("%H:%M"),
            "date": date.today().strftime("%d/%m/%Y"),
            "user": user_input,
            "ai": ai_response
        }

        chat_history.append(chat)

        with open(chat_history_dir,'w',encoding="utf-8") as ch:
            json.dump(chat_history, ch, ensure_ascii=False, indent=4)

    return Response(
        stream_with_context(generate_stream()), 
        content_type={"Content-Type": "text/plain"},
        mimetype="text/event-stream"
    )
    

if __name__ == '__main__':
    app.run(debug=True,port=5012)