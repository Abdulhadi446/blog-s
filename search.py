from duckduckgo_search import DDGS

def search_image(query):
    with DDGS() as ddgs:
        results = ddgs.images(
            query,
            region="us-en",
            safesearch="moderate",
            max_results=10,
            size=None,
            color=None,
            type_image=None,
            layout=None,
            license_image=None,
        )
        for img in results:
            print(img["image"], img["url"])
        return results

if __name__ == "__main__":
    search_image("cats")
