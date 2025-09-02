from datetime import datetime
import re
from django.shortcuts import render

<<<<<<< HEAD

=======
>>>>>>> 84b50a04211a476323ea55508ad13ae40518e90a
# Create your views here.
def inicio(req):
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return render(req, 'inicio.html', {
        'variavel': lista
    })

<<<<<<< HEAD

=======
>>>>>>> 84b50a04211a476323ea55508ad13ae40518e90a
def verDataHora(req):
    agora = datetime.now()
    return render(req, 'data-hora.html', {
        'datahora_atual': agora
<<<<<<< HEAD
   
   
   
    })
=======
    
    
    
    })
>>>>>>> 84b50a04211a476323ea55508ad13ae40518e90a
