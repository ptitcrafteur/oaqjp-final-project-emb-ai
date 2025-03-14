#Callin Watson API for emotion detection

import requests #for API calls
import json #easier to work with JSON

"""Function that takes a String (text_to_anlyze)
    Runs the text through AI to detect emotions
    return a string (text) from the AI object response"""
def emotion_detector(text_to_analyze):
    #We gather the url + header + payload for the call of the API
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, headers=headers, json=payload) #callin the API

    #if API call was a success we return the text response
    if response.status_code == 200:
        data = json.loads(response.text)
        predictions = data.get("emotionPredictions", [])
        
        if predictions:
            emotions = predictions[0].get("emotion", {})
            
            anger = emotions.get("anger", 0)
            disgust = emotions.get("disgust", 0)
            fear = emotions.get("fear", 0)
            joy = emotions.get("joy", 0)
            sadness = emotions.get("sadness", 0)
            
            dominant_emotion = max(emotions, key=emotions.get) if emotions else "unknown"
            
            return {
                "anger": anger,
                "disgust": disgust,
                "fear": fear,
                "joy": joy,
                "sadness": sadness,
                "dominant_emotion": dominant_emotion
            }
    #otherwise we return the error status code
    else:
        return {"error": f"Request failed with status code {response.status_code}"}