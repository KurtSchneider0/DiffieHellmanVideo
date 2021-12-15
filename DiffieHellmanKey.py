from manim import *

#manim render --help
#manim -qh -p *file*.py *Scene*

class DiffieHellmanKey(Scene):
    def construct(self):

        # Spielt das Intro ab

        intro = Text("Diffie-Hellman-\nSchlüsselaustausch", gradient=(BLUE, GREEN)).scale(1.5)
        intro_line = SurroundingRectangle(intro)
        intro_line.set_color(BLUE, GREEN)
        self.wait(1)
        self.play(Write(intro))
        self.play(Create(intro_line))
        self.wait(5.5)

        # Spielt die Erklärung Ab

        self.play(
            FadeOut(intro),
            Uncreate(intro_line)
        )

        Alice = Dot([-3, -1, 0]).scale(3)
        Alice.set_color(PINK)
        self.play(Create(Alice))

        Bob = Dot([3, -1, 0]).scale(3)
        Bob.set_color(BLUE)
        self.play(Create(Bob))

        AliceText = Tex(r"Alice")
        AliceText.shift(3*LEFT + 0.5*DOWN)
        self.play(Write(AliceText))

        BobText = Tex(r"Bob")
        BobText.shift(3*RIGHT + 0.5*DOWN)
        self.play(Write(BobText))

        self.wait(1.5)
        Key = Tex(r"$K=?$").scale(1.25)
        Key.shift(3.5*UP)
        self.play(Write(Key))

        self.wait(3)
        line = Line(Alice.get_center(), Bob.get_center())
        line.set_color(ORANGE)
        self.bring_to_back(line)
        self.play(Create(line))

        self.wait(6)

        Primzahl = Tex(r"- Eine zufällige Primzahl $p$").scale(0.5)
        Primzahl.to_corner(UP + LEFT)
        self.play(Write(Primzahl))

        self.wait(1)
        Zahlg1 = Tex(r"- Eine Zahl $g$, sodass erst für $a=p-1$").scale(0.5)
        Zahlg2 = Tex(r"$1 \equiv g^a \pmod{p}$ gilt").scale(0.5)
        Zahlg1.to_corner(UP + LEFT)
        Zahlg1.shift(0.5*DOWN)
        Zahlg2.to_corner(UP + LEFT)
        Zahlg2.shift(0.75*DOWN)
        self.play(Write(Zahlg1))
        self.play(Write(Zahlg2))
        self.wait(8)

        Zahla = Tex(r"- Eine zufällige Zahl $0\leq a \leq p-2$").scale(0.5)
        Zahla.to_corner(UP + LEFT)
        Zahla.shift(1.25*DOWN)
        self.play(Write(Zahla))

        self.wait(6)
        AliceTex = Tex(r"$A \equiv g^a \pmod{p}$").scale(0.75)
        AliceTex.set_color(PINK)
        AliceTex.generate_target()
        AliceTex.target.set_color(PINK)
        AliceTex.target.shift(3*RIGHT + 1.5*DOWN)
        AliceTex.shift(3*LEFT + 1.5*DOWN)
        self.play(Write(AliceTex))
        self.wait(4)

        AliceTexDot = Dot([-3, -1, 0])
        AliceTexDot.set_color(PINK)
        AliceTexDot.generate_target()
        AliceTexDot.target.set_color(PINK)
        AliceTexDot.target.shift(6*RIGHT)
        self.add(AliceTexDot)
        self.play(
            MoveToTarget(AliceTex),
            MoveToTarget(AliceTexDot),
            run_time=2
        )
        self.wait(2)
        self.play(FadeOut(AliceTexDot))

        ATex = Tex(r"$A$").set_color(PINK)
        ATex.shift(3.75*RIGHT + 1*DOWN)
        self.play(ReplacementTransform(AliceTex, ATex))

        Zahlb = Tex(r"- Eine zufällige Zahl $0\leq b \leq p-2$").scale(0.5)
        Zahlb.to_corner(UP + LEFT)
        Zahlb.shift(1.75*DOWN)
        self.play(Write(Zahlb))

        self.wait(6)
        BobTex = Tex(r"$B \equiv g^b \pmod{p}$").scale(0.75)
        BobTex.set_color(BLUE)
        BobTex.generate_target()
        BobTex.target.set_color(BLUE)
        BobTex.target.shift(3*LEFT + 1.5*DOWN)
        BobTex.shift(3*RIGHT + 1.5*DOWN)
        self.play(Write(BobTex))
        self.wait(4)
        BobTexDot = Dot([3, -1, 0])
        BobTexDot.set_color(BLUE)
        BobTexDot.generate_target()
        BobTexDot.target.set_color(BLUE)
        BobTexDot.target.shift(6*LEFT)
        self.add(BobTexDot)
        self.play(
            MoveToTarget(BobTex),
            MoveToTarget(BobTexDot),
            run_time=2
        )
        self.wait(2)
        self.play(FadeOut(BobTexDot))

        BTex = Tex(r"$B$").set_color(BLUE)
        BTex.shift(3.75*LEFT+1*DOWN)
        self.play(ReplacementTransform(BobTex, BTex))
        self.wait(2)


        BTex2 = Tex(r"$B^a$").set_color(BLUE)
        BTex2.shift(3.75*LEFT+1*DOWN)
        self.play(TransformMatchingTex(BTex, BTex2))
        self.wait(2)

        ATex2 = Tex(r"$A^b$").set_color(PINK)
        ATex2.shift(3.75*RIGHT+1*DOWN)
        self.play(TransformMatchingTex(ATex, ATex2))
        self.wait(2)

        Expl1 = Tex(r"$A^b=(g^b)^a \pmod{p} = g^{ba} \pmod{p}$").scale(0.75)
        Expl1.set_color(ORANGE)
        Expl1.shift(0.75*UP)
        self.play(
            Write(Expl1),
            run_time=6
        )

        Expl2 = Tex(r"$= g^{ab} \pmod{p} =(g^a)^b \pmod{p}=B^a$").scale(0.75)
        Expl2.set_color(ORANGE)
        self.play(
            Write(Expl2),
            run_time=6
        )
        self.wait(5)

        Key2 = Tex(r"$K=B^a=A^b$").scale(1.25)
        Key2.shift(3.5*UP)
        self.play(
            ReplacementTransform(Expl1,Key2),
            ReplacementTransform(Expl2,Key2),
            ReplacementTransform(Key,Key2)
        )
        self.wait(34)
        self.play(
            FadeOut(Key2),
            FadeOut(ATex2),
            FadeOut(BTex2),
            FadeOut(Alice),
            FadeOut(Bob),
            FadeOut(AliceText),
            FadeOut(BobText),
            FadeOut(line),
            FadeOut(Primzahl),
            FadeOut(Zahlg1),
            FadeOut(Zahlg2),
            FadeOut(Zahla),
            FadeOut(Zahlb),
        )
