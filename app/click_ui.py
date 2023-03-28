#Technologies
import click
from simple_term_menu import TerminalMenu

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#models/classes
from models import User, Nominees, Superlative, Votes


#functions

def type_superlative():
    superlative = click.prompt('Please state your superlative: ', type=str)
   
    options = [f'{superlative}', "entry 2", "entry 3"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    click.echo(f"You have written: {options[menu_entry_index]}!")

    superlative_1 = Superlative(name = f'{superlative}', author_id = 1)
    session.add(superlative_1)
    session.commit()


def get_superlative():
    print("getting superlative...")
    superlative = session.query(Superlative.name).all()
    click.echo(superlative)

def login():
    pass



#main function
@click.command()
def main():
    type_superlative()
    get_superlative()



if __name__ == '__main__':
    engine = create_engine('sqlite:///superlatives.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(User).delete()
    session.query(Nominees).delete()
    session.query(Superlative).delete()
    session.query(Votes).delete()

    main()