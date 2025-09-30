class Visit:
    def __init__(self, date, treatment, condition, previous_condition=None):
        self.date = date
        self.treatment = treatment
        self.condition = condition
        self.previous_condition = previous_condition if previous_condition else "N/A"


class MedicalRecord:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name
        self.visits = []  # List of Visit objects

    def add_visit(self, date, treatment, condition):
        previous_condition = self.visits[-1].condition if self.visits else "N/A"
        self.visits.append(Visit(date, treatment, condition, previous_condition))

    def current_condition(self):
        if self.visits:
            return self.visits[-1].condition
        return "No visits recorded"


def binary_search(records, target_id):
    low = 0
    high = len(records) - 1

    while low <= high:
        mid = (low + high) // 2
        if records[mid].patient_id == target_id:
            return mid
        elif records[mid].patient_id < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    # Create patient records
    records = [
        MedicalRecord(1001, "Alice"),
        MedicalRecord(1005, "Bob"),
        MedicalRecord(1010, "Charlie"),
        MedicalRecord(1015, "Diana"),
        MedicalRecord(1020, "Ethan"),
    ]

    # Alice - 4 visits
    records[0].add_visit("2025-01-10", "Paracetamol", "Fever Reduced")
    records[0].add_visit("2025-02-15", "Rest + Flu Medicine", "Recovered")
    records[0].add_visit("2025-03-12", "Vitamin Supplements", "Healthy")
    records[0].add_visit("2025-04-01", "Routine Checkup", "Normal")

    # Bob - 3 visits
    records[1].add_visit("2025-01-20", "Insulin Dose Adjusted", "Stable")
    records[1].add_visit("2025-03-05", "Diet Plan Updated", "Improved")
    records[1].add_visit("2025-04-10", "Insulin + Exercise Plan", "Well Controlled")

    # Charlie - 5 visits
    records[2].add_visit("2025-02-01", "Inhaler", "Breathing Improved")
    records[2].add_visit("2025-02-20", "Nebulizer", "Under Observation")
    records[2].add_visit("2025-03-10", "Inhaler + Oxygen", "Better")
    records[2].add_visit("2025-04-01", "Allergy Test", "Mild Allergy Found")
    records[2].add_visit("2025-04-18", "Allergy Medicine", "Stable")

    # Diana - 4 visits
    records[3].add_visit("2025-01-15", "BP Medicine", "High BP Controlled")
    records[3].add_visit("2025-02-25", "Routine Check", "Stable")
    records[3].add_visit("2025-03-20", "Changed BP Dosage", "Improved")
    records[3].add_visit("2025-04-05", "Exercise + Diet", "Normal BP")

    # Ethan - 3 visits
    records[4].add_visit("2025-01-30", "Oxygen Support", "Severe Covid Symptoms")
    records[4].add_visit("2025-02-15", "Antivirals", "Improving")
    records[4].add_visit("2025-03-10", "Lung Recovery Therapy", "Recovered")

    search_id = int(input("Enter Patient ID to search: "))
    index = binary_search(records, search_id)

    if index != -1:
        record = records[index]
        print("\nPatient Found:")
        print("ID:", record.patient_id)
        print("Name:", record.name)
        print("Total Visits:", len(record.visits))
        print("Current Condition:", record.current_condition())
        print("\nVisit History:")

        for i, visit in enumerate(record.visits, 1):
            print(f"\nVisit {i}:")
            print(f"Date: {visit.date}")
            print(f"Treatment: {visit.treatment}")
            print(f"Condition: {visit.condition}")
            print(f"Previous Condition: {visit.previous_condition}")
    else:
        print("Patient record not found.")


if __name__ == "__main__":
    main()
