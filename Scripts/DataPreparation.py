import requests
import pandas as pd
import geopandas as gpd

### NUSE
nuse_df = pd.read_csv(
    r"https://raw.githubusercontent.com/LauraSuarezS/TalentoTech/main/Data%20raw/NUSE.csv",
    encoding="latin-1",
    sep=";",
)
nuse_df["ID"] = nuse_df["ID"].astype("string")
nuse_df["TIPO_INCIDENTE"] = nuse_df["TIPO_INCIDENTE"].astype("string")
nuse_df["TIPO_DETALLE"] = nuse_df["TIPO_DETALLE"].astype("string")
nuse_df["LOCALIDAD"] = nuse_df["LOCALIDAD"].astype("string")
nuse_df["COD_UPZ"] = nuse_df["COD_UPZ"].astype("string")
nuse_df["UPZ"] = nuse_df["UPZ"].astype("string")
nuse_df = nuse_df.drop_duplicates()


### Tipificación NUSE
nuse_tipificacion_df = pd.read_csv(
    r"https://raw.githubusercontent.com/LauraSuarezS/TalentoTech/main/Data%20raw/NUSETipificacion.csv",
    encoding="latin-1",
    sep=";",
)
nuse_tipificacion_df["COD_INCIDENTE"] = nuse_tipificacion_df["COD_INCIDENTE"].astype(
    "string"
)
nuse_tipificacion_df["INCIDENTE"] = nuse_tipificacion_df["INCIDENTE"].astype("string")
nuse_tipificacion_df["INCIDENTE"] = nuse_tipificacion_df["INCIDENTE"].str.upper()
nuse_tipificacion_df["DEFINICION"] = nuse_tipificacion_df["DEFINICION"].astype("string")
nuse_tipificacion_df["DEFINICION"] = nuse_tipificacion_df["DEFINICION"].str.upper()
nuse_tipificacion_df = nuse_tipificacion_df.drop_duplicates()


## CAI's
cai_response = requests.get(
    r"https://raw.githubusercontent.com/LauraSuarezS/TalentoTech/main/Data%20raw/CAI.geojson"
)
cai_df = gpd.read_file(cai_response.text)
cai_df["CAICOD_ENT"] = cai_df["CAICOD_ENT"].astype("int64")
cai_df["CAICOD_PRO"] = cai_df["CAICOD_PRO"].astype("int64")
cai_df["CAIFECHA_I"] = cai_df["CAIFECHA_I"].astype("datetime64[ns]")
cai_df["CAIFECHA_F"] = cai_df["CAIFECHA_F"].astype("datetime64[ns]")
cai_df["CAIDESCRIP"] = cai_df["CAIDESCRIP"].astype("string")
cai_df["CAIDESCRIP"] = cai_df["CAIDESCRIP"].str.upper()
cai_df["CAIEST_PRO"] = cai_df["CAIEST_PRO"].astype("string")
cai_df["CAIINTERV_"] = cai_df["CAIINTERV_"].astype("string")
cai_df["CAIDIR_SIT"] = cai_df["CAIDIR_SIT"].astype("string")
cai_df["CAIHORARIO"] = cai_df["CAIHORARIO"].astype("string")
cai_df["CAITELEFON"] = cai_df["CAITELEFON"].astype("Int64")
cai_df["CAIIUUPLAN"] = cai_df["CAIIUUPLAN"].astype("string")
cai_df["CAIIUSCATA"] = cai_df["CAIIUSCATA"].astype("Int64")
cai_df["CAIIULOCAL"] = cai_df["CAIIULOCAL"].astype("Int64")
cai_df["CAITEQUIPA"] = cai_df["CAITEQUIPA"].astype("string")
cai_df["CAITEQUIPA"] = cai_df["CAITEQUIPA"].str.upper()
cai_df["CAICELECTR"] = cai_df["CAICELECTR"].astype("string")
cai_df["CAICELECTR"] = cai_df["CAICELECTR"].str.upper()
cai_df["CAICONTACT"] = cai_df["CAICONTACT"].astype("string")
cai_df["CAICONTACT"] = cai_df["CAICONTACT"].str.upper()
cai_df["CAIPWEB"] = cai_df["CAIPWEB"].astype("string")
cai_df["CAIPWEB"] = cai_df["CAIPWEB"].str.upper()
cai_df["CAIIDENTIF"] = cai_df["CAIIDENTIF"].astype("string")
cai_df["CAINOMBRE"] = cai_df["CAINOMBRE"].astype("string")
cai_df["CAINOMBRE"] = cai_df["CAINOMBRE"].str.upper()
cai_df["CAIFECHA_C"] = cai_df["CAIFECHA_C"].astype("datetime64[ns]")
cai_df["CAIEASOCIA"] = cai_df["CAIEASOCIA"].astype("string")
cai_df["CAIEASOCIA"] = cai_df["CAIEASOCIA"].str.upper()
cai_df["CAIFUNCION"] = cai_df["CAIFUNCION"].astype("string")
cai_df["CAIFUNCION"] = cai_df["CAIFUNCION"].str.upper()
cai_df["CAISERVICI"] = cai_df["CAISERVICI"].astype("string")
cai_df["CAISERVICI"] = cai_df["CAISERVICI"].str.upper()

