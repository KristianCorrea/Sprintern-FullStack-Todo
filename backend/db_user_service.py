from model import User

from sqlmodel import select, Session



def get_user(user_id: int, session: Session):
    user = session.get(User,user_id)

    if not user:
        return "User does not found"
    return user

def create_user(user: User, session: Session):
    session.add(user)
    session.commit()
    session.refresh()

    return user
def delete_user(user_id : int,session: Session):
    user = session.get(User,user_id) 

    if not user:
        return "User not found!"             
    session.delete(user)
    session.commit()
    return "User has been deleted!"  