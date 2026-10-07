# **Writing System Generator**

This repository contains a personal project for designing and implementing a **custom writing system generator** using Python.

The project explores how a constructed writing system can be represented computationally, from **phonological input** to **custom glyph generation**. The current system is designed around an **alphasyllabary-inspired writing system**, where consonants function as base glyphs and vowels can be represented as additional vowel components.

The project is developed as an experimental tool for exploring the relationship between:

- Phonology
- Tokenization
- Writing-system design
- Glyph composition
- Digital rendering

---
## **Current Writing System Model**

The current design follows an **[alphasyllabary](https://en.wikipedia.org/wiki/Abugida)-inspired structure**. 

A basic syllable follows:

```text
Consonant + Vowel
```

Where the consonant provides the base glyph and the vowel modifies the base glyph.

For example:

```text
C + a → C
C + i → C + i-mark
C + u → C + u-mark
C + e → C + e-mark
C + o → C + o-mark
```

This design is intentionally inspired by the concept of an inherent vowel while remaining a custom writing system.


---

# **Design Architecture**

The project is divided into several conceptual layers.

![[diagram.png]]

For example, an input token:

```text
ki
```

can be represented as:

```text
k + i
```

and rendered by combining:

```text
consonant glyph: k.png
vowel glyph:     -i.png
```

to produce a single `ki` glyph.


## **Main Components**

### **1. Tokenization**

The tokenizer converts phonological or IPA input into smaller units that can be represented by the writing system.

For example:

```text
fæməli
```

can be segmented into:

```text
fæ → mə → li
```

The tokenizer also handles consonant clusters according to the rules defined by the writing system.

For example:

```text
nsə
```

can be represented as:

```text
n* → sə
```

where `*` represents a consonant without its inherent vowel.

The tokenizer therefore serves as the interface between phonological representation and the structure required by the custom writing system.

---

### **2. Token Standardization**

IPA contains multiple symbols that can represent similar vowel categories. The project therefore provides a normalization stage that maps different IPA symbols into the vowel categories used by the writing system.

For example:

|**IPA**|**Standard**|
|---|---|
|`æ`|`a`|
|`ɑ`|`a`|
|`ɪ`|`i`|
|`ʊ`|`u`|
|`ɛ`|`e`|
|`ɔ`|`o`|

This allows the rendering system to work with a smaller and more consistent set of vowel symbols.

---

### **3. Glyph Mapping**

The relationship between phonological units and image assets is defined using `mapping.json`.

Example:

```json
{
    "consonants": {
        "k": "asset/consonant/ka.png",
        "t": "asset/consonant/ta.png",
        "s": "asset/consonant/sa.png",
        "n": "asset/consonant/na.png",
        "m": "asset/consonant/ma.png",
        "r": "asset/consonant/ra.png"
    },
    "vowels": {
        "a": null,
        "i": "asset/vowel/-i.png",
        "u": "asset/vowel/-u.png",
        "e": "asset/vowel/-e.png",
        "o": "asset/vowel/-o.png"
    }
}
```

The mapping separates the two major components of the writing system:

```text
Consonant
    ↓
Base Glyph

Vowel
    ↓
Vowel Mark
```

The inherent vowel `a` does not require an additional vowel mark.

Therefore:

```text
ka → k glyph
ki → k glyph + i mark
ku → k glyph + u mark
ke → k glyph + e mark
ko → k glyph + o mark
```

---
# **Directory Structure**

The project is organized approximately as follows:

```text
make a writing system/
│
├── main.py
│
├── mapping/ 
│   ├── mapping.json
│   └── renderer.py
│
├── asset/
│   ├── consonant/
│   │   ├── ka.png
│   │   ├── ...
│   │
│   └── vowel/
│       ├── -i.png
│       ├── -u.png
│       ├── -e.png
│       └── -o.png
│
├── core/ 
│   ├── ipa_converter.py
│   ├── standarization.py
│   └── tokenization.py
│
└── README.md
```

**`mapping/`**
Contains the mapping between symbols and glyphs is stored in `mapping.json`. `renderer.py` file contains a Python library for initializing the canvas size to write the writing system on it

**`asset/`**
Contains the `.png` file of the alpasyllabary character

**`core/`**
Contains the library for any preprocessing steps: conversion to IPA, standardization, and tokenization.

---

# **Tools**

The project is currently implemented using Python.

### **Python**

Python is used for:

- Text processing
- IPA tokenization
- Data transformation
- JSON mapping
- Glyph management
- Image composition

### **Pillow**

[Pillow](https://python-pillow.org/) is used for image manipulation and glyph rendering.

It provides functionality for:

- Loading PNG glyphs
- Handling transparency
- Compositing glyph components
- Creating output canvases
- Saving rendered writing as images

### **JSON**

JSON is used as the configuration layer for mapping phonological units to glyph assets.

This allows the writing system to be modified without changing the rendering logic.

---
# **Example**

Run this code:

```python
from mapping.renderer import Renderer
from core.tokenization import tokenize

text = "kakikukekosasisuseso"

renderer = Renderer(width=600,height=400)

renderer.write_conlang(tokenize(text))
renderer.save("doc/result.png")
```

Here's the output:

![[result.png]]

---
# **Project Status**

**Status:** In Development

Goal:
- Convert English & Indonesian text to this writing system
- Complete consonant glyph inventory
- Complete vowel glyph inventory
- Support standalone vowels
- Support consonant clusters
- Complete any writing rule in alpasyllabary.
- Improve glyph positioning
- Improve glyph spacing
- Implement automatic line wrapping
- Add punctuation
- Add sentence-level rendering
- Improve IPA tokenization
- Add a command-line interface
- Add automated tests

---

# **Author**

This repository is a personal project by **Abdulhaqi Hamdi**.

The project is developed as an exploration of programming, linguistics, typography, and constructed writing systems.