import json
from datetime import datetime
import os

def load_tournaments():
    files = ['in-progress.json']  # Adjust to include other files as needed
    tournaments = []
    for file in files:
        try:
            with open(file) as f:
                data = json.load(f)
                if isinstance(data, dict):
                    tournaments.append(data)
                else:
                    print(f"Error: Data in {file} is not in the expected dictionary format.")
        except json.JSONDecodeError as e:
            print(f"Error reading {file}: {e}")
        except Exception as e:
            print(f"An error occurred with {file}: {e}")
    return tournaments

def sort_tournaments(tournaments):
    return sorted(tournaments, key=lambda x: datetime.strptime(x['dates']['from'], '%d-%m-%Y'), reverse=True)

def display_tournaments(tournaments):
    for i, tournament in enumerate(tournaments):
        print(f"{i+1}. {tournament['name']} (Starts: {tournament['dates']['from']})")

def main_menu():
    tournaments = load_tournaments()
    tournaments = sort_tournaments(tournaments)
    
    print("Available Tournaments:")
    display_tournaments(tournaments)
    choice = int(input("Select a tournament number to manage or 0 to create new: "))
    if choice == 0:
        create_tournament()
    else:
        manage_tournament(tournaments[choice-1])

def manage_tournament(tournament):
    print(f"\nManaging Tournament: {tournament['name']}")
    print(f"Start Date: {tournament['dates']['from']}")
    print(f"End Date: {tournament['dates']['to']}")
    print(f"Number of Rounds: {tournament['number_of_rounds']}")
    print(f"Current Round: {tournament.get('current_round', 'Tournament has ended')}")
    print(f"Venue: {tournament['venue']}")
    print("Players:")
    for player in tournament['players']:
        print(f" - {player}")
    
    while True:
        print("\nOptions:")
        print("1. Register a new player")
        print("2. Enter results for the current round")
        print("3. Advance to the next round")
        print("4. Generate a tournament report")
        print("5. Go back to the main menu")
        option = input("Select an option: ")

        if option == '1':
            player_id = input("\nEnter player ID to register: ")
            tournament['players'].append(player_id)
            print(f"Player {player_id} registered successfully.")
        elif option == '2':
            if tournament.get('current_round') is not None:
                round_index = tournament['current_round'] - 1
                if round_index < len(tournament['rounds']):
                    for match in tournament['rounds'][round_index]:
                        print(f"Match between {match['players'][0]} and {match['players'][1]}")
                        winner = input("Enter the winner ID (or 'draw' for no winner): ")
                        match['winner'] = winner
                        match['completed'] = True
                    print("\nResults entered successfully.")
                else:
                    print("\nInvalid round information.")
            else:
                print("\nNo active round to update.")
        elif option == '3':
            if tournament.get('current_round') is not None:
                current_round = tournament['current_round']
                if current_round < tournament['number_of_rounds']:
                    tournament['current_round'] += 1
                    print(f"\nMoved to round {tournament['current_round']}.")
                else:
                    print("\nThis tournament has already completed all its rounds.")
            else:
                print("Tournament rounds not initialized properly.")
        elif option == '4':
            print(f"\nGenerating report for {tournament['name']}")
            # Generate a simple report - this can be enhanced as needed
            print(f"Name: {tournament['name']}, Venue: {tournament['venue']}")
            print(f"Total Players: {len(tournament['players'])}")
            print(f"Rounds Completed: {tournament.get('current_round', 0)}")
        elif option == '5':
            break
        else:
            print("\nInvalid option, please try again.")

def create_tournament():
    print("Creating new tournament...")
    name = input("Enter tournament name: ")
    start_date = input("Enter start date (DD-MM-YYYY): ")
    end_date = input("Enter end date (DD-MM-YYYY): ")
    venue = input("Enter venue: ")
    number_of_rounds = int(input("Enter number of rounds: "))
    new_tournament = {
        "name": name,
        "dates": {
            "from": start_date,
            "to": end_date
        },
        "venue": venue,
        "number_of_rounds": number_of_rounds,
        "current_round": 1,
        "completed": False,
        "players": [],
        "rounds": []
    }
    tournaments = load_tournaments()
    tournaments.append(new_tournament)
    with open('all_tournaments.json', 'w') as f:
        json.dump(tournaments, f)
    print("Tournament created successfully.")

if __name__ == "__main__":
    main_menu()
