from api import db


class Draw(db.Model):
    draw_date = db.Column(db.Date, primary_key=True)
    number_1 = db.Column(db.Integer)
    number_2 = db.Column(db.Integer)
    number_3 = db.Column(db.Integer)
    number_4 = db.Column(db.Integer)
    number_5 = db.Column(db.Integer)
    number_6 = db.Column(db.Integer)
    number_complementary = db.Column(db.Integer)

    def to_dict(self):
        return {
            "draw_date": str(self.draw_date.strftime('%Y-%m-%d')),
            "number_1": self.number_1,
            "number_2": self.number_2,
            "number_3": self.number_3,
            "number_4": self.number_4,
            "number_5": self.number_5,
            "number_6": self.number_6,
            "number_c": self.number_complementary
        }
