import itertools as it
from multiprocessing import Value
import weakref as wr

class medicalrecord:
    def __init__(self):
        self.patient_data = []

    def create_new_record(self, medrecord):
        self.patient_data.append(medrecord)

    def update_medical_record(self, appointments, treatments, tests):
        self.patient_data.append(appointments)
        self.patient_data.append(treatments)
        self.patient_data.append(tests)

class bill:
    def __init__(self):
        self.total_bill = 0.0
        self.payment_method = None
        self.insurance_discount = 0.0

    def payment_methods(self, payment_method):
        self.payment_method = payment_method

    def insurance_coverage(self, insurance_coverage):
        self.insurance_discount = insurance_coverage

    def payment_method_selection(self):
        print("How will you be paying for your medical bill?")
        print("1. Cash")
        print("2. Credit Card")
        print("3. Bank Transfer")
        print("4. Mobile Payment")
        payment_method = input("Select a payment method (1-4): ")
        try:
            if payment_method == "1":
                print(f"You have selected {method1.payment_method}.")
            elif payment_method == "2":
                print(f"You have selected {method2.payment_method}.")
            elif payment_method == "3":
                print(f"You have selected {method3.payment_method}.")
            elif payment_method == "4":
                print(f"You have selected {method4.payment_method}.")
        except ValueError:
            print("Invalid input. Please select a number from 1 to 4.")
        bill.insurance_coverage_selection(self)

    def insurance_coverage_selection(self):
        print("What type of insurance coverage do you have?")
        print("1. No Insurance Coverage")
        print("2. Partial Insurance Coverage")
        print("3. Full Insurance Coverage")
        insurance_coverage = input("Select your insurance coverage (1-3): ")
        try:
            if insurance_coverage == "1":
                print("You have selected No Insurance Coverage.")
                self.insurance_discount = 0.0
                bill.create_total_bill(self)

            elif insurance_coverage == "2":
                print("You have selected Partial Insurance Coverage.")
                self.insurance_discount = 0.50
                bill.create_total_bill(self)

            elif insurance_coverage == "3":
                print("You have selected Full Insurance Coverage.")
                self.insurance_discount = 1.0
                bill.create_total_bill(self)

        except ValueError:
            print("Invalid input. Please select 1, 2, or 3.")

    def add_charge(self, amount):
        self.bills.append(float(amount))

    def create_total_bill(self):
        if hasattr(self, 'treatment_cost'):
            self.total_bill = sum(self.treatment_cost ) * (self.insurance_discount)
            print(f"Patient Name: {patient1.patient_full_name}")
            print(f"Total bill after insurance discount: {self.total_bill} SAR.")

        elif hasattr(self, 'test_cost'):
            self.total_bill = sum(self.test_cost) * (self.insurance_discount)
            print(f"Patient Name: {patient1.patient_full_name}")
            print(f"Total bill after insurance discount: {self.total_bill} SAR.")

        elif hasattr(self, 'medicine_cost'):
            self.total_bill = sum(self.medicine_cost) * (self.insurance_discount)
            print(f"Patient Name: {patient1.patient_full_name}")
            print(f"Total bill after insurance discount: {self.total_bill} SAR.")

    def send_new_medical_record():
        medicalrecord.update_medical_record()

method1 = bill()
method2 = bill()
method3 = bill()
method4 = bill()
insurance1 = bill()
insurance2 = bill()
insurance3 = bill()

method1.payment_methods("Cash")
method2.payment_methods("Credit Card")
method3.payment_methods("Bank Transfer")
method4.payment_methods("Mobile Payment")
insurance1.insurance_coverage("No Insurance Coverage")
insurance2.insurance_coverage("Partial Insurance Coverage")
insurance3.insurance_coverage("Full Insurance Coverage")

class doctor:

    _id_generator = it.count(1000)

    def __init__(self):
        self.doc_id = next(doctor._id_generator)
        self.docdatabase = []
        self.doc_name = None
        self.appointment_no = None
        self.assigned_patient = None

    def add_doctor(self, doc_name):
        self.doc_name = doc_name

    def assign_appointment(self):
        appointment.check_up(self)

