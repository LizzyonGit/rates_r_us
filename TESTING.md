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

Along the way, I did get an issue where after adding only a rating, the average would be updated but the number of ratings in brackets would not be updated. This would be corrected after refreshing the page. This was eventually fixed and I am not sure at what point, probably after approving ratings directly in the view.

##### Edit reviews

I found that all 3 of my review form fields had the same id, and this hindered the edit functionality because the user should be able to update all three fields, so I should be able to access the fields separately. Also, it is not good HTML to have similar ids of course. So I needed to fix this. I thought it was because of crispy, but it turned out it was simply in the template.

Editing the rating field was harder, because after clicking **Edit**, the original rating did not render in the form to update the review. I used print statements to see what values my variables actually got. I needed to access the rating value in a different way than usual, because it said *Rating {{review.rating}}* in the template, and in Devtools it said *Rating: 4* in plain text, so the question was how to access the 4? In this construction, the rating number is always the last character of the string, so I took help from https://javascript.plainenglish.io/javascript-get-last-character-of-string-4a7ac4d52bea, and fetched the number from the string that way. Then, I found *selectedIndex* on stackoverflow and set the *selectedIndex* of the rating field at the rating number plus 1, so I would get the correct value on the field, since index[1] corresponds with a rating of 0, and so forth. 

Sometimes editing did not work, the **Submit** button did not change to **Update** on reviews with only a rating. This was because of the javascript code, since I am collecting content (review title and text) that is not there. I also got an error like this in the console, that it "cannot read properties of null". So I added javascript if statements to evaluate these fields only if they are not empty in the current review. This worked. I was surprised it worked, I thought maybe then you can not add a title and text to a current review that had none, but it still worked. I guess the rest is handled by the view and works as normal as though you would submit a new review.

Another issue, when you wanted to edit a review with a title and text, and would remove the title and text so there is only a rating left, and you updated it, it needed to be approved again. This should not happen as reviews with only a rating do not need approval. I needed to adjust the *if review_form.is_valid() and review.author == request.user:* in the edit_review view corresponding to the code in the movie_detail view. So I added an if else statement to set approved to True if there is no title and text in the new review, and otherwise approved is set to False. I also adapted the message to the two different situations for clearer feedback to the user.

##### Display average rating

Getting the average movie rating on my home page for each listed movie was not straightforward. I had it displayed in the movie_detail page and view, so I looked for a way of getting that exact value for the index.html template, without adding it to my view for the index.html. I found articles about context processors, and some other concepts, but they seemed too complicated for such an easy thing. Then I read through https://forum.djangoproject.com/t/aggregate-an-average-from-two-fields-from-separate-models/19705/2, and I realised I was wrong all along, I should have added my calculation of averages in the **Movie** model as a method, so then I could use that in all my templates based on the **Movie** model. So I did that, and it worked. 

