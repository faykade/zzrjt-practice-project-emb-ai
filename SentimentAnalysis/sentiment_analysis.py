"""
The module that contains sentiment analysis tools that interface with Watson
"""
import json
import requests

# Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
def sentiment_analyzer(text_to_analyse):
    """
    the function that calls the watson AI with text to get a sentiment
    """
    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Create a dictionary with the text to be analyzed
    # Set the headers required for the API request
    header = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers = header, timeout=5000)

    label = None
    score = None

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']

    return {
        'label': label,
        'score': score
    }  # Return the response text from the API
