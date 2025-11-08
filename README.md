# Testing Behave
Assignment for submitting Behave scripts in SE 3150.

*Contents* - there are four projects:

Two from the original repository, to check if your environment is set up correctly:

**isitchristmas**

**peppers-ghost**

isitchristmas demonstrates how to use built in steps. It has a default environment.py and a steps file that contains the required inclusion to use the built in steps.

peppers-ghost uses both built in steps AND custom steps. 

And two I made to be graded:

**cipher**

**squirrel_app**

cipher checks two websites that encrypt with caesar/vignere algorithms. It uses custom steps. I tried testing https://dcode.fr/en at first, but it sends requests to their server and has anti-bot measures. So I had to use similar websites.

squirrel_app runs its own docker containerized app. It uses built in steps.

# Testing

## Squirrel App Setup
For squirrel_app, you will also need to use docker to run the app. cd into its project directory and run these commands:

```cmd
docker build -t squirrel-app .
docker run -d -p 8080:8080 -p 8000:8000 squirrel-app
```

If you go to http://localhost:8000/, it should now show the website. 

Make sure you delete any existing squirrels if they are there, otherwise some tests will fail.

## Running With Behave

To run the behave scripts, cd into the project directory and type `python -m behave`

