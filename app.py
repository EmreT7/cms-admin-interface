from flask import Flask, render_template, request, jsonify
from database import init_db, get_db, Word

app = Flask(__name__)
init_db(app)

@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 20  # Number of items per page
    db = get_db()
    pagination = Word.query.paginate(page=page, per_page=per_page, error_out=False)
    words = pagination.items
    return render_template('index.html', words=words, pagination=pagination)

@app.route('/search')
def search():
    query = request.args.get('query', '')
    db = get_db()
    words = Word.query.filter(Word.wordFirstLang.contains(query) |
                              Word.wordSecondLang.contains(query)).all()
    return jsonify([word.to_dict() for word in words])

@app.route('/update', methods=['POST'])
def update_word():
    data = request.json
    db = get_db()
    word = Word.query.get(data['id'])
    if word:
        word.wordFirstLang = data['wordFirstLang']
        word.sentenceFirstLang = data['sentenceFirstLang']
        word.wordSecondLang = data['wordSecondLang']
        word.sentenceSecondLang = data['sentenceSecondLang']
        db.session.commit()
        return jsonify({'success': True})
    return jsonify({'success': False, 'error': 'Word not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

