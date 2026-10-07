import re

def parse(text):
    """
    Parse the IPA text and return to the list of phonemes
    """
    return text.split()

# Vokal IPA yang digunakan
VOWELS = {
    'a', 'e', 'i', 'o', 'u',
    'æ', 'ɛ', 'ɪ', 'ɔ', 'ʊ',
    'ə', 'ɜ', 'ɑ', 'ʌ'
}

# Tanda yang tidak diperlukan dalam token
IGNORED = {
    'ˈ', 'ˌ',
    ',', '.', '?', '!', ';', ':'
}


def classify(symbol):
    """
    Mengembalikan:
    V = vowel
    C = consonant
    """

    if symbol in VOWELS:
        return 'V'
    else:
        return 'C'


def tokenize(text):
    """
    Mengubah teks IPA menjadi token berdasarkan pola
    konsonan + vokal.

    Contoh:
    'fæməli' -> ['fæ', 'mə', 'li']
    'rɪsivz' -> ['rɪ', 'si', 'vz']
    'haʊ'    -> ['ha', 'ʊ']
    """

    tokens = []

    # Hapus stress mark dan tanda baca
    text = ''.join(
        char for char in text
        if char not in IGNORED
    )

    # Pisahkan berdasarkan spasi
    words = text.split()

    for word in words:
        i = 0
        while i < len(word):
            # --------------------------------
            # 1. Jika karakter adalah vokal
            # --------------------------------
            if classify(word[i]) == 'V':
                tokens.append(word[i])
                i += 1
                continue
            # --------------------------------
            # 2. Jika karakter adalah konsonan
            # --------------------------------
            current = ''
            # Kumpulkan semua konsonan
            while i < len(word) and classify(word[i]) == 'C':
                current += word[i]
                i += 1
            # --------------------------------
            # 3. Jika setelah konsonan ada vokal
            # --------------------------------
            if i < len(word) and classify(word[i]) == 'V':

                current += word[i]
                i += 1

                tokens.append(current)
            else:
                # Konsonan yang berdiri sendiri
                if current:
                    tokens.append(current)
    # ============================================
    # 6. Post-processing struktur C/V
    # ============================================
    result = []
    for token in tokens:
        structure = ''.join(
            classify(char)
            for char in token
        )
        # ----------------------------------------
        # V
        # ----------------------------------------
        if structure == 'V':
            result.append(token)
        # ----------------------------------------
        # C
        # ----------------------------------------
        elif structure == 'C':
            result.append(token)
        # ----------------------------------------
        # CV
        # ----------------------------------------
        elif structure == 'CV':
            result.append(token)
        # ----------------------------------------
        # CC
        #
        # contoh:
        # ld -> l* + d
        # rk -> r* + k
        # ----------------------------------------
        elif structure == 'CC':
            result.append(token[0] + '*')
            result.append(token[1:])
        # ----------------------------------------
        # CCV
        #
        # contoh:
        # nsə -> n* + sə
        # θri -> θ* + ri
        # træ -> t* + ræ
        # ----------------------------------------
        elif structure == 'CCV':
            result.append(token[0] + '*')
            result.append(token[1:])
        # ----------------------------------------
        # CCC
        #
        # contoh:
        # nts -> n* + t* + s
        # ----------------------------------------
        elif structure == 'CCC':
            result.append(token[0] + '*')
            result.append(token[1] + '*')
            result.append(token[2:])
        # ----------------------------------------
        # Struktur lainnya
        # ----------------------------------------
        else:
            result.append(token)
    return result
