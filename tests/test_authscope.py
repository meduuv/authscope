from authscope import repeated_failures, summarize

def test_summary_and_failures():
    events = [{"principal": "alice", "status": "failure"}, {"principal": "alice", "status": "failure"}, {"principal": "alice", "status": "failure"}, {"principal": "alice", "status": "success"}]
    assert summarize(events)["failure"] == 3
    assert repeated_failures(events) == {"alice": 3}
