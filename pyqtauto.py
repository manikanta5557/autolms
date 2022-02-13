import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from selenium import webdriver
from datetime import datetime, timedelta ,time
import time as t
def isNowInTimePeriod(startTime, endTime, nowTime):
		endTime = datetime.strptime(endTime, "%H:%M") 
		startTime= datetime.strptime(startTime, "%H:%M")
		if startTime < endTime:
			return nowTime >= startTime and nowTime <= endTime
		else:
			return nowTime >= startTime or nowTime <= endTime
class LoginForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Login Form')
		self.resize(500, 120)

		layout = QGridLayout()

		label_name = QLabel('<font size="4"> Username </font>')
		self.lineEdit_username = QLineEdit()
		self.lineEdit_username.setPlaceholderText('Please enter your LMS username')
		layout.addWidget(label_name, 0, 0)
		layout.addWidget(self.lineEdit_username, 0, 1)

		label_password = QLabel('<font size="4"> Password </font>')
		self.lineEdit_password = QLineEdit()
		self.lineEdit_password.setPlaceholderText('Please enter your LMS password')
		layout.addWidget(label_password, 1, 0)
		layout.addWidget(self.lineEdit_password, 1, 1)
		button_login = QPushButton('CSE-BATCH 1')
		button_login.clicked.connect(self.linkopener2)
		layout.addWidget(button_login, 2, 0, 1, 2)
		layout.setRowMinimumHeight(2, 75)
		button_login = QPushButton('CSE-BATCH 2')
		button_login.clicked.connect(self.linkopener3)
		layout.addWidget(button_login, 3, 0, 1, 2)
		layout.setRowMinimumHeight(2, 25)
		self.setLayout(layout)
	def noclass(self):
		msg = QMessageBox()
		msg.setText('NO CLASSES NOW ')
		msg.exec_()
	def startBot(self,next_time,username,password,url):
		options = webdriver.ChromeOptions()
		options.add_experimental_option("detach", True)
		options.add_argument("--headless")
		options.add_argument("--disable-gpu")
		options.add_argument("--no-sandbox")
		options.add_argument("enable-automation")
		options.add_argument("--disable-infobars")
		options.add_argument("--disable-dev-shm-usage")
		driver = webdriver.Chrome(options=options)
		driver.get(url)
		driver.find_element_by_name("username").send_keys(username)
		driver.find_element_by_name("password").send_keys(password)
		driver.find_element_by_id("loginbtn").click()
		driver.find_element_by_id("join_button_input").click()
		#--------------------------------------------------
		if next_time==':':
			pass
		else:
			self.sleeper(next_time)
			driver.quit()
			self.linkopener3()
		#--------------------------------------------------
	def startBot1(self,next_time,username,password,url):
		options = webdriver.ChromeOptions()
		options.add_experimental_option("detach", True)
		driver = webdriver.Chrome(options=options)
		driver.get(url)
		driver.find_element_by_name("username").send_keys(username)
		driver.find_element_by_name("password").send_keys(password)
		driver.find_element_by_id("loginbtn").click()
		driver.find_element_by_id("join_button_input").click()
		#--------------------------------------------------
		if next_time==':':
			pass
		else:
			self.sleeper(next_time)
			driver.quit()
			self.linkopener2()
		#--------------------------------------------------
	def linkopener3(self):
		print('started working')
		ima221='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3893'
		ics221='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3958'
		ics222='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3960'
		ics223='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3964'
		ics223_lab ='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3964'
		ics224='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3894'
		ics224_lab='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3894'
		ihs221='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3896'
		ihs222='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3897'
		ics222_lab='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3960'
		ics225='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3895'
		ics225_lab='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3895'
		flag=0
		now=datetime.now()
		usrname=self.lineEdit_username.text()
		passw=self.lineEdit_password.text()
		timeNow = now.strftime('%H:%M')
		timeNow = datetime.strptime(timeNow, "%H:%M")
		if now.strftime('%A') == 'Monday':
			if isNowInTimePeriod('8:30','9:25',timeNow):
				self.startBot('9:40:01',usrname,passw,ics223)
				flag=1
			if isNowInTimePeriod('9:40','10:35',timeNow):
				self.startBot('10:50:01',usrname,passw,ics224)
				flag=1
			if isNowInTimePeriod('10:50','11:45',timeNow):
				self.startBot('12:00:01',usrname,passw,ics221)
				flag=1
			if isNowInTimePeriod('12:00','12:55',timeNow):
				self.startBot('14:00:01',usrname,passw,ima221)
				flag=1
			if isNowInTimePeriod('14:00','16:00',timeNow):
				self.startBot(':',usrname,passw,ics222_lab)
				flag=1
                
                
		if now.strftime('%A') == 'Tuesday':
			if isNowInTimePeriod('8:30','9:25',timeNow):
				self.startBot('9:40:01',usrname,passw,ics221)
				flag=1
			if isNowInTimePeriod('9:40','10:35',timeNow):
				self.startBot('10:50:01',usrname,passw,ima221)
				flag=1
			if isNowInTimePeriod('10:50','11:45',timeNow):
				self.startBot('12:00:01',usrname,passw,ics224)
				flag=1
			if isNowInTimePeriod('12:00','12:55',timeNow):
				self.startBot('14:00:01',usrname,passw,ics222)
				flag=1
			if isNowInTimePeriod('14:00','16:00',timeNow):
				self.startBot(':',usrname,passw,ics224_lab)
				flag=1
                
                
		if  now.strftime('%A')== 'Wednesday':
			if isNowInTimePeriod('8:30','9:25',timeNow):
				self.startBot('9:40:01',usrname,passw,ima221)
				flag=1
			if isNowInTimePeriod('9:40','10:35',timeNow):
				self.startBot('10:50:01',usrname,passw,ics221)
				flag=1
			if isNowInTimePeriod('10:50','11:45',timeNow):
				self.startBot('12:00:01',usrname,passw,ics221)
				flag=1
			if isNowInTimePeriod('12:00','12:55',timeNow):
				self.startBot('14:00:01',usrname,passw,ima221)
				flag=1
			if isNowInTimePeriod('14:00','16:00',timeNow):
				self.startBot(':',usrname,passw,ics225_lab)
				flag=1
		if  now.strftime('%A')== 'Thursday':
			if isNowInTimePeriod('8:30','9:25',timeNow):
				self.startBot('9:40:01',usrname,passw,ics223)
				flag=1
			if isNowInTimePeriod('9:40','10:35',timeNow):
				self.startBot('10:50:01',usrname,passw,ics222)
				flag=1
			if isNowInTimePeriod('10:50','11:45',timeNow):
				self.startBot('12:00:01',usrname,passw,ihs222)
				flag=1
			if isNowInTimePeriod('12:00','12:55',timeNow):
				self.startBot('14:00:01',usrname,passw,ics221)
				flag=1
			if isNowInTimePeriod('14:00','16:00',timeNow):
				self.startBot(':',usrname,passw,ics223_lab)
				flag=1
		if  now.strftime('%A')== 'Friday':
			if isNowInTimePeriod('8:30','9:25',timeNow):
				self.startBot('9:40:01',usrname,passw,ics222)
				flag=1
			if isNowInTimePeriod('9:40','10:35',timeNow):
				self.startBot('10:50:01',usrname,passw,ics224)
				flag=1
			if isNowInTimePeriod('10:50','11:45',timeNow):
				self.startBot('12:00:01',usrname,passw,ics223)
				flag=1
			if isNowInTimePeriod('12:00','12:55',timeNow):
				self.startBot(':',usrname,passw,ics225)
				flag=1
		if flag==0:
			self.noclass()
	def linkopener2(self):
		print('started working')
		ima221='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3888'
		ics221='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3958'
		ics222='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3959'
		ics223='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3963'
		ics223_lab ='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3963'
		ics224='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3889'
		ics224_lab='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3889'
		ihs221='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3891'
		ihs222='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3892'
		ics222_lab='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3959'
		ics225='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3890'
		ics225_lab='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3890'
		flag=0
		now=datetime.now()
		usrname=self.lineEdit_username.text()
		passw=self.lineEdit_password.text()
		timeNow = now.strftime('%H:%M')
		timeNow = datetime.strptime(timeNow, "%H:%M")
		if now.strftime('%A') == 'Monday':
			if isNowInTimePeriod('8:30','9:25',timeNow):
				self.startBot1('9:40:01',usrname,passw,ics223)
				flag=1
			if isNowInTimePeriod('9:40','10:35',timeNow):
				self.startBot1('10:50:01',usrname,passw,ics224)
				flag=1
			if isNowInTimePeriod('10:50','11:45',timeNow):
				self.startBot1('12:00:01',usrname,passw,ics221)
				flag=1
			if isNowInTimePeriod('12:00','12:55',timeNow):
				self.startBot1('14:00:01',usrname,passw,ima221)
				flag=1
			if isNowInTimePeriod('14:00','16:00',timeNow):
				self.startBot1(':',usrname,passw,ics222_lab)
				flag=1
                
                
		if now.strftime('%A') == 'Tuesday':
			if isNowInTimePeriod('8:30','9:25',timeNow):
				self.startBot1('9:40:01',usrname,passw,ics221)
				flag=1
			if isNowInTimePeriod('9:40','10:35',timeNow):
				self.startBot1('10:50:01',usrname,passw,ima221)
				flag=1
			if isNowInTimePeriod('10:50','11:45',timeNow):
				self.startBot1('12:00:01',usrname,passw,ics224)
				flag=1
			if isNowInTimePeriod('12:00','12:55',timeNow):
				self.startBot1('14:00:01',usrname,passw,ics222)
				flag=1
			if isNowInTimePeriod('14:00','16:00',timeNow):
				self.startBot1(':',usrname,passw,ics224_lab)
				flag=1
                
                
		if  now.strftime('%A')== 'Wednesday':
			if isNowInTimePeriod('8:30','9:25',timeNow):
				self.startBot1('9:40:01',usrname,passw,ics224)
				flag=1
			if isNowInTimePeriod('9:40','10:35',timeNow):
				self.startBot1('10:50:01',usrname,passw,ima221)
				flag=1
			if isNowInTimePeriod('10:50','11:45',timeNow):
				self.startBot1('12:00:01',usrname,passw,ics221)
				flag=1
			if isNowInTimePeriod('12:00','12:55',timeNow):
				self.startBot1('14:00:01',usrname,passw,ima221)
				flag=1
			if isNowInTimePeriod('14:00','16:00',timeNow):
				self.startBot1(':',usrname,passw,ics225_lab)
				flag=1
		if  now.strftime('%A')== 'Thursday':
			if isNowInTimePeriod('8:30','9:25',timeNow):
				self.startBot1('9:40:01',usrname,passw,ics223)
				flag=1
			if isNowInTimePeriod('9:40','10:35',timeNow):
				self.startBot1('10:50:01',usrname,passw,ics222)
				flag=1
			if isNowInTimePeriod('10:50','11:45',timeNow):
				self.startBot1('12:00:01',usrname,passw,ihs221)
				flag=1
			if isNowInTimePeriod('12:00','12:55',timeNow):
				self.startBot1('14:00:01',usrname,passw,ics221)
				flag=1
			if isNowInTimePeriod('14:00','16:00',timeNow):
				self.startBot1(':',usrname,passw,ics223_lab)
				flag=1
		if  now.strftime('%A')== 'Friday':
			if isNowInTimePeriod('8:30','9:25',timeNow):
				self.startBot1('9:40:01',usrname,passw,ics222)
				flag=1
			if isNowInTimePeriod('9:40','10:35',timeNow):
				self.startBot1('10:50:01',usrname,passw,ihs222)
				flag=1
			if isNowInTimePeriod('10:50','11:45',timeNow):
				self.startBot1('12:00:01',usrname,passw,ics223)
				flag=1
			if isNowInTimePeriod('12:00','12:55',timeNow):
				self.startBot1(':',usrname,passw,ics225)
				flag=1
		if flag==0:
			self.noclass()
	def sleeper(self,ent):
		ent1=ent.split(':')
		enter=datetime.now()
		exit = time(hour=int(ent1[0]),minute=int(ent1[1]),second=int(ent1[2]))  
		enter_delta = timedelta(hours=enter.hour, minutes=enter.minute, seconds=enter.second)
		exit_delta = timedelta(hours=exit.hour, minutes=exit.minute, seconds=exit.second)
		difference_delta = exit_delta - enter_delta
		li=str(difference_delta).split(':')
		seconds=int(li[0])*60*60+int(li[1])*60+int(li[2])
		t.sleep(seconds)
if __name__ == '__main__':
	app = QApplication(sys.argv)
	form = LoginForm()
	form.show()
	sys.exit(app.exec_())
