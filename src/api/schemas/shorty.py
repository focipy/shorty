from marshmallow import Schema, fields


class ShortyPostSchema(Schema):
    url = fields.Url(required=True)
    custom = fields.String()
