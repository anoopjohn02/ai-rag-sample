
"""
Repository module
"""
from sqlalchemy import select
from app.data import (ConversationHistory, 
                      ConversationMessage, 
                      MessageTokenUsage, 
                      DocumentEmbedding, 
                      DocumentEmbeddingFiles)
from .sql_engine import Session

class ConversationRepo():
    """
    Conversation Repo
    """
    def save_conversation(self, conversation : ConversationHistory):
        """
        Method to save conversations
        """
        with Session() as session:
            session.add(conversation)
            session.commit()

    def get_conversation(self, conv_id):
        """
        Method to fetch one conversations
        """
        with Session() as session:
            stmt = select(ConversationHistory).where(ConversationHistory.id == conv_id)
            return session.scalars(stmt).one()

    def get_user_conversations(self, user_id):
        """
        Method to fetch user conversations
        """
        with Session() as session:
            stmt = select(ConversationHistory).where(ConversationHistory.user_id == user_id,
                                                     ConversationHistory.deleted == False)
            return session.scalars(stmt).all()

class ConversationMessageRepo():
    """
    Conversation Message Repo
    """
    def save_message(self, message : ConversationMessage):
        """
        Method to save a message
        """
        with Session() as session:
            session.add(message)
            session.commit()
    def get_conversation_messages(self, conv_id):
        """
        Method to fetch messages related to given conversation
        """
        with Session() as session:
            stmt = select(ConversationMessage).where(ConversationMessage.conversation_id == conv_id)
            return session.scalars(stmt).all()
    def get_txn_messages(self, txn_id):
        """
        Method to fetch messages related to given conversation
        """
        with Session() as session:
            stmt = select(ConversationMessage).where(ConversationMessage.transaction_id == txn_id)
            return session.scalars(stmt).all()

class MessageTokenUsageRepo():
    """
    Token Usage Repo for Messages
    """
    def save_usage(self, usage : MessageTokenUsage):
        """
        Method to save a message token usage
        """
        with Session() as session:
            session.add(usage)
            session.commit()
    def get_all_message_usages(self):
        """
        Method to fetch all token usages
        """
        with Session() as session:
            stmt = select(MessageTokenUsage)
            return session.scalars(stmt).all()

class DocumentEmbeddingRepo():
    """
    Document Embeddings Repo
    """
    def save_embeddings(self, embedding : DocumentEmbedding):
        """
        Method to save an embedding
        """
        with Session() as session:
            session.add(embedding)
            session.commit()
    def get_all(self):
        """
        Method to fetch all embeddings
        """
        with Session() as session:
            stmt = select(DocumentEmbedding)
            return session.scalars(stmt).all()

class DocumentEmbeddingFilesRepo():
    """
    Document Embedding Files Repo
    """
    def save_embeddings(self, embedding_file : DocumentEmbeddingFiles):
        """
        Method to save embedding files
        """
        with Session() as session:
            session.add(embedding_file)
            session.commit()
