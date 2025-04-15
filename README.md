Deploy

Go to your Heroku dashboard and create a new app.
In the Deploy tab of your new app, under Deployment method, click GitHub. 
Under Connect to GitHub, in the field next to your username on Guthub, type the repository name of the project and click Search. 
The corresponding repository name appears below, click the Connect button.


In settings, under Config Vars, add secret key and database url???


Scroll down to Manual deploy, select the main branch to deploy and click Deploy Branch.

In the top of the page, click Open app to open the app.

Fonts
I looked for cinema feleing in my fonts and after some googleing I decided on Limelight for my larger font sizes and Merriweather for the smaller ones. Limelight is connected to theatre and filmmaking as per its description, and Merriweather was suggested in this blog post: https://wpmudev.com/blog/more-google-font-combinations-for-you-to-use/.

Colours
For my colour scheme, I want to convey a home theater feeling so I took my inspiration from articles about which colours would be good when you build a theater room. Red chairs came to mind, and otherwise dark colours for walls. And some yellow details to mimic the small spotlights on the wall. I read this article https://www.happypaintingcompany.com/blog/the-top-5-best-home-theater-paint-colors/ and https://www.peliplat.com/en/article/10002576/why-are-movie-theater-seats-mostly-red and landed on the following palette:
black, navy, red, yellow.



Issues:
displaying manytomany fields in html, fixed with all. 
manytomany field in admin when adding movie, fixed with horizonal filter

approve review when there is not text, only rating, so it is added right away and calculated in the average. So I want a conditional default value of the approved field, a simple if else statement. I had trouble finding the answer to this, but then I found https://stackoverflow.com/questions/12649659/how-to-set-a-django-model-fields-default-value-to-a-function-call-callable-e/15289517. It did not work at first, when I added the function above the review model.

In admin when title is empty, you cannot click it to approve. So when title is empty but there is text, you cannot approve it. Do I change to title being mandatory? Could make sense. But I can also custumise admin, by setting changing the str method on the model so it represented as a link in the list display in admin, and editable. 
Also when you just add a space, it does not need to be approved. Very good. But then the title is not clickable in amdin, because it does not change to 'open'.



Minor issue, after sending first rating which is approved right away, the total at the top is 0 althought the average is updated. After updating page it is fixed.