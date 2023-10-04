$(document).ready(function () {
    $('#history').DataTable({
        // show by default the rows sorted in descending chronological order (column Start time)
        "order": [
            [1, "asc"]
        ]
    });
});
