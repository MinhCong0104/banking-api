import datetime
from mongoengine import Document, StringField, DateTimeField, ImageField, FloatField, ListField



class Transaction(Document):
    date = DateTimeField(required=True)
    location = StringField(required=False)
    amount = FloatField(required=True)
    player = ListField(required=True)

    created_at = DateTimeField(required=True)
    updated_at = DateTimeField(required=False)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()
        return super(Transaction, self).save(*args, **kwargs)

    @classmethod
    def from_mongo(cls, data: dict, id_str=False):
        """We must convert _id into "id". """
        if not data:
            return data
        id = data.pop("_id", None) if not id_str else str(data.pop("_id", None))
        if "_cls" in data:
            data.pop("_cls", None)
        return cls(**dict(data, id=id))

    meta = {
        "collection": "Transactions",
        "indexes": ["date"],
        "allow_inheritance": True,
        "index_cls": False,
    }
