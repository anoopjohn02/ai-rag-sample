"""
Controller module
"""
import logging

from fastapi import Depends
from fastapi.responses import StreamingResponse
from fastapi_controllers import Controller, get, post

from app.models.chat import Request
from app.models.user import LoggedInUser
from app.services import ChatService, get_message_token_usage, get_document_embeddings
from app.web import valid_access_token, get_user_info


class TestController(Controller):
    """
    A test class will be removed later
    """
    prefix = "/v1/test"
    tags = ["test chat"]

    @post("/stream")
    async def test_stream(self, request: Request):
        """
        Test AOI method
        """
        user = LoggedInUser(id="c7f0bad7-ca8d-43a3-840f-df19d3c0e974",
                    first_name="Anoop",
                    username= "str",
                    email= "str",
                    last_name= "str",
                    realm_roles= [],
                    client_roles= [],
                    )
        service = ChatService()
        logging.info("New chat = %s", request.new_chat)
        logging.info("User %s asked question: %s", user.first_name, request.question)
        agent = service.create_agent(request, user)
        #return agent(request.question)["output"]
        return StreamingResponse(agent.stream(request.question), media_type='text/event-stream')


class ChatController(Controller):

    """
    Chat controller class
    """
    prefix = "/v1/chat"
    tags = ["chat"]
    dependencies = [Depends(valid_access_token)]

    @post("")
    async def chat(self, request: Request, user: LoggedInUser = Depends(get_user_info)):
        """
        Get the answer for the user input
        """
        service = ChatService()
        chat = service.create_agent(request, user)
        logging.info("User %s asked question: %s", user.first_name, request.question)
        return StreamingResponse(chat.stream(request.question), media_type='text/event-stream')

class TokenUsageController(Controller):
    """
    Token usage controller class
    """
    prefix = "/v1/chat/token"
    tags = ["token usage"]
    dependencies = [Depends(valid_access_token)]

    @get("/usage")
    def token_usage(self):
        """
        API to get token usage
        """
        return get_message_token_usage()
    
    @get("/embeddings")
    def embeddings(self):
        """
        API to get embeddings
        """
        return get_document_embeddings()