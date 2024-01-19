import os
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
def sleeper(ent):
		ent1=ent.split(':')
		enter=datetime.now()
		exit = time(hour=int(ent1[0]),minute=int(ent1[1]),second=int(ent1[2]))  
		enter_delta = timedelta(hours=enter.hour, minutes=enter.minute, seconds=enter.second)
		exit_delta = timedelta(hours=exit.hour, minutes=exit.minute, seconds=exit.second)
		difference_delta = exit_delta - enter_delta
		li=str(difference_delta).split(':')
		seconds=int(li[0])*60*60+int(li[1])*60+int(li[2])
		t.sleep(seconds)
def linkopener3():
		
		# ima221='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3893'
		# ics221='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3958'
		# ics222='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3960'
		# ics223='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3964'
		# ics223_lab ='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3964'
		# ics224='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3894'
		# ics224_lab='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3894'
		# ihs221='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3896'
		# ihs222='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3897'
		# ics222_lab='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3960'
		# ics225='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3895'
		# ics225_lab='https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=3895'
		ics422 = 'https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=9215'
		ics423 = 'https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=9214'
		ioe412 = 'https://lms.iiitkottayam.ac.in/mod/bigbluebuttonbn/view.php?id=9219'
		flag=0
		now=datetime.now()
		usrname='2020bcs0030'
		passw='dommaFS69'
		timeNow = now.strftime('%H:%M')
		timeNow = datetime.strptime(timeNow, "%H:%M")
		if now.strftime('%A') == 'Monday':
			if isNowInTimePeriod('8:00','8:55',timeNow):
				startBot('9:00:01',usrname,passw,ics422)
				flag=1
			if isNowInTimePeriod('10:05','12:00',timeNow):
				startBot(':',usrname,passw,ics423)
				flag=1
			# if isNowInTimePeriod('16:15','17:10',timeNow):
			# 	startBot(':',usrname,passw,ics221)
			# 	flag=1
			# if isNowInTimePeriod('12:00','12:55',timeNow):
			# 	startBot('14:00:01',usrname,passw,ics222)
			# 	flag=1
			# if isNowInTimePeriod('14:00','16:00',timeNow):
			# 	startBot('16:00:01',usrname,passw,ics222_lab)
			# 	flag=1
                
                
		if now.strftime('%A') == 'Tuesday':
			if isNowInTimePeriod('8:00','8:55',timeNow):
				startBot(':',usrname,passw,ics423)
				flag=1
			# if isNowInTimePeriod('9:40','10:35',timeNow):
			# 	startBot('10:50:01',usrname,passw,ima221)
			# 	flag=1
			# if isNowInTimePeriod('10:50','11:45',timeNow):
			# 	startBot('12:00:01',usrname,passw,ics224)
			# 	flag=1
			# if isNowInTimePeriod('12:00','12:55',timeNow):
			# 	startBot('14:00:01',usrname,passw,ics222)
			# 	flag=1
			# if isNowInTimePeriod('14:00','16:00',timeNow):
			# 	startBot('16:00:01',usrname,passw,ics224_lab)
			# 	flag=1
                
                
		if  now.strftime('%A')== 'Wednesday':
			if isNowInTimePeriod('8:00','8:55',timeNow):
				startBot('9:00:01',usrname,passw,ioe412)
				flag=1
			if isNowInTimePeriod('9:00','9:55',timeNow):
				startBot('11:05:01',usrname,passw,ics422)
				flag=1
			# if isNowInTimePeriod('10:50','11:45',timeNow):
			# 	startBot('12:00:01',usrname,passw,ics221)
			# 	flag=1
			# if isNowInTimePeriod('12:00','12:55',timeNow):
			# 	startBot('14:00:01',usrname,passw,ima221)
			# 	flag=1
			if isNowInTimePeriod('11:05','12:00',timeNow):
				startBot(':',usrname,passw,ics423)
				flag=1
		if  now.strftime('%A')== 'Thursday':
			if isNowInTimePeriod('9:00','9:55',timeNow):
				startBot('10:05:01',usrname,passw,ioe412)
				flag=1
			if isNowInTimePeriod('10:05','11:00',timeNow):
				startBot(':',usrname,passw,ics422)
				flag=1
			# if isNowInTimePeriod('10:50','11:45',timeNow):
			# 	startBot('12:00:01',usrname,passw,ihs222)
			# 	flag=1
			# if isNowInTimePeriod('12:00','12:55',timeNow):
			# 	startBot('14:00:01',usrname,passw,ics221)
			# 	flag=1
			# if isNowInTimePeriod('14:00','16:00',timeNow):
			# 	startBot(':',usrname,passw,ics223_lab)
			# 	flag=1
		if  now.strftime('%A')== 'Friday':
			if isNowInTimePeriod('8:00','8:55',timeNow):
				startBot('9:00:01',usrname,passw,ioe412)
				flag=1
			if isNowInTimePeriod('11:00','11:55',timeNow):
				startBot(':',usrname,passw,ics423)
				flag=1
			# if isNowInTimePeriod('10:50','11:45',timeNow):
			# 	startBot('12:00:01',usrname,passw,ics223)
			# 	flag=1
			# if isNowInTimePeriod('12:00','12:55',timeNow):
			# 	startBot(':',usrname,passw,ics225)
			# 	flag=1

def startBot(next_time,username,password,url):
		chrome_options = webdriver.ChromeOptions()
		chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--disable-dev-shm-usage")
		chrome_options.add_argument("--no-sandbox")
		driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
		driver.get(url)
		driver.find_element_by_name("username").send_keys(username)
		driver.find_element_by_name("password").send_keys(password)
		driver.find_element_by_id("loginbtn").click()
		driver.find_element_by_id("join_button_input").click()
		#--------------------------------------------------
		#-------------------------------------------------
		if next_time==':':
			t.sleep(3*60*60)
		else:
			sleeper(next_time)
			driver.quit()
			linkopener3()
while True:
    linkopener3()
