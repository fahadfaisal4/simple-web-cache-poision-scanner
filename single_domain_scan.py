import requests
from colorama import Fore, Back, Style



def space_line():
    line = "-"
    print(Fore.YELLOW + line.center(100,"-"))



domain = input(Fore.GREEN + "The domain need to test: ")

domain_scan = "https://"+ domain + "/favicon.ico?version=poc123"



default_headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0' ,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','Connection': 'keep-alive','Cookie': 'amp_ddd6ec=6LwNeSYMZM-n7G2uV7Arh8...1frqdddb9.1frqdo4fu.12.15.27; _gcl_au=1.1.1342798764.1641930296; _ga=GA1.1.690315493.1641930298; _ga_9VSBF2K4BX=GS1.1.1644785199.12.1.1644785571.0; amplitude_id_ddd6ece4d5ddebbf244a249703c9d662opensea.io=eyJkZXZpY2VJZCI6IjMxN2I4Y2QyLTE1OWMtNDBiZC05MDM5LWJmYjc2OWY1MjE4NFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY0Mjc5NzkxNjc2NCwibGFzdEV2ZW50VGltZSI6MTY0Mjc5ODI2NzEzNSwiZXZlbnRJZCI6MjIsImlkZW50aWZ5SWQiOjI0LCJzZXF1ZW5jZU51bWJlciI6NDZ9; _ga_QN8V4MT4GF=GS1.1.1644785182.9.1.1644786001.0; _zendesk_cookie=BAhJIhl7ImRldmljZV90b2tlbnMiOnt9fQY6BkVU--459ed01949a36415c1716b5711271c3d08918307; cf_clearance=.gRQfmAjNAjGh7a.9CdelbjD0eT0qTMseRK19q8h6PQ-1642691128-0-150; __cfruid=f7f63e2ace4e4d724dac16c1dbafe94e4f6e58e5-1644765382; _help_center_session=QjFkUjlvVGNxZXYvMnIrQ2IvUG1saVNlcnZ1RlFBTzZ2UVFwZTdQK015bXZVSUtBMlZ0SGlacXJYUEI0VTlwT1NmRldOUWpJQ2tzaW1UODdoNFROUDhFYzlIaG42d1paRmZoL1p6NnBhd3orZHp3WDhNaWFpVTBhcHB2NWdZT04tLXliaGhlSDhoOWsvMDhpQ1JKZ0NQWHc9PQ%3D%3D--f8d299ad6371592563dfeb361a69dd465d0e46a4; _gid=GA1.2.617533610.1644785200; _zendesk_session=BAh7CkkiD3Nlc3Npb25faWQGOgZFVEkiJTQ2OGFjYjkzNjA1YzEwMzk0ZjUzNzJiZjk3ZDIyNGJmBjsAVEkiDGFjY291bnQGOwBGaQMJ96JJIgpyb3V0ZQY7AEZpA0fcQUkiDmlzX21vYmlsZQY7AFRGSSITd2FyZGVuLm1lc3NhZ2UGOwBUewA%3D--f1b2f49e3295e0933f3cd0f0f72e2d2dec486776; _zendesk_shared_session=-ZmxwMFU1OWw5VzhOZW9SY3UwNXpIaGdLeEhoQzR2UGh0NDM4eWdiTHF0UytYNzUxL3VZRm1pWnBoN1RhaGg1RWtqaUxvZTBWVVhJcjYzL2lkSHBlQnU2SnJlM1dORGh2Z0lva0c1L3NwT2UxYnlOSlBqWmsweS9wSis5UlJlOWhibmxrWFNmelplc0d4dk9sOWl6T0NBPT0tLWdGYzVwMEZqdUd0QnU2NUpjb2RDMmc9PQ%3D%3D--596903f958a6a233bd1e986642cf0936ca2bd332','Upgrade-Insecure-Requests': '1','Pragma': 'no-cache' ,'Cache-Control': 'no-cache','TE': 'Trailers','x-forwarded-scheme': 'http'}

