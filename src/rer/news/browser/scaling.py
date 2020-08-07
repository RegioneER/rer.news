# -*- coding: utf-8 -*-
from Acquisition import aq_base
from logging import getLogger
from plone import api
from plone.api.exc import InvalidParameterError
from plone.namedfile.interfaces import IStableImageScale
from plone.namedfile.scaling import ImageScaling as BaseImageScaling
from zope.interface import alsoProvides
from zope.publisher.interfaces import NotFound


try:
    from plone.scale.storage import AnnotationStorage
except ImportError:
    logger = getLogger('plone.app.imaging')
    logger.warn(
        'Warning: no Python Imaging Libraries (PIL) found. '
        'Can\'t scale images.'
    )


class ImageScaling(BaseImageScaling):
    """
    Override base ImageScaling view.
    If an image is set, we use source image tags and scales.
    """

    def get_image_obj(self):
        context = aq_base(self.context)
        image = getattr(context, 'image', None)
        if not image:
            return None
        return image.to_object

    def publishTraverse(self, request, name):
        """ used for traversal via publisher, i.e. when using as a url """
        stack = request.get('TraversalRequestNameStack')
        if stack and stack[-1] not in self._ignored_stacks:
            # field and scale name were given...
            scale = stack.pop()
            image = self.scale(name, scale)  # this is aq-wrapped
        elif '.' in name:
            # we got a uid...
            uid, ext = name.rsplit('.', 1)
            storage = AnnotationStorage(self.context)
            info = storage.get(uid)
            image = None
            if info is not None:
                image = self.make(info).__of__(self.context)
                alsoProvides(image, IStableImageScale)
        else:
            # otherwise `name` must refer to a field...
            scale_view = self.get_image_scale_view()
            if not scale_view:
                raise NotFound(self, name, self.request)
            return scale_view.scale()
        if image is not None:
            return image
        raise NotFound(self, name, self.request)

    def get_image_scale_view(self):
        image_obj = self.get_image_obj()
        if not image_obj:
            return None
        try:
            return api.content.get_view(
                name='images', context=image_obj, request=self.request
            )
        except InvalidParameterError:
            return None

    def scale(
        self, fieldname=None, scale=None, height=None, width=None, **parameters
    ):
        scale_view = self.get_image_scale_view()
        if not scale_view:
            return None
        return scale_view.scale(fieldname, scale, height, width, parameters)

    def tag(
        self,
        fieldname=None,
        scale=None,
        height=None,
        width=None,
        css_class=None,
        direction='keep',
        **args
    ):
        """
        """
        scale_view = self.get_image_scale_view()
        if not scale_view:
            return None
        return scale_view.tag(
            fieldname=fieldname,
            scale=scale,
            height=height,
            width=width,
            css_class=css_class,
            direction=direction,
        )
