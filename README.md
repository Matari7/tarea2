# tarea2
## Colaboradores
- Cristian Caiza
- Ariel Campoverde

## Como Instalar
Para instalar el programa se necesita instalar Python en el sistema

## COMO CORRE EL PROGRAMA
Ejecutando en el
```bash```
python app.py

## COMO FUNCIONA
El programa ejecutará las funciones expensive_computation y mostrará el tiempo tomado para las operaciones iniciales y subsecuentes, utilizando la caché para optimizar el rendimiento.
 

# Documentation


## What is HATEOAS?
HATEOAS is an acronym that stands for 'Hypermedia as the Engine of Application State'. This term, introduced by Fielding as part of his REST definition, describes one of the key REST properties: since the architecture style is supposed to provide a universal interface, HATEOAS requires the REST client to only move through the web application by following URIs (Uniform Resource Identifiers) in hypermedia format. If this principle is implemented, the client does not require any further information apart from a basic understanding of hypermedia in order to be able to interact with the application or the server.

The individual URIs are provided:
- in the form of href and src attributes for HTML documents or snippets
- using JSON or XML attributes/elements that are automatically recognized by the respective clients

By implementing the HATEOAS principle, the interface of a REST service can be adapted at any time. This is an important advantage of this architecture compared with other application structures, for example, those based on SOAP (Simple Object Access Protocol).

## How can we have security on APIs?
Securing an API necessitates a multifaceted approach that incorporates a combination of strategies, technologies, and best practices. These are the elements to consider when securing an API:

- *Implement authentication methods*: Implement authentication mechanisms such as OAuth, API keys, or tokens. Ensure precise authorization controls to restrict users to authorized resources.
- *Encrypt communications*: Transmit data over HTTPS to encrypt data during transit, safeguarding it from eavesdropping and tampering.
- *Input validation*: Sanitize and validate user input to prevent injection attacks. Block the execution of data received from untrusted sources.
- *Enforce rate limiting*: Enforce rate limiting to deter misuse and protect against DoS attacks. Restrict the number of requests a client can make within a specified timeframe.
- *Encrypt data*: Employ encryption to protect sensitive data at rest and in transit. Utilize established encryption algorithms and ensure secure key management.
- *Adopt API gateways*: Adopt API gateways to centralize and streamline security controls. API gateways can handle authentication, authorization, rate limiting, and logging in a centralized manner.
- *Implement monitoring and logging solutions*: Implement comprehensive and centralized monitoring and logging solutions to detect and respond to security incidents promptly. Continuously monitor for unusual API activity and potential attacks.
- *Regularly audit and test*: Conduct systematic security audits and penetration testing to pinpoint weaknesses and vulnerabilities. Promptly address any issues identified.

## Bibliography
- HATEOAS. (2023, July 12). IONOS Digital Guide; IONOS. [https://www.ionos.com/digitalguide/websites/web-development/hateoas-information-on-the-rest-constraint/](https://www.ionos.com/digitalguide/websites/web-development/hateoas-information-on-the-rest-constraint/)
- Ballejos, L. (n.d.). 8 best practices for securing APIs. NinjaOne. Retrieved June 26, 2024, from [https://www.ninjaone.com/blog/8-best-practices-for-securing-apis/](https://www.ninjaone.com/blog/8-best-practices-for-securing-apis/)
