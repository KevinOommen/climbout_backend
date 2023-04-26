#import response object
from django.http import HttpResponse

#chatbot imports
import os




# Create your views here.
def chatbot_response(request):
    from llama_index import SimpleDirectoryReader
    from llama_index import GPTSimpleVectorIndex
    os.environ['OPENAI_API_KEY'] = "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"
    documents = SimpleDirectoryReader(r'C:\Users\Kevin Oommen Anish\OneDrive\Desktop\climbout_backend\api\chatdata').load_data()
    index = GPTSimpleVectorIndex.from_documents(documents)
    resp = index.query(request.body.decode('utf-8'))

    print(resp)
    return HttpResponse(resp)