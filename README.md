# Active Training Studio

An ecommerce website that offers workout programs, a user can purchase one and keep it forever in his account.
 
## User Stories
 
- As a web dev, I want to learn how to use a payment system.
- Aa a web dev, I want to develop a nice website for users and easy to use for both users and admins.
- As the site admin, I want to easily create and edit workout programs for customers.
- As a user/customer, I want to easily found workout programs that match my preferences and needs.
- As a user/customer, I want to add workout programs to my cart, make the payment and quickly gain access to them.
- As a user/customer, I want to have access to my purchased workouts anytime and place.
- As a user/customer, I want to leave opinions on workouts that I liked.

## Features
 
### Existing Features
- Workout browsing: allows admins and registered users to browse, search and filter through an extensive list of offered workouts and add them to the cart.
- Cart: allows to preview all workouts choosen, with the ability to remove an item, continue shopping or go to the checkout.
- Checkout: using Stripe allows users to complete a purchase with credit card and recieve an instant confirmation about the payment.
- Review: when a user has already purchase a workouts has the option to leave an opinion about it, this will be shared with other users and creating a rating system.
- Profile: on the users profile they have the possibility to see old orders, edit their billing information and access purchased workouts.

### Features Left to Implement
- Meal plans: this would add complete healthy path for all users. In addition to the workouts the user can see a way to complement the excercise rutine with a healthy food intake.
- Workout programs: at the moment this website simulates a real ecommerce site but the actual offered items are not delivered, the idea is to create a separete section to access the workout content.

## Technologies Used

- [Django](https://www.djangoproject.com/)

- [Bootstrap](https://getbootstrap.com/)

- [JQuery](https://jquery.com)

- [Heroku](https://www.heroku.com/)

- [Stripe](https://stripe.com/)

#### Code Validation

For code validation [w3 Validation Service](https://w3.org/) was used for HTML and CSS. For Python [ExtendsClass](https://extendsclass.com/python-tester.html) and [JSHint](https://jshint.com/) for JS.

#### The devices that this site was test were:

- Samsung Galaxy S6
- Samsung Galaxy A50
- Samsung Galaxy A70
- Iphone 8 Plus
- Laptop ASUS S510UA, 15.6"
- Desktop PC, 27"
- Tablet was tested with Chrome developer tools.
- Also, the site was tested on Firefox and Microsoft Edge.

## Contribute
All contributions are welcomed and encouraged.

## Deployment

To deploy this application on Heroku using GitHub follow this instruction:

- Clone the repository.
- Install the necessary dependencies using "pip3 install -r requirments.txt".
- Create a [Stripe](https://stripe.com/) account and follow their [documentation](https://stripe.com/docs/checkout/integration-builder) to get your environment variables for later.
- Create a file in the main directory called ‘env.py’ based on the ‘env.example.py’ and add all your environment variables. Don’t forget to add a secret key for your app.
- Create a [Heroku](https://www.heroku.com/) app and connect it to your GitHub repo. In Heroku (App > Settings > GitHub) to complete the connection. And choose Postgress for the DB.
- Add your environment variables on Heroku as well, on the “Config Vars” section. When adding the DEBUG key, leave the value empty to set it to False.
- Complete a commit, push it to GitHub and using ‘git push heroku master’ command push it to Heroku.

Using AWS to store static an media files is encouraged, a tutorial can be found here: [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html)


## Credits

### Content
- Content was inspired on [Trainerize](https://www.trainerize.com/) and [Darebee](https://darebee.com/)

### Media
- The photos used in this site were obtained from [Darebee](https://darebee.com/)

### Acknowledgements

- To [flynfish](https://stackoverflow.com/questions/7862233/twitter-bootstrap-tabs-go-to-specific-tab-on-page-reload-or-hyperlink)
- To [w3shools](https://www.w3schools.com/)
- To [MDN web docs](https://developer.mozilla.org/)
- To [Stack Overflow](https://stackoverflow.com/)
- To [Font Awesome](https://fontawesome.com/)
- To [Google Fonts](https://fonts.google.com/)