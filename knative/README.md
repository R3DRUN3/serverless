# KNATIVE DEMO

This is a simple demo on how to use the Knative framework for running serverless workload on kubernetes.

## Prerequisites
- `docker`
- `kubectl`
- `KinD`
- `knative` and `knative quickstart plugin` see the <a href="https://knative.dev/docs/getting-started/quickstart-install/">docs</a>.

## Instructions

Create a kind cluster and install knative on it:
```sh
kn quickstart kind
```

Output:
```sh
Running Knative Quickstart using Kind
✅ Checking dependencies...
    Kind version is: 0.17.0

☸ Creating Kind cluster...
Creating cluster "knative" ...
 ✓ Ensuring node image (kindest/node:v1.25.3) 🖼 
 ✓ Preparing nodes 📦
 ✓ Writing configuration 📜
 ✓ Starting control-plane 🕹️
 ✓ Installing CNI 🔌
 ✓ Installing StorageClass 💾
 ✓ Waiting ≤ 2m0s for control-plane = Ready ⏳
 • Ready after 18s 💚
Set kubectl context to "kind-knative"
You can now use your cluster with:

kubectl cluster-info --context kind-knative

Have a nice day! 👋

🍿 Installing Knative Serving v1.9.0 ...
    CRDs installed...
    Core installed...
    Finished installing Knative Serving
🕸️ Installing Kourier networking layer v1.9.0 ...
    Kourier installed...
    Ingress patched...
    Finished installing Kourier Networking layer
🕸 Configuring Kourier for Kind...
    Kourier service installed...
    Domain DNS set up...
    Finished configuring Kourier
🔥 Installing Knative Eventing v1.9.0 ...
    CRDs installed...
    Core installed...
    In-memory channel installed...
    Mt-channel broker installed...
    Example broker installed...
    Finished installing Knative Eventing
🚀 Knative install took: 5m5s
🎉 Now have some fun with Serverless and Event Driven Apps!
```

Follow <a href="https://knative.dev/docs/getting-started/install-func/">this</a> part of the docs to install *kn func* and *func plugin*.

<br/>

Now is time to have some fun and create our first function!
<br/>
run this command:

```sh
func create -l go hello
```
This will create a repo inside your local folder.
<br/>
run the function (this will create a docker image and run a container):
```sh
cd hello && func run --registry test.oci
```

Output:
```console
🙌 Function image built: docker.io/test.oci/hello:latest
Function already built.  Use --build to force a rebuild.
Function started on port 8080
Initializing HTTP function
listening on http port 8080
```

now call it!
```sh
func invoke
```

Output:
```sh
Received response
POST / HTTP/1.1 localhost:8080
  Accept-Encoding: gzip
  User-Agent: Go-http-client/1.1
  Content-Length: 25
  Content-Type: application/json
Body:
```

To continue experimenting with knative, follow the official documentation from <a href="https://knative.dev/docs/getting-started/build-run-deploy-func/">here</a>.