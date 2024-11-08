from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.conf import settings
import os
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)
def hello_world(request):
    return render(request, 'index.html')

# Debugging function to show where Django is looking for templates
def debug_template_paths():
    template_dirs = settings.TEMPLATES[0]['DIRS']  # Usually TEMPLATES is a list
    print("Django template directories:")
    for dir in template_dirs:
        print(f"- {dir}")
        # Check if directory exists before listing templates
        if os.path.exists(dir):
            print(f"Templates in '{dir}':")
            for template in os.listdir(dir):
                print(f"  - {template}")
        else:
            print(f"Directory does not exist: {dir}")
# View function
def my_view(request):
    template_name = 'index.html'  # Specify the template to render

    # Debug template paths only in development mode
    if settings.DEBUG:
        debug_template_paths()

    try:
        # Attempt to render the template
        return render(request, template_name)
    except TemplateDoesNotExist as e:
        # Log the error
        logger.error(f"Template not found: {e}")
        # Return a fallback response for missing templates
        return HttpResponse("The requested template could not be found.", status=404)
