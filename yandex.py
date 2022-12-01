def create_folder(token: str, name: str):
    disk_headers = {'Content-Type': 'application/json',
                    'Authorization': f'OAuth {token}'}
    url_disk = 'https://cloud-api.yandex.net'
    disk_create_folder_method = '/v1/disk/resources'
    response = requests.put(url_disk + disk_create_folder_method,
                 params={'path': f'/{name}'},
                 headers=disk_headers)
    return response.status_code

