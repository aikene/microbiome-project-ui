document.addEventListener('DOMContentLoaded', function() {

    if (document.getElementById("show-history").innerHTML === "1") {
        // Show the Search History page
        document.getElementById("tab1").checked = false;
        document.getElementById("tab2").checked = true;
    }

    document.getElementById("email-notification-checkbox").addEventListener('change', function() {
        setEmailNotification(this.checked);
    })

    // Add event listener to all delete buttons
    document.querySelectorAll('.delete-btn').forEach(deleteBtn => {
        deleteBtn.addEventListener('click', function() {
            const runID = deleteBtn.dataset.id;
            const confirmBtnSpan = document.querySelector(`.confirm-btns-${runID}`);
            deleteBtn.classList.add('hidden-elm');
            confirmBtnSpan.classList.remove('hidden-elm');
        });
    });

    // Add event listener to all cancel buttons
    document.querySelectorAll('.cancel-btn').forEach(cancelBtn => {
        cancelBtn.addEventListener('click', function() {
            const runID = cancelBtn.dataset.id;

            const confirmBtnSpan = document.querySelector(`.confirm-btns-${runID}`);
            confirmBtnSpan.classList.add('hidden-elm');

            const deleteBtn = document.querySelector(`.delete-btn[data-id="${runID}"]`);
            deleteBtn.classList.remove('hidden-elm');
        });
    });

    // Add event listener to all delete buttons
    document.querySelectorAll('.delete-confirm-btn').forEach(deleteBtn => {
        deleteBtn.addEventListener('click', function() {
            deleteUploadedStudy(deleteBtn);
            return false;
        });
    });

    // Hide all edit forms and add event listener to all edit forms
    document.querySelectorAll("[class^='edit-form']").forEach(form => {
        // Initially hide the edit form
        switchToEditView(false, form);

        // Event listener for edit forms
        form.onsubmit = function () {
            // Get the data-id of the form
            const dataID = form.dataset.id;

            // Get the new content and call the editProfile function
            const newContent = form.querySelector('input[name="inputField"]').value;
            editProfile(dataID, newContent);

            return false;
        };
    });

    // Add event listener to all edit links (class names starting with 'edit-link') for switching the edit forms on/off
    document.querySelectorAll("[class^='edit-link']").forEach(editLink => {
        editLink.addEventListener('click', function() {
            switchToEditView(true, editLink);
        });
    });

    // Add event listener to all cancel links (class names starting with 'cancel-link') for switching the edit forms/off
    document.querySelectorAll("[class^='cancel-link']").forEach(cancelLink => {
        cancelLink.addEventListener('click', function() {
            switchToEditView(false, cancelLink);
        });
    });

    // Add event listener to password reset form
    document.querySelectorAll("[class='reset-form-password']").forEach(form => {
        // Initially hide the edit form
        switchToEditView(false, form);

        // Event listener for edit forms
        form.onsubmit = function () {
            // Extract password data
            const currPwdInput = form.querySelector('input[name="currPwd"]');
            const newPwdInput = form.querySelector('input[name="newPwd"]');
            const confNewPwdInput = form.querySelector('input[name="confNewPwd"]');

            const currPwd = currPwdInput.value;
            const newPwd = newPwdInput.value;
            const confNewPwd = confNewPwdInput.value;

            // Clean up
            form.reset();
            changePassword(currPwd, newPwd, confNewPwd);

            return false;
        };
    });
});

function editProfile(dataID, newContent) {
    /**
     * Sends a PUT request to update the profile. Gets the new data.
     * Then hides the edit form and displays the new data.
     */

    // Get the CSRF token
    const token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    // Send put request to edit the profile
    fetch(`/editprofile/${dataID}`, {
        method: 'PUT',
        body: JSON.stringify({content: newContent}),
        headers: {"X-CSRFToken": token}
    })
        .then(response => response.json())
        .then(result => {
            // Get the relevant div
            const contentDiv = document.querySelector(`.content-${dataID}`);

            // Update the content
            contentDiv.innerHTML = result.content;

            // Hide the edit form and show the content itself
            switchToEditView(false, contentDiv);
        })
        .catch(error => {
            console.log(error);
        });

    // Prevent the form from submitting
    return false;
}

