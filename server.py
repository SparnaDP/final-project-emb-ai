''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using the emotion_detector()
        function. The output returned shows the emotional score and its 
        dominant for the provided text.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    scores = emotion_detector(text_to_analyze)
    if not scores:
        return "Invalid input ! try again."
    if not scores["dominant_emotion"]:
        return "Invalid input ! try again."
    return (
        f"For the given statement, the system response is 'anger': {scores['anger']}, "
        f"'disgust': {scores['disgust']}, 'fear': {scores['fear']}, 'joy': {scores['joy']} and "
        f"'sadness': {scores['sadness']}. The dominant emotion is {scores['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
