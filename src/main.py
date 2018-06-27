from google_image_search import google_image_search


def play_game():
    # Determine number of players
    num_players = get_num_players()

    # Generate the number of required words
    num_words = 5

    # Iterate over the number of required words
    all_words = list()
    for player_num in range(1, num_words+1):
        new_word = get_word(player_num)
        all_words.append(new_word)

    # Output the sentance
    final_sentence = " ".join(all_words)
    print(final_sentence)

    # Generate a google image link

    # Open the link
    google_image_search(final_sentence)

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

def get_word(player_num):
    word = input("[Player {}]: Enter a word...".format(player_num))

    return word


if __name__ == "__main__":
    play_game()
