[Back to README](/README.md)

### **User Stories Testing**

- [User Stories Testing](https://github.com/Stealthy20/grocery-shopping-list/blob/main/docs/userstoriestest.pdf)

### **Manual Testing**

**Navigation Bar** 
- The navigation bar is fully responsive on large/medium/small resolutions.
- At 320px, all navigation links are inline and not wrapping on another line.
- All links are correctly redirecting to the correct pages. 
- Signing out, correctly shows the correct dropdown options, Log in and Register.
- Signing in, correctly shows the correct dropdown options, My profile, and Logout.

**Footer**
- Links redirect to the correct social media page.
- Links open in a new browser tab. 

**Add Item**
- User stays on the page when items are added.
- Can't progress without adding mandatory fields.
- Feedback when mandatory fields are missing. 
- Messages are displayed when items are successfully added.
- All buttons correctly redirect.

**Edit item**
- Correctly gets the info from the item that's up for editing.
- Item gets correctly updated. 
- All buttons correctly redirect.

**Category**
- User can add new categories.
- Users can only see their categories and not other users.
- Message is displayed when a category is successfully added.
- Modal displaying the correct item when deleting.
- Item gets deleted when accepting the modal.
- All buttons correctly redirect.

**Shopping List**
- Users can see their own added items correctly.
- Toggle function correctly moves the items under the correct heading when pressed.
- Reset list button successfully deletes all the user's items and not all items in the database.
- All the sorting options work as intended.
- All buttons correctly redirect.

**Delete Modal**
- All delete modals work correctly.
- Modals can be closed by pressing outside of the modal itself.
- All buttons correctly redirect.

**Footer**
- All links are correctly redirecting to the correct pages and open in new tabs

**Chrome Dev Tools**

Chrome dev tools was used throughout the development of the project to test responsiveness.
Responsiveness was tested using Dev Tools to emulate the following devices,
- Iphone 5
- Iphone 6/7/8
- Iphone 6/7/8 Plus
- Iphone X
- Ipad
- Ipad Pro

**Browser Testing**

During development, the testing was mainly done solely using Google Chrome.

In production the site has been tested on the following browsers,
- Google Chrome
- Mozilla Firefox
- Opera
- Microsoft Edge

---

### **Validation**


[W3C HTML Validator](https://validator.w3.org/)
- No Errors


[W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- No Errors


[JSHint JavaScript Validator](https://jshint.com/)
- No Errors


[Code Institute Python Validator](https://pep8ci.herokuapp.com/)

- All files created or modified by me where tested. 
- The following errors where found  

**All these errors are from the settings.py file and can't be shortened without breaking the code**
- 124: E501 line too long (91 > 79 characters) *This is Allauth password vaildators*
- 127: E501 line too long (81 > 79 characters) *This is Allauth password vaildators*
- 130: E501 line too long (82 > 79 characters) *This is Allauth password vaildators*
- 133: E501 line too long (83 > 79 characters) *This is Allauth password vaildators*
- 156: E501 line too long (80 > 79 characters) *This cloudinary storage link*


### **Bugs and Fixes**

**Bug1**
- The user wasn't automatically assigned to the item, which made all user able to add items to each other's lists.

![Bug1](bug1.PNG "Image of the first bug")

**Fix**
- Added the ability for the form to save the item to the user when form is saved. 

![Bug1 fix](bug1fix.PNG "Image of the first bug fix")

**Bug 2**
- The first bug led me to the second one. When I tried to add the item it threw an error. 

![Bug1 fix](bug2.png "Image of the second bug")

**Fix**
- So I removed the category from the form and instead called it and set the choice from the frontend form with this code bellow. 

![Bug2 fix](bug2fix.png "Image of the second bug fix")

**Bug 3**
- When the user wanted to add an item to the list and didn't choose a category which is a required field. The user got a 404 error. 

![Bug3](bug3.png "Image of the third bug")

**Fix**
- I added code to the view to check if the category is truthy, if not throw an error message else proceed. 

![Bug3 fix](bug3fix.png "Image of the third bug fix")

**Bug 4**
- My delete modals didn't pull the right item id to delete the item that was clicked. 

![Bug4](bug4.png "Image of the fourth bug")

**Fix**
- Added {{item.id}} to the modal ID.

![Bug4 fix](bug4fix.png "Image of the fourth bug fix")




