"""
Entry point for Semantic Search Application
"""

from src.semantic_search import search
from src.logger import logger


def main():
    """
    Main application loop
    """

    logger.info("Application Started")

    print("=" * 60)
    print("LLM Internal Lab - Semantic Search")
    print("=" * 60)

    try:
        query = input("\nAsk a question: ").strip()

        if not query:
            print("Query cannot be empty.")
            logger.warning("User submitted empty query")
            return

        logger.info(f"User Query: {query}")

        results = search(query)

        print("\nTop Matches")
        print("-" * 60)

        for rank, (document, score) in enumerate(results, start=1):

            print(
                f"{rank}. Score: {score:.4f}"
            )
            print(
                f"   Document: {document}"
            )
            print()
            logger.info(f"{rank}. Score: {score:.4f}")
            logger.info(  f"   Document: {document}")

        logger.info("Search completed successfully")

    except KeyboardInterrupt:
        print("\nApplication stopped by user.")
        logger.warning("Application interrupted by user")

    except Exception as e:
        print(f"\nError: {e}")
        logger.error(
            f"Unexpected Error: {str(e)}",
            exc_info=True
        )

    finally:
        logger.info("Application Closed")


if __name__ == "__main__":
    main()