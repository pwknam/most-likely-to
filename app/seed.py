from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from models import User, Nominees, Superlative, Votes

if __name__ == '__main__':
    engine = create_engine('sqlite:///superlatives.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(User).delete()
    session.query(Nominees).delete()
    session.query(Superlative).delete()
    session.query(Votes).delete()

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

    date_expired_str = '2023-04-8'
    date_expired_format = datetime.strptime(date_expired_str, '%Y-%m-%d')
    superlative_1 = Superlative(name = "Best Dressed", author_id = 4, date_expired = date_expired_format)
    session.add(superlative_1)
    session.commit()

    superlative_2 = Superlative(name = "Most handsom", author_id = 5, date_expired = date_expired_format)
    session.add(superlative_2)
    session.commit()

    superlative_3 = Superlative(name = "Most beautiful", author_id = 8, date_expired = date_expired_format)
    session.add(superlative_3)
    session.commit()

    superlative_4 = Superlative(name = "Most likely to become president.", author_id = 4, date_expired = date_expired_format)
    session.add(superlative_4)
    session.commit()

    superlative_5 = Superlative(name = "Most likely to become rich", author_id = 4, date_expired = date_expired_format)
    session.add(superlative_5)
    session.commit()

    superlative_6 = Superlative(name = "Most likely to become a doctor", author_id = 4, date_expired = date_expired_format)
    session.add(superlative_6)
    session.commit()

    vote_1 = Votes(voter_id = 4, superlative_id = 2, nominee_id = 5)
    session.add(vote_1)
    session.commit()

    vote_2 = Votes(voter_id = 8, superlative_id = 2, nominee_id = 5)
    session.add(vote_2)
    session.commit()

    vote_3 = Votes(voter_id = 3, superlative_id = 2, nominee_id = 5)
    session.add(vote_3)
    session.commit()

    vote_4 = Votes(voter_id = 4, superlative_id = 2, nominee_id = 5)
    session.add(vote_4)
    session.commit()

    vote_5 = Votes(voter_id = 2, superlative_id = 3, nominee_id = 1)
    session.add(vote_5)
    session.commit()

    vote_6 = Votes(voter_id = 1, superlative_id = 3, nominee_id = 1)
    session.add(vote_6)
    session.commit()

    vote_7 = Votes(voter_id = 9, superlative_id = 3, nominee_id = 1)
    session.add(vote_7)
    session.commit()

    vote_8 = Votes(voter_id = 7, superlative_id = 3, nominee_id = 1)
    session.add(vote_8)
    session.commit()

    









