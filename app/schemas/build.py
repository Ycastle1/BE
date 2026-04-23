import uuid

from pydantic import BaseModel, Field


class BuildCompileRequest(BaseModel):
    """POST /api/v1/build/compile 요청 바디."""

    file_id: uuid.UUID = Field(
        ...,
        description="컴파일 대상 파일 ID",
    )
    compiler_opt: str = Field(
        ...,
        max_length=255,
        description="컴파일러 옵션 문자열 (예: '-O2 -Wall')",
    )


class BuildCompileResponse(BaseModel):
    """컴파일 실행 결과."""

    build_id: uuid.UUID
    status: str = Field(..., description="success | failed")
    binary_path: str | None = None


class ObjdumpResponse(BaseModel):
    """objdump 역어셈블 결과."""

    file_id: uuid.UUID
    assembly: str = Field(..., description="역어셈블된 어셈블리 텍스트")


class BuildLogResponse(BaseModel):
    """컴파일 로그 (stdout/stderr) 조회 결과."""

    build_id: uuid.UUID
    stdout: str = ""
    stderr: str = ""
