
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
  unicode = str
elif six.PY2:
  import __builtin__

from . import config
from . import state
from . import interface_ref
class unnumbered(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/tunnel/ipv4/unnumbered. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for setting unnumbered interfaces.
Includes reference the interface that provides the
address information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__config','__state','__interface_ref',)

  _yang_name = 'unnumbered'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='container', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='container', is_config=True)
    self.__interface_ref = YANGDynClass(base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'interfaces', u'interface', u'tunnel', u'ipv4', u'unnumbered']

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /interfaces/interface/tunnel/ipv4/unnumbered/config (container)

    YANG Description: Configuration data for unnumbered interface
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /interfaces/interface/tunnel/ipv4/unnumbered/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration data for unnumbered interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /interfaces/interface/tunnel/ipv4/unnumbered/state (container)

    YANG Description: Operational state data for unnumbered interfaces
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /interfaces/interface/tunnel/ipv4/unnumbered/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state data for unnumbered interfaces
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='container', is_config=True)


  def _get_interface_ref(self):
    """
    Getter method for interface_ref, mapped from YANG variable /interfaces/interface/tunnel/ipv4/unnumbered/interface_ref (container)

    YANG Description: Reference to an interface or subinterface
    """
    return self.__interface_ref
      
  def _set_interface_ref(self, v, load=False):
    """
    Setter method for interface_ref, mapped from YANG variable /interfaces/interface/tunnel/ipv4/unnumbered/interface_ref (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_ref is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_ref() directly.

    YANG Description: Reference to an interface or subinterface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_ref must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='container', is_config=True)""",
        })

    self.__interface_ref = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_ref(self):
    self.__interface_ref = YANGDynClass(base=interface_ref.interface_ref, is_container='container', yang_name="interface-ref", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/tunnel', defining_module='openconfig-if-tunnel', yang_type='container', is_config=True)

  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  interface_ref = __builtin__.property(_get_interface_ref, _set_interface_ref)


  _pyangbind_elements = {'config': config, 'state': state, 'interface_ref': interface_ref, }

