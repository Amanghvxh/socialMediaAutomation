def set_env_values(username, password):
    with open('.env', 'r') as file:
        content = file.read()

    content = content.replace('USERNAME=--USERNAME--', f'USERNAME={username}')
    content = content.replace('PASSWORD=--PASSWORD--', f'PASSWORD={password}')

    with open('.env', 'w') as file:
        file.write(content)

if __name__ == "__main__":
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    set_env_values(username, password)
    print("Values set successfully!")
