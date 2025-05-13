# Rates 'R Us - Testing

[Live link to website](https://rates-r-us-f1ee65907d50.herokuapp.com/)


- - -

## Contents

* [Automated testing](#automated-testing)
  * [HTML validator](#html-validator)
  * [CSS validator](#css-validator)
  * [Python validator](#python-validator)
  * [JavaScript validator](#javascript-validator)
  * [Lighthouse testing](#lighthouse-testing)
  * [Favicon testing](#favicon-testing)
* [Manual testing](#manual-testing)
  * [User story testing](#user-story-testing)
  * [Issues](#issues)
    * [Logic](#logic)
    * [Accessibility](#accessibility)
    * [Error in console](#error-in-console)
    * [Responsiveness](#responsiveness)
    * [Different fruit looks](#different-fruit-looks)
    * [Safari lacks font support](#safari-lacks-font-support)
  * [Full testing](#full-testing)
    * [Browser testing](#browser-testing)
    * [Device testing](#device-testing)
    * [Feature testing](#feature-testing)
    * [Scenario testing](#scenario-testing)
    * [Unfixed bugs](#unfixed-bugs)


## Automated testing

### HTML validator

When I ran this [HTML validator](https://validator.w3.org/), I needed to add some hidden heading and I had some empty p tags because in the displayed reviews in move_detail.html, because users can chose to not write a text, but this was still displayed. So I added a condition in the template to not display anything if there is no review text. 

For the my_reviews html, it did not work to check the URL in the validator, but the source code gave no errors.

The signup page does give errors in the validator, but they are of the actual form that is used there "form.as_p". I cannot access the form to fix the code. 

Below are the direct links to the validator's result per page (for those that accepted URL input): 
 -  [Home page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frates-r-us-f1ee65907d50.herokuapp.com%2F)
 -  [movie_detail.html(Interstellar example)](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frates-r-us-f1ee65907d50.herokuapp.com%2Finterstellar-2014-11-07%2F)
 -  [Log in page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frates-r-us-f1ee65907d50.herokuapp.com%2Faccounts%2Flogin%2F)
 -  [Log out page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frates-r-us-f1ee65907d50.herokuapp.com%2Faccounts%2Flogout%2F)

The search pages can be rendered with URL but the links to the validator do not work at a later time. I run the following urls and there were no errors: https://rates-r-us-f1ee65907d50.herokuapp.com/search/?q=hello (no search result), https://rates-r-us-f1ee65907d50.herokuapp.com/search/?q=bullock (1 result).

### CSS validator

For style.css, there are no errors in the [Jigsaw validator](https://jigsaw.w3.org/css-validator/). There are some warnings related to the imported Google Fonts and used variables, that can be ignored. Because I ran my code through the [Autoprefixer](https://autoprefixer.github.io/), I also get warnings about this, which can be ignored.

I have re-checked these results along the way in the testing fase, as I have changed my css continuously. Below is the latest result.

![Css warnings](docs/screenshots/css-validator.png)

### Python validator

Firstly, I need to shorten my lines and fix the incorrect white spaces, as I have ignored these problems completely. So before running my code through the [CI Python Linter](https://pep8ci.herokuapp.com/), I will fix this in VS code with help of the PROBLEMS tab. I leave only the url links in my comments too long, as I found this is ok. The Python linter only reports these long url links. The reason I don't want to shorten them, is because the links are descriptive so it's more read-friendly in my opinion to keep the original urls (I checked [stackoverflow](https://stackoverflow.com/questions/10739843/how-should-i-format-a-long-url-in-a-python-comment-and-still-be-pep8-compliant) for this).

![Python warnings]()IMAGE NEEDED

### Javascript validator

I used [JSHint](https://jshint.com/) to validate my reviews.js file. With the setting ES6, the code passes, apart from one error: **One undefined variable: bootstrap**. This has to do with **const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));**. I had this in my previous project as well, and ignored this error because it has to do with bootstrap not being recognised.

 ![JSHint error](docs/screenshots/js-validator.png)

### Lighthouse testing

#### Home page

I get a best practice error saying I have insecure requests not using HTTPS. This has to do with Cloudinary, and I found a solution for this on Slack [in this thread](https://code-institute-room.slack.com/archives/C026PTF46F5/p1706622757171679). Another performance issue is the format of my images, which I though would not be relevant because it is via Cloudinary, but I still have to convert them to WebP. So I converted th images via [tinypng](https://tinypng.com/) and uploaded them again via admin.

After I addressed these, I still had some issues related to Cloudinary and third-party cookies in Chrome. But I decided to leave these issues be, because I do not want to change Cloudinary. I found that Cloudinary was supposed to come with a solution (https://community.cloudinary.com/discussion/comment/1182#Comment_1182?utm_source=community-search&utm_medium=organic-search&utm_term=chrome+cookies), but I have not found any more information. And the latest information is that Chrome might not disable third-party cookies at all (https://www.didomi.io/blog/google-chrome-third-party-cookies-april-2025). I also found that in incognito mode, this issue is gone and Best practices scores 100 %

Also, some of my images still were much larger than displayed, so I needed to fix this. I decided to cut all the movie poster images to around 416 x 624. Not all images have the same ratio, but I made sure the size is never smaller than this, as it is the largest displayed size on the largest screen size. I would urge the superuser to do this as well when they post a new movie. Now the issues I get for performance relate to my usage of Bootstrap, Heroku, Google Fonts, Cloudinary, but the score is 97 for the home page and similar scores for the next pages. For some movies with longer titles or where the image is adjusted by my css media queries I get a lower score because of larger layout shifts, but still acceptible scores of around 90 %. 

For mobile reports, my best practices is a bit lower (96 %) due to the image size being a bit different, as the images can have slightly different sizes as they are all stacked veritcally, so you do not notice different heights. The report it expects the images to be 582 x 873, instead of the 416 x 624 I have uploaded to Cloudinary. I decided to keep this as it is. 

For the mobile version, I get a low performance score due to the large movie posters. I decided to add css for screens up to 575 px and make the image smaller and center the content of the card for style purposes. I still get issues, and now it tells me to use smaller original images as well (see detail page below). But I managed to get 91 % for the first and second page.

![Lighthouse result desktop first home page](docs/screenshots/lighthouse-home-1.png)
![Lighthouse result desktop second home page](docs/screenshots/lighthouse-home-2.png)

![Lighthouse result mobile first home page](docs/screenshots/lighthouse-home-mobile-1.png)
![Lighthouse result mobile second home page](docs/screenshots/lighthouse-home-mobile-3.png)


#### Detail pages

For the detail page, I get from 90 % to 99 % performance, as it only has one image. The image size on the page is smaller than the size in cloudinary because it is smaller than the largest size on the home page, so I do get an issue for that, but I will not use separate images for the home and detail page. Otherwise, I get the same kind of issues as for the home page. The scores differ a little depending on the movie, because of the different content. Movies with longer titles score lower as they have larger layout shifts. Running lighthouse at different times does affect the scrore as well, I have gotten 100 % as well as 87 % at different times.

I get a warning on best practices saying I use a deprecated API "H1UserAgentFontSizeInSection". I googled this error and found [documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#specifying_a_uniform_font_size_for_h1) implying it has to do with h1 inside an article element and that the size should be specified. I tried this by adding class="h2" to my h1. But like someone mentions [here](https://github.com/GoogleChrome/lighthouse/issues/16404), this did not fix it, so then I added a piece of code 
":where(h1) {
  margin-block: 0.67em;
  font-size: 2em;
}" because someone says this should fix it, but this still did not work. I removed the code again. I decide to leave it now. I tested to remove <article> and this actually gave me 100 %. But <article> is there for semantic information, so I want to use it. So instead I used a hidden h1 above article and changed my original h1 to h2 inside the article element. This finally worked and I have 100% on best practices. For mobile I get a bit lower because of the image issue, being too small in cloudinary. But still very good scores.

For accessibility, I got a lower score because my Log in and register links only rely on colour, so I added underline to this. Now I get 100% on desktop. As I mentioned, the scores differ for each movie, but they also differ for the same movie if you run lighthouse several times, so I think the largest issues have been addressed.

![Lighthouse result desktop detail page](docs/screenshots/lighthouse-desktop-detail.png)

![Lighthouse result mobile detail page](docs/screenshots/lighthouse-detail-mobile-1.png)

#### Search page
For the search page, I get an issue for accessibility about my headings not being in a correct descending order. This is because I reuse code from the home page, where there are h2 headings, but on the search page there is not. I added a visually hidden h2 to fix that, now it is 100 %. For search results without any result, this was not an issue in the first place.

The performance score varies but is acceptible, and I do not see how to improve this at the moment.

![Lighthouse result desktop search page no result mobile/desktop](docs/screenshots/lighthouse-search-noresult.png)

![Lighthouse result desktop search page with result desktop](docs/screenshots/lighthouse-search-result-desktop.png)

![Lighthouse result desktop search page with result mobile](docs/screenshots/lighthouse-search-result-mobile.png)

#### My reviews page

My reviews gave an issue for accessibility about my links not having discernible text. Looking better at the page with devtools, I saw the links were placed weirdly and there were a lot of empty links. The HTML validator had not seen this. I fixed the link tag to be inside the innerloop of {% if movie == review.movie %}, and added an aria-label as well. Now, the links look like they should. Rerunning Lighthouse, I get 100% for accessibility.

I get 92 (mobile) and 93 (desktop) for performance and I think this could be improved my implementing pagination. But that is out of scope for the MVP.

![Lighthouse result desktop My reviews](docs/screenshots/lighthouse-myreviews-desktop.png)

![Lighthouse result mobile My reviews](docs/screenshots/lighthouse-myreviews-mobile.png)

#### Log in, log out, register, 404

For the register page, I get an accessibility issue because of the default form text color. The instructions for the password are black on a red background, instead of white like the rest of my text. I fixed it in css, and also made sure the font is the primary font used for p elements. I checked the Log in page and saw that warning texts are black as well, i.e. when you enter the wrong password, so I added that in the same css style. That form does not have an id, so I had to simply set all ul and li descendants of form elements the white color and primary font family, but in this case this is ok, as I don't have ul or li in my other form to leave a review. Below are only the mobile screenshots for testing, but the desktop tests were similar.

My 404 page has a best practice issue about a 404 error in the console, otherwise ok.

![Lighthouse result mobile log in](docs/screenshots/lighthouse-login-mobile.png)

![Lighthouse result mobile log out](docs/screenshots/lighthouse-logout-mobile.png)

![Lighthouse result mobile register](docs/screenshots/lighthouse-register-mobile.png)

![Lighthouse result mobile 404](docs/screenshots/lighthouse-404.png)


### Favicon testing
I ran https://rates-r-us-f1ee65907d50.herokuapp.com/ through Realfavicongenerator's [favicon checker](https://realfavicongenerator.net/favicon-checker/rates-r-us-f1ee65907d50.herokuapp.com%2F), and I got a warning saying my svg icon is not squared, so I created a new one. Now I just have an issue saying "No touch web app title declared", but the web site's title should be used in this case.

## Manual testing

### User story testing

|   User story                                                            | How it is achieved    |
|  -----------                                                             | -----------           |
|**As a site admin, I can:**|
|create, read, update and delete movie posts so that I can manage my website,|Admin platform with **Movies** section enables adding movies with relevant fields, updating them, and deleting them or setting them on draft so they are not visible on the website.|
|create a draft so that I can control when and if posts will be published on the website,|**Status** field in admin can be set on **Draft** and the movie will not be visible on the website.|
|pick out several movies to be highlighted on the website so that I can make my website more personal,|**Top pick** check box in admin and code functionlaity that 3 top picks will display on the first homepage on top, in admin the top picks can be filtered so the user can see which movies are selected for it.|
|write a motivation for my chosen top movies in admin so that I can make the website more personal,|**Pick motivation** field, the text will be displayed in the **Top pic** section on the home page, as well as in the movie detail page under **Moby's review** under the movie description. Even if a movie is not selected as a top pick, the motivation text will display on the movie detail page, as long as the site admin does not remove it.|
|prevent reviews from displaying so that I have control over which reviews appear on my website.|**Reviews** section in admin and the **Approved** check box in each review. A review is not publicly visible until the **Approved** check box is selected. Reviews that only consist of a rating will automaticly get approved, but the site admin can also choose to clear the check box. The reviews have a filter in admin so the site admin can filter on approved or not approved reviews.|
| | |
|**As a site user, I can:**|
|view a paginated list of movie posts so that I can quickly find the movie I want to view,|Paginated home page with max 3 movies, excluding the first home page that has a top pick section by the superuser with 3 extra movies.|
|search movies on title, director or cast member so that I can find what I'm looking for,|**Search** bar on top of the page that leads to a search result page.|
|open a movie post so that I can read the whole post,|From the home or search result page, any user can click on a movie card which leads to the respective movie detail page with the description, Moby's review and all users' (approved) reviews and ratings.|
|register an account so that I can rate movies and add reviews,|**Register** page where the user can create an account, **Log in** page to log in to account and access the movies' review form.|
|review a movie so that I can share my opinion,|When logged in, the review form is available on the movie detail page. A user who has not left a review yet, can fill in this form and submit it.|
|rate movies so that I can contribute to the overall rating of the movie,|When logged in, the review form is available on the movie detail page. A user who has not left a rating yet, can add a rating. If the user does not leave a text review, the rating will be published immediately and calculated in the average movie rating. If the user leaves a text review as well as a rating, the review needs to be approved before the rating will be calculated in the average movie rating.|
|edit or delete my review so that I have control on my contribution to the website|When logged in, a user can view all their reviews on the **My reviews** page. The user can click on the review to go to the specific review on the movie's detail page, and there, the user can click **Edit**. The user moves up to the review form where the old review is displayed, the user can change anything and click **Update**. If the updated review has text, it needs to be approved again by the site admin to be published. If a user clicks **Delete**, a modal pops up where the user can confirm deleting the review, and the review will be removed.|
|edit or delete my rate so that I have control on my contribution to the website,|This works the same as editing or deleting a review, but when a user only rates a movie without any text contribution, the edited rating will be approved automatically and calculated in the movie rating average.|


### Issues

Here I list some issues and bugs that took extra effort to fix.

#### Many-to-many fields

The **Genre** field in the **Movie** model is a many-to-many field and I had some trouble displaying it correctly in html. This was fixed with *.all* in the template (*{{ movie.genre.all|join:", " }}*).

In admin, when you add a movie, the **Cast** is also a many-to-many field. To get this to work as a list of actors that you can select from easily when you add cast members to a movie, and search if the actor is already in the list of created actors, I added a *horizontal filter* (https://stackoverflow.com/questions/14828168/django-show-filter-horizontal-on-user-change-admin-page, https://stackoverflow.com/questions/73570167/django-filter-horizontal-how-to-connect-more-fields-together). I did this for **Genre** and **Directed by** as well, as they are also many-to-many fields.

Another issue I had was related to the search field in admin. I want the site admin to be able to search on actor in admin, and get all movies where this actor is playing. To get this to work, I had to use **cast__name** in *search_fields = ['movie_title', 'cast__name']* in admin.py (https://docs.djangoproject.com/en/5.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields, https://stackoverflow.com/questions/51931762/how-can-we-search-many-to-many-field-in-django-admin-search-field). For the search field in the **Review** model, to find all reviews for a specific movie, it was also needed to use **movie__movie_title**.

#### Review functionality

##### Approve review when there is no text, only a rating

I wanted to approve reviews automatically when there is no text, only a rating, so it is published right away and calculated in the movie's average rating. So I thought about a conditional default value of the approved field, a simple if else statement. I had trouble finding the answer to this, but then I found https://stackoverflow.com/questions/12649659/how-to-set-a-django-model-fields-default-value-to-a-function-call-callable-e/15289517. It did not work, and I tried different places to put the code, below, above, inside the review model. But I read that the field itself cannot have an if statement, so I thought it should be a callable. But I tried something else instead, and added it in the view before the review is saved to the database. Now it sets approved to True when both the title and text are empty, and it displays an appropriate message and the rating is visible and calculated into the average right away. And when title and text are not empty, it needs to be approved by the site admin. In admin, when I add a review with empty title and text, it does not get approved right away, which I think is not a relevant issue as the superuser can just approve it.

In admin when the review title is empty, you can not click it to approve. So when a review's title is empty but there is a text, the site admin could not approve it. So I thought about changing the review title being mandatory. I also thought about customising admin, by setting the *str* method on the model so it would represented as a link in the list display in admin, and clickable. But that turned out has no effect when there is list_display. So i tried to set a title value of *Open* before it saves in the views.py, but that did not work for when you as a user add a space in the title. It turned out that when you just add a space in the review's title, it does not need to be approved, which is very good. But in case of the user adding a space in the title but text in the review text, the title is not clickable in admin, because it does not change to *Open*. I could have ofcourse added that to the condition in views.py, but I thought there should be a better way. I realised that I needed to add *null=True* (now it just had *blank=True*) to the title field (or I tested out lots of different things at this point, https://medium.com/techtrends-digest/what-is-the-difference-between-null-true-and-blank-true-in-django-3b49be024ec5), so that I can have title as the clickable link in admin, since that is good when there is a title, and this *null=True* also fixed that empty titles are dispalyed as *-* in admin, which is good enough since it is clickable so the superuser can approve it. 

Because of *null=True* in the **Review** model title, *None* got displayed as a title in the frontend when a user added a review with no title. So in the template, I had to add another if statement to only display the title if it is not empty.


#### Error in console

The error about *aria-hidden* seemed a much larger issue, as I found posts about it being an issue with the attribute *disabled*: https://github.com/WordPress/gutenberg/issues/56547, and about Bootstrap using this attribute while it should not: https://github.com/twbs/bootstrap/issues/41005. So I did find a workaround [here](https://stackoverflow.com/questions/62677291/aria-hidden-elements-do-not-contain-focusable-elements-issue-when-modal-is-sho) that says you should use *aria-modal* for modals. But I saw in Chrome developer tools that this is actually added in all the modals, and not *aria-hidden*. But the **Game over** modal seemed to sometimes get *aria-hidden* instead of *aria-modal*, and the error only seemed to appear when *aria-hidden* was added. So I thought I could not do anything about it because I can not control which of these are added to this modal.

Below are screenshots of when the error was triggered and when not, without me changing any code. The first screenshot shows that *aria-hidden = true* is added, the second screenshot shows *aria-modal = true* is added to the same modal, and then there is no error.


![Error aria-hidden](docs/screenshots/aria-hidden-error.png)


![No error aria-modal](docs/screenshots/aria-modal.png)


Looking at this issue later again, I found that even sometimes when the *aria-hidden = true* is added, I do not get the error. So since the error talks about *Blocked aria-hidden on an element because its descendant retained focus. The focus must not be hidden from assistive technology*, I decided to check which button is in focus after this modal closes. It seems that no button is in focus, which may mean that the button in focus is in the closed, now hidden modal, and that is the reason for this error. So I thought I should add another *buttonGo.focus();* after this modal closes, to move focus to the **GO** button after you click **Play again**. It is not needed for **Quit** because it just goes back to the start pre-game page. 


I now added *buttonGo.focus();* at the start of the *resetGame* function. This benefits the **Restart** button as well since it uses the same function, and after you click **Restart**, it is good that **GO** is in focus so you can start right away. When I test it, the **GO** button is now in focus after you click **Play again** in the **Game over** modal, and I have not gotten the error in the console anymore. However, since this error was random from the start, I am unsure if this issue is fixed.

#### Responsiveness

I used Chrome developer tools and [Responsinator](http://www.responsinator.com/) to keep track of responsiveness, placement and size of buttons and how the content and background image behaved together on different screen sizes. 

The background image was a challenge, as it's a frame that needs to be around the content at all times. It needs to be stretched and it is not a problem that the aspect ratio is not kept in this case, because it is only a decorative curly frame which can be a bit distorted and still look good. I started with *vh100* and *vw100* which seemed ok, but then when you tilt your smartphone, the game and credit info sections overlapped the frame. So I needed some different css properties. I tried adding the background to another div above the content, but this did not work, and I tried different size values for the background, like *cover*. In the end, *background-size: 100% 100%* worked. First I had *object-fit: fill* as well, as I found these two lines together on some forum, and thought that was the one that did the trick, but I could comment it out in Chrome developer tools without any effect. So I realised it was exactly this *background-size: 100% 100%* that did what I wanted. When I look up why, it makes sense that it works since it sets the image to the full size of its parent element, the *body* in this case. And now I understand better what the different values do since I found a clear description [here](https://cloudinary.com/guides/front-end-development/6-ways-to-stretch-a-background-image-with-css). I understand now as well that *object-fit* does not work on a body tag, it only works on *replaced elements*, as I read [here](https://www.sitepoint.com/using-css-object-fit-object-position-properties/). 
After I found this solution, I just had to adjust the padding and margin for different screen sizes so the content would fit inside the decorative frame and not overlap it.

#### Different fruit looks
The fruit symbols on my newer computer with Window 11 look different than on my older computer with Windows 10. This is something I did not notice until I got a new computer, so it came as a surprise. Normally, this kind of thing depends on a browser, but this was not the case. I had to test if the background colour for a winning combination worked for both computers. I changed the background temporarely in Chrome developer tools for all the columns and think it looks OK.


Later I noticed that Firefox also has a slightly different fruit look than Chrome and Edge on my new Windows 11 computer. Firefox's symbols look a bit more three-dimensional. I tested the green winning background and it still works for them.


My Android phone and iPhone also have different fruits, but they do work with the background colours.


This is the price I am willing to pay by choosing HTML symbols instead of images. For the game functionality, it does not matter and I do think performance is more important than similar images.

#### Safari lacks font support
Unfortunately, Safari does not support *Nabla*, my chosen font for all *h1* elements. I considered creating an image for all h1 elements so that these can be the same for all browsers, but I don't like the impact that would have on performance. I also did not want to change my font, because I really like it. So I tried to find a similar one that would be supported in Safari. I found one in Google Fonts, *Passero One*. After some searching on the internet, I found a way to only target Safari with CSS [in this article](https://wojtek.im/journal/targeting-safari-with-css-media-query). While not ideal, Safari now has a different font for the logo and titles for modals and the 404 page. And the favicon now does not match the logo in Safari, but I find this an acceptable discrepancy. 

Below is a screenshot of how the logo looks in Safari, and this font is also used for the modal titles and the 404 page.

![Logo in Safari](docs/screenshots/safari-logo.png)

### Full testing

#### Browser testing

I tested on Chrome, Edge and FireFox. The layout and functionality were tested in Safari as well.

In Firefox, I get two warnings in the console about the used font using an empty gid in glyph 1 and 209: *downloadable font: glyf: empty gid 1364 used as component in glyph 1 (font-family: "Nabla" style:normal weight:400 stretch:100 src index:0) source: https://fonts.gstatic.com/s/nabla/v10/j8_D6-LI0Lvpe7Makz5UhJt9C3uqg_X_75gyGS4jAxsNIjrRBRdeFQx8.woff2*, and *downloadable font: glyf: empty gid 1649 used as component in glyph 209 (font-family: "Nabla" style:normal weight:400 stretch:100 src index:0) source: https://fonts.gstatic.com/s/nabla/v10/j8_D6-LI0Lvpe7Makz5UhJt9C3uqg_X_75gyGS4jAxsNIjrRBRdeFQx8.woff2*. While I could not figure out what glyphs these are, I found someone else getting the same kind of warning which could be ignored [here](https://github.com/arrowtype/recursive/issues/539). But this was related to a different font. I know that my font *Nabla* is not supported everywhere, but it renders OK in Firefox. When I check the console for the [Google Fonts page for Nabla](https://fonts.google.com/specimen/Nabla/glyphs), I get similar warnings including the two exact ones I got. My conclusion is that I did not do anything wrong, these are warnings related to *Nabla* only.

#### Device testing

Tested on a Dell and a Lenovo laptop, and on a Huawei phone.

This website does not have a lot of different layouts on different screen sizes, the differences I have implemented work as intended:

- From 768px width, the game section and the credit info section display next to each other. Below that, they display vertically with the credit info section under the game section. The credit info section does then not have the empty space between the text and buttons, as it does not need to be aligned with the height of the game section. 

- From 768px width, the header with the logo, intro text and **How to play** button, displays with the logo and intro text left aligned above the game section, and the button left aligned above the credit info section. Below 768px, they are centered and vertically stacked above the game section. 

- From 576px width, there is added padding left and right of the box with fruit columns, below 576px, there is no padding so that the fruits have enough space to be visible on small screens.

- On some screen sizes, the content had a tendency to overlap with the decoration in the background image, while the buttons would be distorted with too large of a padding. I have added Bootstrap classes for padding and margin to the container section for the game and credit info sections, and adapted this with media queries where necessary. Until 368px width, the padding left and right of the game and credit info sections was minimised to allow for the buttons to remain wide enough, with the padding still large enough to not overlap the decoration. Until 650px width, I added extra padding on the bottom to not overlap the decoration. I see that sometimes it still touches the decoration, but I think this is acceptable.

#### Feature testing

|Feature|Expected outcome|Testing performed|Result|Pass/Fail|
| --- | --- | --- | --- | --- |
|**How to play** button|Opens **How to play** modal|Clicked/pressed button|**How to play** modal opens|Pass|
|**How to play** modal|Can close it|Clicked/pressed the closing buttons|**How to play** modal closes|Pass|
|**GO** button|Starts the game|Clicked/pressed button when game has not started|Fruits displayed, **Spins left**, **Credit**, **Rounds played** get default values|Pass|
|**GO** button|Triggers new spin|Clicked/pressed button when game has started|New fruits displayed, **Spins left** decreases with 1|Pass|
|**GO** button|Triggers new round|Clicked/pressed button when 1 spin left|Pauses the last result 1 sec, then moves to new round where **Spins left** is 3, **Credit** decreases with 5, **Rounds played** increases with 1 |Pass|
|**HOLD** button|Holds column from getting new fruits|Clicked/pressed a **HOLD** button, then **GO**|Fruits in the column do not change, other columns change|Pass|
|**HOLD** buttons|Change colour and text when clicked/pressed|Clicked/pressed **HOLD** buttons|Text changes to **HELD**, colour to red, changes back to original when clicked/pressed again|Pass|
|**HOLD** buttons|Only possible to click/press 3 **HOLD** buttons|Clicked/pressed 2 **HOLD** buttons|Third **HOLD** button gets disabled and not possible to click/press, disabled button gets enabled when you click/press one of the **HELD** buttons|Pass|
|Winning middle row|When three identical fruits are there: 1 Change background, 2 Display winner text above columns, 3 **Credit** increases with 10, 4 Game pauses 1 second before new round|Spin until a winning row comes|Background changes to green with golden border, *WINNER!!* displays above columns, **Credit** increases with 10 and game pauses 1 second before new round|Pass|
|**Restart** button|Resets fruits and **Spins left**, **Credit**, **Rounds played** go back to default values |Click/press **Restart** button|Fruits are reset and **Spins left** is 3, **Credit** is 10, **Rounds played** is 0|Pass|
|**Quit** button|Opens **Quit game** modal|Click/press **Quit** button|**Quit game** modal opens|Pass|
|**Quit game** modal|Lets you change your mind and stay on current game, or confirm and quit the current game and go back to the window before the game has started|Click/press the **X**, **Stay** and **Quit** button|**Stay** and **X** closes the modal and lets you continue the current , **Quit** sends you back to the window before the game has started with empty fruit columns and empty values in the credit info section|Pass|
|**Game over** modal|Displays the correct number of rounds you have played, which is 1 more than currently in the background for **Rounds played**, lets you choose to play a new game or quit playing|Check the number of rounds played displayed in the modal, click/press **X**, **Play again** and **Quit** button|Displays the correct number of rounds played, **X** and **Quit** send you back to the pre-game window, **Play again** restarts the game|Pass|
|404 page|Appears when it should|Type in the URL with errors|Page appears|Pass|
|404 page **Play Fruits hold 'em** button|Links to index.html page|Click/press button (Enter key, not Space)|Sends you to index.html|Pass|
|All buttons hover effect|All buttons have a distinctive hover colour effect, except for **HELD** buttons|Hover over all buttons|Minor hover colour effect on **X** in modals, but still OK|Pass|
|All buttons focus effect|All buttons have an extra border around them when they are focused with a key, and they change colour according to the hover effect|Focus all buttons with the keyboard|All buttons have an extra border around when they are in focus, and their colour changes to their hover colour|Pass|

#### Scenario testing

|Scenario|Expected outcome|Testing performed|Result|Pass/Fail|
| --- | --- | --- | --- | --- |
|Completing the game without holding columns|**Spins left**, **Credit**, **Rounds played** are updated accordingly throughout the game|Playing the game and checking the credit info section values|**Spins left** goes from 3 to 1, **Credit** decreases with 5 at start of new round, increases with 10 when winning row, **Rounds played** increases with 1 at start if each round|Pass|
|End of game|During the last round, after the last spin, the game ends and the **Game over** modal triggers|Play through the game until **Credit** is 0, **Spins left** is 1, click/press **GO** and when there is no winning row this last spin|**Game over** modal triggers|Pass|
|Not possible to hold on winning rows|When you get a winning row, you can not hold any of the columns for the next round|Get a winning row and try to click/press **HOLD** buttons|It is not possible to click/press **HOLD** buttons an the new round starts after 1 second with reset columns|Pass|
|Not possible to click/press **GO** during pause at end of a round so **Spins left** will not go negative|**GO** button is not possible to click/press at the end of a round during the 1-second pause|Try to click/press **GO** at end of a round during the pause|It is not possible to click/press **GO** during pause at end of a round, and **Spins left** is not going negative|Pass|
|Winning row on first 'spin'|A winning row counts also when it comes after fruits are reset at start of the game or a new round, not after an actual spin|Playing until I get a winning row at the start|The winning row works as expected with the background, text, credit increase and pause before a new round|Pass|

#### Unfixed bugs

None.