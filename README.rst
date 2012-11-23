================
tastypie-msgpack
================

Created by `Stephen McDonald <http://twitter.com/stephen_mcd>`_

Adds `MsgPack <http://msgpack.org/>`_ support to
`Django Tastypie <http://tastypieapi.org/>`_.

Installation
============

::

    $ pip install -U tastypie-msgpack

Usage
=====

Given a tastypie resource, simply define ``tastypie_msgpack.Serializer``
as the serializer for the resource::

    from tastypie.resources import ModelResource
    from tastypie_msgpack import Serializer
    from myapp.models import MyModel

    class MyResource(ModelResource):
        class Meta:
            resource_name = "thing"
            queryset = MyModel.objects.all()
            serializer = Serializer()

You can now append the ``format=msgpack`` arg to your API URLs!
