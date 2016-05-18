class FormPage(object):
    def __init__(self):
        self.form = '''<!DOCTYPE>
        <html>
        <head>
            <title>Sim Generator - Form</title>
            <link rel="stylesheet" type="text/css" href="main.css">
            <script>
            function validateForm() {
                var a = document.forms["form"]["simName"].value;
                if (a == "") {
                    alert("Sim Name is required");
                    return false;
                }

                var b = document.forms["form"]["simoleons"].value
                if (b == "") {
                    alert("Number is required");
                    return false;
                }
            }
            </script>
        </head>
        <body>
            <form method="GET" action="" name="form" onsubmit="return validateForm()">

            <label for="simName">Sim Name: </label>
            <input type="text" name="simName">

            <label for="simoleons">Enter a number: </label>
            <input type="text" name="simoleons">

            <label for="hairColor">Choose a number: </label>
            <select name="hairColor">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
            </select>

            <label for="eyeColor">Choose a number: </label>
            <select name="eyeColor">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
            </select>

            <input type="submit" value="Submit">
            </form>
        </body>
        </html>
        '''


class ResultsPage(object):
    def __init__(self):
        self.header = '''<!DOCTYPE>
        <html>
        <head>
            <title>Sim Generator - Results</title>
            <link rel="stylesheet" type="text/css" href="main.css">
        </head>
        <body>
        '''

        self.footer = '''
        </body>
        </html>
        '''
