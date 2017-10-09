from selenium import webdriver
import urllib2
import sys, re
chrome_path = r"C:\Users\Shareef\Desktop\chromedriver.exe" #change path to browser here
driver = webdriver.Chrome(chrome_path)


# argv[1] is the input file, argv[2] is the output file
fin = open(sys.argv[1],'r')
fout = open(sys.argv[2],'w')
for line in fin:
	line = line.rstrip()
	fields = re.split('\t',line)
	try:
		driver.get(fields[0])
		driver.implicitly_wait(5)
		link = driver.find_element_by_xpath("""//*[@id="mountNode"]/div/div[1]/div[3]/div[2]/div[5]/span[4]""")
		fout.write(fields[1] + "\t" + link.text + "\n")  
		print fields[1] + "\t" + link.text + "\n"
		print link.text
	except Exception, e:
		print "Not Found"
driver.quit()