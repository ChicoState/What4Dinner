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
    url = generateURL(query, num_of_ingredients, diet_type,
                      health_type, meal_type, calories, time)
    try:
        res = requests.get(url)
    except:
        print("ping_api: Unable to get recipe data")
    return res


def generateURL(query, num_of_ingredients, diet_type, health_type, meal_type, calories, time):
    # Builds the query URL based on filters specified by the user.
    # The only required form field that the user MUST fill out is the "Recipe name" field
    api_key = config("RECIPE_SEARCH_API_KEY")
    app_id = config("RECPIE_APPLICATION_ID")
    domain = "https://api.edamam.com/api/recipes/v2?type=public"
    query_string = f"&q={query}&app_id={app_id}&app_key={api_key}"
    if (num_of_ingredients != ""):
        query_string = query_string + "&ingr={num_of_ingredients}"
    if (diet_type != ""):
        query_string = query_string + "&diet={diet_type}"
    if (health_type != ""):
        query_string = query_string + "&health={health_type}"
    if (meal_type != ""):
        query_string = query_string + "&mealType={meal_type}"
    if (calories != ""):
        query_string = query_string + "&calories={calories}"
    if (time != None):
        query_string = query_string + "&time={time}"

    encoded_query_string = format_url(query_string)
    url = domain + encoded_query_string
    return url


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
        tmp["instructionLink"] = item["recipe"]["url"]
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
