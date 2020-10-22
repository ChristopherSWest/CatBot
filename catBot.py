'''
Program Name: catBot.py
Program Description: This program runs a twitter account that periodically posts pictures of cats.
Programmer's Name: Christopher West
'''
from selenium import webdriver;
from selenium.webdriver import ActionChains;
from selenium.webdriver.common.keys import Keys;
from pynput.keyboard import Key, Controller;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
import time, random, selenium;



def logIn(browser):
	userName = '';
	pWord = '';

	loginElem = browser.find_element_by_link_text('Log in');
	loginElem.click();

	emailElem = browser.find_element_by_class_name('js-username-field');
	emailElem.send_keys(userName);
	time.sleep(1);
	passElem = browser.find_element_by_class_name('js-password-field');
	passElem.send_keys('TheCatman66$!');

	passElem.submit();

def getCatsFunc(browser):
	working = bool(0);

	keyboard.press(Key.ctrl_l);
	
	time.sleep(1);
	for i in range(5):
		keyboard.press('-');
		keyboard.release('-')
		time.sleep(.2);
	keyboard.release(Key.ctrl_l);
	for i in range(3):
		keyboard.press(Key.down);
		time.sleep(.2);
	getCats = browser;
	time.sleep(1);

	imgElems = getCats.find_elements_by_class_name('photo-item__img');
	catElem = imgElems[random.randrange(0,(len(imgElems)-1))];
	actionChains = ActionChains(getCats);
	
	time.sleep(2);


	while working == bool(0):
		try:
			time.sleep(5);
			actionChains.context_click(catElem).perform();
			working = bool(1);
		except selenium.common.exceptions.MoveTargetOutOfBoundsException:
			keyboard.press(Key.esc);
			for i in range(25):
				time.sleep(.2);
				keyboard.press(Key.down);
				keyboard.release(Key.down);
				time.sleep(.2);
				working = bool(0);
	for i in range(9):
		keyboard.press(Key.down);
		keyboard.release(Key.down);
		time.sleep(.5);
	keyboard.press(Key.enter);
	keyboard.release(Key.enter);


	time.sleep(1);
	'''htmlElem = browser.get_element_by_tag_name('html');
	htmlElem.send_keys(Keys.END);
	time.sleep(2);
	'''
	

def postCat(browser):
	catText = ['Cute Cat!','Best Cat!','Cats are Great!', 'Heyo!', 'Cats!!','Awww','Woah!', 'Oh yeah!', 'Pretty Kitty!', 'Sweet Cat!', 'This Cat is Awesome!', 'Wonderful Cat!', 'This cat is baller!', 'Do you like this cat?','I love this Cat!', 'So Cute!'];
	time.sleep(1);
	tweetElem = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='placeholder-532c5']")));
	#tweetElem = browser.find_element_by_id('tweet-box-home-timeline');

	
	tweetElem.send_keys(catText[random.randrange(0,(len(catText)-1))]);
	
	time.sleep(10);
	actions = ActionChains(browser);

	actions.context_click(tweetElem).perform();
	for i in range(4):
		keyboard.press(Key.down);
		keyboard.release(Key.down);
		time.sleep(.5);
	keyboard.press(Key.enter);
	keyboard.release(Key.enter);
	time.sleep(2);
	submit = browser.find_element_by_class_name('button-text');
	submit.click();


keyboard = Controller();
getCats = webdriver.Firefox();
getCats.get('https://www.pexels.com/search/cat/');


#getCat function
getCatsFunc(getCats);


browser = webdriver.Firefox();
browser.get('https://twitter.com');	
logIn(browser);
postCat(browser);


count = 0;

while count < 40:
	time.sleep(1);
	keyboard.press(Key.alt_l);
	keyboard.press(Key.tab);
	keyboard.release(Key.alt_l);
	keyboard.release(Key.tab);
	getCatsFunc(getCats);
	time.sleep(4);
	keyboard.press(Key.alt_l);
	keyboard.press(Key.tab);
	keyboard.release(Key.alt_l);
	keyboard.release(Key.tab);
	time.sleep(5);
	postCat(browser);
	count += 1;
	time.sleep(600);

print('all done');


