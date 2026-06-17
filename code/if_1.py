# ruff: noqa: F403, F405
from manim import *
from base import IFTransition, adicionar_fundo_if


class Cena1(Scene):
    def construct(self):

        circle_backgroud = Circle(
            radius=8.0, fill_color="#2e9e40", fill_opacity=1, stroke_width=0
        ).move_to(RIGHT * 5)

        title = Text(
            "Relacionando Álgebra e a Geometria\nAtráves da Construção de Polígonos\nCom Régua e Compasso",
            font_size=30,
            color="#f0f8ff",
        ).to_edge(RIGHT, buff=0.3)

        rectangle_below_title = (
            Rectangle(
                color="#f0f8ff ", width=title.width / 2, height=0.1, fill_opacity=1
            )
            .next_to(title, DOWN, buff=0.15)
            .align_to(title, LEFT)
        )

        name = (
            Text("Matheus Augusto de Melo Santana")
            .set_color("#f0f8ff")
            .scale(0.5)
            .next_to(title, UP, buff=1.8)
            .align_to(title, LEFT)
        )

        advisor = (
            Text("Orientador: Jorge Algusto\nCoorientador:Vinícius Facó")
            .set_color("#f0f8ff")
            .scale(0.5)
            .next_to(title, DOWN, buff=2.0)
            .align_to(title, LEFT)
        )

        if_logo_start = (
            SVGMobject("img/if_logo_estrutural").to_edge(LEFT, buff=1.5).scale(1.5)
        )

        self.add(circle_backgroud)
        self.play(Create(if_logo_start))
        self.play(Write(title), run_time=1.5, rate_func=smooth)
        self.play(Create(rectangle_below_title))
        self.wait(2)
        self.play(Write(advisor, run_time=1.0))
        self.play(Write(name, run_time=1.0))

        self.wait(2)

        ##############
        # Capa
        #############

        self.play(
            FadeOut(circle_backgroud, if_logo_start, title, advisor, name, run_time=1.5)
        )

        quadrado = Square(side_length=2, color="#f0f8ff")
        IFTransition.apply(self, quadrado, direcao=LEFT, duracao=2.0)
        self.wait(2)


