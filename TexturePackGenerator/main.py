import sys

from texture_pack_generator import generate_texture_pack

from ansi.print_colors import color_print
import ansi.ansi_codes.color as color

IMAGE_ARG_INDEX = 1
DESTINATION_ARG_INDEX = 2

try:
    image_path = sys.argv[IMAGE_ARG_INDEX]
except IndexError as e:
    color_print(f"Failed to find argument for image path.", color=color.RED)
    color_print(f"Remember to run file with `python3 <script_path> <image_path> <destination_path>`", color=color.RED)

    raise e

try:
    destination_path = sys.argv[DESTINATION_ARG_INDEX]
except IndexError as e:
    color_print(f"Failed to find argument for destination path.", color=color.RED)
    color_print(f"Remember to run file with `python3 <script_path> <image_path> <destination_path>`", color=color.RED)

    raise e

generate_texture_pack(image_path, destination_path)