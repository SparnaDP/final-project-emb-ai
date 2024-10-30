import json
import requests

def emotion_detector(text_to_analyze):
    URL = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    HEADER = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    mytext = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, headers = HEADER, json = mytext, timeout = 5)
    if(response.status_code == 400):
        return {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
        }
    formatted_response = json.loads(response.text)
    scores = formatted_response["emotionPredictions"][0]["emotion"]
    scores["dominant_emotion"] = max(scores, key = scores.get)
    return scores
