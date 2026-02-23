from dataclasses import dataclass


@dataclass(frozen=True) #décorateur pour rendre la classe immuable et générer automatiquement __init__, __repr__, etc.
class Contact:
    name: str
    phone: str

    def to_dict(self) -> dict:
        # Stockage demandé : list[dict]
        return {"name": self.name, "phone": self.phone}
    

# sans dataclass, on aurait :
# class Contact:
#     def __init__(self, name: str, phone: str):
#         self.name = name
#         self.phone = phone

# avec le décorateur dataclass, on a automatiquement :
# from dataclasses import dataclass

# @dataclass
# class Contact:
#     name: str
#     phone: str