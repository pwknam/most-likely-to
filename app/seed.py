from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from models import User, Nominees, Superlative, Votes

if __name__ == '__main__':
    engine = create_engine('mysql://avnadmin:AVNS_2Cqf4NGN6xZwnAyCV2w@mysql-251abb6c-mchoi4194-84fd.aivencloud.com:14616/defaultdb?ssl-mode=REQUIRED')
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
        {'username': "none", 'password': 'n'}
    ]

    for person in people:
        author = User(username = person['username'], password = person['password'])
        session.add(author)
        session.commit()
    
    for person in people:
        nominee = Nominees(name = person['username'])
        session.add(nominee)
        session.commit()

    date_expired_str = '2023-03-9'
    date_expired_format = datetime.strptime(date_expired_str, '%Y-%m-%d')
    superlative_1 = Superlative(name = "Most likely to get hit by a pick up truck and survive.", author_id = 4, date_expired = date_expired_format)
    session.add(superlative_1)
    session.commit()

    superlative_9 = Superlative(name = "Best video game player.", author_id = 4, date_expired = date_expired_format)
    session.add(superlative_9)
    session.commit()

    superlative_10 = Superlative(name = "Most likely to become famous.", author_id = 4, date_expired = date_expired_format)
    session.add(superlative_10)
    session.commit()

    superlative_3 = Superlative(name = "Most likely to get build a time traveling machine, then use it to travel back in time to live with dinosaurs.", author_id = 4, date_expired = date_expired_format)
    session.add(superlative_3)
    session.commit()

    superlative_15 = Superlative(name = "Least likely to come back and teach at Flatiron.", author_id = 4, date_expired = date_expired_format)
    session.add(superlative_15)
    session.commit()

    superlative_4 = Superlative(name = "Most likely to get chased by an ostrich after failing to comply by zoo visiting rules.", author_id = 4, date_expired = date_expired_format)
    session.add(superlative_4)
    session.commit()

    superlative_5 = Superlative(name = "Most likely to BECOME a gajillionaire.", author_id = 4, date_expired = date_expired_format)
    session.add(superlative_5)
    session.commit()

    superlative_8 = Superlative(name = "Most likely to MARRY a gajillionaire.", author_id = 4, date_expired = date_expired_format)
    session.add(superlative_8)
    session.commit()


    superlative_6 = Superlative(name = "Sally's bestfriend.", author_id = 4, date_expired = date_expired_format)
    session.add(superlative_6)
    session.commit()

    superlative_7 = Superlative(name = "Most likely to quit coding after this bootcamp", author_id = 4, date_expired = date_expired_format)
    session.add(superlative_7)
    session.commit()

    superlative_2 = Superlative(name = "Most likely to win a prize in an absolutely useless contest. Kyushik will take whoever wins this out to lunch.", author_id = 4, date_expired = date_expired_format)
    session.add(superlative_2)
    session.commit()

    # superlative_17 = Superlative(name = "Sally's bestfriend.", author_id = 17, date_expired = date_expired_format)
    # session.add(superlative_17)
    # session.commit()


    # vote_1 = Votes(voter_id = 17, superlative_id = 1, nominee_id = 2)
    # session.add(vote_1)
    # session.commit()

    # vote_2 = Votes(voter_id = 16, superlative_id = 2, nominee_id = 3)
    # session.add(vote_2)
    # session.commit()

    # vote_3 = Votes(voter_id = 15, superlative_id = 3, nominee_id = 4)
    # session.add(vote_3)
    # session.commit()

    # vote_4 = Votes(voter_id = 14, superlative_id = 4, nominee_id = 5)
    # session.add(vote_4)
    # session.commit()

    # vote_5 = Votes(voter_id = 13, superlative_id = 5, nominee_id = 6)
    # session.add(vote_5)
    # session.commit()

    # vote_6 = Votes(voter_id = 12, superlative_id = 6, nominee_id = 7)
    # session.add(vote_6)
    # session.commit()

    # vote_7 = Votes(voter_id = 11, superlative_id = 7, nominee_id = 8)
    # session.add(vote_7)
    # session.commit()

    # vote_8 = Votes(voter_id = 10, superlative_id = 8, nominee_id = 9)
    # session.add(vote_8)
    # session.commit()

    # vote_9 = Votes(voter_id = 9, superlative_id = 9, nominee_id = 10)
    # session.add(vote_9)
    # session.commit()

    # vote_10 = Votes(voter_id = 8, superlative_id = 10, nominee_id = 11)
    # session.add(vote_10)
    # session.commit()

    # vote_11 = Votes(voter_id = 7, superlative_id = 11, nominee_id = 12)
    # session.add(vote_11)
    # session.commit()

    # vote_12 = Votes(voter_id = 6, superlative_id = 12, nominee_id = 13)
    # session.add(vote_12)
    # session.commit()

    # vote_13 = Votes(voter_id = 5, superlative_id = 13, nominee_id = 14)
    # session.add(vote_13)
    # session.commit()

    # vote_14 = Votes(voter_id = 4, superlative_id = 14, nominee_id = 15)
    # session.add(vote_14)
    # session.commit()

    # vote_15 = Votes(voter_id = 3, superlative_id = 15, nominee_id = 16)
    # session.add(vote_15)
    # session.commit()

    # vote_16 = Votes(voter_id = 2, superlative_id = 16, nominee_id = 17)
    # session.add(vote_16)
    # session.commit()

    # vote_17 = Votes(voter_id = 1, superlative_id = 17, nominee_id = 1)
    # session.add(vote_17)
    # session.commit()

    









