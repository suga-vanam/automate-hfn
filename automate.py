from selenium import webdriver
import time


#cell_fill = ''
#cell = site.find_element_by_xpath('x_path')
#cell.send_keys(cell_fill)

site = webdriver.Chrome()
site.get('https://heartfulness.org/education/essay-event/app/participant/register')

time.sleep(2)

cityname = "coimbatore"
city = site.find_element_by_xpath('//*[@id="district"]')
city.send_keys(cityname)

countryname = "India"
country = site.find_element_by_xpath('//*[@id="state"]')
country.send_keys(countryname)


institutename = "Nehru Arts & Science College"
institute = site.find_element_by_xpath('//*[@id="institute"]')
institute.send_keys(institutename)

clgmail = "karunaikatturai@gmail.com"
mail =  site.find_element_by_xpath('//*[@id="instituteemail"]')
mail.send_keys(clgmail)

clgcity = 'coimbatore'
clg = site.find_element_by_xpath('//*[@id="instcity"]')
clg.send_keys(clgcity)

clgcountry = 'India'
country = site.find_element_by_xpath('//*[@id="country"]')
country.send_keys(clgcountry)

essaylang = 'Tamil'
lang = site.find_element_by_xpath('//*[@id="language"]')
lang.send_keys(essaylang)

participantmail = 'karunaikatturai@gmail.com'
mailid = site.find_element_by_xpath('//*[@id="email"]')
mailid.send_keys(participantmail)

UNESCO = site.find_element_by_xpath('//*[@id="pledge"]')
UNESCO.click()

knowopt = 'Website'
known = site.find_element_by_xpath('//*[@id="howknow"]')
known.send_keys(knowopt)

age = site.find_element_by_xpath('//*[@id="ageaccept"]')
age.click()

grant = site.find_element_by_xpath('//*[@id="condition1"]')
grant.click()

person = site.find_element_by_xpath('//*[@id="condition2"]')
person.click()

terms = site.find_element_by_xpath('//*[@id="userConsent"]')
terms.click()

award = site.find_element_by_xpath('//*[@id="agedeclare2"]')
award.click()

correct = site.find_element_by_xpath('//*[@id="correctentries"]')
correct.click()