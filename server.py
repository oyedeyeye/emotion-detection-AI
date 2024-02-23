"""
Executing this function initiates the application of emotion detector
to be executed over the Flask channel and deployed on localhost:5000.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def render_index_page():
    """returns the index page of the app"""
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_analyzer():
    """
    This code receives the text from the HTML interface and 
    runs emotion detection over it using emotion_detector()
    function. The output returned shows the dominant emotion and its  
    score for the provided text.
    """
    # Get text input from request argument
    text_to_analyze = request.args.get('textToAnalyze')

    # Run Emotion Detector on the text
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        response_text = "Invalid text! Please try again!"
    else:
        response_text = f"For the given statement, the system response is 'anger': \
                        {result['anger']}, 'disgust': {result['disgust']}, 'fear': \
                        {result['fear']}, 'joy': {result['joy']} and 'sadness': \
                        {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."

    return response_text


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
