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

            t2 = DashedLine(
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


class Cena3(Scene):
    def construct(self):
        # Transição e Fundo (Mantendo o padrão do seu código)
        adicionar_fundo_if(self, direcao=RIGHT)

        # ==========================================================
        # SLIDE 1: O que é construtível? (Régua e Compasso)
        # ==========================================================

        titulo = (
            Text(
                "O que é construtível?",
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

        # Texto explicativo sobre a restrição
        texto_restricao = (
            Text(
                "Os gregos estabeleceram que as construções\ndevem ser feitas utilizando apenas:",
                font_size=24,
                color="#2e9e40",
                line_spacing=1.5,
            )
            .next_to(linha, DOWN, buff=0.8)
            .align_to(linha, LEFT)
        )

        self.play(FadeIn(texto_restricao, shift=RIGHT * 0.3))
        self.wait(1.5)

        # Ícones de Régua e Compasso
        # Representação simplificada de uma régua
        regua_shape = Rectangle(
            width=4, height=0.5, color="#2e9e40", stroke_width=2, fill_color="#2e9e40"
        )
        regua_texto = Text(
            "Régua (sem marcações)", font_size=20, color="#2e9e40"
        ).next_to(regua_shape, DOWN)
        regua_group = VGroup(regua_shape, regua_texto)

        # Representação simplificada de um compasso
        ponto_fixo = Dot(color="#2e9e40")
        haste1 = Line(ORIGIN, UP * 2 + LEFT * 0.5, color="#2e9e40")
        haste2 = Line(ORIGIN, UP * 2 + RIGHT * 0.5, color="#2e9e40")
        compasso_shape = VGroup(haste1, haste2, ponto_fixo).move_to(
            ORIGIN
        )  # adiciona o ponto
        compasso_texto = Text("Compasso", font_size=20, color="#2e9e40").next_to(
            compasso_shape, DOWN
        )
        compasso_group = VGroup(compasso_shape, compasso_texto)

        ferramentas = (
            VGroup(regua_group, compasso_group)
            .arrange(RIGHT, buff=2)
            .next_to(texto_restricao, DOWN, buff=1.2)
        )

        self.play(Create(regua_shape), Write(regua_texto), run_time=2.5)
        self.play(Create(compasso_shape), Write(compasso_texto), run_time=2.0)

        pivot = ponto_fixo.get_center()
        self.play(
            Rotate(haste2, angle=PI / 2, about_point=pivot),
            run_time=1.5,
            rate_func=there_and_back,
        )

        self.wait(3)

        # Limpar para o Slide 2
        self.play(FadeOut(texto_restricao), FadeOut(ferramentas), run_time=1)

        # ==========================================================
        # SLIDE 2: Operações Permitidas
        # ==========================================================

        titulo_op = (
            Text(
                "Operações Permitidas",
                font_size=30,
                color="#2e9e40",
            )
            .next_to(linha, DOWN, buff=0.5)
            .align_to(linha, LEFT)
        )

        self.play(
            Transform(titulo, titulo_op)
        )  # Reaproveitando o título ou apenas escrevendo novo

        # Lista de operações com animações simples ao lado
        op1_texto = Text("1. Reta por dois pontos", font_size=20, color="#2e9e40")
        op2_texto = Text("2. Círculo (centro e ponto)", font_size=20, color="#2e9e40")
        op3_texto = Text("3. Intersecções", font_size=20, color="#2e9e40")

        # Animações demonstrativas
        # Demonstração 1: Reta
        p1 = Dot(LEFT * 0.5, color="#2e9e40")
        p2 = Dot(RIGHT * 0.5, color="#2e9e40")
        reta_demo = Line(LEFT * 1.2, RIGHT * 1.2, color="#2e9e40").set_stroke(
            opacity=0.6
        )
        demo1 = VGroup(p1, p2, reta_demo).next_to(op1_texto, RIGHT, buff=2)

        # Demonstração 2: Círculo
        centro = Dot(color="#2e9e40")
        p_raio = Dot(RIGHT * 0.6, color="#2e9e40")
        circ_demo = Circle(radius=0.6, color="#2e9e40").set_stroke(opacity=0.6)
        demo2 = VGroup(centro, p_raio, circ_demo).next_to(op2_texto, RIGHT, buff=2.3)

        # Demonstração 3: Intersecção
        l1 = Line(UP * 0.5 + LEFT * 0.5, DOWN * 0.5 + RIGHT * 0.5, color="#2e9e40")
        l2 = Line(UP * 0.5 + RIGHT * 0.5, DOWN * 0.5 + LEFT * 0.5, color="#2e9e40")
        inter_p = Dot(ORIGIN, color=RED).scale(0.8)
        demo3 = VGroup(l1, l2, inter_p).next_to(op3_texto, RIGHT, buff=3)

        # Sequência de animação
        # Op 1
        self.play(Write(op1_texto))
        self.play(Create(demo1))  # em vez de Create(p1), Create(p2), Create(reta_demo)
        self.wait(0.5)

        # Op 2
        self.play(Write(op2_texto))
        self.play(
            Create(demo2)
        )  # em vez de Create(centro), Create(p_raio), Create(circ_demo)
        self.wait(0.5)

        # Op 3
        self.play(Write(op3_texto))
        self.play(Create(demo3))  # em vez de Create(l1), Create(l2), Create(inter_p)
        self.wait(4)
