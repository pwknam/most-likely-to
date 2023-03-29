#Technologies
import click
from simple_term_menu import TerminalMenu

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from datetime import datetime
from tabulate import tabulate


#models/classes
from models import User, Nominees, Superlative, Votes


#global variables
logged_in_user_id = None

#functions
def login():

    typed_username = click.prompt('Please type your username: ', type=str)
    typed_password = click.prompt('Please type your password: ', type=str)
    users = session.query(User).all()
    for u in users:
        if u.username == typed_username:
            if u.password == typed_password:
                logged_in_user_id = u.id
                homepage()
                return  # exit the function once a matching user is found
    # display error message only after checking all users in the database
    click.echo("Incorrect username/password combo. Please try again!")
    login()

    
def homepage():
    click.echo("What would you like to do?")
    options = ["Create Superlative", "View New Superlatives", "View Superlatives I've Created", "View What I've Been Nominated For"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    click.echo(f"You have chosen: {options[menu_entry_index]}!")
    # Switch statement based on user's selection
    if menu_entry_index == 0:
        create_superlative()
    elif menu_entry_index == 1:
        view_polls_user_not_voted()
    elif menu_entry_index == 2:
        view_user_polls_created()
    elif menu_entry_index == 3:
        # view_my_nominations()
        homepage()


def create_superlative():
    superlative = click.prompt('Please state your superlative: ', type=str)
    click.echo(f"You have written: {superlative}.")
    superlative_1 = Superlative(name = f'{superlative}', author_id = 1)
    session.add(superlative_1)
    session.commit()
    select_recently_unvoted()

def select_recently_unvoted():
    # get all votes from votes table that were cast for the selected superlative
    # results = session.query(Superlative, Votes).filter(Superlative.id == Votes.superlative_id).all()
    click.echo("Here are superlatives that you haven't voted on yet, ranked by most total votes:")
    results = session.query(Superlative.name, func.count(Votes.superlative_id).label('total_votes')).outerjoin(Votes).group_by(Superlative.id).order_by(func.count(Votes.id).desc()).all()

    options = []
    for superlative, votes in results:
        options.append(f'{superlative}')
    options.append("***Go back to the homepage***")
   

    # THIS IS IF YOU WANT TO SEE THE DATA IN THE TABLE:
    # print the results as a table
    table_headers = ["Superlative Name", "Total Votes"]
    table_data = [[superlative, total_votes] for superlative, total_votes in results]
    print(tabulate(table_data, headers=table_headers))

    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if menu_entry_index == len(options)-1:
        homepage()    
    else: vote_on_superlative(superlatives[menu_entry_index], menu_entry_index+1)

def select_popular_unvoted():
    pass
    # COPY AND PAST CODE FROM RECENTLY UNVOTED WITH CHANAGE TO SORTING

def vote_on_superlative(superlative_name, superlative_id):
    # KYUSHIK WRITING THIS CODE NOW
    click.echo(f"{superlative_name, superlative_id}")
    click.echo(f"Kyushik is doing this part!")
    options = []
    options.append("***Go back to the homepage***")
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if menu_entry_index == len(options)-1:
        homepage()   



def view_top_superlatives():

    # TO FIX THIS TO IMPORT THE SUPERLATIVES AND THEN FILTER THEM
    options = [f'{superlative}', "entry 2", "entry 3"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    click.echo(f"You have chosen: {options[menu_entry_index]}!")

    # TO DECIDE WHERE THIS SHOULD ACTUALLY POINT TO
    homepage()


def get_superlative():
    click.echo("getting superlative...")
    superlative = session.query(Superlative.name).all()
    click.echo(superlative)

def view_user_polls_created():
    click.echo("Getting Polls that this user created")
    superlatives = session.query(Superlative).filter(Superlative.author_id == logged_in_user_id)
    
    options = []

    for superlative in superlatives:
        options.append(f'{superlative.name}')
    options.append("***Go back to the homepage***")
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(options[menu_entry_index])

    # TO DECIDE WHERE THE NEXT PAGE IS



def view_polls_user_not_voted():
    click.echo("Getting polls you have not voted on yet")

    # TO WRITE OUT THIS FUNCTION
    click.echo(datetime.now())

def print(value):
    click.echo(value)





#main function
@click.command()
def main():
    login()
    



if __name__ == '__main__':
    engine = create_engine('sqlite:///superlatives.db')
    Session = sessionmaker(bind=engine)
    session = Session()
  
    main()