# ruff: noqa: F403, F405

from manim import *
import numpy as np

config.background_color = "#F0F8FF"


def adicionar_fundo_if(scene, direcao=RIGHT):
    rectangle = (
        Rectangle(color="#2e9e40", height=config.frame_height, width=2)
        .to_edge(direcao, buff=0)
        .set_fill(color="#2e9e40", opacity=1)
    )
    if_logo = SVGMobject("img/if_logo_estrutural")
    if_logo.scale_to_fit_width(1.5)
    if_logo.move_to(rectangle.get_center())
    if_logo.set_color("#F0F8FF")
    scene.play(Create(rectangle), rate_func=smooth)
    scene.play(Create(if_logo), rate_func=smooth)

    scene.add(rectangle, if_logo)


class IFTransition:
    @staticmethod
    def apply(scene, novo_conteudo, direcao=RIGHT, duracao=1.0):

        faixa = Rectangle(
            color="#2e9e40", height=config.frame_height, width=2
        ).set_fill(color="#2e9e40", opacity=1)

        logo = SVGMobject("img/if_logo_estrutural")
        logo.scale_to_fit_width(1.5)
        logo.move_to(faixa.get_center())
        logo.set_color("#F0F8FF")

        faixa_com_logo = Group(faixa, logo)

        borda_direita = config.frame_width / 2
        borda_esquerda = -config.frame_width / 2

        if np.array_equal(direcao, RIGHT):
            faixa_com_logo.move_to(RIGHT * (borda_direita + 1))
            deslize = faixa_com_logo.animate.to_edge(RIGHT, buff=0)
        else:
            faixa_com_logo.move_to(LEFT * (abs(borda_esquerda) + 1))
            deslize = faixa_com_logo.animate.to_edge(LEFT, buff=0)

        scene.add(faixa_com_logo)
        scene.play(deslize, run_time=duracao)
        scene.wait(0.2)

        scene.clear()
        scene.add(novo_conteudo)

        if np.array_equal(direcao, RIGHT):
            recolhe = faixa_com_logo.animate.move_to(LEFT * (abs(borda_esquerda) + 1))
        else:
            recolhe = faixa_com_logo.animate.move_to(RIGHT * (borda_direita + 1))

        scene.play(recolhe, run_time=duracao)
        scene.remove(faixa_com_logo)
