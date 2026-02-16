import requests
import json

def sentiment_analyzer(text_to_analyze):
    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    # Headers required for the API request
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    # Dictionary with the text to be analyzed
    objc = { "raw_document": { "text": text_to_analyze } }

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = objc, headers = header)
    # Return the response text from the API
    formatted_response = json.loads(response.text)
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']

    return {'label': label, 'score': score}