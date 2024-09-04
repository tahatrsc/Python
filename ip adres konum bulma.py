import requests


def get_ip_location(ip):
    try:
        response = requests.get(f"http://ipinfo.io/{ip}/json")
        data = response.json()

        if response.status_code == 200:
            return {
                "IP": ip,
                "City": data.get("city"),
                "Region": data.get("region"),
                "Country": data.get("country"),
                "Location": data.get("loc"),
                "Org": data.get("org")
            }
        else:
            return {"Error": "Unable to fetch data"}

    except Exception as e:
        return {"Error": str(e)}


if __name__ == "__main__":
    ip_address = input("Please enter an IP address: ")
    location_info = get_ip_location(ip_address)
    print(location_info)