cookies = {'Cookie': 'amp_ddd6ec=6LwNeSYMZM-n7G2uV7Arh8...1frqdddb9.1frqdo4fu.12.15.27; _gcl_au=1.1.1342798764.1641930296; _ga=GA1.1.690315493.1641930298; _ga_9VSBF2K4BX=GS1.1.1644785199.12.1.1644785571.0; amplitude_id_ddd6ece4d5ddebbf244a249703c9d662opensea.io=eyJkZXZpY2VJZCI6IjMxN2I4Y2QyLTE1OWMtNDBiZC05MDM5LWJmYjc2OWY1MjE4NFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY0Mjc5NzkxNjc2NCwibGFzdEV2ZW50VGltZSI6MTY0Mjc5ODI2NzEzNSwiZXZlbnRJZCI6MjIsImlkZW50aWZ5SWQiOjI0LCJzZXF1ZW5jZU51bWJlciI6NDZ9; _ga_QN8V4MT4GF=GS1.1.1644785182.9.1.1644786001.0; _zendesk_cookie=BAhJIhl7ImRldmljZV90b2tlbnMiOnt9fQY6BkVU--459ed01949a36415c1716b5711271c3d08918307; cf_clearance=.gRQfmAjNAjGh7a.9CdelbjD0eT0qTMseRK19q8h6PQ-1642691128-0-150; __cfruid=f7f63e2ace4e4d724dac16c1dbafe94e4f6e58e5-1644765382; _help_center_session=QjFkUjlvVGNxZXYvMnIrQ2IvUG1saVNlcnZ1RlFBTzZ2UVFwZTdQK015bXZVSUtBMlZ0SGlacXJYUEI0VTlwT1NmRldOUWpJQ2tzaW1UODdoNFROUDhFYzlIaG42d1paRmZoL1p6NnBhd3orZHp3WDhNaWFpVTBhcHB2NWdZT04tLXliaGhlSDhoOWsvMDhpQ1JKZ0NQWHc9PQ%3D%3D--f8d299ad6371592563dfeb361a69dd465d0e46a4; _gid=GA1.2.617533610.1644785200; _zendesk_session=BAh7CkkiD3Nlc3Npb25faWQGOgZFVEkiJTQ2OGFjYjkzNjA1YzEwMzk0ZjUzNzJiZjk3ZDIyNGJmBjsAVEkiDGFjY291bnQGOwBGaQMJ96JJIgpyb3V0ZQY7AEZpA0fcQUkiDmlzX21vYmlsZQY7AFRGSSITd2FyZGVuLm1lc3NhZ2UGOwBUewA%3D--f1b2f49e3295e0933f3cd0f0f72e2d2dec486776; _zendesk_shared_session=-ZmxwMFU1OWw5VzhOZW9SY3UwNXpIaGdLeEhoQzR2UGh0NDM4eWdiTHF0UytYNzUxL3VZRm1pWnBoN1RhaGg1RWtqaUxvZTBWVVhJcjYzL2lkSHBlQnU2SnJlM1dORGh2Z0lva0c1L3NwT2UxYnlOSlBqWmsweS9wSis5UlJlOWhibmxrWFNmelplc0d4dk9sOWl6T0NBPT0tLWdGYzVwMEZqdUd0QnU2NUpjb2RDMmc9PQ%3D%3D--596903f958a6a233bd1e986642cf0936ca2bd332'}



session = requests.Session()
session.max_redirects = 10

sending_request = session.get(url = domain_scan, headers = default_headers, cookies = cookies , allow_redirects=False)
    
space_line()
print(Fore.BLUE + "The status code : " + str(sending_request.status_code))
space_line()
print(Fore.RED + "The url used for testing : " + sending_request.url)
space_line()
print("Response Headers : " + str(sending_request.headers))

response_headers = sending_request.headers

status_code = sending_request.status_code
space_line()




try:
    sending_request = session.get(url = domain_scan, headers = default_headers, cookies = cookies , allow_redirects=True)
    

except requests.exceptions.TooManyRedirects:
    space_line()
    print(Fore.GREEN + "Target Is vulnerable")
    







