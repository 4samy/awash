import settings

from app.extensions import db


class FoodRequest(db.Model):
    __tablename__ = "food_requests"

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(
        db.Integer, db.ForeignKey("restaurants"),
        nullable=False
    )
    restaurant = db.relationship("Restaurant", lazy="subquery")
    driver_id = db.Column(
        db.Integer, db.ForeignKey("drivers"),
        nullable=True
    )
    driver = db.relationship("Driver", lazy="subquery")
    date_created = db.Column(db.DateTime(timezone=True))
    delivered = db.Column(db.Boolean, nullable=False, default=False)
    point_value = db.Column(db.Integer, nullable=False, default=0)

    @staticmethod
    def identify(food_request_id):
        return FoodRequest.query.get(food_request_id)





