from rest_framework.renderers import JSONRenderer

class WrappedJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # Wrap data in a dictionary
        # wrapped_data = {'data': data}
        wrapped_data = data
        return super(WrappedJSONRenderer, self).render(wrapped_data, accepted_media_type, renderer_context)
