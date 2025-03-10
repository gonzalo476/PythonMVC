class User:
    def __init__(self, user_id=None, name="", email="", phone=""):
        self.id = user_id
        self.name = name
        self.email = email
        self.phone = phone

    def to_dic(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
        }

    @classmethod
    def from_dic(cls, data):
        return cls(
            user_id=data.get("id"),
            name=data.get("name", ""),
            email=data.get("email", ""),
            phone=data.get("phone", ""),
        )
