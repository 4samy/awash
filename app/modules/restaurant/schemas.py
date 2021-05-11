from marshmallow import Schema, fields
# from .models import Restaurant


class RestaurantSchema(Schema):

    class Meta:
        fields = (
            "id",
            "email",
            "name",
            "address",
            "phone_number"
        )

        ordered = True

    id = fields.Int(required=True)
    email = fields.Email(required=True)
    name = fields.Str(required=True)
    address = fields.Str(required=False)
    phone_number = fields.Int(required=False)
