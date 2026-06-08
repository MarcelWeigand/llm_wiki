

## Workflow


1. Training 
2. Save best model in registry (S3, MLflow) --> best_model.pkl
3. Create endpoint for model, loading best_model.pkl from S3
![[Pasted image 20260522143145.png|534]]



Option 1: model loaded from registry at runtime 

4. Create docker image without the .pkl file, only with app.py --> instead save it in S3 --> this way you can update the model without creating a new docker image
5. Push image to ECR
6. Run container on ECS --> runs app.py --> loads model from s3 into RAM (ECS has IAM role to access S3)
7. Restart Container if you have a new model in S3 

	- Pros: much simpler deployment, image changes only when serving _code_ changes, model rollback is just changing an env var back, works very naturally with model registries.
	- Cons: startup is slower (downloading weights on boot), the container has a runtime dependency on the registry being reachable, you need to manage model caching if you want fast restarts.

Option 2: model baked into the image

4. Create docker image with the .pkl file
5. Push image to ECR
6. Run container on ECS
7. Create and deploy a new image using CI/CD every time there is a new model in the registry

	- Pros: fully self-contained, fast cold start, no registry dependency at runtime, easy to roll back (just redeploy the old image tag)
	- Cons: a new model = a new image build + push + deploy cycle, even if the serving code hasn't changed at all. Images get large. Feels heavyweight for frequent retraining
	- used in deep learning with very large models where you want the container to be predictable and pre-warmed, or in edge/offline deployments where there is no registry to call at runtime


Which patterns do teams actually use?

- sth in between 
- the serving image is stable and reused across model versions (Option 1)
- but they also cache the model weights in a volume or use a sidecar container to pre-fetch them so cold start isn't a problem. (Option 2)
- Rebuilding the image is reserved for when the _serving code_ itself changes (new preprocessing logic, new API schema, dependency upgrades)