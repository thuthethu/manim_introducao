# ruff: noqa: F403, F405
from manim import *
from base import IFTransition


class Cena1(Scene):
    def construct(self):
        title = Text(
            "Relacionando Álgebra e a Geometria\natráves da Construção de Polígonos com Régua e Compasso",
            font_size=36,
            color=GREEN,
        )

        name = Text("Matheus Augusto de Melo Santana")
        advisor = Text("Jorge Algusto Conçalo de Brito")
        co_advisor = Text("Vinícius Facó")

        my_info = (
            VGroup(name, advisor, co_advisor)
            .arrange(DOWN, buff=0.6)
            .to_edge(DOWN, buff=1.0)
        )

        self.play(Write(title), run_time=1.5, rate_func=smooth)
        self.wait(2)
        self.play(FadeIn(my_info, shift=UP * 0.3, run_time=1.0))
        self.wait(2)

        quadrado = Square(side_length=2, color=BLACK)
        IFTransition.apply(self, quadrado, direcao=RIGHT, duracao=1.8)
        self.wait(2)
