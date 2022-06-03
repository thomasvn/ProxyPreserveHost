# Investigating ProxyPreserveHost

Initial question: what does `ProxyPreserveHost` do and what impact does it have?

## Definitions

> When enabled, this option will pass the `Host:` line from the incoming request to the proxied host, instead of the hostname specified in the *ProxyPass* line.

> This option should normally be turned Off. It is mostly useful in special configurations like proxied mass name-based virtual hosting, where the original Host header needs to be evaluated by the backend server.

## Explanation of this magical phenomena

`ProxyPreserveHost On`

- Client -> Proxy (Host: Proxy)
- Proxy -> App (Host: Proxy)
- The app now understands its hostname is Proxy

`ProxyPreserveHost Off`

- Client -> Proxy (Host: Proxy)
- Proxy -> App (Host: App)
- The app now understands its hostname is App. Not always the desired effect.

## Running the experiment

```bash
docker-compose up --build
```

## References

- ProxyPreserveHost
  - <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Host>
  - <https://httpd.apache.org/docs/2.4/mod/mod_proxy.html#proxypreservehost>
  - <https://stackoverflow.com/questions/65123980/how-can-i-prevent-proxypreservehost-from-redirecting-indefinitely>
  - <https://stackoverflow.com/questions/51789423/apache-server-reverse-proxy-with-proxypreservehost-on-results-in-404>
  - <https://stackoverflow.com/questions/8908576/why-does-plays-apache-conf-guide-recommend-using-proxypreservehost>
- Experiment
  - <https://docs.docker.com/compose/gettingstarted/>
  - <https://hub.docker.com/_/httpd>

<!-- DEBUG
docker run --rm -it httpd:latest bash
-->

<!-- TODO
- enable the proxy in httpd
- is there even a reason to use a proxy within Kubernetes? All Ingress/Routes are already proxies
- Also investigate `ProxyPass` and `ProxyPassReverse`
-->
