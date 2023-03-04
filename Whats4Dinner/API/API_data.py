import json

import requests
from decouple import config


def format_url(url):
    encoded_url = ""
    for letter in url:
        if letter == " ":
            encoded_url += "%20"
        else:
            encoded_url += letter
    return encoded_url


def get_api_data(query, num_of_ingredients, diet_type, health_type, meal_type, calories, time):
    api_key = config("RECIPE_SEARCH_API_KEY")
    app_id = config("RECPIE_APPLICATION_ID")
    domain = "https://api.edamam.com/api/recipes/v2?type=public"
    query_string = f"&q={query}&app_id={app_id}&app_key={api_key}&ingr={num_of_ingredients}&diet={diet_type}&health={health_type}&mealType={meal_type}&calories={calories}&time={time}"

    encoded_query_string = format_url(query_string)
    url = domain + encoded_query_string
    try:
        res = requests.get(url)
    except:
        print("ping_api: Unable to get recipe data")
    return res


def parse_api_data(data):
    parsed_data = []
    for item in data["hits"]:
        tmp = {}

        # construct each recipe item
        tmp["label"] = item["recipe"]["label"]
        tmp["dietLabels"] = item["recipe"]["dietLabels"]
        tmp["healthLabels"] = item["recipe"]["healthLabels"]
        tmp["cautions"] = item["recipe"]["cautions"]
        tmp["ingredients"] = item["recipe"]["ingredientLines"]
        tmp["mealType"] = item["recipe"]["mealType"]
        tmp["dishType"] = item["recipe"]["dishType"]
        parsed_data.append(tmp)
    print(parsed_data)
    return parsed_data


def main():
    query = "chicken"
    num_of_ingrediants = "4"
    diet_type = "high-protein"
    health_type = "mustard-free"
    meal_type = "Dinner"
    calories = "1200-1600"
    time = "20"
    result = get_api_data(query, num_of_ingrediants,
                          diet_type, health_type, meal_type, calories, time)
    print(result)


if __name__ == '__main__':
    main()
