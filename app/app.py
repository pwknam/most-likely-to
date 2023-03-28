#Technologies
import click
from simple_term_menu import TerminalMenu

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from datetime import datetime

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
    click.echo("getting superlative...")
    superlative = session.query(Superlative.name).all()
    click.echo(superlative)

def login():
    pass

def view_user_polls_created():
    click.echo("Getting Polls that this user created")

    logged_in_user_id = 4
    superlatives = session.query(Superlative).filter(Superlative.author_id == logged_in_user_id)
    
    options = []

    for superlative in superlatives:
        options.append(f'{superlative.name}')
    options.append("***Go back to the homepage***")
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(options[menu_entry_index])
    type_superlative()
    # click.echo(f"Selection: {options[menu_entry_index]}!")


def view_polls_user_not_voted():
    click.echo("Getting polls you have not voted on yet")
    click.echo(datetime.now())

def print(value):
    click.echo(value)





#main function
@click.command()
def main():
    # type_superlative()
    # get_superlative()
    view_user_polls_created()
    # view_polls_user_not_voted()



if __name__ == '__main__':
    engine = create_engine('sqlite:///superlatives.db')
    Session = sessionmaker(bind=engine)
    session = Session()
  
    main()