from user import User
import datetime
from datetime import datetime
from UserUtil import UserUtil
from UserService import UserService

if __name__ == "__main__":
    user = User(
        user_id=230102005,
        name="Nazik",
        surname="Abdrakhmanova",
        birthday=datetime.strptime("2005-11-05", "%Y-%m-%d")
    )

    user.email = UserUtil.generate_email(user.name, user.surname, "example.com")
    user.password = UserUtil.generate_password()

    UserService.add_user(user)

    print(user.get_details())
    print(f"Age: {user.get_age()}")
