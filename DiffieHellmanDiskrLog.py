from manim import *

#manim render --help
#manim -qh -p *file*.py *Scene*

class DiffieHellmanDiskrLog(Scene):
    def construct(self):

        # Spielt das Intro ab

        intro = Text("Diskrete\nLogarithmen", gradient=(BLUE, GREEN)).scale(1.5)
        intro_line = SurroundingRectangle(intro)
        intro_line.set_color(BLUE, GREEN)
        self.wait(1)
        self.play(Write(intro))
        self.play(Create(intro_line))
        self.wait(4)

        # Spielt die Erklärung ab

        diskrLog = Tex(r"$A \equiv g^a \pmod{p}$").scale(1.25)
        diskrLog.set_color(BLUE)
        self.play(
            FadeOut(intro),
            Uncreate(intro_line)
        )
        self.play(Write(diskrLog))
        self.wait(22)

        # Entfernt alles

        self.play(FadeOut(diskrLog))
