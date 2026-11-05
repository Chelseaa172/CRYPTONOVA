from crypto.encryption import generate_key


class KeyManager:

    def __init__(self):
        self.keys = {}
        self.active_key_id = None

    def create_key(self):

        if self.active_key_id:
            self.keys[self.active_key_id]["status"] = "retired"

        key_id = f"KEY-{len(self.keys) + 1}"
        key = generate_key()

        self.keys[key_id] = {
            "key": key,
            "status": "active"
        }

        self.active_key_id = key_id

        return key_id

    def rotate_key(self):
        old_key_id = self.active_key_id
        new_key_id = self.create_key()

        return old_key_id, new_key_id

    def get_active_key(self):
        return self.keys[self.active_key_id]["key"]

    def get_key(self, key_id):
        if key_id not in self.keys:
            raise ValueError("Kunci tidak ditemukan!")

        return self.keys[key_id]["key"]