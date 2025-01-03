import arcade

WIDTH = 800
HEIGHT = 600


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

        self.timer = 0

    def on_draw(self):
        """ Called automatically about 60 times a second to draw objects."""
        arcade.start_render()

        arcade.draw_text(f"{self.timer:.2f}", WIDTH/2, HEIGHT/2, arcade.color.BLACK, 40)
        
    def on_update(self, delta_time):
        """ Called automatically 60 times a second to update our objects."""
        
        self.timer += delta_time


def main():
    """ Main method """
    windown = GameWindow(WIDTH, HEIGHT, "Basic Animation")
    arcade.run()



if __name__ == "__main__":
    main()