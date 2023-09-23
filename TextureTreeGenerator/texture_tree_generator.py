import os
import json

from ansi.print_colors import color_print
import ansi.ansi_codes.background as background
import ansi.ansi_codes.color as color
import ansi.ansi_codes.normal as normal
import ansi.ansi_codes.style as style

def generate_texture_tree(textures_path: str):
    if not os.path.exists(textures_path):
        color_print(f"Textures path '{textures_path}' does not exist.", color=color.RED)
        return
    
    if not os.path.isdir(textures_path):
        color_print(f"Textures path must be a directory and '{textures_path}' is not.", color=color.RED)
        return
    
    config = search_textures(textures_path)
    print(config)

    with open("config.json", 'w') as config_file:
        pretty_config = json.dumps(config, indent=4)
        config_file.write(pretty_config)
        config_file.close()

    return

def search_textures(path: str):
    config = {}
    item_list = os.listdir(path)

    for item in item_list:
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):
            config[item] = search_textures(item_path)
            
        elif os.path.isfile(item_path) and os.path.splitext(item_path)[-1] == ".png":
            file_name = os.path.splitext(item)[0]
            config[file_name] = True

    return config