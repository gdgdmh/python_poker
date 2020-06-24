#!/usr/bin/env python
"""テキサスホールデムテストクラス."""
from poker import texasholdem


def test_initialize_game():
    """ゲームの初期化. ハングアップなどしなければOKとする."""
    t = texasholdem.Texasholdem()
    t.initialize_game()
