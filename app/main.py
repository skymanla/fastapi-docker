from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from app.routers import juso
from app.errors import exception_handler as ex
from a2wsgi import ASGIMiddleware

app = FastAPI(
    title="API Server",
    description="안전거래 벤더사 API 통신",
    version="0.0.1"
)

# exception handler
app.add_exception_handler(HTTPException, ex.http_exception_handler)
app.add_exception_handler(RequestValidationError, ex.regex_error_handler)

# 주소 검색
app.include_router(juso.router)

application = ASGIMiddleware(app)
