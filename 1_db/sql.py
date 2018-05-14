from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jingdian:jingdian@127.0.0.1/yinhublog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

"""
Usage:
python
>> from sqlite import db
>> from sqlite import User
>> db.create_all()
>> 
>> test = User(username="test", email="test@cn.ibm.com")
>> db.session.add(test)
>> db.session.commit()
>>
>> db.session.delete(test)
>> db.session.commit()

>> User.query.all()
>>
>> db.drop_all()
"""


"""
Integer		int
SmallInteger	int
BigInteger	int or long
Float		float
Numeric		decimal.Decimal
String		str
Text		str
Unicode		unicode
UnicodeText	unicode
Boolean		bool
Date		datetime.date
Time		datetime.time
DateTime	datetime.datetime
Interval	datetime.timedelta
Enum		str
PickleType	Any python object
LargeBinary	str
"""

