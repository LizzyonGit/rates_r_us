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

For the my_reviews html, it did not work to chack the URL in the validator, but the source code gave no errors.

The signup page does give errors in the validator, but they are of the actual form that is used there "form.as_p". I cannot access the form to fix the code. 

Below are the direct links to the validator's result per page (for those that accepted URL input): 
 -  [Home page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frates-r-us-f1ee65907d50.herokuapp.com%2F)
 -  [movie_detail.html(Interstellar example)](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frates-r-us-f1ee65907d50.herokuapp.com%2Finterstellar-2014-11-07%2F)
 -  [Log in page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frates-r-us-f1ee65907d50.herokuapp.com%2Faccounts%2Flogin%2F)
 -  [Search page (no result)](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frates-r-us-f1ee65907d50.herokuapp.com%2Fsearch%2F%3Fq%3Dhello)
 -  [Search page with result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frates-r-us-f1ee65907d50.herokuapp.com%2Fsearch%2F%3Fq%3Dbullock)
 -  [Log out page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frates-r-us-f1ee65907d50.herokuapp.com%2Faccounts%2Flogout%2F)


### CSS validator

For style.css, there are no errors in the [Jigsaw validator](https://jigsaw.w3.org/css-validator/). There are some warnings related to the imported Google Fonts and used variables, that can be ignored. Because I ran my code through the [Autoprefixer](https://autoprefixer.github.io/), I also get warnings about this, which can be ignored.

 ![Css warnings](docs/screenshots/css-validator.png)

### Python validator

Firstly, I need to shorten my lines and fix the incorrect white spaces, as I have ignored these problems completely. So before running my code through the [CI Python Linter](https://pep8ci.herokuapp.com/), I will fix this in VS code with help of the PROBLEMS tab. I leave only the url links in my comments too long, as I found this is ok. The Python linter only reports these long url links. The reason I don't want to shorten them, is because the links are descriptive so it's more read-friendly in my opinion to keep the original urls (I checked [stackoverflow](https://stackoverflow.com/questions/10739843/how-should-i-format-a-long-url-in-a-python-comment-and-still-be-pep8-compliant) for this.

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

#### Detail pages

For the detail page, I get from 90 % to 99 % performance, as it only has one image. The image size on the page is smaller than the size in cloudinary because it is smaller than the largest size on the home page, so I do get an issue for that, but I will not use separate images for the home and detail page. Otherwise, I get the same kind of issues as for the home page. The scores differ a little depending on the movie, because of the different content. Movies with longer titles score lower as they have larger layout shifts. Running lighthouse at different times does affect the scrore as well, I have gotten 100 % as well as 87 % at different times.

I get a warning on best practices saying I use a deprecated API "H1UserAgentFontSizeInSection". I googled this error and found [documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#specifying_a_uniform_font_size_for_h1) implying it has to do with h1 inside an article element and that the size should be specified. I tried this by adding class="h2" to my h1. But like someone mentions [here](https://github.com/GoogleChrome/lighthouse/issues/16404), this did not fix it, so then I added a piece of code 
":where(h1) {
  margin-block: 0.67em;
  font-size: 2em;
}" because someone says this should fix it, but this still did not work. I removed the code again. I decide to leave it now. I tested to remove <article> and this actually gave me 100 %. But <article> is there for semantic information, so I want to use it. So instead I used a hidden h1 above article and changed my original h1 to h2 inside the article element. This finally worked and I have 100% on best practices.

For accessibility, I got a lower score because my Log in and register links only rely on colour, so I added underline to this. Now I get 100%.

![Lighthouse result desktop](docs/screenshots/lighthouse-index-desktop-incognito.png)

For mobiles, the performance is 88% with a warning that the h1 element, the title, is the element that takes the longest to load. I really like the font for the title and I think the size is perfect, so I would not want to change it. When I run Lighthouse again for mobiles in incognito mode, the performance is 98% with the same issues as for desktops. So then there is no mention of the title taking too long to load. 

![Lighthouse result mobile](docs/screenshots/lighthouse-index-mobile-incognito.png)

#### My reviews page

 My reviews gives an issue for accessibility about my links not having discernible text. Looking better at the page with devtools, I saw the links were placed weirdly and there were a lot of empty links. The HTML validator had not seen this. I fixed the link tag to be inside the innerloop of {% if movie == review.movie %}, and added an aria-label as well. Now, the links look like they should. Rerunning Lighthouse, I get 100% for accessibility.


#### Log in, log out, register, 404

The first Lighthouse report gives 99% on performance and 100% on accessibility and best practices.

Any issues it mentions are the same as for index.html. In incognito, it gives 100% for performance.

![Lighthouse result desktop](docs/screenshots/lighthouse-404-desktop-incognito.png)

For mobile, it gives 98% for performance, and apart from the same issues as before caused by Bootstrap, Google Fonts and cache policy, it finds an issue with the used font for the h1 element because of a large layout shift. But the score of 98% is good so I am keeping this as it is. However, running it in incognito mode, first I had 88%, but when I tried it again, it got to 98% as well, with those same issues as before.

![Lighthouse result mobile](docs/screenshots/lighthouse-404-mobile-incognito.png)

### Favicon testing
I ran https://lizzyongit.github.io/fruits-hold-em/ through Realfavicongenerator's [favicon checker](https://realfavicongenerator.net/favicon-checker/lizzyongit.github.io%2Ffruits-hold-em%2F), and I only got a warning about a missing title for web apps, which actually would be taken from the website's title if this would be applicable, which it is not because the website is not an app. There is a missing web app manifest which is also not applicable.

## Manual testing

### User story testing

|   User story                                                            | How it is achieved    |
|  -----------                                                             | -----------           |
|**As a gamer, I want to:**|
|easily navigate on the game page on any device, so that I get a user-friendly experience,|Responsive layout, favicon, possible to play with keys as well as mouse, only a few buttons that you need to click|
|find information on how the game works, so that I can play the game,|**How to play** button which you can click to trigger modal with information on how the game works.|
|be able to play the game,|**GO** button that you use both to start the game and spin the fruits, the game is playable with keys as well as with a mouse and not colour-dependent as held **HOLD** buttons change text as well as colour.|
|have the possibilty to hold certain fruits, so that I can increase the chance of winning,|**HOLD** button under each column which you can click to hold a fruit.|
|keep track of how many spins I have left, so that I can adapt my tactic,|**Spins left** in the credit info section, which counts down from 3 to 0.|
|keep track of my credit, so that I can follow my progress,|**Credit** in the credit info section, which increases with 10 for each win, and decreases with 5 at the start of each new round|
|keep track of how many rounds I have played, so that I can follow my progress or decide if I should stop or continue,|**Rounds played** in the credit info section, which increases with 1 at the start of each new round, and the **Game over** modal which pops up after the last round you played if you have no credit left, with the final number of rounds you played.|
|be able to quit or restart the game, so that I have control over the game without needing to leave the website.|**Restart** and **Quit** buttons in the credit info section, the **Quit game** modal triggered by the **Quit** button, with buttons to confirm if you want to quit, or if you change your mind you can stay on the current game, and the **Game over** modal after last round, with a button to restart and a button to quit the game.|
|**As a site owner, I want to offer visitors a:**|
|fun and addictive, user-friendly game, so that I can get a steady user base and gain traffic to my website.|Responsive layout, favicon, the game is easy and fast to play with not too many clicks, and the game is playable with keys as well as with a mouse.|

### Issues

Here I want to highligt some issues and bugs that were not straightforward to fix.

#### Logic

As I started out writing the logic with increasing and decreasing credit, increasing game count, decreasing spins, I stumbled on some minor issues like displaying the correct credit information. I started out calculating with the string value from the UI, which caused problems with additions since the number would just concatenate at the end of the other number, instead of adding up. I thought about converting the string value to a number, which caused an error in the console. So I realised I needed to first calculate and then display it in the UI, like in CIs walkthrough project *Simon says*. I copied the way the *showScore* function works in that project, making the calculations first and then calling the function *showCreditInfo* to show the outcome each time.


The **GO** button was working in a way that the **Spins left** would decrease with 1 each time you click, but this was not good for when you start the game by clicking **GO** when there are no fruits yet, because then you would start out with only two spins left, instead of three. As I believe it is most user-friendly to enable the **GO** button as a way to start the game, even if the **Restart** button also starts a new game, I did not want to disable it in the start and force users to use the other button. So I rewrote my code so that, when there are no fruits and the game has not started yet, the **GO** button calls the same function as the **Restart** button, and when there are fruits, it runs the original code with the decreasing spin count. So to start the game, you can click either button, and during the game when you start over, you click **Restart**.


Initially, when the spin count was 1 and you would click **GO**, or when a winning combination would come up, a new round started right away; the spin count went to 3 directly with the new credit and games played count. So I wanted to display this final spin's result, even though you should not be able to do anything since you would have 0 spins left, or the round ended by a winning combination. Inspired by CI's example *Simon says*, I added a *setTimeout* method to display this final result for the user, before starting the new round. During this timeout, you can not click **HOLD** or **GO**, and it will automatically start a new round, you do not have to click anything. This way it also clear how the counting works, as the in-between step is not missing, and you can for example see that you gain 10 credit with a winning combination, but you lose 5 at the start of the new round. 


After implementing the hold functionality and testing it, I noticed that I needed to change my code for determining the winning combination, as I got winning combinations when the 3 fruits in the middle row were not the same. My code for determining the winning combination looked at the fruits stored in the array at the three indexes used for the middle row, not the fruits actually on the screen in the middle row. My hold functionality updates the array from which the fruits are picked each spin, but it simply does not pick the fruit for held columns. This means that the array stores new fruits every time you spin, while the screen can hold certain columns to keep the same fruits. This discrepancy was easy to fix by making the winning combination function check what is on the screen instead of the array. I am aware that it is not an ideal solution, it would be better to not change certain array indexes at all if a column is held, so the computer does not need to choose random fruits when it is not needed. It would clean up the code, and in a larger application, it would benefit the performance to not run unnecessary code.

#### Accessibility

The game uses a lot of colours to check the contrast of. The Chrome developer tools show the contrast which prompted me to change some button text colours. 


I also had to change my colour background for a winning combination from gold to green, since gold did not work with a winning combination of lemons. I wanted to keep the lemons, so I changed the background to work together with all fruits. I tested this by just adding it to all the columns first, so I could see it with all the fruits after a few spins. I added a gold border for the background since gold does convey that winning feeling. 


I focused a lot on using this game with the keyboard. I think clicking **GO** all the time is not user-friendly, it is easier to press Enter or Space. I found this myself when I was testing the game. I did not have to do anything to get Space and Enter to work for clicking the button. But I did encounter other problems.

##### Disabled buttons

For the game flow, some buttons are disabled in some situations. You can not hold three columns, so when two **HOLD** buttons are clicked, the third HOLD button becomes disabled. But I noticed you could still press the key on it to hold it. Also, after a round with three spins or a winning combination, the game pauses a short time to see the result before starting a new round with three spins. During this time, all **HOLD** buttons and the **GO** button are disabled. But I noticed you could still press the Space or Enter key on the **GO** button, which caused the spins to go negative during this short time. So I needed to find a way to prevent this from happening, as you should not be able to do anything with disabled buttons.

I spent some time finding a solution for this, as I looked specifically for a way to prevent the default behaviour of Enter and Space for disabled buttons. I added a function with the *preventDefault()* method which worked for before the game starts, when there are no fruits and the **HOLD** buttons are disabled, to prevent holding empty columns. But the function prevented normal key behaviour also for not disabled **HOLD** buttons, and it did not work when the **GO** button was disabled. I also tried the function with the *blur()* method that I found, but this did not work as it should either. So I thought I should call the function in each of the rounds and specifically for each button, which seemed to get complicated. I thought it should be easier. I thought that maybe I should give the specific bootstrap *disabled* class this particular function I made, rather than the button itself, but that didn't get me anywhere when I googled for it. 

Then I googled for Bootstrap classes and what to do to prevent key events on disabled buttons. In the Bootstrap documentation, I went to the root of the problem by looking into how to change the disabled class in Bootstrap, then I found the confirmation that the *disabled* class does not prevent key events [here](https://getbootstrap.com/docs/5.3/forms/overview/#disabled-forms), only pointer-events. It says you need to add *tabindex -1* to prevent focus. So it turns out it is better to add the *disabled* attribute instead of the class because the attribute already prevents focus. When I was creating these disabled buttons initially, I went for the *disabled* class because it seemed easier, and I remembered the exact Javascript code for accessing them. I did not think of this crucial difference for key events. So I freshened up my memory about working with attributes instead of classes, and rewrote the code. Attributes are mentioned in the LMS, but I used external sources for more code like *toggleAttribute* from [here](https://developer.mozilla.org/en-US/docs/Web/API/Element/toggleAttribute). It was fairly easy to change this and I did not need any more functions to make it work like it should.

##### Focused buttons

When I was testing the keys with the different buttons, I noticed a difference between hovering with a mouse and focusing with a key. I had added some *:hover* pseudo-classes in my CSS, but not any *:focus* pseudo-classes. I added this to imitate the hovered effect, and while I read more about *:focus*, I found out about *:focus-visible* [here](https://developer.mozilla.org/en-US/docs/Web/CSS/:focus-visible) and how this can be more user-friendly. This was applicable for my *Quit* and *Restart* buttons, since when you focused on it and then clicked with the mouse, after moving the mouse, the focus background colour was still there, which was very unnecessary. Using *:focus-visible*, this background colour is removed when you move the mouse away.

I also noticed that all buttons had a border around them when focused, making it clear which button you are on since they appear larger, together with the different background colour of the button. Except for the button **How to play**, which only changed colour and did not have this extra border around it. I could not find out why this was, as it was a Bootstrap button like the others, with custom styled colours. I found [a post](https://github.com/twbs/bootstrap/issues/38903) that this can happen, so I decided to focus on just adding it in my CSS for the button. I learned about *outline* and found that in Chrome developer tools, I can force a button in a certain state. So I did that for the buttons that worked normally, to find out which code I needed to add for the button that did not work. That's how I added *outline: 0*, and *box-shadow: 0 0 0 0.25rem* with a yellow colour, to the **How to play** button, and now it works.

After I implemented the **Game over** modal, I noticed that the **GO** button loses focus after it's re-enabled at the beginning of a new round. This is bad when you play with the keys and you expect the focus to still be on the **GO** button since you would have always clicked it at the end of the previous round. It did not even have any visible focus anywhere else, but it did not respond to a Space or Enter. I thought this had to do with my new modal and I also got an error about *aria-hidden* in the console (more about this in the next paragraph). I found an easy way to fix the focus issue by just adding *buttonGo.focus();* after the line where the button is enabled again in the *gameDone* function. I found this solution here: https://laracasts.com/index.php/discuss/channels/vue/how-to-focus-on-an-input-after-disabling, and I double-checked other documentation for this method.

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