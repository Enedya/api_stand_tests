import configuration
import requests
import data

"""def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

response = get_docs()
print(response.status_code)"""


#POST
def post_new_user(body):  #devuelve el token #Crear un nuevo usuario #(con el primer print muestra el estado de la solicitud y con el segundo se convierte en diccionario)
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados


response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


response = get_users_table()
print(response.status_code)

#SOLICITUD POST PARA SOLICITAR LOS KIT POR PRODUCTOS Main.Products → Kit search by products (Búsqueda de kits por productos).
""" def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                     json=products_ids,
                     headers=data.headers)

response = post_products_kits(data.products_ids);
print(response.status_code)
print(response.json())
#con response.json() da como resultado un diccionario """


def get_users_table():
    return None
