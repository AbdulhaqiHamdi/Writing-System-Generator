def vowel_standardization(tokens):
    """
    Mengubah simbol vokal IPA bahasa Inggris menjadi
    representasi vokal standar yang digunakan oleh
    writing system.

    Contoh:
        æ  -> a
        ɑ  -> a
        ɪ  -> i
        ʊ  -> u
        ɛ  -> e
        ɔ  -> o
        ə  -> ə
    """

    mapping = {
        'i': 'i',      # /iː/  see
        'ɪ': 'i',      # /ɪ/   sit
        'e': 'e',      # /e/   (variasi transkripsi)
        'ɛ': 'e',      # /ɛ/   bed
        'æ': 'a',      # /æ/   cat
        'ə': 'ə',      # /ə/   about
        'ɜ': 'e',      # /ɜː/  bird
        'ɝ': 'e',      # /ɝ/   American English: bird
        'ɚ': 'ə',      # /ɚ/   American English: teacher
        'u': 'u',      # /uː/  food
        'ʊ': 'u',      # /ʊ/   book
        'o': 'o',      # /o/   (variasi transkripsi)
        'ɔ': 'o',      # /ɔː/  thought
        'ɑ': 'a',      # /ɑː/  father
        'ɒ': 'o',      # /ɒ/   British English: lot
        'ʌ': 'a',      # /ʌ/   cup
        'ɐ': 'a',      # /ɐ/   variasi open central vowel
        'eɪ': 'e',     # day
        'aɪ': 'a',     # my
        'ɔɪ': 'o',     # boy
        'aʊ': 'a',     # now
        'oʊ': 'o',     # go
    }

    # Long vowel mark
    for i, token in enumerate(tokens):
        tokens[i] = token.replace('ː', '')

    # Mapping harus dilakukan dengan longest-match
    # agar diphthong diproses terlebih dahulu.
    for ipa, standard in sorted(
        mapping.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        for i, token in enumerate(tokens):
            tokens[i] = tokens[i].replace(ipa, standard)

    return tokens

