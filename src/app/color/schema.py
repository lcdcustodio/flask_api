from marshmallow import fields, Schema


class ColorSchema(Schema):

    color = fields.String(attribute="color")
    value = fields.String(attribute="value")
