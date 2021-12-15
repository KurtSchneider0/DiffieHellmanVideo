from manim import *

#manim render --help
#manim -qh -p *file*.py *Scene*

class DiffieHellmanExp(Scene):
    def construct(self):

        # Spielt das Intro ab

        intro = Text("Exponentierungs-\nregel", gradient=(BLUE, GREEN)).scale(1.5)
        intro_line = SurroundingRectangle(intro)
        intro_line.set_color(BLUE, GREEN)
        self.wait(1)
        self.play(Write(intro))
        self.play(Create(intro_line))
        self.wait(4)

        # Spielt die Erklärung ab

        Regel = Tex(r"$(g^{a})^{b}=g^{ab}$").scale(1.75)
        Regel.generate_target()
        Regel.target.shift(3*UP)
        Regel.target.set_color(BLUE)
        Regel.set_color(BLUE)
        self.play(
            FadeOut(intro),
            Uncreate(intro_line)
        )
        self.play(Write(Regel))
        self.wait(3)
        self.play(MoveToTarget(Regel))

        self.wait(2)
        Formel1 = Tex(r"$(g^{a})^{b}$")
        self.play(Write(Formel1))

        self.wait(3)
        Formel2 = Tex(r"$(\underbrace{g\cdot...\cdot g}_{a-mal})^b$")
        self.play(ReplacementTransform(Formel1,Formel2))

        self.wait(6)
        Formel3 = Tex(r"$\underbrace{(\underbrace{g\cdot...\cdot g}_{a-mal})\cdot... \cdot (\underbrace{g\cdot...\cdot g}_{a-mal})}_{b-mal}$")
        self.play(ReplacementTransform(Formel2,Formel3))

        self.wait(5)
        Formel4 = Tex(r"$(\underbrace{g\cdot...\cdot g}_{ab-mal})$")
        self.play(ReplacementTransform(Formel3,Formel4))

        self.wait(6)
        Formel5 = Tex(r"$g^{ab}$")
        self.play(ReplacementTransform(Formel4,Formel5))

        # Entfernt alles

        self.play(
            FadeOut(Regel),
            FadeOut(Formel5)
        )
