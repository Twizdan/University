from github import Github

# Заменить на свой токен доступа GitHub
ACCESS_TOKEN = "your_github_access_token"

# Заменить на имя владельца репозитория и его название
REPO_OWNER = "Twizdan"
REPO_NAME = "Machine-Learning"

def test_readme_exists():
    # Создать объект PyGitHub с помощью вашего токена доступа
    g = Github(ACCESS_TOKEN)

    # Получить репозиторий
    repo = g.get_user(REPO_OWNER).get_repo(REPO_NAME)

    # Проверить наличие файла README.md
    readme_file = repo.get_contents("README.md")
    assert readme_file is not None, "README.md file not found"