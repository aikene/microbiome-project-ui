document.addEventListener('DOMContentLoaded', function() {

    if (document.getElementById("show-history").innerHTML === "1") {
        // Show the Search History page
        document.getElementById("tab1").checked = false;
        document.getElementById("tab2").checked = true;
    }

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

document.addEventListener('click', function (e) {
    try {
        // allows for elements inside TH
        function findElementRecursive(element, tag) {
            return element.nodeName === tag ? element : findElementRecursive(element.parentNode, tag);
        }
        var descending_th_class_1 = 'dir-d';
        var ascending_th_class_1 = 'dir-u';
        var ascending_table_sort_class = 'asc';
        var table_class_name = 'sortable';
        var alt_sort_1 = e.shiftKey || e.altKey;
        var element = findElementRecursive(e.target, 'TH');
        var tr = findElementRecursive(element, 'TR');
        var table = findElementRecursive(tr, 'TABLE');
        function reClassify(element, dir) {
            element.classList.remove(descending_th_class_1);
            element.classList.remove(ascending_th_class_1);
            if (dir)
                element.classList.add(dir);
        }
        function getValue(element) {
            var value = (alt_sort_1 && element.dataset.sortAlt) || element.dataset.sort || element.textContent;
            return value;
        }
        if (table.classList.contains(table_class_name)) {
            var column_index_1;
            var nodes = tr.cells;
            var tiebreaker_1 = parseInt(element.dataset.sortTbr);
            // Reset thead cells and get column index
            for (var i = 0; i < nodes.length; i++) {
                if (nodes[i] === element) {
                    column_index_1 = parseInt(element.dataset.sortCol) || i;
                }
                else {
                    reClassify(nodes[i], '');
                }
            }
            var dir = descending_th_class_1;
            // Check if we're sorting ascending or descending
            if (element.classList.contains(descending_th_class_1) ||
                (table.classList.contains(ascending_table_sort_class) && !element.classList.contains(ascending_th_class_1))) {
                dir = ascending_th_class_1;
            }
            // Update the `th` class accordingly
            reClassify(element, dir);
            var reverse_1 = dir === ascending_th_class_1;
            var compare_1 = function (a, b, index) {
                var x = getValue((reverse_1 ? a : b).cells[index]);
                var y = getValue((reverse_1 ? b : a).cells[index]);
                var temp = parseFloat(x) - parseFloat(y);
                var bool = isNaN(temp) ? x.localeCompare(y) : temp;
                return bool;
            };
            // loop through all tbodies and sort them
            for (var i = 0; i < table.tBodies.length; i++) {
                var org_tbody = table.tBodies[i];
                // Put the array rows in an array, so we can sort them...
                var rows = [].slice.call(org_tbody.rows, 0);
                // Sort them using Array.prototype.sort()
                rows.sort(function (a, b) {
                    var bool = compare_1(a, b, column_index_1);
                    return bool === 0 && !isNaN(tiebreaker_1) ? compare_1(a, b, tiebreaker_1) : bool;
                });
                // Make an empty clone
                var clone_tbody = org_tbody.cloneNode();
                // Put the sorted rows inside the clone
                clone_tbody.append.apply(clone_tbody, rows);
                // And finally replace the unsorted tbody with the sorted one
                table.replaceChild(clone_tbody, org_tbody);
            }
        }
    }
    catch (error) {
        // console.log(error)
    }
});

