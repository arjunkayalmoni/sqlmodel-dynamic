from sqlmodel import SQLModel, Field


class SongBase(SQLModel):
    name: str
    artist: str
    year: int | None = None


class Song(SongBase, table=True):
    id: int = Field(default=None, primary_key=True)


class SongCreate(SongBase):
    pass


class SongRead(SongBase):
    pass
