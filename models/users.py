class User:
    def __init__(self, display_name, password, email) -> None:
        self.email = email
        self.password = password
        self.display_name = display_name