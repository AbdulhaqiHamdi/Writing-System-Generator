from mapping.renderer import Renderer
from core.tokenization import tokenize


text = "kakikukekosasisuseso"


renderer = Renderer(
    width=600,
    height=400
)

renderer.write_conlang(tokenize(text))
renderer.save("doc/result.png")
