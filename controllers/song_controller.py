from fastapi import APIRouter, Body, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from dependencies import get_blog_repo, get_db

router = APIRouter(
    prefix="/songs",
    tags=["Songs"]
)