function setEmailNotification(receiveEmail) {
    /**
     * Sends a PUT request to update the email notification preference.
     */
    // Get the CSRF token
    const token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    // Send put request to change the password
    fetch(`/set_email_notification/`, {
        method: 'PUT',
        body: JSON.stringify({receiveEmail: receiveEmail}),
        headers: {"X-CSRFToken": token}
    }).then(response => response.json())
        .then(result => {
            // Get the relevant div
            const msgDiv = document.querySelector(`.page-msg`);

            // Update the content
            if (result.success) {
                msgDiv.classList.remove('alert-danger')
                msgDiv.classList.add('alert-success');
            } else {
                msgDiv.classList.remove('alert-success')
                msgDiv.classList.add('alert-danger');
            }

            const msg = result.message;
            msgDiv.innerHTML = `${msg}`;
            msgDiv.classList.remove('hidden-msg');

        })
        .catch(error => {
            console.log(error);
        });

    // Prevent the form from submitting
    return false;
}

function changePassword(currPwd, newPwd, confNewPwd) {
    /**
     * Sends a PUT request to update the password.
     */
    // Get the CSRF token
    const token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    // Send put request to change the password
    fetch(`/change_password`, {
        method: 'PUT',
        body: JSON.stringify({currPwd: currPwd, newPwd: newPwd, confNewPwd: confNewPwd}),
        headers: {"X-CSRFToken": token}
    })
        .then(response => response.json())
        .then(result => {
            // Get the relevant div
            const contentDiv = document.querySelector(`.content-password`);
            const msgDiv = document.querySelector(`.page-msg`);

            // Update the content
            if (result.success) {
                msgDiv.classList.remove('alert-danger')
                msgDiv.classList.add('alert-success');
            } else {
                msgDiv.classList.remove('alert-success')
                msgDiv.classList.add('alert-danger');
            }

            const msg = result.message;
            msgDiv.innerHTML = `${msg}`;
            msgDiv.classList.remove('hidden-msg');

            // Hide the edit form and show the content itself
            switchToEditView(false, contentDiv);
        })
        .catch(error => {
            console.log(error);
        });

    // Prevent the form from submitting
    return false;
}

function switchToEditView(showEditForm, elm) {
    /**
     * Switches between the edit post form and the post itself.
     */

    // Get the data-id of the elm
    const dataID = elm.dataset.id;

    // Get the last part of the elm's class name
    const identifier = elm.className.split(' ')[0].split('-').pop();

    // Get the display and edit classes
    const displayClass  = 'display-mode-' + identifier;
    const editClass  = 'edit-mode-' + identifier;

    // Get the edit link
    const editLinkClass = 'edit-link-' + identifier;
    const editLink = document.querySelector(`.${editLinkClass}[data-id="${dataID}"]`);

    if (showEditForm) {
        // Edit Mode
        document.querySelector(`.${displayClass}`).style.display = 'none';
        document.querySelector(`.${editClass}`).style.display = 'block';

        if (editLink != null) {
            editLink.style.display = 'none';
        }

    } else {
        // Display Mode
        document.querySelector(`.${displayClass}`).style.display = 'block';
        document.querySelector(`.${editClass}`).style.display = 'none';
        if (editLink != null) {
            editLink.style.display = 'block';
        }
    }
}


function deleteUploadedStudy(deleteBtn) {
    /**
     * Sends a PUT request to remove any the uploaded study
     */

    // Get the data-id to identify the primary key of the object
    const runID = deleteBtn.dataset.id;

    // Get the CSRF token
    const token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    // Send put request to remove the item
    fetch(`/delete_uploaded_study/${runID}/`, {
        method: 'PUT',
        headers: {"X-CSRFToken": token}
    })
        .then(response => response.json())
        .then(result => {
            // Get the relevant div
            const msgDiv = document.querySelector(`.page-msg`);

            // Update the content
            if (result.success) {
                msgDiv.classList.remove('alert-danger')
                msgDiv.classList.add('alert-success');
            } else {
                msgDiv.classList.remove('alert-success')
                msgDiv.classList.add('alert-danger');
            }

            const msg = result.message;
            msgDiv.innerHTML = `${msg}`;
            msgDiv.classList.remove('hidden-msg');

            // Get the div element
            const containerClass = 'table-row-' + runID;
            const containerDiv = document.querySelector(`.${containerClass}`);
            // Set the animation play state to running so that animationend
            // event listener gets triggered to remove containerDiv
            containerDiv.classList.add('hidden-msg');
        })
        .catch(error => {
            console.log(error);
        });

    // Prevent the form from submitting
    return false;
}
