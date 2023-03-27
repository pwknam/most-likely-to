from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Nominees, Superlative, Votes

if __name__ == '__main__':
    engine = create_engine('sqlite:///superlatives.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(User).delete()
    session.query(Nominees).delete()
    session.query(Superlative).delete()
    session.query(Votes).delete()
    
    user_1 = User(username = "Kyushik", password = "pwkn")
    session.add(user_1)
    session.commit()

    user_2 = User(username = "Michelle", password = "mc")
    session.add(user_2)
    session.commit()

    user_3 = User(username = "Sally", password = "sk")
    session.add(user_3)
    session.commit()

    nominee_1 = Nominees(name = "Kyushik")
    session.add(nominee_1)
    session.commit()

    nominee_2 = Nominees(name = "Michelle")
    session.add(nominee_2)
    session.commit()

    nominee_3 = Nominees(name = "Sally")
    session.add(nominee_3)
    session.commit()


    superlative_1 = Superlative(name = "Most likely to become president.", author_id = 1)
    session.add(superlative_1)
    session.commit()

    superlative_2 = Superlative(name = "Best dressed.", author_id = 2)
    session.add(superlative_2)
    session.commit()

    superlative_3 = Superlative(name = "Smartest.", author_id = 3)
    session.add(superlative_3)
    session.commit()


    vote_1 = Votes(voter_id = 1, superlative_id = 1, nominee_id = 3)
    session.add(vote_1)
    session.commit()

    vote_2 = Votes(voter_id = 2, superlative_id = 2, nominee_id = 1)
    session.add(vote_2)
    session.commit()

    vote_3 = Votes(voter_id = 3, superlative_id = 3, nominee_id = 2)
    session.add(vote_3)
    session.commit()


