import asyncio

import yaml
from fastapi import FastAPI
from yeelight import Bulb

app = FastAPI()

file_path = "conf.yaml"


@app.post("/room")
async def room_light(ct, bri):
    lamp_data: dict = get_data_yaml()
    if lamp_data.get('flag_f.lux'):
        ct = int(ct)
        bri = int(float(bri) * 100)

        bulb.set_color_temp(ct)
        bulb.set_brightness(bri)


@app.get("/rgb")
async def rgb_color(red: int, green: int, blue: int):
    bulb.set_rgb(red, green, blue)


@app.post("/set_lamp")
async def set_lamp(ip_lump: str):
    lamp_data: dict = get_data_yaml()
    lamp_data['ip_lamp'] = ip_lump
    await set_data_yaml(lamp_data)


@app.get("/get_flag")
async def get_flag():
    lamp_data: dict = get_data_yaml()
    return lamp_data.get('flag_f.lux')


@app.post("/set_flag")
async def set_flag():
    lamp_data: dict = get_data_yaml()
    lamp_data['flag_f.lux'] = not (lamp_data['flag_f.lux'])
    await set_data_yaml(lamp_data)


async def set_data_yaml(lamp_data):
    with open(file_path, 'w') as file:
        yaml.dump(lamp_data, file)


def get_data_yaml():
    with open(file_path) as file:
        dictionary_data: dict = yaml.safe_load(file)
    return dictionary_data


data = get_data_yaml()
bulb = Bulb(data.get('ip_lamp'))
