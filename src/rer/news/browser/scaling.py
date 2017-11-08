# -*- coding: utf-8 -*-
from plone.app.imaging.scaling import ImageScaling as BaseImageScaling
from Acquisition import aq_base
from plone import api
from plone.api.exc import InvalidParameterError


class ImageScaling(BaseImageScaling):
    """
    Override base ImageScaling view.
    If an image is set, we use source image tags and scales.
    """

    def get_image_scale_view(self):
        context = aq_base(self.context)
        image = getattr(context, 'image', None)
        if not image:
            return None
        image_obj = image.to_object
        try:
            return api.content.get_view(
                name='images',
                context=image_obj,
                request=self.request,
            )
        except InvalidParameterError:
            return None

    def scale(self, fieldname=None, scale=None, height=None, width=None,
              **parameters):
        scale_view = self.get_image_scale_view()
        if not scale_view:
            return None
        return scale_view.scale(fieldname, scale, height, width, parameters)

    def tag(self, fieldname=None, scale=None, height=None, width=None,
            css_class=None, direction='keep', **args):
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
            direction=direction
        )
