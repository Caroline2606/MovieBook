import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp


class Query(graphene.ObjectType):
    post = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_post(self, info, name):
        return "Post " + name


app = FastAPI()
app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query)))
