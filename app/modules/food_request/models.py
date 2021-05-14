import settings

from app.modules.utils import utcnow_datetime_aware
from app.extensions import db

STATUS_DEFAULT = "Pending Driver Accept"


class FoodRequest(db.Model):
    __tablename__ = "food_requests"

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(
        db.Integer, db.ForeignKey("restaurants.id"),
        nullable=False
    )
    # restaurant = db.relationship("Restaurant", lazy="subquery")
    driver_id = db.Column(
        db.Integer, db.ForeignKey("drivers.id"),
        nullable=True
    )
    # driver = db.relationship("Driver", lazy="subquery")
    date_created = db.Column(
        db.DateTime(timezone=True),
        default=utcnow_datetime_aware,
        nullable=False
    )
    delivered = db.Column(db.Boolean, nullable=False, default=False)
    point_value = db.Column(db.Integer, nullable=False, default=10)
    driver_eta_restaurant = db.Column(db.Integer)
    driver_eta_dropoff = db.Column(db.Integer)
    status = db.Column(db.Text, nullable=True, default=STATUS_DEFAULT)
    food_type = db.Column(db.String(256), nullable=True)
    food_quantity = db.Column(db.String(254), nullable=True)
    pickup_time = db.Column(db.String(60), nullable=True)
    shelter = db.Column(db.String(254), nullable=True)

    @staticmethod
    def identify(food_request_id):
        return FoodRequest.query.get(food_request_id)

    # def __init__(self, **kwargs):
    #     """Creates Food Request Object"""

    def __repr__(self):
        return f"<Food Request id: {self.id}>"

