const editButtons = document.getElementsByClassName("btn-edit");
const reviewRating = document.getElementById("id_rating");
const reviewTitle = document.getElementById("id_title");
const reviewText = document.getElementById("id_text");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("review_id");

    // The three fields are accessed here
    let reviewScoreText = document.getElementById(`review_rating${reviewId}`).innerText;
    console.log(reviewScoreText);
    let reviewScore = reviewScoreText.charAt(reviewScoreText.length - 1);
    console.log(reviewScore);
    reviewRating.selectedIndex = (parseInt(reviewScore) + 1);
    let reviewSubject = document.getElementById(`review_title${reviewId}`).innerText;
    reviewTitle.value = reviewSubject;
    let reviewContent = document.getElementById(`review_text${reviewId}`).innerText;
    reviewText.value = reviewContent;

    submitButton.innerText = "Update";
    reviewForm.setAttribute("action", `edit_review/${reviewId}`);
  });
}