const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_content");
/** The id_content ID isn't in the template. Instead, the browser automatically generates it from {{ comment_form | crispy }}. Using the Model as refernce for the generated name, you can 
 * view this inside developer tools, In a nutshell this tells the PC to look for the empty comment textbox made with crispy */
const commentForm = document.getElementById("commentForm");
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
  button.addEventListener("click", (e) => { /** listens for a click event and assigns the button to variable "e" */
    let commentId = e.target.getAttribute("comment_id"); /** collects comment_id e.g. "2" */
    let commentContent = document.getElementById(`comment${commentId}`).innerText;/** appends the collected id e.g "2" too "comment2" */
    commentText.value = commentContent; /** fills the empty form textbox with the desired comment to edit */
    submitButton.innerText = "Update"; /** changes the normal "submit" button to "update" for good UX design */
    commentForm.setAttribute("action", `edit_comment/${commentId}`); /** basically parses the new edited comment to the python view function "comment_edit", more below */
  });
}
/** The JavaScript code also modifies the comment form's action attribute to ensure it knows which comment it is updating when you click the Edit button:
commentForm.setAttribute("action", `edit_comment/${commentId}`);

Here, the code constructs the appropriate action URL for the comment being edited. When the form is submitted,
this updated URL directs Django to the comment in the database that needs updating.

Note: An action value on a form appends onto the current URL. As the user is viewing the specific blog post, this post's <slug:slug>/ is
already part of the URL and only edit_comment/<int:comment_id> is needed to complete the URL path with the action attribute. For example:

form action = "edit_comment/7"> // returns http://urladdress.com/<slug:slug>/edit_comment/7

How does this Javascript and Python work together?

Information Flow to comment_edit view.py function

User Interaction: The user clicks an edit button next to a comment.
JavaScript Handling: The JavaScript code retrieves the comment content and prepares the form for editing. It sets the form action to edit_comment/${commentId}.
Form Submission: The user edits the comment and submits the form. The form action URL (edit_comment/${commentId}) is used to send the request to the Django view.
Django View Processing: The Django view function processes the form submission, validates the data, and updates the comment in the database.
Feedback and Redirect: The user receives feedback (success or error message) and is redirected to the post detail page.

In summary:

JavaScript: Prepares the form for editing by populating it with the existing comment content and updating the form action.
Django View: Processes the form submission, validates the data, updates the comment, and provides feedback to the user.


*/

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("comment_id");
      deleteConfirm.href = `delete_comment/${commentId}`;
      deleteModal.show();
    });
  }
/** This code ensures that the delete link on the modal's confirmation button is updated with the right comment ID. Therefore, when the user confirms the deletion,
 *  Django receives the correct URL and knows which comment to remove from the database. */