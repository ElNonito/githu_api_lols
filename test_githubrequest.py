from GithubRequest import GithubRequest
from Response import Response

events = GithubRequest.get_events()

def test_events_is_our_response_class():
    assert isinstance(events, Response)

