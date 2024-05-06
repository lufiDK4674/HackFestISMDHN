from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
sentiment_pipeline = pipeline("sentiment-analysis" , model = "cardiffnlp/twitter-roberta-base-sentiment")

@app.route('/predict_sentiment', methods=['POST'])
def predict_sentiment():
    data = request.json
    text = data['text']
    result = sentiment_pipeline(text)
    sentiment_label = label_mapping[result[0]['label']]
    sentiment_score = result[0]['score']
    sentiment_score_rank = score_to_rank(sentiment_label, sentiment_score)
    return jsonify({
        'sentiment': sentiment_label,
        'score_rank': sentiment_score_rank
    })

if __name__ == '__main__':
    app.run(debug=True)
