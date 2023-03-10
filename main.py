import yaml
from fastapi import FastAPI
from yeelight import Bulb

app = FastAPI()

file_path = "conf.yaml"

with open(file_path) as file:
    dictionary_data = yaml.safe_load(file)
    ip_lamp = dictionary_data.get('ip_lamp')
    flag = dictionary_data.get('flag_f.lux')


@app.post("/room")
async def room_light(ct, bri):
    if flag:
        ct = int(ct)
        bri = int(float(bri) * 100)

        bulb.set_color_temp(ct)
        bulb.set_brightness(bri)


@app.get("/rgb")
async def rgb_color(red: int, green: int, blue: int):
    bulb.set_rgb(red, green, blue)


@app.post("/set_lamp")
async def set_lamp(ip_lump: str):
    dictionary_data['ip_lamp'] = ip_lump
    await set_data_yaml(dictionary_data)


@app.get("/get_flag")
async def get_flag():
    return dictionary_data.get('flag_f.lux')


@app.post("/set_flag")
async def set_flag():
    dictionary_data['flag_f.lux'] = not(dictionary_data['flag_f.lux'])
    await set_data_yaml(dictionary_data)


async def set_data_yaml(data):
    with open(file_path, 'w') as file:
        yaml.dump(data, file)


bulb = Bulb(ip_lamp)
