#!/usr/bin/env python
"""トランプ配布クラス."""
from poker import trump_hand


class TrumpDeal:
    """トランプ配布クラス."""

    def __init__(self):
        """コンストラクタ."""
        pass

    def deal(self, deck, hands):
        """手札にトランプを配布する."""
        if deck.size() <= 0:
            return
        if len(hands) == 0:
            raise ValueError("hands invalid")
        player_index = 0
        player_max = len(hands)
        while deck.size() > 0:
            t = deck.draw()
            hands[player_index].add(t)
            player_index += 1
            if player_index >= player_max:
                player_index = 0
