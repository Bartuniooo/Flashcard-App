def update_card(card, was_correct):
    if was_correct:
        card.interval *= 2
    else:
        card.interval = 1
