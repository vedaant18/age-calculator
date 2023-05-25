from PyQt6.QtWidgets import QApplication, QVBoxLayout,QLabel,QWidget,QLineEdit,QGridLayout,QPushButton
import sys
from datetime import *
class Agecalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management system")
        grid=QGridLayout()

        #widget 


        namelable=QLabel("Name:")
        self.name_line_edit=QLineEdit()

        birth_lable=QLabel("Date of birth MM/DD/YYYY")
        self.birthdate_line_lable=QLineEdit()

        #widget add
        grid.addWidget(namelable,0,0)
        grid.addWidget(self.name_line_edit,0,1)
        grid.addWidget(birth_lable,1,0)
        grid.addWidget(self.birthdate_line_lable,1,1)
        

        #add button
        cal_button=QPushButton("Calculate age")
        cal_button.clicked.connect(self.age_calculate)
        self.output_lable=QLabel("")
        grid.addWidget(cal_button,2,0,1,2)
        grid.addWidget(self.output_lable,3,0,1,2)



        self.setLayout(grid)
    def age_calculate(self):
        current_year=datetime.now().year
        current_month=datetime.now().month
        birth_year=self.birthdate_line_lable.text()
        birth_month=datetime.strptime(birth_year,"%m/%d/%Y").date().month
        year_of_birth= datetime.strptime(birth_year, "%m/%d/%Y").date().year
        if birth_month > current_month:
            age= current_year - year_of_birth
            age=age-1
        else:
            age= current_year - year_of_birth
        self.output_lable.setText(f"{self.name_line_edit.text()} is {age} years old ")



app=QApplication(sys.argv)  
agecal=Agecalculator()
agecal.show()
sys.exit(app.exec())
print(type(agecal))


