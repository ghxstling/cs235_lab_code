# **COMPSCI 235 - LAB 5**
###### Name: Dylan Choy
###### UPI: dcho282

## **Hands-on Lab Activity:**

### Questions

**1.** All templates in the app extend from `layout.html` What is the syntax for extending from a layout template?
>  The syntax for extending from a layout template `example.html` is:
```html
<body>
    {% extends "example.html"%}
</body>
```

**2.** What method should you call to generate a dynamic URL for `localhost/people/40`?
> You should call the `url_for('function-name', parameters)` method, where `function-name` is the function that handles the dynamic URL, and `parameters` is any variables that are required by the function to call.

**3.** What the benefit of using the blueprint compared with using the default route (app.route())?
>  A blueprint allows you to organise groups of related view functions together rather than having just one file for all views, similar to creating an object class in Python. This allows for better code readability and maintainability.