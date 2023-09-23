import ansi.ansi_codes.normal as normal

def color_print(text, background = 0, color = 0, style = 0):
    background_code = f"\33[{background}m" if background > 0 else ""
    color_code = f"\33[{color}m" if color > 0 else ""
    style_code = f"\33[{style}m" if style > 0 else ""
    reset_code = f"\33[{normal.NORMAL}m"

    print(background_code + color_code + style_code + text + reset_code)