import sys
import requests
from typing import Dict, List


def get_user_input() -> Dict[str, str]:
    """
    Get user input for the base URL and the list of endpoints.

    :return: A dictionary containing the base URL and the list of endpoints.
    """
    base_url = input("Enter the base URL: ")
    endpoints = input("Enter the endpoints (comma-separated): ").split(',')
    return {"base_url": base_url, "endpoints": endpoints}


def make_requests(base_url: str, endpoints: List[str]) -> List[Dict[str, str]]:
    """
    Make HTTP GET requests to the specified endpoints and return the results.

    :param base_url: The base URL for the requests.
    :param endpoints: The list of endpoints to make requests to.
    :return: A list of dictionaries containing the results of the requests.
    """
    results = []
    for endpoint in endpoints:
        url = f"{base_url}/{endpoint}"
        response = requests.get(url)
        if response.status_code == 200:
            results.append({"endpoint": endpoint, "data": response.json()})
        else:
            results.append({"endpoint": endpoint, "error": response.status_code})
    return results


def display_results(results: List[Dict[str, str]]) -> None:
    """
    Display the results of the HTTP GET requests.

    :param results: A list of dictionaries containing the results of the requests.
    """
    for result in results:
        if "data" in result:
            print(f"Endpoint: {result['endpoint']}")
            print(f"Data: {result['data']}")
        else:
            print(f"Endpoint: {result['endpoint']}")
            print(f"Error: {result['error']}")


def main() -> None:
    """
    The main function of the program.
    """
    user_input = get_user_input()
    results = make_requests(user_input["base_url"], user_input["endpoints"])
    display_results(results)


if __name__ == "__main__":
    main()
