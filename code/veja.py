# ruff: noqa: F403, F405
from typing_extensions import runtime
from manim import *


class ShowLogo(Scene):
    def construct(self):
        banner = ManimBanner()
        self.play(banner.create(run_time=2))
        self.play(banner.expand(run_time=2))
        self.wait(2)
        self.play(Unwrite(banner))


# Função de criar a linha do meio para poder ser reutilizavel
def center_line():
    return Line(UP * 4, DOWN * 4)


# Criar uma classe dos codigos que vão aparecer na cena, para poder se reutilizavel
class CodeBlock(Code):
    def __init__(
        self,
        code_string: str | None = None,
        language: str | None = "python",
        formatter_style: str = "vim",
        tab_width: int = 4,
        add_line_numbers: bool = True,
        line_numbers_from: int = 1,
        background: Literal["rectangle", "window"] = "window",
        background_config: dict = {"stroke_width": 1, "stroke_color": WHITE},
        paragraph_config: dict = {"font": "Adwaita Mono"},
        **kwargs,
    ):
        super().__init__(
            code_string=code_string,
            language=language,
            formatter_style=formatter_style,
            tab_width=tab_width,
            add_line_numbers=add_line_numbers,
            line_numbers_from=line_numbers_from,
            background=background,
            background_config=background_config,
            paragraph_config=paragraph_config,
            **kwargs,
        )


class CreateCircle(Scene):
    def construct(self):

        # codigo que vai aparecer na cena
        code_python_circle = """\
            from manim import *
                class CriarUmCirculo(Scene):
                    def construct(self):
                        circle = Circle()

                        self.play(circle)

            """
        # estruturação do codigo, de como ele vai ficar estilizado na cena
        code_block_circle = Code(code_string=code_python_circle)

        # Ajusatr o bloco de codigo para que tenha cantoas arrendodados
        code_block_circle.scale(0.8).to_edge(LEFT, buff=0.5)

        # Criar a linha que vai dividir a tela no meio
        line = center_line()

        # codigo a ser exibido no lado direito
        circle = Circle()
        circle.to_edge(RIGHT, buff=3.0)

        # Colocando a animação que foi feta acima na tela
        self.play(Create(line))
        self.wait()
        self.play(
            Create(code_block_circle),
            Create(circle),
            run_time=3,
            rate_func=smooth,
        )
        self.wait(4)


class CreateSquare(Scene):
    def construct(self):

        # codigo que vai aparecer na cena
        code_python_square = """\
            from manim import *
                class CriarUmQuadrado(Scene):
                    def construct(self):
                        square = Square()

                        self.play(square)
            """

        code_block_square = Code(code_string=code_python_square)

        code_block_square.scale(0.8).to_edge(LEFT, buff=0.5)

        line = center_line()

        square = Square()
        square.to_edge(RIGHT, buff=3.0)

        self.play(Create(line))
        self.wait()
        self.play(
            Create(code_block_square),
            Create(square),
            run_time=3,
            rate_func=smooth,
        )
        self.wait(4)
