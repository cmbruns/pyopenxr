import os


def add_folder_to_api_layer_path(folder_name: str):
    starting_api_path = os.getenv("XR_API_LAYER_PATH")
    if starting_api_path is None or len(starting_api_path) < 1:
        os.environ["XR_API_LAYER_PATH"] = folder_name
    elif folder_name in starting_api_path.split(os.pathsep):
        pass  # It's already there
    else:
        # pro-tip: os.pathsep is very different from os.path.sep
        os.environ["XR_API_LAYER_PATH"] += f"{os.pathsep}{folder_name}"


__all__ = [
    "add_folder_to_api_layer_path",
]
