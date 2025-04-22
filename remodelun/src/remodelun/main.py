import warnings
from datetime import datetime
from crew import MUNCrew
from dotenv import load_dotenv

load_dotenv()
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    topic = input("Entrez le sujet du débat MUN : ")
    country = input("Entrez le pays représenté : ")
    inputs = {
        'topic': topic,
        'country': country,
        'current_year': datetime.now().year
    }

    try:
        MUNCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        print(f"Erreur durant l'exécution : {e}")

if __name__ == "__main__":
    run()
