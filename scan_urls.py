import requests


def scan_urls(start, end, pl_start=0, pl_end=0):
    for i in range(start, end + 1):
        for j in range(pl_start, pl_end + 1):
            url = f"https://view.shahaf.info/0/0/{i}"
            payload = {"TimeTableView1%24ControlId": str(j)}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print(f"URL {url} payload {j} returned status code 200")
                if "מערכת" in response.text:
                    print(f"URL {url} payload {j} returned the word 'מערכת'")
                #print(response.text)
            else:
                pass
                # print(f"URL {url} returned status code {response.status_code}")


if __name__ == "__main__":
    start_number = int(input("Enter the start number: "))
    end_number = int(input("Enter the end number: "))

    pl_start = int(input("Enter the start number for the payload: "))
    pl_end = int(input("Enter the end number for the payload: "))

    scan_urls(start_number, end_number, pl_start, pl_end)
