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


#functions
def login():
    typed_username = click.prompt('Please type your username: ', type=str)
    typed_password = click.prompt('Please type your password: ', type=str)
    users = session.query(User).all()
    for u in users:
        if u.username == typed_username:
            if u.password == typed_password:
                global logged_in_user_id
                logged_in_user_id = u.id
                homepage()
                return  # exit the function once a matching user is found
    # display error message only after checking all users in the database
    click.echo("Incorrect username/password combo. Please try again!")
    login()

def homepage():
    click.echo("What would you like to do?")
    options = ["Create Superlative", "View Popular Superlatives", "View Superlatives I've Created", "View What I've Been Nominated For"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    click.echo(f"You have chosen: {options[menu_entry_index]}!")
    # Switch statement based on user's selection
    if menu_entry_index == 0:
        create_superlative()
    elif menu_entry_index == 1:
        select_popular_unvoted()
    elif menu_entry_index == 2:
        view_user_polls_created()
    elif menu_entry_index == 3:
        view_my_nominations()

def create_superlative():
    superlative = click.prompt('Please state your superlative: ', type=str)
    click.echo(f"You have written: {superlative}.")
    superlative_1 = Superlative(name = f'{superlative}', author_id = logged_in_user_id)
    session.add(superlative_1)
    session.commit()
    select_popular_unvoted()
# TRIED TO REFACTOR OUT CREATE TERMINAL
# def create_terminal(options=[], results = [], penultimate_option=None):
#     for superlative, votes in results:
#         options.append(f'{superlative}')
#     options.append("***Go Back To Homepage***")
#     if penultimate_option:
#         options.append({penultimate_option})
#     terminal_menu = TerminalMenu(options)
#     menu_entry_index = terminal_menu.show()
#     return options, menu_entry_index
def select_popular_unvoted():
    # get all votes from votes table that were cast for the selected superlative
    click.echo("Here are superlatives that you haven't voted on yet, ranked by most total votes:")

      # NEED TO FIX THIS TO MAKE IT FILTER BY NOT VOTED ON

    results = session.query(Superlative.name, func.count(Votes.superlative_id).label('total_votes')).outerjoin(Votes).group_by(Superlative.id).order_by(func.count(Votes.id).desc()).all()
    # Attempted refactoring
    options = []
    for superlative, votes in results:
        options.append(f'{superlative}')
    options.append("***View recent superlatives")
    options.append("***Go Back To Homepage***")

    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    # THIS IS IF YOU WANT TO SEE THE DATA IN THE TABLE:
    # print the results as a table
    # table_headers = ["Superlative Name", "Total Votes"]
    # table_data = [[superlative, total_votes] for superlative, total_votes in results]
    # print(tabulate(table_data, headers=table_headers))
    if menu_entry_index == len(options)-1:
        homepage()
    elif menu_entry_index == len(options)-2:
        select_recent_unvoted()
    else:
        global selected_superlative_name, selected_superlative_id
        selected_superlative_name = options[menu_entry_index]
        selected_superlative_id = menu_entry_index + 1
        # vote_on_superlative()
        # summary_table()
        # homepage() 
        vote_on_superlative()
def select_recent_unvoted():
    # get all votes from votes table that were cast for the selected superlative
    # results = session.query(Superlative, Votes).filter(Superlative.id == Votes.superlative_id).all()
    click.echo("Here are superlatives that you haven't voted on yet, ranked by most recently created:")
    
    # NEED TO FIX THIS TO MAKE IT FILTER BY NOT VOTED ON
    results = session.query(Superlative).order_by(Superlative.date_created.desc()).all()
    # click.echo(f"{results}")
    options = []
    for superlative in results:
        options.append(f'{superlative.name}')
    options.append("***Vote on most popular superlatives***")
    options.append("***Go back to the homepage***")
    # click.echo(f"{options}")
    # THIS IS IF YOU WANT TO SEE THE DATA IN THE TABLE:
    # print the results as a table
    # table_headers = ["Superlative Name", "Total Votes"]
    # table_data = [[superlative, total_votes] for superlative, total_votes in results]
    # print(tabulate(table_data, headers=table_headers))
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    click.echo(f"{results}")
    if menu_entry_index == len(options)-1:
        homepage()
    elif menu_entry_index == len(options)-2:
        select_popular_unvoted()
    else: 
        global selected_superlative_name, selected_superlative_id
        selected_superlative_name = options[menu_entry_index]
        selected_superlative_id = menu_entry_index + 1
        vote_on_superlative()
        summary_table()
        homepage() 
        # vote_on_superlative(options[menu_entry_index], menu_entry_index+1)
    # pass
    # COPY AND PAST CODE FROM RECENTLY UNVOTED WITH CHANAGE TO SORTING

def get_superlative():
    click.echo("getting superlative...")
    superlative = session.query(Superlative.name).all()
    click.echo(superlative)

def view_user_polls_created():
    click.echo("Getting Polls that you created")
    superlatives = session.query(Superlative).filter(Superlative.author_id == logged_in_user_id)
    # click.echo(f"{logged_in_user_id}")



    options = []
    
    for superlative in superlatives:
        options.append(f'{superlative.name}')
    if len(options) == 0:
        click.echo(f"You have not created any superlatives.")
        
    table_headers = ["Superlative Name"]
    table_data = set(options)
    print(tabulate(table_data, headers=table_headers))
     
    # options.append()
    terminal_menu = TerminalMenu(["***Go back to the homepage***"])
    menu_entry_index = terminal_menu.show()
    if menu_entry_index == 0:
        homepage()

def view_my_nominations():
    click.echo("Getting Polls that you are nominated for")
    # WORKING HERE
    merged_data = session.query(Superlative, Votes)\
                        .join(Votes, Superlative.id == Votes.superlative_id)\
                        .filter(Votes.nominee_id == logged_in_user_id)\
                        .all()
    # click.echo(f"{logged_in_user_id}")
    if not merged_data:
        click.echo(f"You have not been nominated for any superlatives.")
    options = []
    for superlative, vote in merged_data:
        options.append(f'{superlative.name}')

    # print the results as a table
    table_headers = ["Superlative Name"]
    table_data = set(options)
    print(tabulate(table_data, headers=table_headers))
     
    # options.append()
    terminal_menu = TerminalMenu(["***Go back to the homepage***"])
    menu_entry_index = terminal_menu.show()
    if menu_entry_index == 0:
        homepage()
    

def view_polls_user_not_voted():
    click.echo("Getting polls you have not voted on yet")
    # TO WRITE OUT THIS FUNCTION
    click.echo(datetime.now())

def print(value):
    click.echo(value)
def summary_table():
    superlative_id = selected_superlative_id  # replace with the desired superlative id

    results = (
        session.query(
            Nominees.name,
            func.count(Votes.nominee_id).label('vote_count')
        )
        .join(Votes, Nominees.id == Votes.nominee_id)
        .filter(Votes.superlative_id == superlative_id)
        .group_by(Nominees.id)
        .order_by(func.count(Votes.nominee_id).desc())
        .all()
    )

    table_data = [[name.title(), vote_count] for name, vote_count in results]

    click.echo(tabulate(table_data, headers=['Nominee Name', 'Vote Count'], tablefmt='orgtbl'))

def vote_on_superlative():
    voting_options = []
    users = session.query(Nominees.name).all()
    for user in users:
        voting_options.append(user[0].title())
    
    terminal_menu = TerminalMenu(voting_options)
    click.echo(f'Superlative Name: {selected_superlative_name}' )
    menu_entry_index = terminal_menu.show()

    selected_nominee_id = session.query(Nominees.id).filter(Nominees.name == voting_options[menu_entry_index].lower()).first()

    new_vote = Votes(voter_id = logged_in_user_id, superlative_id = selected_superlative_id, nominee_id = selected_nominee_id[0])

    click.echo(f'You voted {voting_options[menu_entry_index]} for this particular Superlative')

    session.add(new_vote)
    session.commit()
#main function
@click.command()
def main():
    login()
if __name__ == '__main__':
    engine = create_engine('sqlite:///superlatives.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    main()
    # voting_screen()
    # selected_superlative = session.query(Superlative).filter(Superlative.name == "Best Dressed").first()
    # def view_leaderboard_for_selected_superlative(selected_superlative):
    #     click.echo(selected_superlative.name)
    #     nominees = session.query(Votes.nominee_id).filter(Votes.superlative_id == selected_superlative.id).all()
    #     nominee_ids = [nominee[0] for nominee in nominees]
    #     click.echo(nominee_ids)
    # view_leaderboard_for_selected_superlative(selected_superlative)