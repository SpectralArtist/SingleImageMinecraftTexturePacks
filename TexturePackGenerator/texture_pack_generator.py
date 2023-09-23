import os
import shutil
import json
import zipfile

from ansi.print_colors import color_print
import ansi.ansi_codes.color as color

def generate_texture_pack(image_path: str, destination_path: str):
    if not os.path.exists(image_path):
        color_print(f"Image path '{image_path}' does not exist.", color=color.RED)
        return
    
    if not os.path.isfile(image_path):
        color_print(f"Image path '{image_path}' is not a file.", color=color.RED)
        return

    if not os.path.exists(destination_path):
        color_print(f"Destination path '{destination_path}' does not exist.", color=color.RED)
        return
    
    if not os.path.isdir(destination_path):
        color_print(f"Destination path must be a directory and '{destination_path}' is not.", color=color.RED)
        return
        
    file_extension = os.path.splitext(image_path)[-1].lower()
    if file_extension != ".png":
        color_print("The image file is not a PNG file. Texture pack can no longer be guaranteed to work after generation.", color.YELLOW)

    with open("./config.json") as config_file:
        config_json = json.loads(config_file.read())
        config_file.close()

    textures_path = os.path.join(destination_path, "src", "assets", "minecraft", "textures")
    os.makedirs(textures_path, exist_ok=True)
    file_path_list = traverse_config(textures_path, config_json)

    total_space_needed = os.path.getsize(image_path) * len(file_path_list)
    if check_disk_space(destination_path, total_space_needed):
        color_print(f"Not enough space on disk! {total_space_needed} bytes required to run!", color.RED)
        raise OSError("Not enough space on disk!")

    for file_path in file_path_list:
        shutil.copy(image_path, f"{file_path}{file_extension}")

    shutil.make_archive("textures", "zip", os.path.join(destination_path, "src"))
    textures_zip = zipfile.ZipFile(os.path.join(os.getcwd(), "textures.zip"), 'a')
    textures_zip.write(os.path.join(os.getcwd(), "pack.mcmeta"), "pack.mcmeta")

    return

def check_disk_space(destination_path: str, total_space_needed: int):
    _, _, free = shutil.disk_usage(destination_path)

    return total_space_needed > free

def traverse_config(directory_path: str, config: dict) -> list[str]:
    if not os.path.exists(directory_path):
        os.mkdir(directory_path)
    
    file_path_list = []
    for key, value in config.items():
        if isinstance(value, dict):
            sub_directory_path = os.path.join(directory_path, key)
            sub_directory_file_path_list = traverse_config(sub_directory_path, value)
            file_path_list += sub_directory_file_path_list

        elif value:
            file_path = os.path.join(directory_path, key)
            file_path_list.append(file_path)

    return file_path_list