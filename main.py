from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from enum import Enum

from EEGGenerator import EEGGenerator

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


class AlgorithmName(str, Enum):
    ica = "ICA"
    dwt = "DWT"
    ar = "AR"


@app.get('/eeg-generator')
async def eeg_generator(request: Request):
    eeg_generator = EEGGenerator(fs=256, start_time=0, end_time=10)
    signal = eeg_generator.simulate_eeg()
    eeg_generator.visualize(signal)
    eeg_generator.save_to_csv(signal)
    return templates.TemplateResponse("synthetic-eeg-generator.html", {"request": request})

@app.get('/eeg-loader')
async def eeg_loader(request: Request):
    return templates.TemplateResponse("eeg-loader.html", {"request": request})


@app.get("/")
async def read_root(request: Request):
     return templates.TemplateResponse("start.html", {"request": request})


@app.get("/algorithm/{algorithm_name}")
async def get_algorithm(algorithm_name: AlgorithmName):
    if algorithm_name == AlgorithmName.ica:
        return {"algorithm_name": algorithm_name, "message": "ICA"}

    return {"algorithm_name": "None", "message": "Choose algorithm"}