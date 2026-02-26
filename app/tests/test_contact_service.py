import unittest
from services.contact_service import ContactService


class TestContactService(unittest.TestCase):
    def setUp(self):
        self.service = ContactService()

    def test_add_contact_success(self):
        c = self.service.add_contact("Alice", "+33 6 12 34 56 78")
        self.assertEqual(c["name"], "Alice")
        self.assertEqual(c["phone"], "+33 6 12 34 56 78")

    def test_add_contact_empty_name_raises(self):
        with self.assertRaises(ValueError):
            self.service.add_contact("", "0612345678")

    def test_add_contact_empty_phone_raises(self):
        with self.assertRaises(ValueError):
            self.service.add_contact("Bob", "")

    def test_add_contact_invalid_phone_raises(self):
        with self.assertRaises(ValueError):
            self.service.add_contact("Bob", "phone???")

    def test_list_contacts(self):
        self.service.add_contact("Alice", "0612345678")
        self.service.add_contact("Bob", "0711223344")
        contacts = self.service.list_contacts()
        self.assertEqual(len(contacts), 2)

    def test_duplicate_contact_raises(self):
        self.service.add_contact("Alice", "0612345678")
        with self.assertRaises(ValueError):
            self.service.add_contact("Alice", "0612345678")

    def test_update_contact_success(self):
        self.service.add_contact("Alice", "0612345678")
        updated = self.service.update_contact(1, "Alice Martin", "0698765432")
        self.assertEqual(updated["name"], "Alice Martin")
        self.assertEqual(updated["phone"], "0698765432")
        self.assertEqual(self.service.list_contacts()[0]["name"], "Alice Martin")

    def test_update_contact_invalid_index_raises(self):
        self.service.add_contact("Alice", "0612345678")
        with self.assertRaises(ValueError):
            self.service.update_contact(0, "X", "0612345678")
        with self.assertRaises(ValueError):
            self.service.update_contact(2, "X", "0612345678")

    def test_update_contact_empty_name_raises(self):
        self.service.add_contact("Alice", "0612345678")
        with self.assertRaises(ValueError):
            self.service.update_contact(1, "", "0698765432")

    def test_update_contact_invalid_phone_raises(self):
        self.service.add_contact("Alice", "0612345678")
        with self.assertRaises(ValueError):
            self.service.update_contact(1, "Alice", "invalid???")


if __name__ == "__main__":
    unittest.main()