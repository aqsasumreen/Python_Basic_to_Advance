# import argparse # Requests is a really nice library. I'd like to use it for downloading big files (>1GB). The
# problem is it's not possible to keep whole file in memory; I need to read it in chunks. And this is a problem with
# the following code:
#  import requests
#
#
# def download_file(url , local_filename):
#     # local_filename = url.split('/')[-1]
#     # NOTE the stream=True parameter below
#     with requests.get(url, stream=True) as r:
#         r.raise_for_status()
#         with open(local_filename, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192):
#                 # If you have chunk encoded response uncomment if
#                 # and set chunk_size parameter to None.
#                 #if chunk:
#                 f.write(chunk)
#     return local_filename
#
#
# parser = argparse.ArgumentParser()
# parser.add_argument('url', help='URl of file to download')
# parser.add_argument('output', help=' by which name do you want to download')
# args = parser.parse_args()
# # print(args.url)
# # print(args.output)
# download_file(args.url, args.output)

