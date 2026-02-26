from services.contact_service import ContactService


def print_menu() -> None:
    print("\n=== Contacts App (CMD) ===")
    print("1) Créer un contact")
    print("2) Lister les contacts")
    print("3) Modifier un contact")
    print("0) Quitter")


def main() -> None:
    service = ContactService()

    while True:
        print_menu()
        choice = input("Choix: ").strip()

        if choice == "1":
            name = input("Nom: ").strip()
            phone = input("Téléphone: ").strip()

            try:
                created = service.add_contact(name, phone)
                print(f"Contact créé: {created['name']} - {created['phone']}")
            except ValueError as e:
                print(f"❌ Erreur: {e}")

        elif choice == "2":
            contacts = service.list_contacts()
            if not contacts:
                print("Aucun contact.")
            else:
                print("\n--- Liste des contacts ---")
                for i, c in enumerate(contacts, start=1):
                    print(f"{i}. {c['name']} - {c['phone']}")

        elif choice == "3":
            contacts = service.list_contacts()
            if not contacts:
                print("Aucun contact à modifier.")
            else:
                print("\n--- Liste des contacts ---")
                for i, c in enumerate(contacts, start=1):
                    print(f"{i}. {c['name']} - {c['phone']}")
                try:
                    idx = int(input("Numéro du contact à modifier: ").strip())
                    name = input("Nouveau nom: ").strip()
                    phone = input("Nouveau téléphone: ").strip()
                    updated = service.update_contact(idx, name, phone)
                    print(f"Contact modifié: {updated['name']} - {updated['phone']}")
                except ValueError as e:
                    print(f"❌ Erreur: {e}")

        elif choice == "0":
            print("Exit Bye !")
            break

        else:
            print("Choix invalide. Réessaie.")


if __name__ == "__main__":
    main()