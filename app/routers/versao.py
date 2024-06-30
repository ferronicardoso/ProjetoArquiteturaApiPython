from fastapi import APIRouter

router = APIRouter()


@router.get("/versao", name="Versão", description="Obtem a versão da aplicação")
async def versao():
    return "1.0.0"
