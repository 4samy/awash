from marshmallow import Schema, fields
from app.modules.restaurant.schemas import RestaurantSchema


class RewardsSchema(Schema):

    class Meta:
        fields = (
            "id",
            "restaurant_id",
            "point_cost",
            "description",
            "restaurant"
        )

        ordered = True

    id = fields.Int(required=True)
    restaurant_id = fields.Int(required=True)
    point_cost = fields.Int(required=True)
    description = fields.Str(required=False)
    restaurant = fields.Nested(RestaurantSchema, only=("id", "email", "name", "address", "phone_number"))
