from PIL import Image, ImageDraw, ImageFont
import json

# Open the file and load the data
with open('mapping/mapping.json', 'r', encoding='utf-8') as file:
    data =  json.load(file)

consonants = list(data["consonants"].keys())
vowels = list(data["vowels"].keys())[1:]

def locate_glyph(token):
    for consonant in consonants:
        # Konsonan + inherent vowel 'a'
        if token == f"{consonant}a":
            return (
                data["consonants"][consonant],
                None
            )
        # Konsonan + vowel
        for vowel in vowels:
            if token == f"{consonant}{vowel}":
                return (
                    data["consonants"][consonant],
                    data["vowels"][vowel]
                )
    return None

class Renderer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = Image.new("RGB", (self.width, self.height), color="white") #canvas
        self.draw = ImageDraw.Draw(self.image)

    def write_conlang(self, tokens):
            # Starting coordinates and layout settings
            x, y = 20, 20
            spacing = 10         # Space between adjacent characters
            right_margin = 20    # Minimum distance from the right edge
            line_height = 70     # Vertical distance to drop down for a new line
            
            for i in tokens:
                dir = locate_glyph(i)
                
                if dir is None:
                    print(f"Glyph for token '{i}' not found.")
                    continue
                    
                # 1. Load images and determine character width beforehand to check bounds
                if dir[1] is None:
                    C = Image.open(dir[0]).convert("RGBA")
                    item_width = C.width
                elif dir[1] is not None:
                    C = Image.open(dir[0]).convert("RGBA")
                    V = Image.open(dir[1]).convert("RGBA")
                    # Account for the offset of the vowel (x + 15 + C.width - V.width) plus its width
                    item_width = max(C.width, 15 + C.width - V.width + V.width)
                
                # 2. Check if the character exceeds the right side of the canvas
                if x + item_width > self.width - right_margin:
                    x = 20          # Reset X to the left margin
                    y += line_height # Move down to the next line
                
                # 3. Paste the glyph(s) onto the canvas
                if dir[1] is None:
                    print(f"{dir} Located")
                    self.image.paste(C, (x, y), C) # Added mask (C) for proper transparency
                elif dir[1] is not None:
                    print(f"{dir} Located")
                    self.image.paste(C, (x, y), C)
                    self.image.paste(V, (x + 15 + C.width - V.width, y + 20), V)
                
                # 4. Advance X for the next character
                x += item_width + spacing
    
    def save(self, path):
        self.image.save(path)