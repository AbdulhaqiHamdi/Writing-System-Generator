import eng_to_ipa as p
from g2p_id import G2P

def convert_en_to_ipa(text):
    """
    Convert the given text to its IPA representation.

    Args:
        text (str): The input text to be converted.

    Returns:
        str: The IPA representation of the input text.
    """
    return p.convert(text)

# def convert_id_to_ipa(text):
#     """
#     Convert the given Indonesian text to its IPA representation.

#     Args:
#         text (str): The input Indonesian text to be converted.

#     Returns:
#         str: The IPA representation of the input Indonesian text.
#     """
#     g2P = G2p()
#     return g2p(text)