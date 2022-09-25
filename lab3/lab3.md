# **COMPSCI 235 - LAB 3**
###### Name: Dylan Choy
###### UPI: dcho282

## **Notes**

HTML Page Essential
- Head:
    - `<title>`: Name of the page that will be displayed in the browser tab
    - `<script>`: Internal JavaScript that powers the front-end logic of the web page
    - `<style>`: Internal CSS that allows you to customise the look and feel of certain elements or the whole page
    - `<link>`: Allows you to link with external CSS and JavaScript code
    - `<meta>`: Extra information about the page, such as which character set to use (charset)
- Note:
    - `<meta>` is commonly used for Search Engine Optimisation (SEO) and ensuring that the web page is responsive and compatible on different devices and screen sizes
    - External CSS and JS are always preferred over Internal JS, to ensure that your code is well maintained and organised

Basic Tags
- Heading:              `<h1></h1>, <h2></h2> ... <h6></h6>`
- Paragraph:            `<p></p>`
- Link:                 `<a href="https://www.google.co.nz">Google</a>`
- Image:                `<img src="source_URL" alt="Text when image cannot be loaded">`
- Line break:           `<br> or <br/>`
- Style application:    `<div>`

Table and List
```html
<!-- Table example -->
<table>
    <tr>
        <th>ID</th>
        <th>First name</th>
        <th>Last name</th>
    </tr>
    <tr>
        <th>1</th>
        <th>Leone1</th>
        <th>Meyer</th>
    </tr>
    <tr>
        <th>2</th>
        <th>Dewitt</th>
        <th>Vega</th>
    </tr>
</table>

<!-- List example -->

<!-- U for Unordered list (bullet points) -->
<ul>
    <li>Coffee</li>
    <li>Tea</li>
    <li>Milk</li>
</ul>

<!-- O for Ordered 1, 2, 3, ... -->
<ol>
    <li>Apple</li>
    <li>Orange</li>
    <li>Kiwifruit</li>
</ol>
```

Form
```html
<form action="">
    <label for="username">Username</label><br />
    <input type="text" id="username" name="username" /><br />
    
    <label for="password">Password</label><br />
    <input type="password" id="password" name="password" /><br />

    <button type="submit">Log in</button>
</form>
```

- The "Submit" type buttom will tell the form-handler to trigger an action once activated by the user
- The "Password" type will render any character typed by the user with ***, thus obscuring whatever was written
- There are many other types we can use for our form, such as email, checkbox, range, etc.

CSS
- CSS stands for Cascading Style Sheets, which allows you to add style to most HTML elements in the body
    - Select by element: Changes the theme of all the tags with the same tag name
    - Select by ID: Changes the style for one specific element (uses #idName)
    - Select by Class: Most commonly used and very flexible (uses .classname)
- The best way to write CSS is to either use the Browser Developer Tool (F12), or to try your idea on CodePen

Bootstrap
- Bootstrap is a frontend template that allows you to create professional looking websites effectively
- There is a great amount of support from the community, namely on Stack Overflow
- It makes minimal changes to an existing page by adding Popper.js, which is Bootstrap's CSS and JS
- Every CSS styles uses class selectors to change the style on a web page 

## **Hands-on Lab Activity:**

### Questions

**1.**  What is HTML and what are HTML tags?
> HTML stands for Hypertext Markup Language, which is the language used to format all webpages we use on the Internet and contains hypertext information within links. HTML tags are designators that define the content and structure of objects displayed in a page, such as headings, paragraphs, images, etc.

**2.**  How many levels of heading does an HTML have?
> There are 6 levels of headings.

**3.**  Here is a HTML page that has a syntax error:
```html
<h3>This is my awesome title!</h1>
```
What does it look like in a rendered page?
> This renders the text as a level 3 heading. 

**4.**  How to add a comment to a HTML page?
> You enclose your comments as follows: `<!-- This is a comment -->`. These are ignored by HTML when rendered in a browser

**5.**  Name 3 commonly used CSS selectors.
> The 3 commonly used selectors are element selectors, class selectors, and ID selectors.

**6.**  Whatʼs the difference between padding and margin in CSS?
> Padding is the amount of space between the element's border and the element's content, whereas margin is the amount of space around the element's border.

**7.**  What units can you use when defining a padding? (Name at least 2.)
> You can use either use pt or px as your units of length.
