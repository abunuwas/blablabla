# service-policy

[ ![Codeship Status for boughtbymany/service-policy](https://app.codeship.com/projects/75537930-769f-0134-dd65-4269843b54e0/status?branch=master)](https://app.codeship.com/projects/179609)



## How to deploy

Initial deploy to dev environment for the first time

    $ fab deploy:initial=True

You will then need to associate the AWS api key and AWS api stage with an AWS Usage Plan [using the AWS web UI](https://eu-west-1.console.aws.amazon.com/apigateway/home?region=eu-west-1#/usage-plans/ohwgtw?screen=details). This is a [known issue](https://github.com/Miserlou/Zappa/issues/390) in Zappa.

Update existing deployment

    $ fab deploy


You can deploy to other environments by specifying the environment name in the deploy command

    $ fab deploy:production


**NOTE**
> Zappa does not update the AWS config when deploying. If you have changed any Zappa settings which affect the AWS Api Gateway then you will need to remove the existing deployment using the `undeploy` command.
>
>     $ zappa undeploy --settings=zappa_settings/dev.hjson
>
> If it is a production environment you will need to make a duplicate production environment with the new config and then update all other services to use the new one, before deleting the original.
>