cai_campos_dict = {
    "OBJECTID": "OBJECTID",
    "CAIDESCRIP": "DESCRIPCION",
    "CAIHORARIO": "HORARIO",
    "CAITELEFON": "TELEFONO",
    "CAIIULOCAL": "IDENTIFICADOR_UNICO_LOCALIDAD",
    "CAICELECTR": "CORREO_ELECTRONICO",
    "CAICONTACT": "CONTACTO",
    "CAIPWEB": "PAGINA_WEB",
    "CAINOMBRE": "NOMBRE",
    "CAIFECHA_C": "FECHA_CORTE",
    "CAICOD_PLA": "CODIGO_PLAN",
    "CAICOD_PRO": "CODIGO_PROYECTO",
    "CAIANIO_GE": "ANIO",
    "CAIFECHA_I": "FECHA_INICIAL",
    "CAIFECHA_F": "FECHA_FINAL",
    "CAIEST_PRO": "ESTADO_PROYECTO",
    "CAIINTERV_E": "INTERVENCION_ESPACIO_PUBLICO",
    "CAIDIR_SIT": "DIRECCION_SITIO",
    "CAICOD_SIT": "IDENTIFICADOR_SEGPLAN",
    "CAITEQUIPA": "TIPO_EQUIPAMIENTO",
    "CAIEASOCIA": "EQUIPAMIENTO_ASOCIADO",
    "CAIFUNCION": "FUNCIONALIDAD",
    "CAISERVICI": "SERVICIO",
    "CAIIUUPLAN": "CODIGO_UPZ",
}

cai_df = cai_df.rename(columns=cai_campos_dict)
cai_df = cai_df.drop_duplicates()
cai_upz_cant_df = (
    cai_df.groupby("CODIGO_UPZ", as_index=False)
    .size()
    .rename(columns={"size": "CANTIDAD_CAI"})
)


# Join de datasets

result_security_df = nuse_df.merge(
    nuse_tipificacion_df, how="left", left_on="TIPO_INCIDENTE", right_on="COD_INCIDENTE"
)
result_security_df = result_security_df.merge(
    cai_upz_cant_df, how="left", left_on="COD_UPZ", right_on="CODIGO_UPZ"
)

# Filtrado de columnas

result_security_df = result_security_df[
    [
        "ANIO",
        "MES",
        "LOCALIDAD",
        "UPZ",
        "CANT_INCIDENTES",
        "INCIDENTE",
        "DEFINICION",
        "CANTIDAD_CAI",
    ]
]

result_security_df["CANTIDAD_CAI"] = (
    result_security_df["CANTIDAD_CAI"].fillna(0).astype("int64")
)

result_security_df = result_security_df[
    result_security_df["INCIDENTE"].isin(
        [
            "RIÑA",
            "ALTERACIÓN DEL ORDEN PÚBLICO",
            "PERSONA O VEHÍCULO SOSPECHOSO",
            "ATRACO / HURTO EN PROCESO",
        ]
    )
]
result_security_df.to_csv(r"Data refinada\security.csv", sep=";", index=False)
