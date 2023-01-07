from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from dependencies import get_db, get_singer_repository, get_album_repository, get_track_repository
from repositories.album_repository import AlbumRepository
from repositories.singer_repository import SingerRepository
from repositories.track_repository import TrackRepository
from schemas.album_schemas import AlbumInDB
from schemas.artist_schemas import ArtistInDB
from schemas.track_schemas import TrackInDB

router = APIRouter()

@router.get("/singers/", response_model=List[ArtistInDB], status_code=status.HTTP_200_OK, name="get-all-singers")
async def get_all_artists(db: Session = Depends(get_db), singer_repository: SingerRepository = Depends(get_singer_repository)) -> List[ArtistInDB]:
    """Lista de todos los artistas"""

    singers = await singer_repository.find(db=db)

    return singers


@router.get("/singers/{id}/", response_model=List[AlbumInDB], status_code=status.HTTP_200_OK, name="get-all-albums-by-singers")
async def get_all_albums_by_singer(id: int, db: Session = Depends(get_db), album_repository: AlbumRepository = Depends(get_album_repository)) -> List[AlbumInDB]:
    """Lista de álbumes de un artista"""

    albums = await album_repository.findAlbumsByArtistId(artist_id=id, db=db)

    # En caso de no encontrar albunes retornamos NOT FOUND
    if not albums:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Singer not found")

    return albums


@router.get("/albums/{id}/", response_model=List[TrackInDB], status_code=status.HTTP_200_OK, name="get-all-tracks-by-album")
async def get_all_tracks_by_album(id: int, db: Session = Depends(get_db), track_repository: TrackRepository = Depends(get_track_repository)) -> List[TrackInDB]:
    """Lista de canciones de un álbum en particular"""

    tracks = await track_repository.findTracksByAlbumId(album_id=id, db=db)

    # En caso de no encontrar canciones retornamos NOT FOUND
    if not tracks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album not found")

    return tracks


@router.get("/singer/{id}/", response_model=List[TrackInDB], status_code=status.HTTP_200_OK, name="get-all-tracks-by-artist")
async def get_all_tracks_by_artist(id: int, db: Session = Depends(get_db), track_repository: TrackRepository = Depends(get_track_repository)) -> List[TrackInDB]:
    """Lista de todas las canciones de un artista en particular"""

    tracks = await track_repository.findTrackByArtistId(artist_id=id, db=db)

    # En caso de no encontrar canciones retornamos NOT FOUND
    if not tracks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Singer not found")

    return tracks


@router.get("/song/{id}/", response_model=TrackInDB, status_code=status.HTTP_200_OK, name="get-track-detail")
async def get_all_tracks_by_artist(id: int, db: Session = Depends(get_db), track_repository: TrackRepository = Depends(get_track_repository)) -> TrackInDB:
    """Detalle completo de una canción en particular"""

    track = await track_repository.findOneById(track_id=id, db=db)

    # En caso de no encontrar la canción retornamos NOT FOUND
    if not track:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Track not found")

    return track

