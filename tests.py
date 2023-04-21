"""Testsq for Balloonicorn's Flask app."""

import unittest
import party


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        """Code to run before every test."""

        self.client = party.app.test_client()
        party.app.config['TESTING'] = True

    def test_homepage(self):
        """Can we reach the homepage?"""

        result = self.client.get("/")
        self.assertIn(b"having a party", result.data)

    def test_no_rsvp_yet(self):
        """Do users who haven't RSVPed see the correct view?"""

        # assertIn(a, b)           a in b
        # assertNotIn(a, b)        a not in b


        # FIXME: Add a test to show we haven't RSVP'd yet
        result = self.client.get("/")
        # test that you see the RSVP form
        self.assertIn(b"RSVP", result.data)
        # test that you don’t see the party details
        self.assertNotIn(b"Party Details", result.data)

    def test_rsvp(self):
        """Do RSVPed users see the correct view?"""

        rsvp_info = {'name': "Jane", 'email': "jane@jane.com"}

        result = self.client.post("/rsvp", data=rsvp_info,
                                  follow_redirects=True)

        # FIXME: check that once we log in we see party details--but not the form!
        # test that you don’t see the RSVP form
        self.assertNotIn(b"RSVP", result.data)

        # test that you do see the party details
        self.assertIn(b"Party Details", result.data)

    def test_rsvp_mel(self):
        """Can we keep Mel out?"""

        # FIXME: write a test that mel can't invite himself
        rsvp_info = {'name': "Mel Melitpolski", 'email': "mel@ubermelon.com"}
        

        result = self.client.post("/rsvp", data=rsvp_info,
                                  follow_redirects=True)
        self.assertIn(b"RSVP", result.data)
        self.assertNotIn(b"Party Details", result.data)


if __name__ == "__main__":
    unittest.main()
