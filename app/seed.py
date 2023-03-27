from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Superlative, Votes

if __name__ == '__main__':
    engine = create_engine('sqlite:///superlatives.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # session.query(User).delete()
    # session.query(Superlative).delete()
    # session.query(Votes).delete()
    
    user_1 = User("Kyushik", "pwkn")
    session.add(user_1)
    session.commit(user_1)

    user_2 = User("Sally", "sk")
    session.add(user_2)
    session.commit(user_2)

    user_3 = User("Michelle", "mc")
    session.add(user_3)
    session.commit(user_3)

    superlative_1 = Superlative("Most likely to become president")
    session.add(superlative_1)
    session.commit(superlative_1)