doctor1 = doctor()
doctor2 = doctor()
doctor3 = doctor()
doctor1.add_doctor("Dr. Smith")
doctor2.add_doctor("Dr. Johnson")
doctor3.add_doctor("Dr. Kirk")

class hospitalroom:

    _id_generator = it.count(100)

    def __init__(self):
        self.room_no = next(type(self)._id_generator)
        self.room_type = None
        self.doctorClass = None
        self.appointment_no = None

    def create_room(self, room_type, doctorClass):
        self.room_type = room_type
        self.doctorClass = doctorClass

    def assign_appointment_no():
        pass

    def assign_doctor(self):
        pass

room1 = hospitalroom()
room2 = hospitalroom()
room3 = hospitalroom()
room4 = hospitalroom()
room5 = hospitalroom()

room1.create_room("Doctor's Office", doctor1)
room2.create_room("Doctor's Office", doctor2)
room3.create_room("Doctor's Office", doctor3)
room4.create_room("Surgery Room", doctor1)
room5.create_room("Lab Test Room", doctor2)

class medicine:

    _id_generator = it.count(1000)

    def __init__(self):
        self.medicine_id = next(self._id_generator)
        self.medicine_name = []
        self.cost_per_unit = []
        self.stock = 100

    def add_medicine_stock(self, medicine_name, cost_per_unit):
        self.medicine_name.append(medicine_name)
        self.cost_per_unit.append(cost_per_unit)
        self.stock += 50

    def check_medicine_stock(self):
        for i in range(len(self.medicine_name)):
            print(f"Medicine: {self.medicine_name[i]}, Cost: {self.cost_per_unit[i]}, Stock: {self.stock}")

    def prescribe_deduct_medicine_stock(self, quantity):
        if self.stock < quantity:
            print("Not enough stock.")
            return False

        self.stock -= quantity
        return True

med1 = medicine()
med2 = medicine()
med3 = medicine()
med4 = medicine()
med5 = medicine()

med1.add_medicine_stock("Penicillin", 10)
med2.add_medicine_stock("Erythromycin", 15)
med3.add_medicine_stock("Paracetamol", 15)
med4.add_medicine_stock("Antiviral Drugs", 15)
med5.add_medicine_stock("Vaccination Vials", 100)

class treatment:
    def __init__(self):
        self.assigned_doc = None
        self.assigned_patient = None
        self.room_no = None
        self.treatment_type = []
        self.treatment_cost = []

    def add_treatment_type(self, treat_type, treat_cost):
        self.treatment_type.append(treat_type)
        self.treatment_cost.append(treat_cost)

    def give_patient_treatment(self):
        print(f"You have received a {self.treatment_type}.")
        print(f"Treatment cost: {self.treatment_cost} SAR.")
        bill.payment_method_selection(self)

    def take_medicinal_treatment():
        print("The doctor has prescribed a treatment for you.")
        print("1. Vaccination")
        print("2. Disinfection")
        print("3. Surgery")
        treatment_selection = input("Please select a treatment option: ").upper()
        try:
            if treatment_selection == "1":
                print("You have selected Vaccination.")
                treatment1.give_patient_treatment()
            elif treatment_selection == "2":
                print("You have selected Disinfection.")
                treatment2.give_patient_treatment()
            elif treatment_selection == "3":
                print("You have selected Surgery.")
                treatment3.give_patient_treatment()
        except ValueError:
            print("Invalid input.")

treatment1 = treatment()
treatment2 = treatment()
treatment3 = treatment()

treatment1.add_treatment_type("Vaccination", 100)
treatment2.add_treatment_type("Disinfection", 100)
treatment3.add_treatment_type("Surgery", 5000)

class prescription:
    def __init__(self):
        self.medicine_name = None
        self.total_medicine_cost = None

    def medicine_prescription(self):
        print("You have been prescribed medicine by your doctor.")
        medicines_available = {"A": med1, "B": med2, "C": med3, "D": med4}
        print("A. Penicillin (10)")
        print("B. Erythromycin (15)")
        print("C. Paracetamol (15)")
        print("D. Antiviral Drugs (15)")
        prescription_selection = input("Selection: ")
        selection = medicines_available.get(prescription_selection)
        if selection is not None:
            print(f"You have been prescribed {selection.medicine_name}.")
            print(f"Total cost: {selection.cost_per_unit} SAR.")
            bill.create_total_bill(self)

        if selection.prescribe_deduct_medicine_stock(7):
            print(f"Prescribed {selection.medicine_name[0]}.")
            print(f"Remaining stock: {selection.stock}")
            bill.create_total_bill(self)

