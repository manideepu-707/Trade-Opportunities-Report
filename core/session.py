sessions = {}

def track_session(user: str):
    if user not in sessions:
        sessions[user] = 0
    sessions[user] += 1