import requests

# response_get = requests.get("https://www.pygame.org/project-Pygame+Text+Input-3013-.html")
response_get = requests.delete("https://www.pygame.org/project-Pygame+Text+Input-3013-.html")


print(response_get.status_code)
print(response_get.url)
print()
print(response_get.text)
print(response_get.content)