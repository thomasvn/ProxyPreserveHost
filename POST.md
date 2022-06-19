# ProxyPreserveHost

Sometimes, teams favor deploying [reverse proxies](https://www.nginx.com/resources/glossary/reverse-proxy-server/) in front of their application servers or even their kubernetes clusters.

For apps that sit behind these reverse proxies, there are a number of additional considerations these apps should handle to ensure compatibility & awareness of the reverse proxy [1]:

- support for context paths (e.g. proxy.com/app1)
- awareness of hostname (either through config or HTTP header)

## How ProxyPreserveHost can affect an app's awareness of Hostname

[`ProxyPreserveHost`](https://httpd.apache.org/docs/2.4/mod/mod_proxy.html#proxypreservehost) is a Apache httpd directive which passes the [`Host:`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Host) line from the incoming request to the proxied host.

This is important because sometimes, apps use this `Host:` HTTP header to understand its hostname. And this hostname may in turn be used in a variety of locations within the app, such as in links to internal web resources, or when performing SAML SSO authentication.

![ProxyPreserveHost=Off Diagram](img/ProxyPreserveHost.Off.png)

As shown above, the reverse proxy makes another `HTTP GET` requst on behalf of the client. In this `GET` request, the HTTP Header `Host: webapp:5000` is used.

![ProxyPreserveHost=On Diagram](img/ProxyPreserveHost.On.png)

When `ProxyPreserveHost On`, the same `Host:` HTTP header sent from the client is used (even though it does not match the hostname of the `GET` request).

## Running an experiment

To verify the above, we can run a quick experiment. Running `docker-compose up --build` with the code in this [repo](https://github.com/thomasvn/ProxyPreserveHost) will start a Flask webapp and an Apache httpd serving as a reverse proxy. The webapp simply prints out "Hello World!" and the contents of the HTTP GET Request to the browser.

When `ProxyPreserveHost Off`:

![ProxyPreserveHost=Off Experiment](img/Experiment.Off.png)

When `ProxyPreserveHost On`:

![ProxyPreserveHost=On Experiment](img/Experiment.On.png)

## Notes

[1] A reverse proxy can function without these features. However in my experience some reverse proxy implementations heavily rely on these features within the application.

<!-- 
TODO:
- attach screenshot from experiment

DONE:
- quick intro on reverse proxies (provide a link)
- draw a diagram (sketch.io) to replace text explanation
-->

<!--
REFERENCES:
- https://podrezo.medium.com/using-a-reverse-proxy-with-your-web-application-5eec92001193
-->