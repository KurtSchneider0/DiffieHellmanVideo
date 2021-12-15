from manim import *

#manim render --help
#manim -qh -p *file*.py *Scene*

class DiffieHellmanIntro(Scene):
    def construct(self):

        # Spielt das Intro ab

        intro = Text("Diffie-Hellman-\nSchlüsselaustausch", gradient=(BLUE, GREEN)).scale(1.5)
        intro_line = SurroundingRectangle(intro)
        intro_line.set_color(BLUE, GREEN)
        self.wait(1)
        self.play(
            Write(intro),
            run_time = 4
        )
        self.play(
            Create(intro_line),
            run_time = 3
        )
        self.wait(14)
        self.play(
            FadeOut(intro),
            Uncreate(intro_line)
        )

        # Spielt die Zusammenfassung ab

        self.wait(4)
        Grundkonzepte = Tex(r"Grundkonzepte").scale(1.75)
        Grundkonzepte.set_color(BLUE, GREEN)
        Grundkonzepte.generate_target()
        Grundkonzepte.target.shift(3*UP)
        self.play(Write(Grundkonzepte))
        self.wait(2)
        self.play(MoveToTarget(Grundkonzepte))
        self.wait(4)

        Modulo = Tex(r"- Modulo Operator")
        Modulo.shift(2*UP)
        self.play(Write(Modulo))
        self.wait(3.5)

        Expo = Tex(r"- Exponentierungsregel")
        Expo.shift(1*UP)
        self.play(Write(Expo))
        self.wait(3.5)

        diskrLog = Tex(r"- Diskrete Logarithmen")
        self.play(Write(diskrLog))
        self.wait(3.5)

        self.play(
            Unwrite(Grundkonzepte),
            Unwrite(Modulo),
            Unwrite(Expo),
            Unwrite(diskrLog)
        )
