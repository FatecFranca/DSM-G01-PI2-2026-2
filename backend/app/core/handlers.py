import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from app.core.config import settings
from app.core.exceptions import (
    ConflitoError,
    DadoInvalidoError,
    NaoAutenticadoError,
    NaoAutorizadoError,
    NaoEncontradoError,
    ReenvioDeCodigoError,
    ServicoIndisponivelError,
    TentativasExcedidasError,
    VerificacaoInvalidaError,
)

logger = logging.getLogger("gymtech.errors")


def register_exception_handlers(app: FastAPI) -> None:
    """Liga cada erro de negócio (e falhas de banco/servidor) ao status HTTP correspondente."""

    @app.exception_handler(NaoAutenticadoError)
    async def nao_autenticado_handler(request: Request, exc: NaoAutenticadoError):
        return JSONResponse(
            status_code=401,
            content={"detail": str(exc)},
            headers={"WWW-Authenticate": "Bearer"},
        )

    @app.exception_handler(NaoAutorizadoError)
    async def nao_autorizado_handler(request: Request, exc: NaoAutorizadoError):
        return JSONResponse(status_code=403, content={"detail": str(exc)})

    @app.exception_handler(NaoEncontradoError)
    async def nao_encontrado_handler(request: Request, exc: NaoEncontradoError):
        return JSONResponse(status_code=404, content={"detail": str(exc)})

    @app.exception_handler(ConflitoError)
    async def conflito_handler(request: Request, exc: ConflitoError):
        return JSONResponse(status_code=409, content={"detail": str(exc)})

    @app.exception_handler(TentativasExcedidasError)
    async def tentativas_excedidas_handler(request: Request, exc: TentativasExcedidasError):
        return JSONResponse(
            status_code=429,
            content={"detail": str(exc)},
            headers={"Retry-After": str(exc.segundos_restantes)},
        )

    @app.exception_handler(VerificacaoInvalidaError)
    async def verificacao_invalida_handler(request: Request, exc: VerificacaoInvalidaError):
        return JSONResponse(status_code=400, content={"detail": str(exc)})

    @app.exception_handler(ReenvioDeCodigoError)
    async def reenvio_handler(request: Request, exc: ReenvioDeCodigoError):
        return JSONResponse(
            status_code=429,
            content={"detail": str(exc)},
            headers={"Retry-After": str(exc.segundos_restantes)},
        )

    @app.exception_handler(ServicoIndisponivelError)
    async def servico_indisponivel_handler(request: Request, exc: ServicoIndisponivelError):
        return JSONResponse(status_code=503, content={"detail": str(exc)})

    @app.exception_handler(DadoInvalidoError)
    async def dado_invalido_handler(request: Request, exc: DadoInvalidoError):
        return JSONResponse(status_code=422, content={"detail": str(exc)})

    @app.exception_handler(SQLAlchemyError)
    async def sqlalchemy_error_handler(request: Request, exc: SQLAlchemyError):
        logger.exception("Erro de banco de dados na requisição %s %s", request.method, request.url.path)
        return JSONResponse(
            status_code=503,
            content={
                "detail": "Erro ao acessar o banco de dados. Verifique se o MySQL está rodando e se o banco 'gymtech' foi criado."
            },
        )

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        logger.exception("Erro interno inesperado na requisição %s %s", request.method, request.url.path)
        detalhe = f"Erro interno no servidor: {exc}" if settings.DEBUG else "Erro interno no servidor."
        return JSONResponse(status_code=500, content={"detail": detalhe})
