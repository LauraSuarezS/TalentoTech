import requests, os

def download_files(url_dict):
    folder_files = r'Data raw'
    response = requests.get(url_dict["url"], stream=True)
    print(f'Descargando {url_dict["filename"]}')
    with open(os.path.join(folder_files, f'{url_dict["filename"]}.{url_dict["ext"]}'), "wb") as file:
        for chunk in response.iter_content(chunk_size=512):
            if chunk:
                file.write(chunk)


urls_dict = [
    {
        "filename": "NUSE",
        "url": r'https://datosabiertos.bogota.gov.co/dataset/9bdf518e-b756-4865-983f-0521111fbcd1/resource/30d65a8b-d0ed-4e95-977e-0d7cc2ea89ef/download/llamadastramitadas-c4-bogota_numerounicodeseguridadyemergencias-nuse_linea-123-31082022.csv',
        "ext": 'csv'
    },
    {
        "filename": "NUSETipificacion",
        "url": r'https://datosabiertos.bogota.gov.co/dataset/9bdf518e-b756-4865-983f-0521111fbcd1/resource/fa426f3f-b2b0-491b-8287-dfeca438f558/download/guiatipificacionincidentes.csv',
        "ext": 'csv'
    },
    {
        "filename": "CAI",
        "url": r'https://datosabiertos.bogota.gov.co/dataset/bcc51101-762b-4e13-9455-f77502c75a0f/resource/202c5810-6880-43f8-b801-df70aaf6d237/download/comandoatencioninmediata.geojson',
        "ext": 'geojson'
    }
]


for url_dict in urls_dict:
    download_files(url_dict)

