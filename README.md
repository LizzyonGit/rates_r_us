Deploy

Go to your Heroku dashboard and create a new app.
In the Deploy tab of your new app, under Deployment method, click GitHub. 
Under Connect to GitHub, in the field next to your username on Guthub, type the repository name of the project and click Search. 
The corresponding repository name appears below, click the Connect button.


In settings, under Config Vars, add secret key and database url???


Scroll down to Manual deploy, select the main branch to deploy and click Deploy Branch.

In the top of the page, click Open app to open the app.

Fonts
I looked for a cinema feelng in my fonts and after some googleing I decided on Limelight for my larger font sizes and Merriweather for the smaller ones. Limelight is connected to theatre and filmmaking as per its description, and Merriweather was suggested in this blog post: https://wpmudev.com/blog/more-google-font-combinations-for-you-to-use/.

Colours
For my colour scheme, I want to convey a home theater feeling so I took my inspiration from articles about which colours would be good when you build a theater room. Red chairs came to mind, and otherwise dark colours for walls. And some yellow details to mimic the small spotlights on the wall. I read this article https://www.happypaintingcompany.com/blog/the-top-5-best-home-theater-paint-colors/ and https://www.peliplat.com/en/article/10002576/why-are-movie-theater-seats-mostly-red and landed on the following palette:
black, navy, red, yellow.



Issues:
displaying manytomany fields in html, fixed with all. 
manytomany field in admin when adding movie, fixed with horizonal filter

approve review when there is not text, only rating, so it is added right away and calculated in the average. So I want a conditional default value of the approved field, a simple if else statement. I had trouble finding the answer to this, but then I found https://stackoverflow.com/questions/12649659/how-to-set-a-django-model-fields-default-value-to-a-function-call-callable-e/15289517. It did not work, and I tried different places to put the code, below, above, inside the review model. But I read that the field itself cannot have if statement, so I thought it should be a callable. 

But I tried something else instead.

So I added it in the view before the review is saved to the database. Now it sets approved to True when both title and text are empty, and it displays an appropriate message and the rating is visible and calculated into the average right away. And when title and text are not empty, it needs to be approved. When I add a review with empty title and text in admin, it does not get approved right away, which I think is not a relevant issue as the superuser can just approve it.
Because of the null=True, the None got visible as a title in the frontend, so in the template, I had to add another if statement to only display the title if it is not empty

