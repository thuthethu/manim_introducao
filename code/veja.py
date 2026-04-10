# ruff: noqa: F403, F405
from manim import *


class MostrarLogo(Scene):
    def construct(self):
        banner = ManimBanner()
        self.play(banner.create(run_time=2))
        self.play(banner.expand(run_time=2))
        self.wait(2)
        self.play(Unwrite(banner))


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


class ShowStuff(Scene):
    def construct(self):

        # codigo que vai aparecer na cena
        code_python = """\
            from manim import *
                class CriarUmCirculo(Scene):
                    def construct(self):
                        circle = Circle()

                        self.play(circle)

            """
        # estruturação do codigo, de como ele vai ficar estilizado na cena
        code_block = Code(code_string=code_python)

        # Ajusatr o bloco de codigo para que tenha cantoas arrendodados
        code_block.scale(0.8).to_edge(LEFT, buff=0.5)

        # Criar a linha que vai dividir a tela no meio
        linha_do_meio = Line(UP * 4, DOWN * 4)

        # codigo a ser exibido no lado direito
        circle = Circle()
        circle.to_edge(RIGHT, buff=3.0)

        self.play(Create(linha_do_meio))
        self.wait(2)
        self.play(FadeIn(code_block, shift=LEFT), Create(circle))
        self.wait(4)
