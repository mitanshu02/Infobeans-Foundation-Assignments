from config import APPLICATIONS, WEBSITES
from app_actions import open_application, open_website,open_installed_app,search_web
from help_commands import show_commands, get_commands_text
from screenshot_actions import take_screenshot
from system_actions import increase_brightness,decrease_brightness,show_desktop,switch_window,open_settings,increase_volume,decrease_volume,toggle_mute,open_file_explorer,close_tab, close_application
from api import search_repositories,get_repository,get_latest_release,get_issues,get_user,search_articles,get_news,search_questions

def process_command(command):
    command = command.lower().strip()

    if command == "search a question":
        query = input("Enter your question: ").strip()

        questions = search_questions(query)

        print()
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                    STACK OVERFLOW                            ║")
        print("╚══════════════════════════════════════════════════════════════╝")

        for i, question in enumerate(questions, 1):
            print(f"{i}. {question['title']}")
            print(f"Score: {question['score']}")
            print(f"Answers: {question['answer_count']}")
            print(f"URL: {question['link']}")
            print()

        print()
        print("================================================================")

        input("\nPress Enter to continue...")
        return f"Found {len(questions)} questions."

    if command in ("show latest tech news","show news","tech news"):
        news = get_news()
        print()
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                    LATEST TECH NEWS                          ║")
        print("╚══════════════════════════════════════════════════════════════╝")

        for i, article in enumerate(news, 1):
            print(f"\n  {i}. {article['title']}")
            print(f"     Source: {article['source']['name']}")
            print(f"     {article['description']}")
            print(f"     URL: {article['url']}")
            print("--------------------------------------------------------------")
        print()
        print("================================================================")
        input("\nPress Enter to continue...")

        return f"Found {len(news)} tech news articles."

    if command == "find a repository":
        query = input("Enter repository to search: ").strip()
        results = search_repositories(query)

        for i, repo in enumerate(results, 1):
            print(f"\n{i}. {repo['full_name']}")
            print(f"Description: {repo['description']}")
            print(f"Stars: {repo['stargazers_count']}")
            print(f"URL: {repo['html_url']}")

        input("\nPress Enter to continue...")
        return f"Found {len(results)} repositories."


    if command == "show a repository":
        name = input("Enter repository (owner/repository): ").strip()

        if "/" not in name:
            return "Please enter repository as owner/repository."
        
        owner, repo = name.split("/", 1)
        data = get_repository(owner, repo)

        print(f"\nName: {data['full_name']}")
        print(f"Description: {data['description']}")
        print(f"Stars: {data['stargazers_count']}")
        print(f"Forks: {data['forks_count']}")
        print(f"Language: {data['language']}")
        print(f"Open Issues: {data['open_issues_count']}")
        print(f"URL: {data['html_url']}")

        input("\nPress Enter to continue...")
        return f"Showing information for {data['full_name']}."


    if command == "show latest release":
        name = input("Enter repository (owner/repository): ").strip()
        
        if "/" not in name:
            return "Please enter repository as owner/repository."
        owner, repo = name.split("/", 1)
        data = get_latest_release(owner, repo)

        print(f"\nRelease: {data['name']}")
        print(f"Tag: {data['tag_name']}")
        print(f"Published: {data['published_at']}")
        print(f"URL: {data['html_url']}")

        input("\nPress Enter to continue...")
        return f"Latest release of {owner} {repo} is {data['tag_name']}."


    if command == "show repository issues":
        name = input("Enter repository (owner/repository): ").strip()

        owner, repo = name.split("/", 1)
        if "/" not in name:
            return "Please enter repository as owner/repository."
        issues = get_issues(owner, repo)

        for i, issue in enumerate(issues, 1):
            print(f"\n{i}. {issue['title']}")
            print(f"Number: {issue['number']}")
            print(f"URL: {issue['html_url']}")

        input("\nPress Enter to continue...")
        return f"Found {len(issues)} open issues."


    if command == "show github user":
        username = input("Enter GitHub username: ").strip()
        data = get_user(username)

        print(f"\nUsername: {data['login']}")
        print(f"Name: {data['name']}")
        print(f"Bio: {data['bio']}")
        print(f"Repositories: {data['public_repos']}")
        print(f"Followers: {data['followers']}")
        print(f"Following: {data['following']}")
        print(f"Profile: {data['html_url']}")

        input("\nPress Enter to continue...")
        return f"Showing GitHub profile of {data['login']}."

    if command == "search a technical article":
        query = input("Enter topic: ").strip()
        results = search_articles(query)

        print()
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                    TECHNICAL ARTICLES                        ║")
        print("╚══════════════════════════════════════════════════════════════╝")

        for i, article in enumerate(results, 1):
            print()
            print(f"{i}. {article['title']}")
            print(f"{article['description']}")
            print(f"URL: {article['url']}")

        print()
        print("================================================================")
        input("\nPress Enter to continue...")
        return f"Found {len(results)} articles."

    if command == "help":
        show_commands()
        return get_commands_text()

    if command == "take screenshot":
        path = take_screenshot()
        print(f"Screenshot saved at: {path}")
        return f"Screenshot saved at: {path}"
    
    if command == "increase brightness":
        increase_brightness()
        return "Brightness increased."


    if command == "decrease brightness":
        decrease_brightness()
        return "Brightness decreased."

    if command == "show desktop":
        show_desktop()
        return "Desktop displayed."

    if command == "switch window":
        switch_window()
        return "Switched window."

    if command == "open settings":
        open_settings()
        return "Opening settings."

    if command == "increase volume":
        increase_volume()
        return "Volume increased."

    if command == "decrease volume":
        decrease_volume()
        return "Volume decreased."

    if command in ("toggle mute", "mute pc"):
        toggle_mute()
        return "Mute toggled."

    if command == "open notion":
        open_installed_app("Notion")
        return "Opening Notion."


    if command == "open telegram":
        open_installed_app("Telegram")
        return "Opening Telegram."

    if command in ("open file explorer", "open explorer"):
        open_file_explorer()
        return "Opening file explorer."

    if command == "open whatsapp":
        open_installed_app("WhatsApp")
        return "Opening WhatsApp."

    if command == "open chrome":
        open_installed_app("Google Chrome")
        return "Opening Chrome."
    
    if command == "open edge":
        open_installed_app("Microsoft Edge")
        return "Opening Microsoft Edge."


    if command == "open brave":
        open_installed_app("Brave")
        return "Opening Brave."

    if command == "open powershell":
        open_installed_app("PowerShell")
        return "Opening PowerShell."

    if command in ("close tab", "close current tab"):
        close_tab()
        return "Current tab closed."


    if command in ("close application", "close app"):
        close_application()
        return "Application closed."


    if command == "open photos":
        open_installed_app("Photos")
        return "Opening Photos."

    if command.startswith("search "):
        query = command[7:].strip()

        if not query:
            return False

        search_web(query)
        return f"Searching for {query}"
    
    if command.startswith("open "):
        target = command[5:]

        if target in WEBSITES:
            return open_website(target)

        if target in APPLICATIONS:
            return open_application(target)

        return False

    return False