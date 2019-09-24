
[![Netlify Status](https://api.netlify.com/api/v1/badges/5704b9aa-4caf-483a-ac82-055b6a9dd28e/deploy-status)](https://app.netlify.com/sites/jovial-pare-04b6fe/deploys)



Here are the versions we're using,

node = v10.16.3
npm = 6.9.0
python = 3.7.3
pip = 19.1.1


If you want to help improve the site, here is how you can set it up locally,

Run the following,

```
$ npm install
$ pip install -r requirements.txt
$ nikola build
$ nikola build
$ nikola serve
```

It is *not* a typo. You need to run `nikola build` twice. What seems to be
happening is that nikola starts collecting CSS/static files before our gulp
tasks can complete. So, the second time you run `nikola build` will grab
everything. 

`nikola serve` is used to setup a local webserve, so you can visit
http://localhost:8000/  to see the website. 

If you want to clean your build environment run,

```
$ npm run clean
$ nikola clean
```

