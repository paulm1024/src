#<pycode(py_ua)>
import ida_idaapi

# -----------------------------------------------------------------------
class op_t(ida_idaapi.py_clinked_object_t):
    """Class representing operands"""
    def __init__(self, lnk = None):
        ida_idaapi.py_clinked_object_t.__init__(self, lnk)

    def _create_clink(self):
        return _ida_ua.op_t_create()

    def _del_clink(self, lnk):
        return _ida_ua.op_t_destroy(lnk)

    def assign(self, other):
        """Copies the contents of 'other' to 'self'"""
        return _ida_ua.op_t_assign(self, other)

    def __eq__(self, other):
        """Checks if two register operands are equal by checking the register number and its dtype"""
        return (self.reg == other.reg) and (self.dtyp == other.dtyp)

    def is_reg(self, r):
        """Checks if the register operand is the given processor register"""
        return self.type == o_reg and self.reg == r

    def has_reg(self, r):
        """Checks if the operand accesses the given processor register"""
        return self.reg == r.reg

    #
    # Autogenerated
    #
    def __get_n__(self):
        return _ida_ua.op_t_get_n(self)
    def __set_n__(self, v):
        _ida_ua.op_t_set_n(self, v)
    def __get_type__(self):
        return _ida_ua.op_t_get_type(self)
    def __set_type__(self, v):
        _ida_ua.op_t_set_type(self, v)
    def __get_offb__(self):
        return _ida_ua.op_t_get_offb(self)
    def __set_offb__(self, v):
        _ida_ua.op_t_set_offb(self, v)
    def __get_offo__(self):
        return _ida_ua.op_t_get_offo(self)
    def __set_offo__(self, v):
        _ida_ua.op_t_set_offo(self, v)
    def __get_flags__(self):
        return _ida_ua.op_t_get_flags(self)
    def __set_flags__(self, v):
        _ida_ua.op_t_set_flags(self, v)
    def __get_dtyp__(self):
        return _ida_ua.op_t_get_dtyp(self)
    def __set_dtyp__(self, v):
        _ida_ua.op_t_set_dtyp(self, v)
    def __get_reg_phrase__(self):
        return _ida_ua.op_t_get_reg_phrase(self)
    def __set_reg_phrase__(self, v):
        _ida_ua.op_t_set_reg_phrase(self, v)
    def __get_value__(self):
        return _ida_ua.op_t_get_value(self)
    def __set_value__(self, v):
        _ida_ua.op_t_set_value(self, v)
    def __get_addr__(self):
        return _ida_ua.op_t_get_addr(self)
    def __set_addr__(self, v):
        _ida_ua.op_t_set_addr(self, v)
    def __get_specval__(self):
        return _ida_ua.op_t_get_specval(self)
    def __set_specval__(self, v):
        _ida_ua.op_t_set_specval(self, v)
    def __get_specflag1__(self):
        return _ida_ua.op_t_get_specflag1(self)
    def __set_specflag1__(self, v):
        _ida_ua.op_t_set_specflag1(self, v)
    def __get_specflag2__(self):
        return _ida_ua.op_t_get_specflag2(self)
    def __set_specflag2__(self, v):
        _ida_ua.op_t_set_specflag2(self, v)
    def __get_specflag3__(self):
        return _ida_ua.op_t_get_specflag3(self)
    def __set_specflag3__(self, v):
        _ida_ua.op_t_set_specflag3(self, v)
    def __get_specflag4__(self):
        return _ida_ua.op_t_get_specflag4(self)
    def __set_specflag4__(self, v):
        _ida_ua.op_t_set_specflag4(self, v)

    n = property(__get_n__, __set_n__)
    type = property(__get_type__, __set_type__)
    offb = property(__get_offb__, __set_offb__)
    offo = property(__get_offo__, __set_offo__)
    flags = property(__get_flags__, __set_flags__)
    dtyp = property(__get_dtyp__, __set_dtyp__)
    reg = property(__get_reg_phrase__, __set_reg_phrase__)
    phrase = property(__get_reg_phrase__, __set_reg_phrase__)
    value = property(__get_value__, __set_value__)
    addr = property(__get_addr__, __set_addr__)
    specval = property(__get_specval__, __set_specval__)
    specflag1 = property(__get_specflag1__, __set_specflag1__)
    specflag2 = property(__get_specflag2__, __set_specflag2__)
    specflag3 = property(__get_specflag3__, __set_specflag3__)
    specflag4 = property(__get_specflag4__, __set_specflag4__)