In admin when title is empty, you cannot click it to approve. So when title is empty but there is text, you cannot approve it. Do I change to title being mandatory? Could make sense. But I can also custumise admin, by setting changing the str method on the model so it represented as a link in the list display in admin, and editable. But that turned out has no effect when there is list_display. So i tried to set a title value before it's saves in the views.py, but that did not work for when you add a space in the title.
Also when you just add a space, it does not need to be approved. Very good. But then the title is not clickable in amdin, because it does not change to 'open'. I could have ofcourse added that to the condition, but I thought there should be a better way. I realised that I needed to add null=True (now it just had blank=True) to the title field (or I tested out lots of stuff at this point, https://medium.com/techtrends-digest/what-is-the-difference-between-null-true-and-blank-true-in-django-3b49be024ec5), so that I can have title as the clickable link in admin, since that is good when there is a title, and this null=True also fixed that empty titles are dspalyed as -, which is good enough since it is clickable so the superuser can edit it. 





Minor issue, after sending first rating which is approved right away, the total at the top is 0 althought the average is updated. After updating page it is fixed. Deleting a review affects both right away, so I should implement something like that with url?


Editing reviews
I found that my form fields had the same id to all 3 of my form fields, and this hinders the edit functionality because the user should be able to update all three fields, so I should be able access the fields separately. Also, it is not good html. So I needed to fix this. I thought i was because of crispy, but it was just in the template.
Editing the rating field was harder, as the selected option did not render in the form after clicking Edit. I needed to access it in a different way than usual, because it is "Rating {{review.rating}}" in the template, and in devtools it says "Rating: 4" in plain text, so how to access the 4? 

I used print statements to see what values my variables actually got, since they are different form the actual reviews that users left, and the form when you fill it in.

In this construction, the rating number is always the last character of the string, so I took help from this source https://javascript.plainenglish.io/javascript-get-last-character-of-string-4a7ac4d52bea, and fetched the number from the string that way. Then, I found selectedIndex on stackoverflow and set the selectedIndex of the rating field at the rating number plus 1, so I would get the correct value on the field, since index[1] corresponds with a rating of 0, and so forth. 

However, the rating was not changed but there was a new rating coming. I have to fix this.. Fixed now don't know what happened, maybe I was inpacient and pressed several times.
Sometimes edit does not work, submit does not change to update on reviews with only a rating. This is becaus of JS I assume, since I am collecting content that is not there. I also get an error like this in the console, that it "cannot read properties of null". So I added javascript if statements to evaluate these fields only if they are not empty in the current review. This worked. I was surprised it worked, I thought maybe then you cannot add a title and text to a current review that had none, but it still worked. I guess the rest is handled by the view and works as normal as though you would submit a new review.

Also, when you want to edit a review with title and text, and remove title and text so there is only a rating left, and you submit it, it needs to be approved. This should not happen. I need to adjust the "if review_form.is_valid() and review.author == request.user:" in the edit_review view corresponding to the code in the movie_detail view. So I added an if else statement to set approved to True if there is no title are text in the new review, and otherwise approved is set to false. I also adapted the message to the two different situations for clearer feedback to the user.


Admin
Search fields some issues creating the right code in admin.py for the search fields when they are foreignkey or manytomany. Fixed with https://docs.djangoproject.com/en/5.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields.

Security
I got a GitHub warning about gunicorn and needed to upgrade to a higher version than CIs walkthrough.


Issue that took longer time
Getting the average rating in my home screen. I had it in my movie_detail sceen and view, so I looked for a way of getting that exact value for the index.html template, without adding it to my view for the index.html. I found articles about context processors, and some other concepts, but they seemed too complicated for such an easy thing. Then I read through this post https://forum.djangoproject.com/t/aggregate-an-average-from-two-fields-from-separate-models/19705/2, and I realised I was wrong all along, I should have added my calculation of averages in the Movie model as a method, so then I can use that in all my templates based on my Movie model. So I did that, and it worked. I also read that .count can be used directly in the template instead of adding it as a variable in the view, so I did that, and on some forum someone said that rounding to two decimals is best done in the template to avoid calculation errors, so I did that with |floatformat:2.https://www.reddit.com/r/djangolearning/comments/jtvbxn/rounding_an_aggregation_to_2_decimal_places/. The good thing is now I could also easily add it to my search results list.


Design of index page
I wanted to add something so that the index is not just a list of movies. Other movie websites have several blocks with content or images and genre based rows. So to add something extra to the home page, I decided to create a feature with top picks by the superuser. The superuser can change those whenever so other movies get the spot. This would actually need a bit more background information on this website since it becomes personalised, so for now I can add this in the footer.

To only dispaly the top pics on the first page was more difficult than I thought it would be, I could not use a simple "if page does not have prev" condition, which is the same as the first page. Then I found that I could use the variable page_obj.number and used "page_obj.number == 1" as a condition to only display the top pics on the first page. But, the pagination also affected the top pics, so I needed to fix that pagination would only affect the all movies section.

I found a way to put hte logic in the view and add two different querysets to the class based view of index.html, with post from Pran Kumar Sarkar in: https://stackoverflow.com/questions/48872380/display-multiple-queryset-in-list-view
I used this to create a queryset for all published movies, and one for all published movies with top_pick selected. And by adding the [:3] it was easy to just get 3 movies. 
Now I just had to fix the pagination issue.
With the solution of two querysets for the ListView, paginate_by raised an error so I needed to check a different way to paginate. I checked similar issues on the internet and realised it has to do with me having two dictionaries in my queryset, so it does not know which queryset to paginate. Here it says I should use another method: https://stackoverflow.com/questions/60560493/django-listview-pagination-when-passing-multiple-objects-in-queryset and I also found it in the django doc that that is better to do, so I have to change it. 
After changing it and redoing the html template tags, it worked to paginate. Now, it also worked to have the condition of if page_obj.number == 1 % in my template, so the top picks only appear on the first page. The [:3] worked for this context override as well, so I kept that to only fetch 3 top picks. 

I have also decided that it makes more sense to display the top pick motivation belonging to the movie, so I added a text field to the model allowing the superuser to write a text (max 300 characters) for the top pick motivation, and if the field is not empty, display it in the index html in the top pic section. 


Only 1 review per user

I found a useful post (https://stackoverflow.com/questions/46082573/django-forms-allow-logged-in-user-to-submit-only-one-comment-per-individual-pos) about implementing this limitation and followed those steps to implement this in the view, and in the template. Then the only issue was that after you leave a review and get the confirmation message, the form is still there since the page is not updated. So I just added the same return statements as when you edit or delete a review,a nd this worked. Now after leaving a review, you see the confirmation message and the form is gone. 

But this raised a bug, when you edit a review, the form does not show. I found a suggestion here: https://stackoverflow.com/questions/792410/django-how-can-i-identify-the-calling-view-from-a-template, by Carl Meyer, to create different template blocks. However, I went with the easier solution of instead of hiding the form and raising a PermissionDenied exception, I added an error message when you try to submit a new review in the movie_detail view, and this worked. So the user should read that they can only leave 1 review per movie, as is written in the form header.

For a user who is not logged in, I got an error trying to view the movie_detail pages: "Field 'id' expected a number but got <SimpleLazyObject: <django.contrib.auth.models.AnonymousUser object at 0x00000189D24B7470>>.". I realised my page was checking the id of a user, and this caused the error for not logged in users. The page was checking this because I wanted to hide the form for when a user has left a review already. So I just needed to move my "user_reviews = movie.reviews.filter(author=request.user)" inside the "if request.method == "POST":" condition (as not logged in users cannot post anythong because they don't see the form), and remove it from the context, and the issue was fixed.


My reviews page
Creating a my revies page was not hard, and linking to the correct movie detail page from each review was in the end doable in the template, as I was struggling to fix the slug in the view, but ended up with simple for loop and if statement in the template. I wanted to link to the specific review on the movie detail page, and this was easy with the help of this forum: https://www.reddit.com/r/django/comments/fjbx0c/linking_to_an_anchor_on_another_page_in_django/. 

Populating database via API from TMDB
I wanted to add movie data from the TMDB API into my website and followed a tutorial doing something like this, but it ignored admin and the fact that I want to add the possibility for the superuser to change info and add the top pick text. I looked a lot for this issue but all solutions seemed to use the views.py file, and I felt I did not need to do it there, because my views.py works fine collecting data from the models. This post seemed promising and easy, so I decided to test it: https://stackoverflow.com/questions/32139777/populate-django-database-with-data-from-api-get-request by Shobhit Srivastava. So I decided to change back some of the changes I did following the tutorial and restore urls.py and views.py to what it was.
I halfway stopped trying populating the database as I saw too many issues arrising, like the directors not being accessible directly in TMDB. My real reason for trying to get API data is that I need movie images that I am allowed to use and not affected by copyright. So I went to look for a simple way to get thos images only and upload them manually in my admin through cloudinary. This was not easy either, but with urllib.request (https://stackoverflow.com/questions/30229231/python-save-image-from-url, Ankit Lad), I managed. With https://www.kaggle.com/code/mrinalkalitapy20/data-extraction-using-python-and-tmdb-api I found how to make simple requests, so I decided to create a new file get_api.py and run that to get the images I need. I put this file in gitignore as it is not needed anywhere and just for itnernal use to get the images. This way, I don't need to keep the API key secret because I was struggling with this (accessing the settings variable).

For movie descriptions, I found https://aifreebox.com/list/ai-movie-description-generator


Summernote editor and text color

I realised that with the default summernote rich text editor, the font colour was set in html and I could not override this. But I need the text to be white, like the other normal fields in the movie-detail view. So I looked for a way to remove the possibility of choosing a font colour in the Summernote field, and found https://github.com/lqez/django-summernote/blob/main/README.md. So I added a custom toolbar for Summernote in settings.py. I also removed the font family from the toolbar so this would also be the same as the other fields. Now, the superuser can add some styles only. I had to check the existing plot fields make sure there were no previous styles in the html code, otherwise they would still be the wrong colour.

Styling messages
Could not remove personalised message so now it is just django messages. Wanted it to be on top of content but was messing with padding etc. 

Admin
As instructions to the superusers, I would add a text about the image to be uploaded, which should be ratio... and format webp. I would also add how many characters top pick can be.


************************************************************************
# Rates 'R Us

[Live link to website](https://rates-r-us-f1ee65907d50.herokuapp.com/)

**Rates 'R Us** is a movie review website by Moby Viesca, a famous movie critic. There are movie posts and Moby's top movies have their own little section on the first page, with Moby's motivation. Each movie has its own page with more information and if applicable, Moby's review. As a user, you can register and rate or review the movies as well! Your rating counts. You can see all your reviews on the **My reviews** page.

![Screenshot webpages on different devices](docs/screenshots/amiresponsive.png)
Generated by [Am I Responsive](https://ui.dev/amiresponsive).

## Index
- [Planning](#planning)
- [Features](#features)
- [Testing](#testing)
- [Technologies used](#technologies-used)
- [Deployment and development](#deployment-and-development)
- [Credits](#credits)

## Planning

### Site goals

The website aims to offer users:
- insight in movies and Moby Viesca's take on them,
- a way to rate and review movies and contribute to the overall rating.

### User stories

See [project board](https://github.com/users/LizzyonGit/projects/5/views/1) for the agile methodology followed during this project and end result.

#### As a site admin, I can:

- create, read, update and delete movie posts so that I can manage my website,
- create a draft so that I can control when and if posts will be published on the website,
- pick out several movies to be highlighted on the website so that I can make my website more personal,
- write a motivation for my chosen top movies in admin so that I can make the website more personal,
- prevent reviews from displaying so that I have control over which reviews appear on my website.

#### As a site user, I can

- view a paginated list of movie posts so that I can quickly find the movie I want to view,
- search movies on title, director or cast member so that I can find what I'm looking for,
- open a movie post so that I can read the whole post,
- register an account so that I can rate movies and add reviews,
- review a movie so that I can share my opinion,
- rate movies so that I can contribute to the overall rating of the movie,
- edit or delete my review so that I have control on my contribution to the website,
- edit or delete my rating so that I have control on my contribution to the website.

### Design
#### Database

Below is my initial database schema. I used [Lucidchart](https://lucid.app/lucidchart/) to create it.

<details>
    <summary>Database schema</summary>This schema includes some features I did not implement, and it misses some features that I did implement. I did not implement the **Likes** model and related field in the **Review** model. The **Top pick** functionality called for an check box and field in the **Movie** model. The *average rating* is not in the database, but implemented as a model method.

  ![Database schema](docs/erd-start.png)

</details>

#### Wireframes

Below are my initial wireframes for mobile and laptop screen sizes. I used [Figma](https://www.figma.com/) to create them.

<details>
    <summary>Home, movie_detail, Register, Log in and My reviews</summary>These are my first wireframes. The final design does not differ much from the wireframes, but I did not implement a star rating, filter (but I created a search field instead), and in My reviews I did not add a filter or editing or deleting possibilities. Log out, 404 are missing.

  ![Home, movie_detail, Register, Log in, My reviews wireframes for mobile](docs/wireframes/mobile-wireframes.png)

</details>
<details>
    <summary>Home page and movie_detail/summary>I only saw the home page and movie_detail page with all the movie poster to be different on larger screen sizes, so I only created wireframes for these pages for tablet/desktop sizes. I chenged from rows with two movies to rows with three movies, as movie posters are not wide so this fits better. Then I just moved the poster to the right in the movie_detail page and the description takes a wider space under the image and short movie facts.

  ![Home page and movie_detail for desktop](docs/wireframes/desktop-wireframes.png)

</details>


#### Colour schemes

For my colour scheme, I want to convey a home theater feeling so I took my inspiration from articles about which colours would be good when you build a theater room. Red chairs came to mind, and otherwise dark colours for walls. And some yellow details to mimic the small spotlights on the wall. I read articles https://www.happypaintingcompany.com/blog/the-top-5-best-home-theater-paint-colors/ and https://www.peliplat.com/en/article/10002576/why-are-movie-theater-seats-mostly-red and landed on the following palette:
black, navy, red, yellow.

This is my palette: https://coolors.co/ffea00-000080-8b0000-000000.

#### Fonts

I looked for a cinema feeling in my fonts and after some googleing I decided on *Limelight* for my larger font sizes and logo, and *Merriweather* for the smaller ones. *Limelight* is connected to theatre and filmmaking as per its description in [Google Fonts](https://fonts.google.com/specimen/Limelight/about), and *Merriweather* was suggested in this blog post: https://wpmudev.com/blog/more-google-font-combinations-for-you-to-use/.

#### Logos and images

The logo is the website name written in font *Limelight*.

The favicon is an image of the **R** in the logo. To create the favicon files, I used [RealFaviconGenerator](https://realfavicongenerator.net/).

All movie posters come from [TMDB](https://www.themoviedb.org/), collected via API, converted to a smaller size (via Microsoft Photos) and webP format (via [tinify](https://tinypng.com)), and manually uploaded in admin to Cloudinary. 

I made the placeholder movie poster in Microsoft Paint.

## Features 

### Existing features

- __Header__

  - The header holds the logo, a motivating text, and the button **How to play**. 

 ![Header](docs/screenshots/header.png)

- __How to play modal__

  - When you click **How to play**, the corresponding modal opens with information on how to play the game. You can close this modal by clicking **Close** or **X** in the top right corner.

 ![How to play modal](docs/screenshots/how-to-play-modal.png)

- __Game section__

  The game section holds three columns, a **HOLD** button under each column, and a **GO** button at the bottom. Here is where you play the game.

     __GO button__

     - You click **GO** to start the game so the columns get filled with fruits, and from there, you just click **GO** to 'spin' the columns each time. 
  
     __HOLD buttons__

     - You can click **HOLD** to prevent the column above it from spinning. The **HOLD** button changes from green to red with the button text **HELD**, and it changes back when you click it again. When you hold two columns, the third **HOLD** button becomes disabled so you can not hold three columns. If you enable one of the two **HELD** buttons again, the disabled button gets enabled again.

     - Your chosen held columns stay held between the spins, but the buttons get reset at the start of a new round.

     - With the **HOLD** buttons, you increase your chance of winning, for example, if you get two identical fruits in a spin, you can hold them so only the third fruit needs to be correct, giving you a 20% chance of a winning middle row.
  
     __Winning row__

     - When you have a winning middle row, the background for the row changes from red to green with a golden border, and a text appears above the columns with **WINNER!!**. Regardless of how many spins you have left, the round ends with a winning row. The round's final display of fruits displays for one second, and during this time, all **HOLD** buttons and the **GO** button become disabled, until the new round starts automatically with reset fruits.

     __No winning row__

     - When you have zero spins left and no winning combination, the round ends just like when you would have a winning combination; the final spin's fruits display for one second, during which **HOLD** and **GO** buttons are disabled, and a new round starts automatically after that.
     
  ![Game section before start](docs/screenshots/game-before-start.png)

  ![Game section in play with one held column](docs/screenshots/game-in-play.png)

  ![Game section with winning row](docs/screenshots/winning-game.png)

- __Credit info section__

  The credit info section holds the following information, so the user can keep track of how the game is going at all times:

    __Spins left__
    - The spin count counts down from 3 to 0 each round. A new round gives you 3 spins. At the start of a new round, new fruits are set and count right away if you win, without needing to spin. So effectively, you get four fruit spins, but you can not control the first one.

    __Credit__
    - You start the game with 10 credit. Apart from the first round, which is effectively free, at the start of each new round, credit decreases with 5. If you get a winning row, credit increases with 10 during the 1-second pause at the end of the round. This may look like credit only increases with 5, because a new round takes 5 credit at the start. When you have two winning combinations in a row, credit increases with 10 twice, but then takes 5 at the start of a new round. If this new round does not start with a winning combination, it looks like credit increases with 15.

    - When credit is 0 after the last spin of a round, the **Game over** modal pops up. Credit can not go negative.
  
    __Rounds played__
    - The number of rounds you played starts at 0 for your first round, and increases with 1 at the start of each new round. If you never get winning combinations, you can play 3 rounds. This is because the first round is effectively free, because you start with 10 credit in the first round, and it does not decrease until the start of the next round. 

  The section holds the following buttons:

   __Restart button__
     - The **Restart** button starts a new game right away with reset fruits and the credit info default values. It works the same as the first time you click **GO**.
   
   __Quit button__
     - The **Quit** button triggers the **Quit game** modal.

  ![Credit info section](docs/screenshots/credit-info-section.png)

- __Game over modal__

   - The **Game over** modal informs you that you have no credit left for a new round. It informs you how many rounds you have managed to play. The more rounds, the luckier you have been, since everyone starts with the same credit and you can only gain credit by winning rounds. 
   
   - When you click **Play again**, a new game starts. When you click **Quit** or the **X** in the top right corner, you go back to the start page, before a game starts.
 
   ![Game over modal](docs/screenshots/game-over-modal.png)

- __Quit game modal__

   - The **Quit game** modal opens when you click the **Quit** button, and asks you to confirm if you want to quit the game. You can click **Stay** or the **X** in the top right corner, to stay on the current game. You can click **Quit** to go back to the start page, to before a game starts.
   
   ![Quit game modal](docs/screenshots/quit-game-modal.png)

- __The 404 page__

  - The 404.html page consists of a simple text saying it is not a lucky page, and a **Play Fruits hold 'em** button that links to the home page.
  
  ![404 not found](docs/screenshots/404.png)

  Project file: 404.html

### Features left to implement

- Sound toggle with different sounds depending on a win or not.
- More exciting graphics when you have a winning row, like flashing effects.
- Different credit values for different fruits.
- Different winning lines.
- Spinning wheel effect in each spin before the fruits are settled.
- Social media links or links to an external website of the game makers.
- Shiny effects and bling overall in the game.

## Testing 

See [TESTING.md](TESTING.md).

## Technologies used

### Languages

- HTML
- CSS
- JavaScript

### Frameworks - libraries - programs used

- [Bootstrap](https://getbootstrap.com/) version 5.3
- [Figma](https://www.figma.com/) for wireframes
- Chrome DevTools for verifying responsibility and troubleshooting code
- [CodePen](https://codepen.io/pen/) for troubleshooting code
- [Gitpod](https://www.gitpod.io/) for coding
- [GitHub](https://github.com/) for version control and hosting
- [Google Fonts](https://fonts.google.com/) for my font pair
- [Canva](https://www.canva.com/) for background image
- Windows Paint for the cropping background image
- [TinyPNG](https://tinypng.com/) for compressing image size and converting to .webp
- Windows snipping tool for the favicon
- [RealFaviconGenerator](https://realfavicongenerator.net/) for creating favicon icons and the HTML code, and checking the favicon
- [Responsinator](http://www.responsinator.com/) for checking responsiveness
- [Autoprefixer](https://autoprefixer.github.io/) for adding the necessary prefixes to my CSS stylesheet
- [Am I Responsive](https://ui.dev/amiresponsive) for an image displaying the website on different screens

## Deployment and development

### Deployment
The site was deployed to GitHub pages. The steps to deploy are: 
  1. In the GitHub repository, navigate to the **Settings** tab,
  2. In the left menu, select **Pages**,
  3. Under **Source**, select **Deploy from a branch**,
  4. Under **Branch**, select **main**,
  5. Click **Save**, 
  6. In the GitHub repository, in the right menu, click **Deployments** to view the link to the deployed website.

The live link can be found here - https://lizzyongit.github.io/fruits-hold-em/index.html.

### Local development
To fork the repository:
  - In the GitHub repository, click the **Fork** button in the top right corner.

To clone the repository:
  1. In the GitHub repository, click the **Code** button.
  2. In the **Local** tab, select if you want to clone with HTTPS, SSH, or GitHub CLI, and copy the link below it.
  3. Open the terminal in your code editor and change the current working directory to the location you want to clone this repository to.
  4. Type *git clone* and paste the link from step 2, and press Enter.

## Credits 

### Content 

- All content is written by me.

### Media

- The original background image is on Canva, by 'hielmannuraddin's Team', called [Black and Gold Classic Background A4 Document](https://www.canva.com/sv_se/mallar/EAGICesfS6E-black-and-gold-classic-background-a4-document/). I edited this image in Canva.

### Resources

__Planning__
- For a font pairing idea, [this article](https://www.creatopy.com/blog/google-font-pairings/#21).
- To decide on which colours to use, I have researched several websites:
  - https://www.newwavemagazine.com/single-post/the-psychology-of-color-in-casinos-how-design-choices-influence-the-player-s-mood
  - https://colorfulconsole.com/the-art-of-slot-machine-design-using-colors-to-enhance-gameplay/ 
  - https://www.globalbrandsmagazine.com/color-schemes-popular-among-online-gambling-brands/ 
  - https://fashionisers.com/2020/06/22/color-psychology-in-online-casino-games-design/ 
  - https://hickmandesign.co.uk/blog/other/psychology-of-casino-game-design/?srsltid=AfmBOoqN_NQjVzYCdMEXdxkKP7hirVuOcc1yR1pRNuj2DlTwndNwtmi- 
  - https://www.globalbrandsmagazine.com/casino-colors-psychology-lucky-gambling-colors/
  - https://www.myperfectcolor.com/paint/101581-true-value-3496-casino-green#:~:text=The%20RGB%20values%20for%20True,light%20that%20a%20color%20reflects
- For getting a colour scheme and checking the color contrast, [Coolors.co](https://coolors.co).

__During development and testing__
- Bootstrap documentation [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/).
- [W3schools](https://www.w3schools.com/) for getting the fruit icons and reading up on concepts.
- [MDN Web Docs](https://developer.mozilla.org/en-US/) to read up on concepts.
- [Stackoverflow](https://stackoverflow.com/) for general code questions.
- Inspiration and code bits from CI walkthrough project *Simon says*.
- How to redirect to another page with JavaScript: [tutorialspoint](https://www.tutorialspoint.com/how-to-redirect-to-another-webpage-using-javascript).
- How to open a Bootstrap modal with JavaScript: [Stackoverflow](https://stackoverflow.com/questions/62101647/.javascript-bootstrap-open-bootstrap-modal-with-javascript-and-not-with-button).
- To set focus on an element: [Laracasts](https://laracasts.com/index.php/discuss/channels/vue/how-to-focus-on-an-input-after-disabling).
- Troubleshoot *aria-hidden* error: 
 - https://github.com/WordPress/gutenberg/issues/56547, 
 - https://github.com/twbs/bootstrap/issues/41005, 
 - https://stackoverflow.com/questions/62677291/aria-hidden-elements-do-not-contain-focusable-elements-issue-when-modal-is-sho.
- Troubleshoot missing *focus-outline* on buttons: https://github.com/twbs/bootstrap/issues/38903.
- To understand background-size setting: [Cloudinary](https://cloudinary.com/guides/front-end-development/6-ways-to-stretch-a-background-image-with-css).
- Slack post on a console error I got as well: https://code-institute-room.slack.com/archives/D07L9QW7YS3/p1738070720220649.
- How to target Safari with CSS: [Wojtek Witkowski](https://wojtek.im/journal/targeting-safari-with-css-media-query). 

__Project finalisation__ 
- [Grammarly](https://www.grammarly.com/grammar-check) spellchecker.
- [Diffchecker](https://www.diffchecker.com/text-compare/) for checking Autoprefixer changes.
- Other students' readme files for learning about local development processes.

### Acknowledgments
- My mentor Jubril for the feedback.
- My cohort facilitator Kay for the pep talks.