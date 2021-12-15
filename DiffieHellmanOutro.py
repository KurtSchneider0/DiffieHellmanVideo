from manim import *

#manim render --help
#manim -qh -p *file*.py *Scene*

class DiffieHellmanOutro(Scene):
    def construct(self):

        # Spielt das Outro ab

        outro = Text("Das wars", gradient=(BLUE, GREEN)).scale(1.5)
        outro_line = SurroundingRectangle(outro)
        outro_line.set_color(BLUE, GREEN)
        self.wait(1)
        self.play(Write(outro))
        self.play(Create(outro_line))
        self.wait(4)
        self.play(
            FadeOut(outro),
            Uncreate(outro_line)
        )
        self.wait(1)
