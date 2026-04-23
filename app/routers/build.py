import uuid

from fastapi import APIRouter, HTTPException, Query, status

from app.schemas.build import (
    BuildCompileRequest,
    BuildCompileResponse,
    BuildLogResponse,
    ObjdumpResponse,
)

router = APIRouter(prefix="/api/v1/build", tags=["build"])


@router.post(
    "/compile",
    response_model=BuildCompileResponse,
    status_code=status.HTTP_201_CREATED,
    summary="빌드 실행",
    description="격리된 환경에서 C/ASM 소스 코드를 ELF 바이너리로 컴파일한다.",
    response_description="생성된 빌드 레코드 및 상태",
)
def compile_file(body: BuildCompileRequest):
    # TODO: 격리 컨테이너에서 컴파일 실행, Build 레코드 생성
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "Not implemented")


@router.get(
    "/objdump",
    response_model=ObjdumpResponse,
    summary="역어셈블",
    description="빌드된 ELF 바이너리의 기계어를 어셈블리어로 변환하여 반환한다.",
    response_description="objdump 결과 텍스트",
)
def objdump_file(
    file_id: uuid.UUID = Query(..., description="역어셈블 대상 파일 ID"),
):
    # TODO: 최신 성공 빌드의 binary_path 를 objdump 실행 후 텍스트 반환
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "Not implemented")


@router.get(
    "/logs",
    response_model=BuildLogResponse,
    summary="로그 조회",
    description="지정된 빌드의 컴파일 에러 및 경고 메시지(stdout/stderr)를 조회한다.",
    response_description="빌드 로그 텍스트",
)
def get_build_logs(
    build_id: uuid.UUID = Query(..., description="조회할 빌드 ID"),
):
    # TODO: build_id 로 저장된 로그 파일/컬럼 읽어 반환
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "Not implemented")
