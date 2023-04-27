#import response object
from django.http import HttpResponse
from  .serializers import eventserializer
from rest_framework.generics import ListAPIView, CreateAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView
from .models import events
#chatbot imports
import os
from llama_index import SimpleDirectoryReader
from llama_index import GPTSimpleVectorIndex
os.environ['OPENAI_API_KEY'] = "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"
from rest_framework.decorators import api_view
from rest_framework.response import Response




CWD_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the path to the chatbot data directory
CHATBOT_DATA_DIR = os.path.join(CWD_DIR, 'api\\chatdata')


# Create your views here.
def chatbot_response(request):
    
    scale=0
    documents = SimpleDirectoryReader(CHATBOT_DATA_DIR).load_data()
    index = GPTSimpleVectorIndex.from_documents(documents)

    response1 = index.query("display 1 if the file have either of word's kakanad,aluva,cherai")
    if (int(str(response1))==1):
        scale+=1
        
    response2 = index.query("display 1 if the file have describtion about a person or event")
    if (int(str(response1))==1):
        scale+=1
    response3 = index.query("display 1 if the file have any mentions about timings in between 6 pm,7 pm,8 pm,9 pm,10 pm,11 pm,12 am")
    
    if (int(str(response1))==1):
        scale+=1
        
    if (scale==3):
        print("\nthe file is genuine\n******take immediate action******")
    else:
        print("not that imp")
@api_view(['GET'])
def chatbot_query(request):
    import os
    from llama_index import SimpleDirectoryReader
    from llama_index import GPTSimpleVectorIndex
    os.environ['OPENAI_API_KEY'] = "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"

    documents = SimpleDirectoryReader(os.path.join(CHATBOT_DATA_DIR,'query')).load_data()
    index = GPTSimpleVectorIndex.from_documents(documents)

    response = index.query(request.body.decode('utf-8'))
    return HttpResponse(response)


class add_event(CreateAPIView):
    queryset=events.objects.all()
    serializer_class=eventserializer
# call a function to get the response from the chatbot when you add an event using add_event api
    def perform_create(self,serializer):
        serializer.save()
        location=self.request.data['location']
        date=self.request.data['date']
        time=self.request.data['time']
        name=self.request.data['name']
        desc=self.request.data['desc']

        #write the above data to a new file on sugbsequesnt calls to this api
        with open(os.path.join(CHATBOT_DATA_DIR,'report.txt'),'w') as f:
            f.write("Report:\n")
            f.write(location+'\n')
            f.write(date+'\n')
            f.write(time+'\n')
            f.write(name+'\n')
            f.write(desc+'\n')        

        
        with open(os.path.join(CHATBOT_DATA_DIR,'response.txt'),'w') as f:
            f.write("Response:\n")
            f.write(str(chatbot_response(self.request))+'\n')

class list_events(ListAPIView):
    queryset=events.objects.all()
    serializer_class=eventserializer