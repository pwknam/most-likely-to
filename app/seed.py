from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Nominees, Superlative, Votes

if __name__ == '__main__':
    engine = create_engine('sqlite:///superlatives.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(User).delete()
    session.query(Nominees).delete()

    people = [
        {'username': "nick", 'password': 'n'},
        {'username': "chrisc", 'password': 'c'},
        {'username': "finn", 'password': 'f'},
        {'username': "michelle", 'password': 'm'},
        {'username': "bobby", 'password': 'b'},
        {'username': "anson", 'password': 'a'},
        {'username': "sally", 'password': 's'},
        {'username': "kyushik", 'password': 'k'},
        {'username': "jacob", 'password': 'j'},
        {'username': "brett", 'password': 'b'},
        {'username': "bill", 'password': 'b'},
        {'username': "jack", 'password': 'j'},
        {'username': "min", 'password': 'm'},
        {'username': "valencia", 'password': 'v'},
        {'username': "ian", 'password': 'i'},
        {'username': "eshwar", 'password': 'e'},
        {'username': "chrisw", 'password': 'w'},
    ]

    for person in people:
        author = User(username = person['username'], password = person['password'])
        session.add(author)
        session.commit()
    
    for person in people:
        nominee = Nominees(name = person['username'])
        session.add(nominee)
        session.commit()







