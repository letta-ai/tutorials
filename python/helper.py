from datetime import datetime
from dataclasses import dataclass
from typing import Optional

@dataclass
class ToolCall:
    name: str
    arguments: str
    tool_call_id: str

@dataclass
class Message:
    id: str
    date: datetime
    message_type: str
    reasoning: Optional[str] = None
    content: Optional[str] = None
    tool_call: Optional[ToolCall] = None
    tool_return: Optional[str] = None
    status: Optional[str] = None
    tool_call_id: Optional[str] = None
    stdout: Optional[str] = None
    stderr: Optional[str] = None

class MessageFormatter:
    def __init__(self):
        self.emoji_map = {
            'reasoning_message': '🤔',  # thinking emoji for reasoning
            'tool_call_message': '🛠️',  # tool emoji for tool calls
            'tool_return_message': '🔄',  # return emoji for tool returns
            'assistant_message': '🤖',  # robot emoji for assistant
            'user_message': '👤'  # face emoji for user
        }
    
    def format_message(self, message: Message) -> str:
        """Format a message with appropriate emoji and layout."""
        emoji = self.emoji_map.get(message.message_type, '❓')
        timestamp = message.date.strftime("%Y-%m-%d %H:%M:%S")
        #print(message.message_type)
        # Build the formatted message
        formatted = f"[{timestamp}] {emoji} "
        
        if message.message_type == "reasoning_message":
            formatted += f"Reasoning: {message.reasoning}"
        elif message.message_type == "user_message" or message.message_type == "assistant_message":
            formatted += f"Message: {message.content}"
        elif message.message_type == "tool_call_message":
            formatted += f"Tool Call: {message.tool_call.name}\n"
            formatted += f"{message.tool_call.arguments}"
        elif message.message_type == "tool_return_message":
            status_str = f" (Status: {message.status})" if message.status else ""
            formatted += f"Tool Return: {message.tool_return}{status_str}"
            
        return formatted

def print_message(message): 
    print(MessageFormatter().format_message(message))