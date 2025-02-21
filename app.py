from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for session management

# Dummy user for login
users = {
    'manager': 'password'
}

# In-memory storage for teams
# Each team will have a unique ID, a name, and a list of players.
# Each player is represented as a dict with a name and last 5 game results.
teams = {}
team_counter = 1  # Used to assign a unique ID to each new team

@app.route('/')
def home():
    # Redirect the user to the login page
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login page:
    - GET: Render the login form.
    - POST: Validate the username and password.
    """
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Check if the username exists and password matches
        if username in users and users[username] == password:
            session['user'] = username  # Store the user in session
            return redirect(url_for('dashboard'))
        else:
            error = "Invalid credentials. Please try again."
    return render_template('login.html', error=error)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    """
    Manager Dashboard:
    - GET: Displays a form to create a new team and a list of existing teams.
    - POST: Processes the new team creation.
    
    The form expects:
      - team_name: The name of the team.
      - players: A comma-separated list of player names.
    
    For demonstration, each player is automatically assigned dummy last 5 game results.
    """
    if 'user' not in session:
        return redirect(url_for('login'))
    global team_counter
    if request.method == 'POST':
        team_name = request.form.get('team_name')
        players = request.form.get('players')  # Expecting a comma-separated string
        team_id = team_counter
        team_counter += 1
        
        player_list = []
        if players:
            # Split player names by comma and strip extra whitespace
            for p in players.split(','):
                p = p.strip()
                if p:
                    # Here we simulate the player's last 5 games with a static list.
                    # In a real application, these would be dynamically generated or stored.
                    last_games = ["Win", "Loss", "Win", "Win", "Loss"]
                    player_list.append({'name': p, 'last_games': last_games})
        
        teams[team_id] = {
            'team_name': team_name,
            'players': player_list
        }
        # After creating the team, redirect back to the dashboard.
        return redirect(url_for('dashboard'))
    
    return render_template('dashboard.html', teams=teams)

@app.route('/team/<int:team_id>/review')
def review_team(team_id):
    """
    Team Review Page:
    - Displays the team name at the top.
    - For each player in the team, it lists their last five game results.
    """
    if 'user' not in session:
        return redirect(url_for('login'))
    team = teams.get(team_id)
    if not team:
        return "Team not found", 404
    return render_template('team_review.html', team=team)

if __name__ == '__main__':
    # Run the app in debug mode (remove debug=True in production)
    app.run(debug=True)