# ----------------------------------------------------------------------
#
# Misc constants
#
UA_MAXOP   = 6
"""The maximum number of operands in the insn_t structure"""

# -----------------------------------------------------------------------
class insn_t(ida_idaapi.py_clinked_object_t):
    """Class representing instructions"""
    def __init__(self, lnk = None):
        ida_idaapi.py_clinked_object_t.__init__(self, lnk)

        # Create linked operands
        self.Operands = []
        for i in xrange(0, UA_MAXOP):
            self.Operands.append(op_t(insn_t_get_op_link(self.clink, i)))

        # Convenience operand reference objects
        self.Op1 = self.Operands[0]
        self.Op2 = self.Operands[1]
        self.Op3 = self.Operands[2]
        self.Op4 = self.Operands[3]
        self.Op5 = self.Operands[4]
        self.Op6 = self.Operands[5]

    def assign(self, other):
        """Copies the contents of 'other' to 'self'"""
        return _ida_ua.insn_t_assign(self, other)

#<pydoc>
#    def copy(self):
#        """Returns a new copy of this class"""
#        pass
#</pydoc>

    def _create_clink(self):
        return _ida_ua.insn_t_create()


    def _del_clink(self, lnk):
        return _ida_ua.insn_t_destroy(lnk)


    def __iter__(self):
        return (self.Operands[idx] for idx in xrange(0, UA_MAXOP))


    def __getitem__(self, idx):
        """
        Operands can be accessed directly as indexes
        @return op_t: Returns an operand of type op_t
        """
        if idx >= UA_MAXOP:
            raise KeyError
        else:
            return self.Operands[idx]

    def is_macro(self):
        return self.flags & INSN_MACRO != 0

    def is_canon_insn(self):
        return _ida_ua.insn_t_is_canon_insn(self.itype)

    def get_canon_feature(self):
        return _ida_ua.insn_t_get_canon_feature(self.itype)

    def get_canon_mnem(self):
        return _ida_ua.insn_t_get_canon_mnem(self.itype)

    #
    # Autogenerated
    #
    def __get_cs__(self):
        return _ida_ua.insn_t_get_cs(self)
    def __set_cs__(self, v):
        _ida_ua.insn_t_set_cs(self, v)
    def __get_ip__(self):
        return _ida_ua.insn_t_get_ip(self)
    def __set_ip__(self, v):
        _ida_ua.insn_t_set_ip(self, v)
    def __get_ea__(self):
        return _ida_ua.insn_t_get_ea(self)
    def __set_ea__(self, v):
        _ida_ua.insn_t_set_ea(self, v)
    def __get_itype__(self):
        return _ida_ua.insn_t_get_itype(self)
    def __set_itype__(self, v):
        _ida_ua.insn_t_set_itype(self, v)
    def __get_size__(self):
        return _ida_ua.insn_t_get_size(self)
    def __set_size__(self, v):
        _ida_ua.insn_t_set_size(self, v)
    def __get_auxpref__(self):
        return _ida_ua.insn_t_get_auxpref(self)
    def __set_auxpref__(self, v):
        _ida_ua.insn_t_set_auxpref(self, v)
    def __get_segpref__(self):
        return _ida_ua.insn_t_get_segpref(self)
    def __set_segpref__(self, v):
        _ida_ua.insn_t_set_segpref(self, v)
    def __get_insnpref__(self):
        return _ida_ua.insn_t_get_insnpref(self)
    def __set_insnpref__(self, v):
        _ida_ua.insn_t_set_insnpref(self, v)
    def __get_flags__(self):
        return _ida_ua.insn_t_get_flags(self)
    def __set_flags__(self, v):
        _ida_ua.insn_t_set_flags(self, v)

    cs = property(__get_cs__, __set_cs__)
    ip = property(__get_ip__, __set_ip__)
    ea = property(__get_ea__, __set_ea__)
    itype = property(__get_itype__, __set_itype__)
    size = property(__get_size__, __set_size__)
    auxpref = property(__get_auxpref__, __set_auxpref__)
    segpref = property(__get_segpref__, __set_segpref__)
    insnpref = property(__get_insnpref__, __set_insnpref__)
    flags = property(__get_flags__, __set_flags__)


