from __future__ import annotations

from typing import List, Dict
from models.contact import Contact


class ContactService:
    """
    Service métier: gère la logique (ajout, liste).
    Stockage en mémoire sous forme list[dict] comme demandé.
    """

    def __init__(self) -> None:
        self._contacts: List[Dict[str, str]] = []

    def add_contact(self, name: str, phone: str) -> dict:
        name = (name or "").strip()
        phone = (phone or "").strip()

        if not name:
            raise ValueError("Le nom est obligatoire.")
        if not phone:
            raise ValueError("Le numéro de téléphone est obligatoire.")
        if not self._is_valid_phone(phone):
            raise ValueError("Numéro invalide (utilise chiffres, espaces, +, -, parenthèses).")

        # Exemple de règle simple: éviter doublons exacts (name+phone)
        for c in self._contacts:
            if c["name"].lower() == name.lower() and c["phone"] == phone:
                raise ValueError("Ce contact existe déjà.")

        contact = Contact(name=name, phone=phone)
        data = contact.to_dict()
        self._contacts.append(data)
        return data

    def list_contacts(self) -> List[dict]:
        # On retourne une copie pour éviter modifications externes
        return list(self._contacts)

    def update_contact(self, index: int, name: str, phone: str) -> dict:
        """Modifie un contact par son numéro dans la liste (index 1-based)."""
        name = (name or "").strip()
        phone = (phone or "").strip()

        if not name:
            raise ValueError("Le nom est obligatoire.")
        if not phone:
            raise ValueError("Le numéro de téléphone est obligatoire.")
        if not self._is_valid_phone(phone):
            raise ValueError("Numéro invalide (utilise chiffres, espaces, +, -, parenthèses).")

        if index < 1 or index > len(self._contacts):
            raise ValueError("Numéro de contact invalide.")

        i = index - 1
        for j, c in enumerate(self._contacts):
            if j != i and c["name"].lower() == name.lower() and c["phone"] == phone:
                raise ValueError("Un autre contact avec ce nom et numéro existe déjà.")

        self._contacts[i] = {"name": name, "phone": phone}
        return self._contacts[i]

    @staticmethod
    def _is_valid_phone(phone: str) -> bool:
        allowed = set("0123456789 +()-")
        return all(ch in allowed for ch in phone) and any(ch.isdigit() for ch in phone)