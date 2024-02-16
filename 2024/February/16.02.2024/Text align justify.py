"""
Your task in this Kata is to emulate text justification in monospace font. You will be given a single-lined text and the expected justification width. The longest word will never be greater than this width.

Here are the rules:

Use spaces to fill in the gaps between words.
Each line should contain as many words as possible.
Use '\n' to separate lines.
Gap between words can't differ by more than one space.
Lines should end with a word not a space.
'\n' is not included in the length of a line.
Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
Last line should not be justified, use only one space between words.
Last line should not contain '\n'
Strings with one word do not need gaps ('somelongword\n').
Example with width=30:

Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor.
Also you can always take a look at how justification works in your text editor or directly in HTML (css: text-align: justify).

Have fun :)
"""


def justify(text: str, width: int) -> str:
    """
    This function takes in a single line of text and a maximum width, and returns the justified text.

    The function breaks the text into words, and then attempts to fit each word onto a line while keeping the total width within the specified limit. It does this by adding spaces between words to adjust the spacing as needed.

    The function handles situations where the last word does not fit on the last line by adding a space to the end of the line, rather than truncating the word.

    Args:
        text (str): The text to justify.
        width (int): The maximum width of the justified text.

    Returns:
        str: The justified text.

    """
    words = text.split()
    lines = []
    current_line = words[0]

    for word in words[1:]:
        if len(current_line) + len(word) + 1 <= width:
            current_line += ' ' + word
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)

    justified_text = ""
    for i in range(len(lines) - 1):
        line = lines[i]
        line_words = line.split()
        num_words = len(line_words)
        num_spaces_needed = width - sum(len(word) for word in line_words)
        num_gaps = num_words - 1
        if num_gaps > 0:
            spaces_per_gap, extra_spaces = divmod(num_spaces_needed, num_gaps)
            justified_line = ""
            for j in range(num_words - 1):
                justified_line += line_words[j] + ' ' * (spaces_per_gap + (1 if j < extra_spaces else 0))
            justified_line += line_words[-1]
            justified_text += justified_line + '\n'
        else:
            justified_text += line + '\n'

    justified_text += lines[-1]

    return justified_text


if __name__ == '__main__':
    justify('123 45 6', 7)
