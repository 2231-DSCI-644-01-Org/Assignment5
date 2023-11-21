from model import Repo, Issue, Comment
from data_collection.scraper import GithubScraper

class Parser:
    def __init__(self):
        self.scraper = GithubScraper()

    def get_data(self, query_path, params, token):
        """
        Get data from the GitHub API using the scraper.

        Args:
            query_path (str): Path to the GraphQL query file.
            params (dict): Parameters for the request.
            token (str): GitHub API token.

        Returns:
            dict: JSON response from the API.
        """
        return self.scraper.get_data(query_path, params, token)

    def parse_data(self, data):
        # TODO: Implement the data parsing logic here
        # Hint: Start with parsing comments first, then move on to issues
        pass

    def parse_comments(self, data):
        # TODO: Implement the comment parsing logic here
        pass

    def parse_issue_node(self, issue_node):
        # TODO: Implement the issue parsing logic here
        pass

    def parse_issues(self, data):
        # TODO: Implement the issues parsing logic here
        pass
