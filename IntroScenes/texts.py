from manim import *

class text(Scene):
    def construct(self):
        firstLine = Text("Hi")
        secondLine = Text("Welcome Back")
        self.play(FadeIn(firstLine))
        self.play(firstLine.animate.move_to(UP),run_time = 1)
        self.play(FadeIn(secondLine))