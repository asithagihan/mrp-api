from aws_cdk import (
    core,
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_apigateway as apigateway,
    aws_cognito as cognito,
    aws_lambda as lambda_,
)
from constructs import Construct


class CdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a new Cognito user pool
        user_pool = cognito.UserPool(
            self,
            "lissome-user-pool",
            standard_attributes=cognito.StandardAttributes(
                phoneNumber=cognito.StandardAttributesPhoneNumber(required=False)
            ),
            signInAliases=cognito.SignInAliases(email=True),
            selfSignUpEnabled=True,
            email=cognito.UserPoolEmail(
                with_ses=cognito.WithSes(
                    ses_region="ap",
                    from_email="info@lissomefresh.com",
                    from_name="Lissomefresh",
                )
            ),
        )

        # Create a Cognito client for the user pool
        user_pool_client = user_pool.add_client(
            "lissome-client",
            oAuth=cognito.OAuthSettings(
                flows=cognito.OAuthFlows(authorizationCodeGrant=True),
                callbackUrls=[
                    "https://api.lissomefresh.com",
                    "http://localhost:8000",
                ],
                scopes=[
                    cognito.OAuthScope(
                        scope_name="email",
                        description="Allows access to the user's email address",
                    )
                ],
            ),
        )

        lissome_api = apigateway.RestApi(self, "lissome-api")

        authorizer = lissome_api.add_authorizer(
            "lissome-authorizer",
            cognito.CognitoUserPoolsAuthorizer(cognito_user_pools=[user_pool]),
        )

        lissome_lambda_function = lambda_.Function(
            self,
            "lissome-fastapi",
            runtime=lambda_.Runtime.PYTHON_3_11,
            handler="main.handler",
            code=lambda_.Code.from_asset("./../api"),
        )

        lissome_lambda_function.add_event_source(
            apigateway.LambdaRestApiEventSource(
                path="/",
                method="ANY",
                authorization_type=apigateway.AuthorizationType.COGNITO,
                authorizer=authorizer,
            )
        )

        lissome_lambda_function.add_event_source(
            apigateway.LambdaRestApiEventSource(
                path="/*",
                method="ANY",
                authorization_type=apigateway.AuthorizationType.COGNITO,
                authorizer=authorizer,
            )
        )
