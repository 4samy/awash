import settings

from app.extensions import db


class Rewards(db.Model):
    __tablename__ = "rewards"

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(
        db.Integer, db.ForeignKey("restaurants.id"),
        nullable=False
    )
    point_cost = db.Column(db.Integer, nullable=False, default=0)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"<Rewards id: {self.id}>"
