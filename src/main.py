
def play_game():
    # Determine number of players
    num_players = get_num_players()

    # Generate the number of required words

    # Construct the number of words for each user

    # Output the sentance

    # Generate a google image link

    # Open the link
    import pdb; pdb.set_trace()
    return

def get_num_players():
    num_players = input("Enter the number of players (as an integer)...")

    try:
        _ = int(num_players)
    except Exception:
        #FIXME Error catching does not seem to work :-(
        raise ValueError("{} is not a valid integer. Please restart!".format(num_players))
    finally:
        return num_players

if __name__ == "__main__":
    play_game()
