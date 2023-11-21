import uvicorn

from app.main import create_app
from app.conf.settings import settings

app = create_app()

if __name__ == '__main__':
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=settings.PORT,
        loop='uvloop',
    )
