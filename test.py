from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import IntegrityError

engine = create_engine('sqlite:///tasks.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Define Models

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=True)
    description = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="tasks")

Base.metadata.create_all(engine)

def get_user_by_email(email):
    return session.query(User).filter_by(email=email).first()

def confirm_action(prompt):
    return input(prompt+ " (yes/no):").strip().lower() == 'yes'

def add_user(name, email)-> bool:
    user = User(name=name, email=email)
    if get_user_by_email(email):
        print("User with that email already exists.")
        return False
    try:
        session.add(user)
        session.commit()
        print(f"User {name} created successfully.")
        return True
    except IntegrityError:
        session.rollback()
        print("An error occurred. Please try again.")
        return False


def add_task(email, title, description):
    user = get_user_by_email(email)
    if not user:
        print("User not found.")
        return False
    try:
        session.add(Task(title=title, description=description, user=user))
        session.commit()
        print(f"Task created successfully.")
        return True
    except IntegrityError:
        session.rollback()
        print("An error occurred. Please try again.")
        return False


def main():
    print(get_user_by_email('joline@gmail.com').id)

if __name__ == '__main__':
    main()