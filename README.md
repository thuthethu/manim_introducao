
# IF Manim

Projeto desenvolvido para a criação de animações matemáticas e apresentações acadêmicas utilizando Manim.

O objetivo é fornecer uma base reutilizável para estudantes e professores do Instituto Federal criarem conteúdos visuais para aulas, projetos de pesquisa, TCCs, monitorias e divulgação científica.

## Funcionalidades

* Componentes visuais padronizados do Instituto Federal
* Transições personalizadas com identidade institucional
* Estrutura modular para criação de cenas
* Compatibilidade com Manim Community
* Compatibilidade com Manim Slides
* Reutilização de objetos e animações em diferentes projetos

## Estrutura do Projeto

```text
code/
├── base.py          # Componentes reutilizáveis
├── if.py            # Cenas relacionadas ao projeto atual
├── img/             # Logos e recursos gráficos
└── media/           # Arquivos renderizados

slides/
└── slide.py         # Apresentações interativas

README.md
pyproject.toml
```

## Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/if-manim.git
cd if-manim
```

Instale as dependências:

```bash
uv sync
```

ou

```bash
pip install -r requirements.txt
```

## Renderizando uma cena

```bash
manim code/if.py Cena1
```

## Utilizando Manim Slides

```bash
manim-slides render slides/slide.py Capa
```

Depois:

```bash
manim-slides present Capa
```

## Objetivos futuros

* Biblioteca de construções geométricas
* Visualizações de Álgebra Linear
* Animações de Análise Complexa
* Conteúdos para disciplinas de Licenciatura em Matemática
* Modelos institucionais para apresentações acadêmicas

## Licença

MIT License.