class Cena2(Scene):
    def construct(self):
        adicionar_fundo_if(self, direcao=RIGHT)

        titulo = (
            Text(
                "Os Problemas Clássicos Gregos",
                font_size=36,
                color="#2e9e40",
            )
            .to_edge(UP, buff=0.5)
            .to_edge(LEFT, buff=2.5)
        )

        linha = (
            Rectangle(color="#2e9e40", width=titulo.width, height=0.05, fill_opacity=1)
            .next_to(titulo, DOWN, buff=0.1)
            .align_to(titulo, LEFT)
        )

        self.play(Write(titulo), Create(linha), run_time=1.0)
        self.wait(1.0)

        def fazer_angulo():
            """Ângulo com três raios — um original e dois mostrando a trissecção."""
            origem = ORIGIN
            r1 = Line(origem, origem + RIGHT * 1.2, color="#2e9e40", stroke_width=2)
            r2 = Line(
                origem,
                origem + (RIGHT * 0.9 + UP * 0.8),
                color="#2e9e40",
                stroke_width=2,
            )
            arco = Arc(
                radius=0.5,
                start_angle=0,
                angle=np.arctan2(0.8, 0.9),
                color="#2e9e40",
                stroke_width=2,
            )
            # Linhas de trissecção tracejadas
            ang = np.arctan2(0.8, 0.9)
            t1 = DashedLine(
                origem,
                origem + (RIGHT * np.cos(ang / 3) + UP * np.sin(ang / 3)) * 1.0,
                color="#2e9e40",
                stroke_width=1.5,
            ).set_stroke(opacity=0.6)

            t2 = Line(
                origem,
                origem + (RIGHT * np.cos(2 * ang / 3) + UP * np.sin(2 * ang / 3)) * 1.0,
                color="#2e9e40",
                stroke_width=1.5,
            ).set_stroke(opacity=0.6)

            return VGroup(r1, r2, arco, t1, t2)

        def fazer_circulo_quadrado():
            """Círculo com um quadrado inscrito ao lado — quadratura do círculo."""
            circulo = Circle(radius=0.5, color="#2e9e40", stroke_width=2)
            quadrado = Square(side_length=0.88, color="#2e9e40", stroke_width=2)
            igual = Text("≈", font_size=20, color="#2e9e40")

            return VGroup(circulo, igual, quadrado)

        def criar_cubo(scala=1.0):
            """Dois quadrados deslocados ligados nos cantos — representação de cubo."""
            frente = Square(side_length=0.8, color="#2e9e40", stroke_width=2)
            tras = Square(side_length=0.8, color="#2e9e40", stroke_width=2).shift(
                UP * 0.4 * scala + RIGHT * 0.4 * scala
            )

            arestas = VGroup(
                *[
                    Line(
                        frente.get_corner(d),
                        tras.get_corner(d),
                        color="#2e9e40",
                        stroke_width=2,
                    )
                    for d in [UL, UR, DR, DL]
                ]
            )

            return VGroup(frente, tras, arestas)

        def fazer_cubo():
            cubo_pequeno = criar_cubo(0.6)

            cubo_grande = criar_cubo(1.0)

            seta = MathTex("V \\longrightarrow 2 V", color="#2e9e40").scale(0.5)

            return VGroup(
                cubo_pequeno,
                seta,
                cubo_grande,
            ).arrange(RIGHT, buff=0.25)

        # Dados de cada card: (título, descrição, figura)
        dados = [
            (
                "Duplicação do Cubo",
                "Construir um cubo com\no dobro do volume\nde um cubo dado.",
                fazer_cubo(),
            ),
            (
                "Trissecção do Ângulo",
                "Dividir um ângulo\narbitrário em\ntrês partes iguais.",
                fazer_angulo(),
            ),
            (
                "Quadratura do Círculo",
                "Construir um quadrado\ncom a mesma área\nde um círculo dado.",
                fazer_circulo_quadrado(),
            ),
        ]

        cards = VGroup()
        boxes = VGroup()

        for titulo_card, desc_card, figura in dados:
            t = Text(titulo_card, font_size=20, color="#2e9e40")
            d = Text(desc_card, font_size=14, color="#2e9e40", line_spacing=1.2)
            figura.scale_to_fit_width(1.6)

            conteudo = VGroup(t, d, figura).arrange(DOWN, buff=0.25, aligned_edge=LEFT)

            box = RoundedRectangle(
                width=3.5, height=3.5, color="#2e9e40", corner_radius=0.21
            )

            conteudo.move_to(box.get_center())

            cards.add(conteudo)
            boxes.add(box)

        # Posicionar lado a lado abaixo da linha
        grupo = VGroup(*[VGroup(b, c) for b, c in zip(boxes, cards)])
        grupo.arrange(RIGHT, buff=0.5).next_to(linha, DOWN, buff=0.5)

        # Animar: retângulo expande de cima para baixo, depois aparece o conteúdo

        for box, conteudo in zip(boxes, cards):
            titulo_card = conteudo[0]
            descricao = conteudo[1]
            figura = conteudo[2]

            box_colapsada = box.copy().stretch_to_fit_height(0.01).align_to(box, UP)

            self.add(box_colapsada)

            # Abre o card
            self.play(
                box_colapsada.animate.become(box),
                run_time=1.0,
            )

            # Título
            self.play(
                Write(titulo_card),
                run_time=1.6,
            )

            self.wait(0.5)

            # Figura
            self.play(
                FadeIn(figura, scale=0.8),
                run_time=1.6,
            )

            # Texto
            self.play(
                FadeIn(descricao, shift=UP * 0.1),
                run_time=2.6,
            )

            self.wait(1.0)
