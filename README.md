Checker Board Assignment

    - Continue to learn how to pass information fro the url to the route
    - Practice linking static files to templates
    - Get comfortable passing information from the route to the template
    - Understand how to use for loop properly in the template
    - Recognize the value of creating a html/css first and then adding logic/code

    You program should have the following output
        1. Create a new Flask project
        2. Have the root toute render a template with a checkerboard on it. Example:
            - http://localhost:5000 - should display 8 by 8 checkerboard
        3. Have the css in a separate stylesheet and link this to the template
        4. Have another route accpet a single parameter (i.e "/<x>") and render a checkerboard with x many rows, with alternating colors. Example:
            - http://localhost:5000/4 - should display 8 by 4 checkerboard
        5. NINJA BONUS: Have another route accept 2 parameters (i.e "/<x>/<y>") and render a checkerboard with x rows and y columns, with alteernating colors. Example:
            - http://localhost:5000/10/10 - should display 10 by 10 checkerboard. Beofre you pass x or y to jinja, please remember to convert it to integer first.
        6. SENSEI BONUS: Have another route accept 4 parameters (i.e "/<x>/<y>/<color1>/<color2>") and render a checkerboard with x rows and y columns, with alternating colors, color1 and color2. Example:
            - http://localhost:5000/10/10/color1/color2 - should display 10 by 10 checkerboard with alternatin colors of yellow and blue.