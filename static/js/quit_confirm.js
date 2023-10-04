function quit_confirm() {
    let confirm = window.confirm("Are you sure you want to quit?");
    if (confirm) {
        // user pressed "OK"
        alert("😢 You ended the game! Statistics have been saved in the history.");
        window.location.href = "/quit"; // redirects the user to route "/quit"
    }
}
