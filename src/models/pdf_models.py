from pathlib import Path
from pydantic import BaseModel


class PDF(BaseModel):
    path: Path
