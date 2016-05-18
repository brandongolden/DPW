function validateForm() {
    var x = document.forms["form"]["simName"].value;
    if (x == null || x == "") {
        alert("Name must be filled out");
        return false;
    }
}