class labtest:
    def __init__(self):
        self.test_type = None
        self.test_cost = None

    def lab_test_selection(self):
        print("Lab Test Options:")
        print("1. Blood Test")
        print("2. Stool Test")
        print("3. Urine Test")
        test_selection = input("Select a lab test (1-3): ")

        try:
            test_selection = int(test_selection)
            if test_selection == 1:
                test1.blood_test()
            elif test_selection == 2:
                test2.stool_test()
            elif test_selection == 3:
                test3.urine_test()
        except ValueError:
            print("Invalid input. Please enter a number (1-3).")

    def test_types(self, testtype, testcost):
        self.test_type = testtype
        self.test_cost = testcost

    def blood_test(self):
        print(f"You have received a {test1.test_type}.")
        print(f"Total cost: {test1.test_cost} SAR.")
        bill.create_total_bill(self)

    def stool_test(self):
        print(f"You have received a {test2.test_type}.")
        print(f"Total cost: {test2.test_cost} SAR.")
        bill.create_total_bill(self)

    def urine_test(self):
        print(f"You have received a {test3.test_type}.")
        print(f"Total cost: {test3.test_cost} SAR.")
        bill.create_total_bill(self)


test1 = labtest()
test2 = labtest()
test3 = labtest()

test1.test_types("Stool Test", 500)
test2.test_types("Urine Test", 500)
test3.test_types("Blood Test", 1000)

class appointment:

    _appointment_no_generator = it.count (100)

    def __init__(self):
        self.appointment_no = next(type(self)._appointment_no_generator)
        self.appointments = []

    def create_appointment(self, new_patient):
        new_appointment = ({"patient_full_name" : new_patient.patient_full_name, "doc_name": doctor1.doc_name, "room_no": room1.room_no, "appointment_no": self.appointment_no})
        print(f"Appointment created for {new_patient.patient_full_name} with {doctor1.doc_name} at room number {room1.room_no}.")
        print(f"Your appointment number is {new_appointment['appointment_no']}")
        doctor.assign_appointment(self)

    def check_up(self):
        print("The Doctor has made the decision to...")
        print("A. Bring you in for treatment")
        print("B. Prescribe medicine for you")
        print("C. Bring you in for a lab test.")
        doctors_input = input("Please select an option (A/B/C): ").upper()
        try:
            if doctors_input == "A":
                treatment.take_medicinal_treatment()
            elif doctors_input == "B":
                prescription.medicine_prescription(self)
            elif doctors_input == "C":
                labtest.lab_test_selection(self)
        except ValueError:
            print("Invalid input. Please enter A, B, or C.")

    def bring_up_patient_records():
        print()


class patient:

    _patient_no_generator = it.count(10000)

    def __init__(self, patient_full_name):
        self.patient_no = next(type(self)._patient_no_generator)
        self.patient_full_name = patient_full_name
        self.patient_data = medicalrecord()
        self.appointment_no = None
        self.assigned_doc = None
        self.wallet = 15000

    def save_account_record(self):
        self.patient_data.create_new_record({"fullname": self.patient_full_name, "patientno": self.patient_no})

    def create_account(self):
        print("Account Creation for Patients")
        patient_input_name = input("Enter Full Name: ").strip()
        new_patient = patient(patient_input_name)
        new_patient.save_account_record()
        input_create_appointment = input("Create appointment? (Yes/No) ").upper()
        try:
            if input_create_appointment == "YES":
                patient.create_patient_appointment(self, new_patient)
            elif input_create_appointment == "NO":
                pass
        except ValueError:
            print("Invalid input. Please enter Yes or No.")
        
    def create_patient_appointment(self, new_patient):
        print(f"Patient:  {new_patient.patient_full_name}")
        print(f"Patient Number: {new_patient.patient_no}")
        new_appointment = appointment()
        new_appointment.create_appointment(new_patient)
        self.appointment_no = new_appointment.appointment_no


patient_full_name = medicalrecord()
patient1 = patient(patient_full_name)
patient1.create_account()