from pydantic import UUID4, BaseModel, ConfigDict, Field


class JobResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class UserSalaryPostRequest(BaseModel):
    unique_id: UUID4
    job_id: int
    experience: int = Field(..., ge=0, le=10)
    salary: int = Field(..., gt=0, le=100_000)

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "unique_id": "2323f2ac-4066-4e32-9412-0321c70dd8dc",
                "job_id": 5,
                "experience": 2,
                "salary": 4500,
            }
        },
    )


class UserSalaryPostResponse(BaseModel):
    user_experience: int
    user_salary: int
    job_salary: int

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={"example": {"user_experience": 5, "user_salary": 5500, "job_salary": 6000}},
    )


class JobsGetResponse(BaseModel):
    job_id: int = Field(..., description="직무 id, 추후 POST 요청 시 선택한 직무 id 반환")
    name: str = Field(..., description="직무명")


class UserProfilePostRequest(BaseModel):
    unique_id: UUID4 = Field(..., description="클라이언트 uuid")
    age: int = Field(..., ge=18, le=50, description="나이")
    save_rate: int = Field(..., ge=0, le=100, description="저축률")
    has_car: bool = Field(..., description="자동차 보유")
    monthly_rent: bool = Field(..., description="웰세 여부")

    class Config:
        use_enum_values = True


class UserCarRankResponse(BaseModel):
    car: str = Field(..., description="자동차 등급")
    percentage: int = Field(..., description="비교 등급")
