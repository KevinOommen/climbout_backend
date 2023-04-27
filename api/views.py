#import response object
from django.http import HttpResponse
from  .serializers import eventserializer
from rest_framework.generics import ListAPIView, CreateAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView
from .models import events
#chatbot imports
import os


CWD_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the path to the chatbot data directory
CHATBOT_DATA_DIR = os.path.join(CWD_DIR, 'api\\chatdata')


# Create your views here.
def chatbot_response(request):
    from llama_index import SimpleDirectoryReader
    from llama_index import GPTSimpleVectorIndex
    os.environ['OPENAI_API_KEY'] = "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"
    
    documents = SimpleDirectoryReader(CHATBOT_DATA_DIR).load_data()
    index = GPTSimpleVectorIndex.from_documents(documents)
    resp = index.query(request.body.decode('utf-8'))

    print(resp)
    return HttpResponse(resp)

class add_event(CreateAPIView):
    queryset=events.objects.all()
    serializer_class=eventserializer
