from manim import *


class IntroScene(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        triangle = Triangle()
        square.set_fill(YELLOW,opacity=0.5)
        circle.set_fill(ORANGE,opacity=0.7)
        triangle.set_fill(RED,opacity=0.9)
        square.move_to(LEFT)
        triangle.move_to(RIGHT)
        self.play(FadeIn(square))
        self.play(square.animate.shift(RIGHT),ReplacementTransform(square,circle),run_time=2)
        self.play(Rotate(circle,2/PI),run_time = 0.5)
        self.play(circle.animate.shift(RIGHT),ReplacementTransform(circle,triangle), run_time=2)
        self.wait(0.5)
        self.play(FadeOut(triangle))