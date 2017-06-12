import unittest
from Json2Sqlite import Json2Sqlite
import os
class TestJson2Sqlite(unittest.TestCase):
    def test_BoolToInt_False(self):
        c = Json2Sqlite()
        self.assertEqual(0, c.BoolToInt(False))
    def test_BoolToInt_True(self):
        c = Json2Sqlite()
        self.assertEqual(1, c.BoolToInt(True))
    def test_BoolToInt_None(self):
        c = Json2Sqlite()
        value = None
        with self.assertRaises(Exception) as e:
            c.BoolToInt(value)
            self.assertEqual(e.msg, '引数はbool型のみ有効ですが、渡された引数の型は {0}, 値は {1} です。'.format(type(value), value))
            # 引数はbool型のみ有効ですが、渡された引数の型は <class 'NoneType'>, 値は None です。
    def test_BoolToInt_Int(self):
        c = Json2Sqlite()
        value = 0
        with self.assertRaises(Exception) as e:
            c.BoolToInt(value)
            self.assertEqual(e.msg, '引数はbool型のみ有効ですが、渡された引数の型は {0}, 値は {1} です。'.format(type(value), value))
            # 引数はbool型のみ有効ですが、渡された引数の型は <class 'int'>, 値は 0 です。

    def test_IntToBool_0(self):
        c = Json2Sqlite()
        self.assertEqual(False, c.IntToBool(0))
    def test_IntToBool_1(self):
        c = Json2Sqlite()
        self.assertEqual(True, c.IntToBool(1))
    def test_IntToBool_None(self):
        c = Json2Sqlite()
        value = None
        with self.assertRaises(Exception) as e:
            c.IntToBool(value)
            self.assertEqual(e.msg, '引数はint型のみ有効ですが、渡された引数の型は {0}, 値は {1} です。'.format(type(value), value))
    def test_IntToBool_False(self):
        c = Json2Sqlite()
        value = False
        with self.assertRaises(Exception) as e:
            c.IntToBool(value)
            self.assertEqual(e.msg, '引数はint型のみ有効ですが、渡された引数の型は {0}, 値は {1} です。'.format(type(value), value))
    def test_ArrayToString_Bool(self):
        c = Json2Sqlite()
        values = [False, True]
        self.assertEqual("False,True", c.ArrayToString(values))
    def test_ArrayToString_Int(self):
        c = Json2Sqlite()
        values = [1,2,3]
        self.assertEqual("1,2,3", c.ArrayToString(values))
    def test_ArrayToString_Str(self):
        c = Json2Sqlite()
        values = ['ab','cd','ef']
        self.assertEqual("ab,cd,ef", c.ArrayToString(values))
    def test_ArrayToString_None(self):
        c = Json2Sqlite()
        values = [None, None]
        self.assertEqual("None,None", c.ArrayToString(values))
    def test_ArrayToString_List(self):
        c = Json2Sqlite()
        values = [[1,2], [3,4]]
        self.assertEqual("[1, 2],[3, 4]", c.ArrayToString(values))
    def test_ArrayToString_Tuple(self):
        c = Json2Sqlite()
        values = [(1,2), (3,4)]
        self.assertEqual("(1, 2),(3, 4)", c.ArrayToString(values))
    def test_ArrayToString_Dict(self):
        c = Json2Sqlite()
        values = [{'k': 'v'}, {'k1': 100}]
        self.assertEqual("{'k': 'v'},{'k1': 100}", c.ArrayToString(values))
    def test_ArrayToString_Error_None(self):
        c = Json2Sqlite()
        values = None
        with self.assertRaises(Exception) as e:
            c.ArrayToString(values)
            self.assertEqual(e.msg, '引数はint型のみ有効ですが、渡された引数の型は {0}, 値は {1} です。'.format(type(values), values))
    def test_ArrayToString_Error_Bool(self):
        c = Json2Sqlite()
        values = True
        with self.assertRaises(Exception) as e:
            c.ArrayToString(values)
            self.assertEqual(e.msg, '引数はint型のみ有効ですが、渡された引数の型は {0}, 値は {1} です。'.format(type(values), values))
    def test_ArrayToString_Error_Int(self):
        c = Json2Sqlite()
        values = 0
        with self.assertRaises(Exception) as e:
            c.ArrayToString(values)
            self.assertEqual(e.msg, '引数はint型のみ有効ですが、渡された引数の型は {0}, 値は {1} です。'.format(type(values), values))
    def test_ArrayToString_Error_Str(self):
        c = Json2Sqlite()
        values = 'abc'
        with self.assertRaises(Exception) as e:
            c.ArrayToString(values)
            self.assertEqual(e.msg, '引数はint型のみ有効ですが、渡された引数の型は {0}, 値は {1} です。'.format(type(values), values))
    def test_ArrayToString_Error_Tuple(self):
        c = Json2Sqlite()
        values = (1,2,3)
        with self.assertRaises(Exception) as e:
            c.ArrayToString(values)
            self.assertEqual(e.msg, '引数はint型のみ有効ですが、渡された引数の型は {0}, 値は {1} です。'.format(type(values), values))
    def test_ArrayToString_Error_Dict(self):
        c = Json2Sqlite()
        values = {'k': 'v'}
        with self.assertRaises(Exception) as e:
            c.ArrayToString(values)
            self.assertEqual(e.msg, '引数はint型のみ有効ですが、渡された引数の型は {0}, 値は {1} です。'.format(type(values), values))

    def test_StringToArray_Bool(self):
        c = Json2Sqlite()
        values = "False,True"
        self.assertEqual(['False','True'], c.StringToArray(values))
    def test_StringToArray_Int(self):
        c = Json2Sqlite()
        values = "1,2,3"
        self.assertEqual(['1','2','3'], c.StringToArray(values))
    def test_StringToArray_Str(self):
        c = Json2Sqlite()
        values = "abc,def,ghi"
        self.assertEqual(['abc','def','ghi'], c.StringToArray(values))
    def test_StringToArray_BlankItem(self):
        c = Json2Sqlite()
        # 空値の場合は無視される
        values = ",,,abc,,,def,,,"
        self.assertEqual(['abc','def'], c.StringToArray(values))
    def test_StringToArray_SpaceBlankItem(self):
        c = Json2Sqlite()
        # 半角スペース, TAB(ハードタブ,\tエスケープ), 改行(\nエスケープ), 全角スペースだけの要素は無視される
        values = "   ,		,\n,\n\n,abc,　,,def, 　\t\n"
        self.assertEqual(['abc','def'], c.StringToArray(values))
    def test_StringToArray_TripleQuotation_BlankItem(self):
        c = Json2Sqlite()
        # 改行(トリプルクォーテーション)の場合は無視される
        values = """\
        ,
        
        ,
        ,abc,def,
        
        
"""
        self.assertEqual(['abc','def'], c.StringToArray(values))
    def test_StringToArray_Space(self):
        c = Json2Sqlite()
        # 半角スペース, TAB, 改行, 全角スペースが前後や間についている場合はそのまま付与される
        values = " abc ,	def	,\nghi\n,　jkl　, m　n	o\n"
        self.assertEqual([' abc ','	def	','\nghi\n','　jkl　',' m　n	o\n'], c.StringToArray(values))

    def test_StringToArray_Error_None(self):
        c = Json2Sqlite()
        values = None
        with self.assertRaises(Exception) as e:
            c.StringToArray(values)
            self.assertEqual(e.msg, '引数はstr型のみ有効ですが、渡された引数の型は {0}, 値は {1} です。'.format(type(values), values))
    def test_StringToArray_Error_Int(self):
        c = Json2Sqlite()
        values = 0
        with self.assertRaises(Exception) as e:
            c.StringToArray(values)
            self.assertEqual(e.msg, '引数はstr型のみ有効ですが、渡された引数の型は {0}, 値は {1} です。'.format(type(values), values))
    def test_StringToArray_Error_Bool(self):
        c = Json2Sqlite()
        values = False
        with self.assertRaises(Exception) as e:
            c.StringToArray(values)
            self.assertEqual(e.msg, '引数はstr型のみ有効ですが、渡された引数の型は {0}, 値は {1} です。'.format(type(values), values))
    def test_StringToArray_Error_List(self):
        c = Json2Sqlite()
        values = ['abc', 'def']
        with self.assertRaises(Exception) as e:
            c.StringToArray(values)
            self.assertEqual(e.msg, '引数はstr型のみ有効ですが、渡された引数の型は {0}, 値は {1} です。'.format(type(values), values))

