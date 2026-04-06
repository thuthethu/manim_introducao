# ruff: noqa: F403, F405
from manim import *


class ShowStuff(Scene):
    def construct(self):

        # codigo que vai aparecer na cena
        code_python = """
            from manim import *
                class CriarUmCirculo(Scene):
                    def construct(self)
                        circle = Circle()

                        self.play(circle)

            """
        # estruturação do codigo, de como ele vai se portar na cena
        code_block = Code(
            background="window",
            language="python",
            code_string=code_python,
            tab_width=3,
            formatter_style="vim",
            background_config={"stroke_width": 1, "stroke_color": WHITE},
            paragraph_config={"font": "Adwaita Mono"},
        )

        # Ajusatr o bloco de codigo para que tenha cantoas arrendodados
        code_block.scale(0.8).to_edge(LEFT, buff=0.5)

        # Criar a linha que vai dividir a tela
        linha_do_meio = Line(UP * 4, DOWN * 4)

        # codigo a ser exibido no lado direito
        circle = Circle()
        circle.next_to(linha_do_meio, RIGHT, buff=1.0)

        self.play(Create(linha_do_meio))
        self.wait(2)
        self.play(FadeIn(code_block, shift=LEFT), DrawBorderThenFill(circle))
        self.wait(4)
