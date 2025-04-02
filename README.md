# Poetry
## Exploiting the vulnerabilities
This app uses dependencies holding known vulnerabilities - two are direct and one is transitive.

Here are the exploitable vulnerable packages: 
- [fastecdsa - Timing Attack](https://snyk.io/vuln/SNYK-PYTHON-FASTECDSA-511943)
- [flask-cors - Directory Traversal](https://snyk.io/vuln/SNYK-PYTHON-FLASKCORS-608972)
- [ihatemoney - Authorization Bypass](https://snyk.io/vuln/SNYK-PYTHON-IHATEMONEY-595715)./...