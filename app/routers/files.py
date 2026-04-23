import uuid

from fastapi import APIRouter, Header, HTTPException, status

from app.schemas.file import FileCreate, FileDetail, FileSummary

router = APIRouter(prefix="/api/v1/files", tags=["files"])


@router.get(
    "",
    response_model=list[FileSummary],
    summary="파일 목록 조회",
    description="사용자가 보유한 모든 소스 코드 파일의 요약 목록을 반환한다.",
    response_description="파일 요약 정보 리스트",
)
def list_files(user_id: str = Header(..., description="요청 사용자 ID")):
    # TODO: user_id 로 소유 파일 조회 (app/services/file_service.py 예정)
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "Not implemented")


@router.get(
    "/{file_id}",
    response_model=FileDetail,
    summary="파일 열기",
    description="특정 소스 코드의 상세 내용(본문 포함)을 조회한다.",
    response_description="파일 상세 정보",
)
def get_file(file_id: uuid.UUID):
    # TODO: file_id 로 파일 본문/메타데이터 조회
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "Not implemented")


@router.post(
    "",
    response_model=FileDetail,
    status_code=status.HTTP_201_CREATED,
    summary="코드 저장",
    description="새로운 소스 코드를 저장하거나 기존 코드를 업데이트한다.",
    response_description="저장된 파일 상세 정보",
)
def create_or_update_file(
    body: FileCreate,
    user_id: str = Header(..., description="요청 사용자 ID"),
):
    # TODO: title 기준 upsert — 동일 title 있으면 업데이트, 없으면 신규 생성
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "Not implemented")


@router.delete(
    "/{file_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="파일 삭제",
    description="특정 저장 파일을 삭제한다. 연관된 빌드 결과물도 함께 삭제된다.",
    response_description="삭제 완료 (빈 응답)",
)
def delete_file(file_id: uuid.UUID):
    # TODO: 소유권 검증 후 삭제
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "Not implemented")
