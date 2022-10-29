# Web-Crawlie
A basic web crawler created using FastAPI and Beautiful soup

# How It Works
Enter an appropriate url into the API, it finds your requested URL, scrapes the title,
description , image and keywords associated with the website (if any) and returns them

# sample Input

'''json{ 
    "url":"https://stripe.com" 
}'''

#sample output

'''json {
        "msg": {
            "title": "Stripe | Payment Processing Platform for the Internet",
            "Description": "Stripe is a suite of APIs powering online payment processing and commerce solutions for internet businesses of all sizes. Accept payments and scale faster.",
            "Keywords": null,
            "Image": "https://images.ctfassets.net/fzn2n1nzq965/3AGidihOJl4nH9D1vDjM84/9540155d584be52fc54c443b6efa4ae6/homepage.png?q=80"
        },
        "status": true
    },
    200'''
