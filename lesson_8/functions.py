print("START OF THE SCRIPT")

some_url = "https://www.google.com/search?q=python&sca_esv=90c5a382e857b6e1&sxsrf=ACQVn09fts-Q5NOVO2yo5NcM3VUV4v3w2g%3A1712387753774&source=hp&ei=qfYQZr3SLKCUxc8PkJ2d4AI&iflsig=ANes7DEAAAAAZhEEuSRolE4_qkT7PSqpjCZYGPzt7mdC&udm=&ved=0ahUKEwj9yp2-ha2FAxUgSvEDHZBOBywQ4dUDCBU&uact=5&oq=python&gs_lp=Egdnd3Mtd2l6IgZweXRob24yDBAjGIAEGIoFGBMYJzIMECMYgAQYigUYExgnMgoQIxiABBiKBRgnMg0QABiABBiKBRhDGLEDMggQABiABBixAzIQEAAYgAQYigUYQxixAxiDATIIEAAYgAQYywEyDRAAGIAEGIoFGEMYsQMyCBAAGIAEGLEDMgoQABiABBiKBRhDSO0MUOEGWLkKcAF4AJABAJgBYqABrQSqAQE2uAEDyAEA-AEBmAIHoALZBKgCCsICBxAjGOoCGCfCAgsQABiABBixAxiDAcICDhAAGIAEGIoFGLEDGIMBwgIUEC4YgAQYigUYsQMYgwEYxwEYrwHCAgUQABiABMICERAuGIAEGLEDGIMBGMcBGNEDwgIKEC4YgAQYigUYQ5gDD5IHAzQuM6AH2T8&sclient=gws-wiz"
# if some_url.startswith("http"):
#     short_url = some_url.split("/")[2]
# else:
#     short_url = None


def make_short_url():
    print("\tSTART OF THE FUNCTION")
    if some_url.startswith("http"):
        short_url = some_url.split("/")[2]

    else:
        short_url = None
    print(f"\tShort URL is: {short_url}")
    print("\tEND OF THE FUNCTION")


for i in range(10):
    print(f"{i}) make function call")
    make_short_url()

print("END OF THE SCRIPT")


'''
DRY - Dont Repeat Yourself
'''
