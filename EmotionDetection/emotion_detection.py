import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyze):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the Emotion Predict analysis service
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
     # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        # Extract the required set of emotions, including anger, disgust, fear, joy and sadness, 
        # along with their scores.
        emotions_dict = formatted_response['emotionPredictions'][0]['emotion']

        # Find the dominant emotion, which is the emotion with the highest score
        emotion_max_score = 0
        emotion_with_max_score_key = None
        for key, value in emotions_dict.items():
            if value > emotion_max_score:
                emotion_max_score = value
                emotion_with_max_score_key = key
        # print(f"Dominant emotion is {emotion_with_max_score_key} with value of: {emotion_max_score}")
        return {
            'anger': emotions_dict['anger'],
            'disgust': emotions_dict['disgust'],
            'fear': emotions_dict['fear'],
            'joy': emotions_dict['joy'],
            'sadness': emotions_dict['sadness'],
            'dominant_emotion': emotion_with_max_score_key
        }  # Return the response text from the API
    # If the response status code is 400, set results to None
    elif response.status_code == 400:
        return{
            'anger' : None,
            'disgust' : None,
            'fear' : None,
            'joy' : None,
            'sadness' : None,
            'dominant_emotion' : None
        }
