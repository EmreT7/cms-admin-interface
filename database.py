import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask import Flask

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wordFirstLang = db.Column(db.String(100), nullable=False)
    sentenceFirstLang = db.Column(db.String(500))
    wordSecondLang = db.Column(db.String(100), nullable=False)
    sentenceSecondLang = db.Column(db.String(500))

    def to_dict(self):
        return {
            'id': self.id,
            'wordFirstLang': self.wordFirstLang,
            'sentenceFirstLang': self.sentenceFirstLang,
            'wordSecondLang': self.wordSecondLang,
            'sentenceSecondLang': self.sentenceSecondLang
        }

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'
    db.init_app(app)

    with app.app_context():
        db.create_all()
        if Word.query.count() == 0:
            with open('initial_data.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data:
                    word = Word(
                        wordFirstLang=item['wordFirstLang'],
                        sentenceFirstLang=item['sentenceFirstLang'],
                        wordSecondLang=item['wordSecondLang'],
                        sentenceSecondLang=item['sentenceSecondLang']
                    )
                    db.session.add(word)
            db.session.commit()
            print("Initial data loaded")

def get_db():
    return db