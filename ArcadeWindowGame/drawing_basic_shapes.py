"""
Drawing Basic Shapes. 

IMPORTANT NOTE: Arcade is very slow with drawing primitives. Even drawing 20 - 30 
rectangles with arcade.draw_rectangle_filled() slows down the program.
You can use ShapeList to speed up drawing primitives but I highly recommend 
using images and Sprite/SpriteLists for all your games. Arcade can draw Sprites
in SpriteList VERY FAST!


"""


import arcade

WIDTH = 800
HEIGHT = 600


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Called automatically about 60 times a second to draw objects."""
        arcade.start_render()
        arcade.draw_text("Hello, World!", 100, HEIGHT/2, arcade.color.BLACK,
                    30)
        arcade.draw_circle_filled(100, 100, 50, arcade.color.RED)  
        arcade.draw_rectangle_filled(500, 100, 200, 100, arcade.color.BLUE)
        arcade.draw_line(100, 100, 500, 100, arcade.color.BLACK, line_width=3)         
    
    def on_update(self, delta_time):
        """ Called automatically 60 times a second to update our objects."""
        pass


def main():
    """ Main method """
    windown = GameWindow(WIDTH, HEIGHT, "Basic Drawing")
    arcade.run()



if __name__ == "__main__":
    main()