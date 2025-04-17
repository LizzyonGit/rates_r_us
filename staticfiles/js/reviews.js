const editButtons = document.getElementsByClassName("btn-edit");
const reviewRating = document.getElementById("id_rating");
const reviewTitle = document.getElementById("id_title");
const reviewText = document.getElementById("id_text");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

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
    // Last character of string which is always the rating number
    let reviewScore = reviewScoreText.charAt(reviewScoreText.length - 1);
    // Sets the selected option at the index of rating number +1, so the value is correct, bacuse index[0] = ----
    reviewRating.selectedIndex = (parseInt(reviewScore) + 1);

    // The following code collects and prepopulates title and text if they are not empty.

    let titleField = document.getElementById(`review_title${reviewId}`);

    if (titleField) {
        let reviewSubject = titleField.innerText;
        reviewTitle.value = reviewSubject;
    }

    let textField = document.getElementById(`review_text${reviewId}`);
    if (textField){
        let reviewContent = textField.innerText;
        reviewText.value = reviewContent;
    } 

    submitButton.innerText = "Update";
    reviewForm.setAttribute("action", `edit_review/${reviewId}`);
  });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated review's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific review.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let reviewId = e.target.getAttribute("review_id");
      deleteConfirm.href = `delete_review/${reviewId}`;
      deleteModal.show();
    });
  }