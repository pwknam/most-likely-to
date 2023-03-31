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
from sqlalchemy import and_

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
                global logged_in_user_id
                logged_in_user_id = u.id
                homepage()
                return  # exit the function once a matching user is found
    # display error message only after checking all users in the database
    click.echo("Incorrect username/password combo. Please try again!")
    login()

def homepage():
    click.echo("What would you like to do?")
    options = ["Create Superlative", "Vote on Superlatives", "View Superlatives I've Created", "View What I've Been Nominated For"]
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

def select_popular_unvoted():


    # get all superlatives with no votes cast by the logged in user, sorted by popularity
    query = (
        session.query(Superlative.name, Superlative.id, func.count(Votes.id).label('vote_count'))
        .outerjoin(Votes, and_(Superlative.id == Votes.superlative_id, Votes.voter_id == logged_in_user_id))
        .group_by(Superlative.id)
        .having(func.count(Votes.id) == 0)
        .order_by(func.count(Votes.id).desc().nullslast(), Superlative.name)
    )

    results = query.all()

    superlatives = [result[0] for result in results]
    # ids = [result[1] for result in results]
    options = []  # Use a list to store options in the order returned by the query

    for superlative in superlatives:
        options.append(f'{superlative}')  # Add each option to the list


    options.append("***Go Back To Homepage***")
    options.append("***View recent superlatives***")
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    if menu_entry_index == len(options)-2:
        homepage()
    elif menu_entry_index == len(options)-1:
        select_recent_unvoted()
    else:
        global selected_superlative_name, selected_superlative_id
        selected_superlative_name = options[menu_entry_index]
        selected_superlative_id = results[menu_entry_index][1]
        vote_on_superlative()

        
def select_recent_unvoted():
    # get all votes from votes table that were cast for the selected superlative
    click.echo("Here are superlatives that you haven't voted on yet, ranked by most recently created:")
    subquery = (
        session.query(
            Votes.superlative_id,
            # func.max(Votes.date_created).label('date_created')
        )
        .group_by(Votes.superlative_id)
        .subquery()
    )

    superlatives = (
        session.query(Superlative.name, Superlative.id)
        .outerjoin(subquery, Superlative.id == subquery.c.superlative_id)
        .outerjoin(Votes, and_(Superlative.id == Votes.superlative_id, Votes.voter_id == logged_in_user_id))
        .filter(Votes.id == None)
        .order_by(Superlative.date_created.desc())
    )

    options = []
    ids = []
    for superlative_name, superlative_id in superlatives:
        options.append(superlative_name)
        ids.append(superlative_id)

    options.append("***View all superlatives")
    options.append("***Go back to homepage***")



    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if menu_entry_index == len(options)-1:
        homepage()
    elif menu_entry_index == len(options)-2:
        select_popular_unvoted()
    else: 
        global selected_superlative_name, selected_superlative_id
        selected_superlative_name = options[menu_entry_index]
        selected_superlative_id = ids[menu_entry_index]
        vote_on_superlative()
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

    options = set()  # Use a set to store unique options
    for superlative in superlatives:
        options.add(superlative.name)  # Add each option to the set
    if len(options) == 0:
        click.echo("You have not created any superlatives.")

    table_headers = ["Superlative Name"]
    table_data = [[option] for option in options]  # Create a list of lists with one option per inner list
    print(tabulate(table_data, headers=table_headers, tablefmt='orgtbl'))

     
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
    # options = []
    # for superlative, vote in merged_data:
    #     options.append(f'{superlative.name}')

    # # print the results as a table
    # table_headers = ["Superlative Name"]
    # table_data = set(options)
    # print(tabulate(table_data, headers=table_headers))
     
    
    options = set()  # Use a set to store unique options
    for superlative, v in merged_data:
        options.add(superlative.name)  # Add each option to the set
    if len(options) == 0:
        click.echo("You have not created any superlatives.")


    table_headers = ["Superlative Name"]
    table_data = [[option] for option in options]  # Create a list of lists with one option per inner list
    print(tabulate(table_data, headers=table_headers, tablefmt='orgtbl'))

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
    summary_table()
    homepage()

#main function
@click.command()
def main():
    login()
if __name__ == '__main__':
    engine = create_engine('postgres://superlatives_db_user:U2xSDYmvOcLJECHAoM3GlKORXb5U8TXl@dpg-cgjfaeu4dadak452v50g-a.oregon-postgres.render.com/superlatives_db')
    Session = sessionmaker(bind=engine)
    session = Session()
    main()
    # selected_superlative = session.query(Superlative).filter(Superlative.name == "Best Dressed").first()
    # voting_screen()

def view_leaderboard_for_selected_superlative(selected_superlative):
    click.echo(selected_superlative.name)
    nominees = session.query(Votes.nominee_id).filter(Votes.superlative_id == selected_superlative.id).all()
    nominee_ids = [nominee[0] for nominee in nominees]
    click.echo(nominee_ids)
    # view_leaderboard_for_selected_superlative(selected_superlative)