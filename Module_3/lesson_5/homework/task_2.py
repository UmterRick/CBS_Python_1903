class Contact:
    def __init__(self, surname, name, mob_phone, email):
        self.surname = surname
        self.name = name
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        return f"{self.name} {self.surname} ({self.email}) - {self.mob_phone}"

    def sent_message(self, message):
        print("\nSending...")
        print(f"'{message}' to {self.mob_phone}")
        print("Delivered")


class UpdateContact(Contact):
    def __init__(self, surname, name, mob_phone, email, job):
        super().__init__(surname, name, mob_phone, email)
        self.job = job

    def get_message(self, message, sender):
        print("\nGot new message")
        print(f"{sender}: {message}")


upd_contact = UpdateContact("Surname", "Name", 380671112233, "surname_name@gmail.com", "Manager")
if __name__ == "__main__":
    print(upd_contact.__dict__)
    print(upd_contact.__class__.__base__)
    print(upd_contact.__class__.__bases__)
