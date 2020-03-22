# Django-best-practices
Repo for Django best practices guide

Before that, look into Django.

# What is Django:
1. Co-founders: Adrian Holovaty, Simon Willison
2. MVT pattern - DRY, KISS - less code, extensible, pluggable, low coupling
3. Intentions - Rapid development, scalable, all inclusive for business reqts.

# Why Django:
1. Security - 
    Cross site scripting - django templates, 
    Cross site request forgery - CSRF validation, 
    SQL injection - Django Queryset API,
    Clickjacking - X-Frame-Options header,
    SSL & HTTPS - SECURE_SSL_REDIRECT, SECURE_PROXY_SSL_HEADER,
    Session - django sessions,
    referrer - Referrer header,
    Host validation - ALLOWED_HOSTS
 2. Scalable -
    Decoupled characteristic of Archi. enables to add DB servers, cache servers, appln servers
    i.e. easy horizontal scalable
 3. Recognition: Instagram, Mozilla, Pinterest, Open Stack, Disqus, National Geographic etc.
 
 
 Read More: Read More: https://www.djangoproject.com/start/overview/
 
 Other similar Python frameworks: Bottle, Flask, CherryPy, Tornado, web.py, web2py
 
 # Similarities of Java based frameworks - Spring or Spring Boot and Python - Django:
 Below list of similarities between Java and Python, but mind you not same
 1. Auto application configuration - Django settings
 2. Maven, Gradle Dependencies - Pip, pipenv requirements
 3. Dispatcher servlet - Django dispatcher
 4. View-resolver - routes aka urls
 5. Thymeleaf template engine, Facelets - Jinja, Mako etc.
 6. Servlet - WSGI, ASGI
 7. Hibernate - Builtin Django ORM
 8. Jhipster, Spark REST - Django or Django Rest Framework
 9. JDBC API - Django Query API
 10. Struts - Django
 11. Vert.x async, event-driven - Twisted
 12. Spring Boot CLI - Django admin management commands
 13. Actuator - Python CProfile builtin package
 14. Application Events & Listeners - Django signals & receivers
 15. ApplicationArguments - Python command line arguments aka argparse
 16. Admin Features - Django admin portal
 17. Profile based configuration setup - django-configurations external package
 18. Spring Session - Django Session
 19. spring-boot-test - Django unit tests
 