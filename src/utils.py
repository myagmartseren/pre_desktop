from pathlib import Path
OUTPUT_PATH = Path(__file__).parent

def relative_to_assets(path: str) -> Path:
    ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frames")
    return ASSETS_PATH / Path(path)
def relative_to_files(path:str) -> Path:
    ASSETS_PATH = OUTPUT_PATH / Path(r"../files")
    return ASSETS_PATH / Path(path)

def read_private_key():
    private_key_path = OUTPUT_PATH / Path(r"../files/private_key")
    with open(private_key_path,"rb") as f:
        private_key = f.read()
        return private_key