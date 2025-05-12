#inportaciones de dependencias
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

#Importar los paises
from data import paises

#crear el objeto de la aplicacion
app = FastAPI()

#V vistas
#a qui se indica a fast api
#donde se encuentran las plantillas html
templates = Jinja2Templates(directory="templates")

#definir la ruta del API
@app.get("/paises", response_class=HTMLResponse)
def prueba(request: Request):
    return templates.TemplateResponse("paises.html",
                                      {
                                          "request" : request,
                                          "paises" : paises
                                       })
