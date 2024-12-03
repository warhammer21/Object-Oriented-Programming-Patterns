# User class
import hashlib

class User:
    def __init__(self, username, password):
        """Create a new user object. The password will be encrypted before storing."""
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password):
        """Encrypt the password with the username and return the SHA digest."""
        hash_string = (self.username + password).encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        """Return True if the password is valid for this user, False otherwise."""
        return self._encrypt_pw(password) == self.password


# Customer class inheriting from User
class Customer(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def log_in(self):
        """Simulate customer log in."""
        print(f"{self.username} logged in as a customer.")


# Delivery Personnel class inheriting from User
class DeliveryPersonnel(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def accept_order(self):
        """Simulate accepting an order."""
        print(f"{self.username} accepted an order.")


# Admin class inheriting from User
class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def check_menu(self):
        """Simulate checking the menu."""
        print(f"{self.username} is checking the menu.")

    def manage_order(self):
        """Simulate managing an order."""
        print(f"{self.username} is managing orders.")


# Authenticator class
class Authenticator:
    def __init__(self):
        """Manage users logging in and out."""
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)

    def login(self, username, password):
        """Log a user in if the username and password are valid."""
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)
        if not user.check_password(password):
            raise InvalidPassword(username)
        user.is_logged_in = True
        return True  # Login successful

    def is_logged_in(self, username):
        """Check if a user is logged in."""
        user = self.users.get(username)
        return user.is_logged_in if user else False


# Authorizor class
class Authorizor:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, perm_name):
        """Create a new permission."""
        if perm_name in self.permissions:
            raise PermissionError("Permission already exists")
        self.permissions[perm_name] = set()

    def permit_user(self, perm_name, username):
        """Grant the given permission to the user."""
        if perm_name not in self.permissions:
            raise PermissionError("Permission does not exist")
        if username not in self.authenticator.users:
            raise InvalidUsername(username)
        self.permissions[perm_name].add(username)

    def check_permission(self, perm_name, username):
        """Check if a user has a specific permission."""
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        if perm_name not in self.permissions:
            raise PermissionError("Permission does not exist")
        if username not in self.permissions[perm_name]:
            raise NotPermittedError(username)
        return True

    # Placeholder methods for role-specific actions
    def edit_menu_items(self):
        """Placeholder for editing menu items."""
        pass  # Implement role-specific authorization checks here

    def accept_delivery_assignments(self):
        """Placeholder for accepting delivery assignments."""
        pass  # Implement role-specific authorization checks here

    def browse_menus(self):
        """Placeholder for browsing menus."""
        pass  # Implement role-specific authorization checks here

    def place_orders(self):
        """Placeholder for placing orders."""
        pass  # Implement role-specific authorization checks here


# Custom exceptions
class UsernameAlreadyExists(Exception):
    pass

class PasswordTooShort(Exception):
    pass

class InvalidUsername(Exception):
    pass

class InvalidPassword(Exception):
    pass

class PermissionError(Exception):
    pass

class NotLoggedInError(Exception):
    pass

class NotPermittedError(Exception):
    pass
