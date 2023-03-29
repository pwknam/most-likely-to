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
    click.echo(f"You have written: {superlative}. Here are the superlatives you can vote on:")
    options = [f'{superlative}', "entry 2", "entry 3"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    # click.echo(f"You have written: {options[menu_entry_index]}!")

    date_expired_str = '2023-04-8'
    date_expired_format = datetime.strptime(date_expired_str, '%Y-%m-%d')
    superlative_1 = Superlative(name = f'{superlative}', author_id = 1)
    session.add(superlative_1)

    # MY COMMIT ISNT WORKING FOR SOME REASON, PLZ HELP!
    session.commit()

    view_user_polls_created()


def get_superlative():
    click.echo("getting superlative...")
    superlative = session.query(Superlative.name).all()
    click.echo(superlative)

def login():
    user_id = None
    typed_username = click.prompt('Please type your username: ', type=str)
    typed_password = click.prompt('Please type your password: ', type=str)
    users = session.query(User).all()
    for u in users:
        if u.username == typed_username:
            if u.password == typed_password:
                user_id = u.id
                options_list(user_id)
                return  # exit the function once a matching user is found
    # display error message only after checking all users in the database
    click.echo("Incorrect username/password combo. Please try again!")
    login()

    
def options_list(logged_in_user_id):
    click.echo("What would you like to do?")
    options = ["Create Superlative", "View Superlatives", "View My Superlatives", "View What I've Been Nominated For"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(options[menu_entry_index])
    click.echo(f"You have chosen: {options[menu_entry_index]}!")

def view_user_polls_created(logged_in_user_id):
    click.echo("Getting Polls that this user created")

    # logged_in_user_id = 4
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
    login()
    # type_superlative()
    # get_superlative()
    # view_user_polls_created()
    # view_polls_user_not_voted()



if __name__ == '__main__':
    engine = create_engine('sqlite:///superlatives.db')
    Session = sessionmaker(bind=engine)
    session = Session()
  
    main()