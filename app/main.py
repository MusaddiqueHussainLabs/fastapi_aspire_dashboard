import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.api_v1.api import api_router

import logging
from app.handlers.otlp_tracing import configure_oltp_grpc_tracing
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

logging.basicConfig(level=logging.INFO)
tracer = configure_oltp_grpc_tracing()
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Fast API",
    version="1.0",
    description="Fast API description",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

FastAPIInstrumentor.instrument_app(app)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)

# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8080, log_level='info')