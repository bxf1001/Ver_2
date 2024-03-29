import sys
import json
import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QGridLayout, QMessageBox
from qt_material import apply_stylesheet
import Whatsappcall
# Read the user data from the JSON file
with open('user_data.json', 'r') as f:
    user_data = json.load(f)

# A custom widget class that inherits from QWidget
class UserDataWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a label for user id
        self.user_id_label = QLabel("User ID:", self)

        # Create a line edit for user id input
        self.user_id_edit = QLineEdit(self)

        # Create a button for user id search
        self.user_id_button = QPushButton("Search", self)
        self.user_id_button.clicked.connect(self.search_user)

        # Create a combo box for selecting a key
        self.key_combo = QComboBox(self)
        self.key_combo.addItems(["1", "2", "3"])
        self.key_combo.currentTextChanged.connect(self.print_value)

        self.key_combo_1 = QComboBox(self)
        self.key_combo_1.addItems(["1", "2", "3"])
        self.key_combo_1.currentTextChanged.connect(self.print_value_1)

        self.combo_box_timer1 = QComboBox(self)
        self.combo_box_timer2 = QComboBox(self)

        for i in range(1, 13):
            self.combo_box_timer1.addItem(str(i))

        # Connect combo box 1 signal to update combo box 2
        self.combo_box_timer1.currentIndexChanged.connect(self.update_combo_box2)


        # Create a label for displaying the value
        self.value_label = QLabel("Number 1:", self)
        self.value_label_1 = QLabel("Number 2:", self)

        # Create a label to display the selected minutes
        self.selected_minutes_label = QLabel(self)

        # Create a button for making a WhatsApp call
        self.call_button = QPushButton("Call", self)
        self.call_button.clicked.connect(self.make_call)

        # Create a grid layout and add the widgets
        self.grid = QGridLayout(self)
        self.grid.addWidget(self.user_id_label, 0, 0)
        self.grid.addWidget(self.user_id_edit, 0, 1)
        self.grid.addWidget(self.user_id_button, 0, 3)
        self.grid.addWidget(self.key_combo, 1, 0)
        self.grid.addWidget(self.key_combo_1, 2, 0)                    
        self.grid.addWidget(self.value_label, 1, 1)
        self.grid.addWidget(self.value_label_1, 2, 1)
        self.grid.addWidget(self.call_button, 1, 3)
        self.grid.addWidget(self.combo_box_timer1,1,2)
        self.grid.addWidget(self.combo_box_timer2,2,2)
        self.grid.addWidget(self.selected_minutes_label,3,2)

        # Set the window title and size
        self.setWindowTitle("User Data")
        self.resize(500, 200)

    def search_user(self):
        # Get the user id from the line edit
        user_id = self.user_id_edit.text()

        # Check if the user id is in the user data dictionary
        if user_id in user_data:
            # Get the values for the user id
            values = user_data[user_id]

            # Set the current index of the combo box to 0
            self.key_combo.setCurrentIndex(0)
            self.key_combo_1.setCurrentIndex(1)

            # Set the value label to the first value
            self.value_label.setText(f"Value: {values['1']}")

            self.value_label_1.setText(f"Value: {values['2']}")

            # Enable the call button
            self.call_button.setEnabled(True)
        else:
            # Clear the value label
            self.value_label.setText("Value:")

            # Disable the call button
            self.call_button.setEnabled(False)

            # Show a message box with an error message
            QMessageBox.critical(self, "Error", "User ID not found")

    def update_combo_box2(self):
        selected_value = int(self.combo_box_timer1.currentText())
        remaining_values = [int(i) for i in range(1, 13) if i <= 12 - selected_value]
        self.combo_box_timer2.clear()
        self.combo_box_timer2.addItems(remaining_values)
        self.selected_minutes_label.setText(f"Selected minutes: {selected_value}")


    def print_value(self):
        # Get the user id from the line edit
        user_id = self.user_id_edit.text()

        # Check if the user id is in the user data dictionary
        if user_id in user_data:
            # Get the values for the user id
            values = user_data[user_id]

            # Get the current key from the combo box
            key = self.key_combo.currentText()
            

            # Set the value label to the corresponding value
            self.value_label.setText(f"Value: {values[key]}")
            

    def print_value_1(self):
        # Get the user id from the line edit
        user_id = self.user_id_edit.text()

        # Check if the user id is in the user data dictionary
        if user_id in user_data:
            # Get the values for the user id
            values_1 = user_data[user_id]

            # Get the current key from the combo box
            
            key_1 = self.key_combo_1.currentText()

            # Set the value label to the corresponding value
            
            self.value_label_1.setText(f"Value: {values_1[key_1]}")
    def make_call(self):
        # Get the user id from the line edit
        user_id = self.user_id_edit.text()

        # Get the values for the user id
        values = user_data[user_id]

        # Get the current key from the combo box
        key = self.key_combo.currentText()
        key_1 = self.key_combo_1.currentText()

        add_time= self.combo_box_timer1
        add_time_1=self.combo_box_timer2

        # Get the current value
        value = values[key]
        value_1 = values[key_1]


        if key and add_time :
        # Get the current time
            add_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        # Make a WhatsApp call to the value
            Whatsappcall.phone_number(value)
            Whatsappcall.timer(add_time)


        # Print the value and the time to the console
            print(f"{value} (Called at {add_time})")

        # Create a new dictionary to store timestamped data
            timestamped_data = {
                "user_id": user_id,
                "key": key,
                "number": value,
                "timestamp": add_time
            }

        # Write the timestamped data to a new file
            with open('timestamped_data.json', 'a') as f:
                json.dump(timestamped_data, f)
                f.write('\n')  # Add a newline for readability

        if key_1 and add_time_1:
        # Get the current time
            add_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        # Make a WhatsApp call to the value
            Whatsappcall.phone_number(value_1)
            Whatsappcall.timer(add_time_1)


        # Print the value and the time to the console
            print(f"{value} (Called at {add_time})")

        # Create a new dictionary to store timestamped data
            timestamped_data = {
                "user_id": user_id,
                "key": key,
                "number": value,
                "timestamp": add_time
            }

        # Write the timestamped data to a new file
            with open('timestamped_data.json', 'a') as f:
                json.dump(timestamped_data, f)
                f.write('\n')  # Add a newline for readability



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = UserDataWidget()
    widget.show()

    # apply dark blue theme with round style
    apply_stylesheet(app, theme='dark_blue.xml', extra={'round': True})

    sys.exit(app.exec_())
