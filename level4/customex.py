#Create a custom exception

class InvalidAgeError(Exception):
    pass


def register_user(age):

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")

    print("Registration successful!")


try:
    register_user(19)

except InvalidAgeError as error:
    print("Error:", error)