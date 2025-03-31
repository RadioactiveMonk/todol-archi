from dataclasses import dataclass
from urllib.parse import urlparse


@dataclass
class Bookmark:
    title: str
    url: str

    @property
    def domain(self) -> str:
        """Retourne le domaine (ex: openai.com) extrait de l'url"""
        parsed = urlparse(self.url)
        return parsed.netloc.removeprefix("www.")

    @property
    def is_secure(self) -> bool:
        """Indique si l'url utilise HTTPS"""
        return self.url.startswith("https://")


# -- zone de test minimaliste


def main():
    fav = Bookmark(title="ChatGpt", url="https://chat.openai.com")
    print(f"📌 {fav.title}")
    print(f"🔗 Domaine : {fav.domain}")
    print(f"🔒 Connexion sécurisée : {fav.is_secure}")


if __name__ == "__main__":
    main()
