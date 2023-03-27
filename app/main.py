from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError, ValidationError
from app.routers import juso, kms_api, iros_api, goods
from app.errors import exception_handler as ex
from a2wsgi import ASGIMiddleware

app = FastAPI(
    title="API Server",
    description="안전거래 벤더사 API 통신",
    version="0.0.1"
)

# exception handler
app.add_exception_handler(HTTPException, ex.http_exception_handler)
app.add_exception_handler(RequestValidationError, ex.request_error_handler)
app.add_exception_handler(ValidationError, ex.validation_error_handler)

# 주소 검색
app.include_router(juso.router)
# kms api
app.include_router(kms_api.router)
# 중솔 API
app.include_router(iros_api.router)
# 물건 상태 API
app.include_router(goods.router)

application = ASGIMiddleware(app)
