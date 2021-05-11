from marshmallow import Schema, fields
from app.modules.driver.schemas import DriverSchema
from app.modules.restaurant.schemas import RestaurantSchema


class FoodRequestSchema(Schema):

    class Meta:
        fields = (
            "id",
            "restaurant_id",
            "driver_id",
            "date_created",
            "delivered",
            "point_value",
            "driver_eta_restaurant",
            "driver_eta_dropoff",
            "restaurant",
            "driver"
        )

        ordered = True

    id = fields.Int(required=True)
    restaurant_id = fields.Int(required=True)
    driver_id = fields.Int(required=False)
    date_created = fields.DateTime()
    delivered = fields.Bool(required=False)
    point_value = fields.Int(required=False)
    driver_eta_restaurant = fields.Int(required=False)
    driver_eta_dropoff = fields.Int(required=False)
    restaurant = fields.Nested(RestaurantSchema, only=("id", "email", "name", "address", "phone_number"))
    driver = fields.Nested(DriverSchema, only=("id", "email", "first_name", "last_name", "car_description", "reward_points"))
