import sys

from ansi.print_colors import color_print
import ansi.ansi_codes.color as color

from texture_tree_generator import generate_texture_tree

TEXTURES_ARG_INDEX = 1

try:
    textures_path = sys.argv[TEXTURES_ARG_INDEX]
except IndexError as e:
    color_print(f"Failed to find argument for the textures directory.", color=color.RED)
    color_print(f"Remember to run file with `python3 <script_path> <textures_path>`", color=color.RED)

    raise e

generate_texture_tree(textures_path)