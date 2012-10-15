from django import forms
from django.template import loader

GOOGLECDN = '//ajax.googleapis.com/ajax/libs/'


class JQueryWidget(forms.TextInput):
    class Media:
        js = (
               '%s/jquery/1.8.2/jquery.min.js' % GOOGLECDN,
               '%s/jqueryui/1.8.23/jquery-ui.min.js' % GOOGLECDN,
             )
        css = {
            'all': (
                    'css/jquery-ui.css',
                   )
        }


class AutocompleteWidget(JQueryWidget):
    template_name = 'autocomplete.html'

    def __init__(self, *args, **kwargs):
        super(AutocompleteWidget, self).__init__(*args, **kwargs)
        self.model = kwargs.get("model")

    def get_context(self, name='', value='', attrs=None):
        context = {
            'type': self.input_type,
            'name': name,
            'hidden': self.is_hidden,
            'required': self.is_required,
            'True': True,
        }

        # True is injected in the context to allow stricter comparisons
        # for widget attrs. See #25.
        if self.is_hidden:
            context['hidden'] = True

        if value is None:
            value = ''

        if value != '':
            # Only add the value if it is non-empty
            context['value'] = self._format_value(value)

        context['attrs'] = self.build_attrs(attrs)

        for key, attr in context['attrs'].items():
            if attr == 1:
                # 1 == True so 'key="1"' will show up only as 'key'
                # Casting to a string so that it doesn't equal to True
                # See #25.
                if not isinstance(attr, bool):
                    context['attrs'][key] = str(attr)

        context['model'] = self.model
        return context

    def render(self, attrs=None, **kwargs):
        context = self.get_context(attrs=attrs or {}, **kwargs)
        return loader.render_to_string(
                self.template_name,
                dictionary=context,
                context_instance=None)
