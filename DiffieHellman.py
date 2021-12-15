from manim import *
from DiffieHellmanIntro import DiffieHellmanIntro
from DiffieHellmanModulo import DiffieHellmanModulo
from DiffieHellmanExp import DiffieHellmanExp
from DiffieHellmanDiskrLog import DiffieHellmanDiskrLog
from DiffieHellmanKey import DiffieHellmanKey
from DiffieHellmanOutro import DiffieHellmanOutro


#manim render --help
#manim -qh -p *file*.py *Scene*

class DiffieHellman(Scene):
    def construct(self):
        DiffieHellmanIntro.construct(self)
        DiffieHellmanModulo.construct(self)
        DiffieHellmanExp.construct(self)
        DiffieHellmanDiskrLog.construct(self)
        DiffieHellmanKey.construct(self)
        DiffieHellmanOutro.construct(self)
