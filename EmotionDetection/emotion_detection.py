"""
emotion_detector: function that return analysis of emotion in input text
"""
import requests
import json


#Emotion Detector function
def emotion_detector(text_to_analyze):
    """Returns analysis of emotion in input text

        Arguments:
            text_to_analyze: string dict that is to be analyzed
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    my_obj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=my_obj, headers=header, timeout=360)
    # Convert Response text to json
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        # Extract Emotion dict from the formatted json response
        emotion = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotion['anger']
        disgust_score = emotion['disgust']
        fear_score = emotion['fear']
        joy_score = emotion['joy']
        sadness_score = emotion['sadness']

        # Compute the dominant emotion with the highest score
        dominant_emotion = max(emotion, key=lambda score: emotion[score])

    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    # formatted emotion predictor object/dict
    emotion_predictor = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

    return emotion_predictor
