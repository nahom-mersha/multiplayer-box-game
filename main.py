from visuals.ui import MainWindow
from game.logic import Player, KeyHandler

game = MainWindow()
keyhandler = KeyHandler(game.root)
players = Player(game.player_ids, game.canvas, keyhandler.keys_dict)
keyhandler.binding_keys()
players.update_movement()

game.run()