django-quickwidget
==================

The idea is to initially provide a generic way of adding a <input type="text" /> on into a template that has an
$('#id').autocomplete({..});  call. 

The source of the JQuery autocomplete call would point to a generic view. 

* Provide a template inclusion tag. {% autocomplete model widget_id %}
  * This will include the html input tag and JavaScript
* Need to identify the call and what objects to get
* Model.{something?}.autocomplete(term=term) will return the autocompleted objects
  * I don't know what something is. Would I use a model manager ? Or just add the autocomplete method directly to 
     the model ?

* The autocomplete method can also return the correctly formatted JSON 