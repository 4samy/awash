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
            "status",
            "food_type",
            "food_quantity",
            "pickup_time",
            "shelter",
            "restaurant",
            "driver"
        )

        ordered = True

    id = fields.Int(required=True)
    restaurant_id = fields.Int(required=True)
    driver_id = fields.Int(required=False)
    date_created = fields.DateTime(format='%m/%d/%Y')
    delivered = fields.Bool(required=False)
    point_value = fields.Int(required=False)
    driver_eta_restaurant = fields.Int(required=False)
    driver_eta_dropoff = fields.Int(required=False)
    status = fields.Str(required=False)
    food_type = fields.Str(required=False)
    food_quantity = fields.Str(required=False)
    pickup_time = fields.Str(required=False)
    shelter = fields.Str(required=False)
    restaurant = fields.Nested(RestaurantSchema, only=("id", "email", "name", "address", "phone_number"))
    driver = fields.Nested(DriverSchema, only=("id", "email", "first_name", "last_name", "car_description", "reward_points"))
