from marshmallow import Schema, fields
# from .models import Driver


class DriverSchema(Schema):

    class Meta:
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "car_description",
            "reward_points"
        )

        ordered = True

    id = fields.Int(required=True)
    email = fields.Email(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=False)
    phone_number = fields.Int(required=True)
    car_description = fields.Str(required=False)
    reward_points = fields.Int(required=False)
