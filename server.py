#Flask server for emotion detector

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector #the function for emotion detection

app = Flask(__name__) #setting up flask

#Endpoint to emotionDetector
@app.route('/emotionDetector', methods=['GET'])
def emotion_detection():
    text_to_analyze = request.args.get("textToAnalyze", "") #getting the text
    
    #error handling
    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400
    
    result = emotion_detector(text_to_analyze) #calling the API
    response_text = (f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, "
                     f"'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. "
                     f"The dominant emotion is {result['dominant_emotion']}.")
    
    return jsonify({"response": response_text})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)