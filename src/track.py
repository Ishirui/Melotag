from pathlib import Path
from PIL import Image
from datetime import date

class InvalidTrackException(ValueError):
    pass

class Track:
    def __init__(self, path:Path|str ):
        self.original_path:Path = path if path.isinstance(Path) else Path(path) #Might throw an exception, will be handled outside of the constructor
        
        if not path.is_file():
            raise InvalidTrackException(f"Path {path} does not point to file") #Path objects have a nice str()
        
        self.fileType:str = path.suffix
        
        if self.fileType != ".mp3":
            raise NotImplementedError(f"We only support mp3's for the moment, sorry !. This file was the cause: {path}")
        
        #Implemented ID3 tags
        
        self.APIC:Image = None
        self.COMM:str = None
        self.TALB:str = None
        self.TIT2:str = None
        self.TIT3:str = None
        self.IPLS:list = None
        self.PCNT:int = None
        self.TBPM:int = None
        self.TCOM:str = None
        self.TEXT:str = None
        self.TPUB:str = None
        self.TRCK:int = None
        self.TDAT:date = None
        
        #Custom features
        
        self.new_path:path = None
        
    def __repr__(self):
        path = self.original_path
        title = self.TIT2 if self.TIT2 is not None else path.stem
        artist = self.IPLS[0] if self.IPLS is not None else ""
        
        return f"Track: {title} - {artist} || {path}"
    
    def extract_tags_from_file(self):
        #TODO Find a good library for this function
        pass
        
    def generate_new_path(self, root:Path|str):
        if self.TALB is None or self.IPLS is None or self.TIT2 is None:
            raise ValueError(f"Not enough info to generate new path for {self}")
        
        path_text = f"{root}\\{self.IPLS[0]}\\{self.TALB}\\{self.TRCK} - {self.TIT2}.mp3"
        
        try:
            self.new_path = Path(path_text)
        except (RuntimeError, OSError):
            raise ValueError(f"Could not resolve path {path_text}")
            
        
        