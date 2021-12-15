from manim import *

#manim render --help
#manim -qh -p *file*.py *Scene*

class DiffieHellmanModulo(Scene):
    def construct(self):

        # Spielt das Intro ab

        intro = Text("Modulo\nOperator", gradient=(BLUE, GREEN)).scale(1.5)
        intro_line = SurroundingRectangle(intro)
        intro_line.set_color(BLUE, GREEN)
        self.wait(1)
        self.play(Write(intro))
        self.play(Create(intro_line))
        self.wait(3)

        # Spielt die Erklärung ab

        Header = Tex(r"Modulo Operator").scale(1.75)
        Header.shift(3*UP)
        self.play(Uncreate(intro_line))
        self.play(ReplacementTransform(intro, Header))

        self.wait(6)
        aModulob = Tex(r"$a \pmod{b}$").scale(1.5)
        aModulob.generate_target()
        aModulob.target.shift(2*UP)
        aModulob.target.set_color(BLUE)
        aModulob.set_color(BLUE)
        self.play(Write(aModulob))
        self.wait(10)
        self.play(MoveToTarget(aModulob))

        aModulobRect = SurroundingRectangle(aModulob)
        aModulobRect.set_color(BLUE)
        self.play(Create(aModulobRect))

        Modulo94 = Tex(r"$1 \equiv 9 \pmod{4}$")
        Modulo94.generate_target()
        Modulo94.target.shift(1.5*LEFT)
        Modulo94.target.set_color(PINK)
        Modulo94.set_color(PINK)
        self.play(Write(Modulo94),
                  run_time = 2)
        self.wait(8)
        self.play(MoveToTarget(Modulo94))

        Modulo94Rect = SurroundingRectangle(Modulo94)
        Modulo94Rect.set_color(PINK)
        self.play(Create(Modulo94Rect))

        ModuloProzent = Tex(r"$9 \% 4 = 1$")
        ModuloProzent.shift(1.5*RIGHT)
        ModuloProzent.set_color(PINK)
        self.play(Write(ModuloProzent),
                  run_time = 2)
        self.wait(4)

        ModuloProzentRect = SurroundingRectangle(ModuloProzent)
        ModuloProzentRect.set_color(PINK)
        self.play(Create(ModuloProzentRect))

        # Entfernt alles

        self.play(
            FadeOut(Header),
            FadeOut(aModulob),
            Uncreate(aModulobRect),
            FadeOut(Modulo94),
            Uncreate(Modulo94Rect),
            FadeOut(ModuloProzent),
            Uncreate(ModuloProzentRect)
        )
