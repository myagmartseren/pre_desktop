from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frames")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
