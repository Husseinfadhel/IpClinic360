from tortoise.transactions import in_transaction
from config import create_app
from pydantic import BaseModel
from db import Ip

app = create_app()


class PatchIP(BaseModel):
    ip: str
    user: str


@app.patch('/ip')
async def patch_ip(schema: PatchIP):
    exi = await Ip.filter(username=schema.user).exists()
    if exi:
        await Ip.filter(username=schema.user).update(ip=schema.ip)
    else:
        async with in_transaction() as conn:
            new = Ip(username=schema.user, ip=schema.ip)
            await new.save(using_db=conn)
    return {
        "success": True
    }


@app.get('/ip/{user}')
async def get_ip(user):
    query = await Ip.filter(username=user).first()
    return {
        "ip": query.ip,
        "success": True
    }
