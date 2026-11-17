
patients = []


def add_patient(patient_id, name, priority):
    if priority not in [1, 2, 3]:
        print("Invalid priority!")
        return

    patient = [patient_id, name, priority]
    patients.append(patient)

    print("Patient added successfully!")



def display_next():
    if len(patients) == 0:
        print("No patients waiting.")
    else:
        highest = 0

        for i in range(1, len(patients)):
            if patients[i][2] < patients[highest][2]:
                highest = i

        print("\nNext Patient to be Treated:")
        print("Patient ID:", patients[highest][0])
        print("Patient Name:", patients[highest][1])
        print("Priority:", patients[highest][2])



def dequeue():
    if len(patients) == 0:
        print("No patients to remove.")
    else:
        highest = 0

        for i in range(1, len(patients)):
            if patients[i][2] < patients[highest][2]:
                highest = i

        treated = patients.pop(highest)

        print("\nPatient treated and removed:")
        print("Patient ID:", treated[0])
        print("Patient Name:", treated[1])


# Function to display all patients in priority order
def display_all():
    if len(patients) == 0:
        print("No patients waiting.")
    else:
        temp = patients.copy()

        temp.sort(key=lambda x: x[2])

        print("\nAll Waiting Patients:")

        for p in temp:
            print("Patient ID:", p[0],
                  "| Name:", p[1],
                  "| Priority:", p[2])


# Main Program
add_patient(101, "Amit", 2)
add_patient(102, "Priya", 1)
add_patient(103, "Rahul", 3)
add_patient(104, "Sneha", 1)

display_all()

display_next()

dequeue()

display_all()
