import random

def click():
    """Placeholder function
    TODO: remove this function
    - Simulates the clicking of the card
    - Returns a random image name string
    """
    strings = ['R', 'A', 'G', 'N', 'O', 'K']
    random_idx = random.randint(0, (len(strings) - 1))

    randint = random.randint(0, 1)
    if randint:
        return "letter-{}.png".format(strings[random_idx])
    return "letter-{}-1.png".format(strings[random_idx])

def card_game(attempts_count = 6, deck = False, solved = [], is_shared = False):
    """
    CRITERIA_MATCH:
    - is NOT the same card
    - is the same image
    - is not listed in 'solved_cards'
    """

    # There is a default of 6 attemps. This will be increased by 4 to be a total of 10 when the user
    # shares the game on Facebook.
    attempts = attempts_count
    shared_to_fb = is_shared

    # Initial values are "-" to denote that the card has not yet been opened
    # Once the card is opened, it will change the value of that card's index to the name of the image
    # in the card.
    # Example: memory_deck = ['letter-A-1.png', 'letter-B.png', '-', '-', '-']
    memory_deck = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ]

    if deck:
        memory_deck = deck

    # solved_cards is the container of open cards that are a match. This will let us track the status
    # of open cards. Open cards should not be clicked anymore as they are already out of the game.
    solved_cards = solved

    # loop through each attempt
    for attempt in range(0, attempts - 1):
        # loop through each card in the deck
        print('*'*20)
        print("---Current Attempt: {}---".format(attempt))
        print("Current Memory Deck:", memory_deck)
        for idx, card in enumerate(memory_deck):
            if card == '-':
                print("Opening card: {}".format(idx))
                # if the card is still closed, click the card
                # get the image name of the current card
                image_name = click()
                # REPLACE THE CARD's VALUE
                memory_deck[idx] = image_name
                print("Card is {}".format(image_name))

                # find an open card in the deck that matches CRITERIA_MATCH
                for i, val in enumerate(memory_deck):
                    # Criteria:
                    not_same_card = i != idx
                    is_same_image = image_name == val
                    not_solved = i not in solved_cards
                    if not_same_card and is_same_image and not_solved:
                        # if CRITERIA_MATCH, click the matched card
                        matched_image = click()
                        # TODO: REPLACE THE CARD's VALUE
                        memory_deck[idx] = matched_image
                        # TODO: Add this card's and the current card's indices to solved_cards
                        solved_cards = list(set(solved_cards + [i, idx]))
                        print("Current card ({}) matched Card #{}, with the value of {}".format(idx, i, matched_image))
            else:
                # TODO: Remove this `else` statement. This is only here as a marker.
                pass
        attempts = attempts - 1
        break

    # if attempts == 0, and shared_to_fb is still false, call an share_to_fb routine
    if not attempts and not shared_to_fb:
        # Share to FB
        # Reset game
        card_game(4, memory_deck, solved_cards, True)

    if not attempts and shared_to_fb:
        # Summarize everything
        print("Finished card game. Solved cards: {}".format(len(solved_cards) / 2))
        print("Final deck:")
        print(memory_deck)
        print('-'*20)

if __name__ == "__main__":
    card_game()