I also read that *.count* can be used directly in the template instead of adding it as a variable in the view, so I did that, and on some forum (https://www.reddit.com/r/djangolearning/comments/jtvbxn/rounding_an_aggregation_to_2_decimal_places/) someone said that rounding to two decimals is best done in the template to avoid calculation errors, so I did that with *|floatformat:2*. The good thing is that now I could also easily add it to my search results list and page.

##### One review per movie per user

I found a useful post (https://stackoverflow.com/questions/46082573/django-forms-allow-logged-in-user-to-submit-only-one-comment-per-individual-pos) about implementing this limitation and followed those steps to implement this in the view, and in the template. Then the only issue was that after you leave a review and get the confirmation message, the form is still there since the page is not updated. So I just added the same return statements as when you edit or delete a review, and this worked. Now, after giving a review, you see the confirmation message and the form is gone.

But this raised a bug, when you edit a review, the form does not show because it is set to not be visible when there is already a review by the user. I found a suggestion here: https://stackoverflow.com/questions/792410/django-how-can-i-identify-the-calling-view-from-a-template, by Carl Meyer, to create different template blocks. However, I went with the easier solution of instead of hiding the form and raising a *PermissionDenied* exception, I added an error message when you try to submit a new review in the movie_detail view, and this worked. So the user should read that they can only give 1 review per movie, as is written in the form header.

For a user who is not logged in, I got an error trying to view the movie_detail pages: *Field 'id' expected a number but got <SimpleLazyObject: <django.contrib.auth.models.AnonymousUser object at 0x00000189D24B7470>>.*. I realised my page was checking the id of a user, and this caused the error for not logged in users. The page was checking this because I wanted to hide the form for when a user has left a review already. So I just needed to move my "user_reviews = movie.reviews.filter(author=request.user)" inside the "if request.method == "POST":" condition (as not logged in users cannot post anything because they don't see the form), and remove it from the context, and the issue was fixed.

##### My reviews page

Creating a **My reviews** page was not hard, and linking to the correct movie detail page from each review was in the end doable in the template, as I was struggling to fix the slug in the view, but ended up with a simple for loop and if statement in the template. I wanted to link to the specific review on the movie detail page, and this was easy with the help of this forum: https://www.reddit.com/r/django/comments/fjbx0c/linking_to_an_anchor_on_another_page_in_django/.

#### Populate the database via TMDB API

I wanted to add movie data from the TMDB API into my website and followed a tutorial doing something like this, but it ignored admin and the fact that I want to add the possibility for the superuser to change info and add the top pick text. I looked a lot for this issue but all solutions seemed to use the views.py file, and I felt I did not need to do it there, because my views.py works fine collecting data from the models. This post seemed promising and easy, so I decided to test it: https://stackoverflow.com/questions/32139777/populate-django-database-with-data-from-api-get-request by Shobhit Srivastava. So I decided to change back some of the changes I did following the tutorial and restore urls.py and views.py to what it was. I halfway stopped trying populating the database as I saw too many issues arrising, like the directors not being accessible directly in TMDB. 

My real reason for trying to get API data is that I needed movie images that I am allowed to use and that are not affected by copyright. So I went to look for a simple way to get those images only and upload them manually in my admin through Cloudinary. This was not easy either, but with *urllib.request* (https://stackoverflow.com/questions/30229231/python-save-image-from-url, Ankit Lad), I managed. With https://www.kaggle.com/code/mrinalkalitapy20/data-extraction-using-python-and-tmdb-api I found how to make simple requests, so I decided to create a new file get_api.py and run that to get the images I need. I put this file in gitignore as it is not needed anywhere and just for internal use to get the images. This way, I did not need to keep the API key a secret since the whole file would be secret, since I was struggling with accessing the settings variable somehow.

#### Index page design

I wanted to add something so that the index page is not just a list of movies. Other movie websites have several blocks with content or images and genre based rows. So to add something extra to the home page, I decided to create a feature with top picks by the superuser to display on the home page. The superuser is supposedly a famous movie critic Moby Viesca (or his workers pretend to be him). The superuser can change the top picks whenever so other movies get the spot. This extra feature actually called for a bit more background information on the website since it becomes personalised, so I added the movie critic's name in the footer.

To only display the top picks on the first page was more difficult than I thought it would be, it did not work to use a simple *if page does not have prev* condition, which effectively is the same as the first page. Then I found that I could use the variable *page_obj.number* and used *page_obj.number == 1* as a condition to only display the top picks on the first page. 

But, the pagination also affected the top picks, so I needed to fix that pagination would only affect the all movies section.

I found a way to put the logic in the view and add two different querysets to the class based view of index.html, with help from a post from Pran Kumar Sarkar (https://stackoverflow.com/questions/48872380/display-multiple-queryset-in-list-view). I used this to create a queryset for all published movies, and one for all published movies with top_pick selected. And by adding the [:3] it was easy to just get 3 movies. 

Now I just had to fix the pagination issue. With the solution of two querysets for the ListView, *paginate_by* raised an error so I needed to check a different way to paginate. I checked similar issues on the internet and realised it has to do with me having two dictionaries in my queryset, so it does not know which queryset to paginate. Here it says I should use another method: https://stackoverflow.com/questions/60560493/django-listview-pagination-when-passing-multiple-objects-in-queryset, and I also found it in the django docs that that is better to do, so I had to change it. 

After changing it and redoing the html template tags, it worked to paginate. Now, it also worked to have the condition of if page_obj.number == 1 % in my template, so the top picks only appear on the first page. The [:3] worked for this context override as well, so I kept that to only fetch 3 top picks. 

I have also decided that it makes more sense to display some sort of top pick motivation for the movie, so I added a text field to the model allowing the superuser to write a text (max 300 characters) for the top pick motivation, and if the field is not empty, display it in the index html in the top pic section (as well as in the movie detail view).

#### Summernote editor and text colour

I realised that with the default Summernote rich text editor, the font colour was set in html and I could not override this. But I needed the text to be white, like the other normal fields in the movie_detail view. So I looked for a way to remove the possibility of choosing a font colour in the Summernote field, and found https://github.com/lqez/django-summernote/blob/main/README.md. So I added a custom toolbar for Summernote in settings.py. I also removed the font family from the toolbar so this would also be the same as the other fields. Now, the superuser can add some styles only. I had to check all the existing plot fields and make sure there were no previous styles in the html code, otherwise they would still be the wrong colour.

#### Messages

First, I had a personal welcome message that stayed on the screen, and I could not find an easy way to remove it, as it would come back with each new page load. So now, I only use django messages. They can be removed with the cross.

#### Security

I got a GitHub warning about gunicorn and needed to upgrade to a higher version than CIs walkthrough. So I installed gunicorn again and adjusted the requirements.txt. I needed to ask a question on slack how to do this.




#### Responsiveness

I used Chrome developer tools along the way to fix responsiveness with media queries and bpptstrap classes. Finally, I used [Responsinator](http://www.responsinator.com/) to check responsiveness, after installing *Ignore X-Frame headers*.

I noticed I needed extra padding on the home page from the second page, because the **Top pic** section is not there and when the navbar is wider on small screens, it overlaps a bit.

For the **Register** and **Log in** pages, there was need for margin below the form button. Even if I could not log in, I assumed the same would be true for the **Log out** page. I simply changed *mt-3* to *my-3*.

In the reviews, there was need for a space between the username and date.


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

*Remember Me* on **Log in** page. I do not like the capital M in *Me*, and would fix it if it was easy. But I have to override the whole form if I do this, and feel that is not a priority. So I decided to leave it.