import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class FileCreate(BaseModel):
    """POST /api/v1/files 요청 바디 — 소스 코드 저장/업데이트."""

    title: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="파일 제목 (예: hello.c)",
    )
    content: str = Field(
        ...,
        description="소스 코드 본문",
    )
    lang: str = Field(
        ...,
        max_length=16,
        description="언어 식별자 (예: c, asm)",
    )


class FileSummary(BaseModel):
    """파일 목록 조회 시 단일 항목."""

    model_config = ConfigDict(from_attributes=True)

    file_id: uuid.UUID
    title: str
    lang: str
    updated_at: datetime | None = None


class FileDetail(BaseModel):
    """파일 상세 조회 응답 — 본문 포함."""

    model_config = ConfigDict(from_attributes=True)

    file_id: uuid.UUID
    title: str
    lang: str
    content: str
    updated_at: datetime | None = None
