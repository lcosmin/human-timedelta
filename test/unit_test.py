from htd import parse


def test_parse():
    test_cases = {"10s": 10,
                  "10 s": 10,
                  "4.2 s": 4.2,
                  "0.5h": 30 * 60,      # half an hour, 30 minutes
                  "1.2 hours": (60 + 12) * 60,
                  "10 m": 10 * 60,
                  "30 minutes": 30 * 60,
                  "1d": 24 * 60 * 60,
                  "1.5 days": (24 + 12) * 60 * 60,
                  "1 day": 24 * 60 * 60
                  }

    for test, expected in test_cases.iteritems():
        assert parse(test).total_seconds() == expected
