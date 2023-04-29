document.addEventListener("DOMContentLoaded", function() {
    Dropzone.autoDiscover=false;

    const dropzone = new Dropzone('#dz-form',{
        maxFilesize: 10000,
        acceptedFiles:'.csv, .fastq',
        autoProcessQueue: false,
        uploadMultiple: true,
        parallelUploads: 100,
        maxFiles: 100,
        addRemoveLinks: true,

        init: function() {
            var myDropzone = this;

            document.getElementById("upload").addEventListener("click", function(e) {
                  // Don't submit the form yet.
                  // e.preventDefault();
                  e.stopPropagation();
                  myDropzone.processQueue();
            });

            document.getElementById("reset").addEventListener("click", function(e) {
                  // Don't submit the form yet.
                  e.stopPropagation();
                  myDropzone.removeAllFiles(true);
            });

            myDropzone.on("addedfile", function(file) {
                if (this.files.length) {
                    var _i, _len;
                    for (_i = 0, _len = this.files.length; _i < _len - 1; _i++) // -1 to exclude current file
                    {
                        if(this.files[_i].name === file.name && this.files[_i].size === file.size && this.files[_i].lastModified.toString() === file.lastModified.toString())
                        {
                            this.removeFile(file);
                        }
                    }
                }
            });

            this.on("sendingmultiple", function() {
                // Gets triggered when the form is actually being sent.
                console.log("Sent the form.");
            });

            this.on("successmultiple", async function(files, response) {
                console.log("Received response.");
                await handle_response(response, this);
            });

            this.on("errormultiple", async function(files, response) {
                // Gets triggered when there was an error sending the files.
                console.log("Received error.");
                await handle_response(response, this);
            });

            // this.on("complete", function(file) {
            //    this.removeAllFiles(true);
            // })
          }
    })
});

function handle_response(response, dropzone) {
    // Get the relevant div
    const msgDiv = document.querySelector(`.page-msg`);

    // Update the content
    if (response.success) {
        msgDiv.classList.remove('alert-danger')
        msgDiv.classList.add('alert-success');
    } else {
        msgDiv.classList.remove('alert-success')
        msgDiv.classList.add('alert-danger');
    }

    dropzone.removeAllFiles(true);

    const msg = response.message;
    msgDiv.innerHTML = `${msg}`;
    msgDiv.classList.remove('hidden-msg');
}

