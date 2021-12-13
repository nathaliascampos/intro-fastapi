from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# Rota Raiz


@app.get("/")
def raiz():
    return {"Ola": "Mundo"}

# Criar model


class Usuario(BaseModel):
    id: int
    email: str
    senha: str


# Criar base de dados
base_de_dados = [
    Usuario(id=1, email="nathalia@nathalia.com.br", senha="nat123"),
    Usuario(id=2, email="teste@teste.com.br", senha="teste123")
]

# Rota Get All


@app.get("/usuarios")
def get_todos_os_usuarios():
    return base_de_dados

# Rota Get Id


@app.get("/usuarios/{id_usuario}")
def get_usuario_usando_id(id_usuario: int):
    for usuario in base_de_dados:
        if(usuario.id == id_usuario):
            return usuario

    return {"Status": 404, "Mensagem": "Não encontrou usuário"}

# Rota Insere


@app.post("/usuarios")
def insere_usuario(usuario: Usuario):
    # criar regras de negócio
    # verificar id e email
    base_de_dados.append(usuario)
    return usuario


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.post("/items/")
async def create_item(item: Item):

    item_dict = item.dict()

    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})

    return item
