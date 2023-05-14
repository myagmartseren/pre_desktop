from pathlib import Path

OUTPUT_PATH = Path(__file__).parent

def relative_to_assets(path: str) -> Path:
    ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frames")
    return ASSETS_PATH / Path(path)
def relative_to_files(path:str) -> Path:
    ASSETS_PATH = OUTPUT_PATH / Path(r"../files")
    return ASSETS_PATH / Path(path)
