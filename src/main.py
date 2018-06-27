import time

from google_image_search import google_image_search


def play_game():
    # Determine number of players
    num_players = get_num_players()

    # Generate the number of required words
    num_words = num_players

    word_types = get_word_types_array(num_words)

    # Iterate over the number of required words
    all_words = list()
    for player_num in range(1, num_words+1):
        new_word = get_word(player_num, word_types)
        all_words.append(new_word)

    # Output the sentance
    final_sentence = " ".join(all_words)
    print('The', final_sentence)

    time.sleep(2)

    # Open the link
    google_image_search(final_sentence)

    return


def get_word_types_array(num_words):
    if num_words == 2:
        return ['noun', 'verb']
    if num_words == 3:
        return ['noun', 'transitive verb', 'noun']
    if num_words == 4:
        return ['adjective', 'noun', 'transitive verb', 'noun']
    if num_words == 5:
        return ['adjective', 'noun', 'transitive verb', 'adjective', 'noun']


def get_num_players():
    num_players = input("Enter the number of players (as an integer, 2-5)...")

    try:
        num_players_as_int = int(num_players)
    except Exception:
        #FIXME Error catching does not seem to work :-(
        raise ValueError("{} is not a valid integer. Please restart!".format(num_players))
    finally:
        return num_players_as_int

def get_word(player_num, word_types):
    word = input("[Player {}]: Enter a {}...".format(player_num, word_types[player_num - 1]))

    return word


if __name__ == "__main__":
    play_game()
