import random

class SecretSanta:
    def __init__(self, employees, previous_assignments):
        self.employees = employees
        self.previous_assignments = previous_assignments

    def assign(self):
        assignments = []
        available_recipients = self.employees[:]

        for giver in self.employees:
            valid_recipients = [
                recipient for recipient in available_recipients
                if recipient.email != giver.email
                and recipient.email != self.previous_assignments.get(giver.email)
            ]

            if not valid_recipients:
                raise ValueError("Constraints cannot be satisfied.")

            recipient = random.choice(valid_recipients)
            assignments.append((giver, recipient))
            available_recipients.remove(recipient)

        return assignments
