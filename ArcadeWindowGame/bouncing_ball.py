import arcade

WIDTH = 800
HEIGHT = 600


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

        self.center_x = WIDTH/2
        self.change_x = 5
        self.radius = 50

        

    def on_draw(self):
        """ Called automatically 60 times a second to draw objects."""
        arcade.start_render()
        arcade.draw_circle_filled(self.center_x, HEIGHT/2, self.radius, arcade.color.RED)


    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.center_x += self.change_x

        if self.center_x >= WIDTH - self.radius:
            self.center_x = WIDTH - self.radius  # fix collision first
            self.change_x *= -1                  # then change direction
        if self.center_x <= self.radius:
            self.center_x = WIDTH - self.radius # fix collision first
            self.change_x *= -1                 # then change direction


    

def main():
    """ Main method """
    window = GameWindow(WIDTH, HEIGHT, "Basic Bounce")
    arcade.run()


if __name__ == "__main__":
    main()