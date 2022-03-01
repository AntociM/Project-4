# Spotless Co.
The Spotless Co. is a presentation website for a fictional professional cleaning company based in Stockholm, Sweden. The company's target group is private clients, who can book services via the website's booking platform. The website is also providing a contact form.
![Home page]( docs/home-page-print.jpg)

The live site can be viewded [here](https://spotlessco.herokuapp.com/).

## User Stories

As a **site user** I can **register an account** so that **I gain access to my subscription and manage upcoming events**.

As a **site user** I can **create, read, update and delete requests** so that **I can manage the wanted services**.

As a **site user** I can **receive information about my booking status** so that **I am informed in advance, and I can adjust**.

As a **site user** I can **add details to my request** so that **the requested service is provided according to my specifications**.

As a **site user** I can **have a profile associated with my account** so that **I can see and modify my details**.

As a **site user** I can **read information about the company's services** so that **I am well informed, and I can choose according to my preferences**.

As a **site user** I can **read past clients testimonials** so that **I get valuable guidance from people who have used these services**.

As a **site user** I can **contact the company** so that **I can get more helpful information or address some specific concerns**.

As a **site admin** I can **approve or disapprove client's booking requests** so that **I can do operational planning according to available resources**.

As a **site admin** I can **create, read, update and delete content** so that **I can manage my websites content**.

As a **site admin** I can **contact our clients** so that **I can inform them in case of any change**.

As a **site admin** I can **update the users' list** so that **I can add, edit and delete users**.

As a **site admin** I can **access the admin page via user interface** so that **I can manage the website**.

This user stories are part of agile tools used for this project.  In order to integrate issues and pull requests, GitHub projects was used.

![](docs/project.jpg)

## Wireframes

- Home page 

![](docs/home-page.jpg)

- Testimonials

![](docs/testimonials.jpg)

- Contact page

![](docs/contact.jpg)

- Login form

![](docs/login-page.jpg)

- Signup form

![](docs/Signup-form.jpg)

- User's dashboard

![](docs/user-page.jpg)

Some design changes come up during the development process. One of the changes was integrating About Us as a section on Home Page, compared to the initial design to be a separate page.
## Site Structure

The application has 3 main pages: Home, Services, and Contact. It also has several additional pages related to Admin, sign up, sign in and sign out.

## Design Choices

### Typhography

- The font family is 'Poppins' from Google fonts. It is a modern, professional font and does not distract user from content.

### Color Pallet

- The primary color used has a pale tint of azure, and on the website, blue in different shadows and hues are present. Blue is associated with professional and modern aspects and gives the user a calming and familiar look.

![](docs/Colors.png)

## Data Model

- Spotless website is based on MVC model (Model. View, and Controller). It consists of a database with relationships between models (represented by tables in the above image). The models are CustomUser, Booking, Service, and Contact. The views then render the models in a way dictated by the URLs.

![](docs/mvc.jpg)

## Features

### Existing features

#### Home Page

##### Navigation bar

- It is located at the top of every page—the company's logo on the left-hand side and the menu on the other side. Navigation elements are displayed inline for displays over 750px. The Navigation Bar swifts to a dropdown list for smaller screens, represented by three lines in the top right corner.

![](docs/nav.jpg)

##### Main image and intro

- Located under Navigation, is an image chosen to represent the tidiness of a home, with an overleyed intro text. 

![](docs/home-page-print.jpg)

##### Website interaction

- This section let the user know how can acces the wished service. 

##### Our Goal and About Us 
- Structured in 2 separated elements, these sections help the user find more information about the company's history and the values and strives that are representative.

![](docs/About us.jpg)

##### Service Overview
- A responsively styled services display to allow the user a quick overview. Each service has a representative icon next to it. 
- An embedded link will redirect the user to the services page.

![](docs/services-home.jpg)

##### Testimonials

- The testimonials section provides the user with some feedback from past clients. There are three testimonials displayed giving a picture, feedback and name.

![](docs/testimonials.jpg)

##### Footer

- Footer has a basic style, displays social media links and copyright information.

![](docs/footer.jpg)

#### Services Page

- At the top of the page is a representative image with overlayed text providing helpful information.
- Fallows an enumeration of services. Each service has a representative icon, description, price/h, and a button redirecting the user to the booking form.

![](docs/service-page.jpg)

#### Contact Page

- Styled in 2 columns (contact form and contact information) in full display and for small screens, content stack on top of each other. 
- On the left-hand side is the contact form, which includes name, email, telephone, title, and message. When a user submits a contact request, the application logs the contact to the database for a record. Initially, all contacts are marked as 'unreplied'. A quick reference to see the contact's status.

![](docs/contact-form.jpg)

























Credits: 
- Icons provided by: https://www.iconfinder.com 