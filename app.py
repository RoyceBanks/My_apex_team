import tkinter as tk
from tkinter import messagebox

# Simulated data for demonstration purposes
users_db = {"manager": "password123"}  # Username and password pairs
team_members = {}  # Will hold the team with player names and match history

# Helper Functions
def add_member_to_team(name):
    if name in team_members:
        return f"{name} is already in the team!"
    team_members[name] = []
    return f"{name} added to the team!"

def remove_member_from_team(name):
    if name not in team_members:
        return f"{name} is not in the team!"
    del team_members[name]
    return f"{name} removed from the team!"

def get_last_5_matches(name):
    if name in team_members:
        # Here, just mock some match results data
        return team_members[name][:5]  # Return last 5 matches (or fewer if not enough)
    return f"{name} not found in team."

# Login Page
def show_login_page():
    login_window = tk.Tk()
    login_window.title("Login Page")

    # Label
    login_label = tk.Label(login_window, text="Please Login", font=("Helvetica", 16))
    login_label.pack(pady=10)

    # Username and Password Inputs
    username_label = tk.Label(login_window, text="Username:")
    username_label.pack(pady=5)
    username_entry = tk.Entry(login_window)
    username_entry.pack(pady=5)

    password_label = tk.Label(login_window, text="Password:")
    password_label.pack(pady=5)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack(pady=5)

    # Login Button
    def login_action():
        username = username_entry.get()
        password = password_entry.get()
        if username in users_db and users_db[username] == password:
            login_window.destroy()
            show_team_management_page()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    login_button = tk.Button(login_window, text="Login", command=login_action)
    login_button.pack(pady=20)

    login_window.mainloop()

# Team Management Page
def show_team_management_page():
    team_window = tk.Tk()
    team_window.title("Team Management")

    # Title label
    title_label = tk.Label(team_window, text="Team Management", font=("Helvetica", 16))
    title_label.pack(pady=10)

    # Add and Remove Member Buttons
    def add_member():
        name = name_entry.get()
        result = add_member_to_team(name)
        messagebox.showinfo("Add Member", result)

    def remove_member():
        name = name_entry.get()
        result = remove_member_from_team(name)
        messagebox.showinfo("Remove Member", result)

    # Name input for adding/removing members
    name_label = tk.Label(team_window, text="Enter Player Name:")
    name_label.pack(pady=5)
    name_entry = tk.Entry(team_window)
    name_entry.pack(pady=5)

    # Add and Remove Buttons
    add_button = tk.Button(team_window, text="Add Player", command=add_member)
    add_button.pack(pady=5)

    remove_button = tk.Button(team_window, text="Remove Player", command=remove_member)
    remove_button.pack(pady=5)

    # Show Team Button
    def show_team():
        team = "\n".join(team_members.keys()) if team_members else "No team members yet."
        messagebox.showinfo("Team Members", team)

    show_button = tk.Button(team_window, text="Show Team", command=show_team)
    show_button.pack(pady=20)

    # Go to Match Breakdown Page
    def go_to_match_page():
        team_window.destroy()
        show_match_breakdown_page()

    match_button = tk.Button(team_window, text="Go to Match Breakdown", command=go_to_match_page)
    match_button.pack(pady=5)

    team_window.mainloop()

# Match Breakdown Page
def show_match_breakdown_page():
    match_window = tk.Tk()
    match_window.title("Match Breakdown")

    # Title Label
    match_label = tk.Label(match_window, text="Match Breakdown", font=("Helvetica", 16))
    match_label.pack(pady=10)

    # Select a Player for Match Breakdown
    def show_match_history():
        player_name = player_name_entry.get()
        matches = get_last_5_matches(player_name)
        if isinstance(matches, list):
            matches_text = "\n".join(matches) if matches else "No matches yet."
        else:
            matches_text = matches
        messagebox.showinfo(f"{player_name} - Last 5 Matches", matches_text)

    # Player name input for match breakdown
    player_name_label = tk.Label(match_window, text="Enter Player Name:")
    player_name_label.pack(pady=5)
    player_name_entry = tk.Entry(match_window)
    player_name_entry.pack(pady=5)

    # Show Match Button
    match_button = tk.Button(match_window, text="Show Last 5 Matches", command=show_match_history)
    match_button.pack(pady=20)

    match_window.mainloop()

# Start the app
show_login_page()
