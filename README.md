# Distance Calculator
#### Video Demo:  <https://youtu.be/RLb9iCu0NYQ>
#### Description:

Distance Calculator is a Python project that uses the Flask library to create a web application that allows the user to calculate the distance between two points on Google Maps. For this, the Google Maps API is used to access information about routes, distances and travel time between two addresses.
How it works

The project consists of four main files:

    1. Transp.py: this is the main project file that contains the application logic. It uses the Flask framework to create routes to the web server, receives the HTML form data and uses the Google Maps API to calculate the distance between two addresses and return the results in an HTML page. All this happens because of the function "distance():" which is a view of the flask. It receives a GET request with source and destination parameters of an address. These parameters are used to make an HTTP call to the Google Maps Distance Matrix API, which returns information about the distance and estimated time between given addresses.
    
    First, an API key is defined as a string constant. Next, the values ​​of the address parameters of the GET request are obtained using the request.args object. If any of the fields are missing, the function returns an error page using render_template().
    
    The source variable is created by concatenating the street, number, city and state fields provided by the GET request. The same is done for destination. These values ​​are used to construct the Google Maps Distance Matrix API URL, which is accessed using requests.get() and the result is converted to JSON using .json().
    The function checks if the 'distance' key is present in the JSON dictionary returned by the API. If not, an error page is returned. Otherwise, the function extracts the information of distance, estimated time, origin coordinates and destination coordinates from the JSON dictionary.
    
    Finally, the function creates a URL to Google Maps using the source and destination values ​​and the API key, and returns an HTML page displaying the obtained information, as well as an embedded Google Maps map using the created URL.
    Soon after we will have another function called "index():" inside a route defines the root endpoint ("/") of the application and specifies that the allowed HTTP method is GET. When the user makes a GET request to the root of the application, the index() function is executed. The index() function simply renders the "distance.html" template using Flask's render_template() function. The template will be rendered with whatever context is passed to it. If the "distance.html" file does not exist in the templates directory, the route will fail and return a 404 error.

    The snippet if __name__ == '__main__': app.run() is used to start the Flask web server. It checks to see if the script is running directly from Python, and if so, starts the server.

    2. distance.html: this is the HTML file that contains the form so that the user can enter the addresses they want to calculate the distance and also contains the styling of the page so that the user has a better experience. The form contains fields for the street, number, city and state of origin and destination and a button to "Calculate" the distance between the points.

    3. result.html: this is the HTML file that is returned to the user after completing the form. It contains information about the distance between the addresses, the travel time, the origin and destination coordinates and a Google Maps map that shows the route between the two addresses, all these dynamic variables that are returned by the "render_template" used in the code python. The page will also contain a button for a new search, which, when clicked, will return to the distance.html page with all the form fields blank for a new request.

    4. invalid.html: this html file will be returned to the user if filling out the form in the distance.html file is filled out incorrectly, or if the form is not filled out. The invalid.html page will return an error message and a "back" button to perform a new search.

### How to run the project:

To run the project, follow these steps:

    Download the project source code and extract the files into a directory of your choice.

    Install the required dependencies. To do this, run the following command in the terminal:

    `pip install flask requests`

### Google Maps API:
Using the Google Maps API requires a valid API key to make API calls. To configure the API, you need to create a Google Cloud Platform account, create a project, enable the Google Maps API, and create an API key. After getting the API key, you need to insert it into the Transp.py file, replacing the value of the "api_key" variable.

Start the Flask server. To start the Flask server, run the following command in the terminal: 

    `python Transp.py`

Run the python app in your code editor, or type "flask run" in your terminal to run the code. The terminal will give you a local ip that pressing `ctrl + click` on ip will open a web page with the project.

Enter the addresses you want to calculate the distance and click the "Calculate" button. The result will be displayed on a new page with information on distance, travel time, origin and destination coordinates and a Google Maps map that shows the route between the two addresses.

## Conclusion

Distance calculator is a simple but useful project for anyone who needs to calculate distances and travel time between two addresses. It uses the Google Maps API and the Flask framework to create an easy to use and configure web application. With a few changes, it can be adapted for other purposes and integrated into other projects.