# Create 'cmd' into the global scope
cmd = insn_t(_ida_ua.py_get_global_cmd_link())
"""cmd is a global variable of type insn_t. It is contains information about the last decoded instruction.
This variable is also filled by processor modules when they decode instructions."""

# ----------------------------------------------------------------------
# op_t related constants

#
# op_t.type
#                 Description                          Data field
o_void     =  0 # No Operand                           ----------
o_reg      =  1 # General Register (al,ax,es,ds...)    reg
o_mem      =  2 # Direct Memory Reference  (DATA)      addr
o_phrase   =  3 # Memory Ref [Base Reg + Index Reg]    phrase
o_displ    =  4 # Memory Reg [Base Reg + Index Reg + Displacement] phrase+addr
o_imm      =  5 # Immediate Value                      value
o_far      =  6 # Immediate Far Address  (CODE)        addr
o_near     =  7 # Immediate Near Address (CODE)        addr
o_idpspec0 =  8 # Processor specific type
o_idpspec1 =  9 # Processor specific type
o_idpspec2 = 10 # Processor specific type
o_idpspec3 = 11 # Processor specific type
o_idpspec4 = 12 # Processor specific type
o_idpspec5 = 13 # Processor specific type
                # There can be more processor specific types

#
# op_t.dtyp
#
dt_byte = 0 #  8 bit
dt_word = 1 #  16 bit
dt_dword = 2 #  32 bit
dt_float = 3 #  4 byte
dt_double = 4 #  8 byte
dt_tbyte = 5 #  variable size (ph.tbyte_size)
dt_packreal = 6 #  packed real format for mc68040
dt_qword = 7 #  64 bit
dt_byte16 = 8 #  128 bit
dt_code = 9 #  ptr to code (not used?)
dt_void = 10 #  none
dt_fword = 11 #  48 bit
dt_bitfild = 12 #  bit field (mc680x0)
dt_string = 13 #  pointer to asciiz string
dt_unicode = 14 #  pointer to unicode string
dt_3byte = 15 #  3-byte data
dt_ldbl = 16 #  long double (which may be different from tbyte)
dt_byte32 = 17 # 256 bit
dt_byte64 = 18 # 512 bit

#
# op_t.flags
#
OF_NO_BASE_DISP = 0x80 #  o_displ: base displacement doesn't exist meaningful only for o_displ type if set, base displacement (x.addr) doesn't exist.
OF_OUTER_DISP = 0x40 #  o_displ: outer displacement exists meaningful only for o_displ type if set, outer displacement (x.value) exists.
PACK_FORM_DEF = 0x20 #  !o_reg + dt_packreal: packed factor defined
OF_NUMBER = 0x10 # can be output as number only if set, the operand can be converted to a number only
OF_SHOW = 0x08 #  should the operand be displayed? if clear, the operand is hidden and should not be displayed

#
# insn_t.flags
#
INSN_MACRO  = 0x01   # macro instruction
INSN_MODMAC = 0x02   # macros: may modify the database to make room for the macro insn

#</pycode(py_ua)>
