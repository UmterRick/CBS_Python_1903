from short_url import ShortUrl



url_service = ShortUrl()


while True:
    action = input("Add, get or exit")
    match action:
        case 'add':
            url = input("Add url: ")
            name = input("Create Name: ")
            url_service.write_new_url(url, name)
        case 'get':
            name = input("Name: ")
            url = url_service.get_url_by_name(name)
            print(url)
        case 'exit':
            break


