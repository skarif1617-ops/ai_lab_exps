def get_input(question):                   # ask a yes/no question
    response = input(question + " (yes/no): ").strip().lower()   # read, trim, lowercase
    return response == "yes"               # True if yes, else False

def diagnose():
    print("\n--- Medical Diagnosis Expert System ---\n")
    fever = get_input("Do you have fever?")           # collect facts (symptoms)
    cough = get_input("Do you have cough?")
    body_ache = get_input("Do you have body ache?")
    sore_throat = get_input("Do you have sore throat?")
    headache = get_input("Do you have headache?")
    fatigue = get_input("Do you feel fatigued?")
    runny_nose = get_input("Do you have a runny nose?")

    if fever and cough and body_ache:                  # rule 1
        print("\nYou may be suffering from: Flu")
    elif cough and sore_throat and runny_nose:         # rule 2
        print("\nYou may be suffering from: Common Cold")
    elif fever and headache and fatigue:               # rule 3
        print("\nYou may be suffering from: Dengue")
    elif fever and sore_throat and not cough:          # rule 4
        print("\nYou may be suffering from: Tonsillitis")
    else:                                              # no rule matched
        print("\nDiagnosis is unclear. Please consult a doctor.")

if __name__ == "__main__":
    diagnose()