# Copyright (c) 2011-2012, ImageCat Inc.
#
# SIDD is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# only, as published by the Free Software Foundation.
#
# SIDD is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License version 3 for more details
# (a copy is included in the LICENSE file that accompanied this code).
#
# You should have received a copy of the GNU Lesser General Public License
# version 3 along with SIDD.  If not, see
# <http://www.gnu.org/licenses/lgpl-3.0.txt> for a copy of the LGPLv3 License.
#
# Version: $Id: ms_level_table.py 18 2012-10-24 20:21:41Z zh $

"""
dialog for editing mapping scheme branches
"""
from PyQt4.QtCore import Qt, QVariant, QString, QAbstractTableModel
from ui.constants import logUICall, get_ui_string
from ui.helper.common import build_multivalue_attribute_tooltip

class MSLevelTableModel(QAbstractTableModel):
    """
    table model supporting visualization of node in mapping scheme tree
    """
    def __init__(self, values, weights, parser, valid_codes, is_editable=[True, True]):
        """ constructor """
        super(MSLevelTableModel, self).__init__()

        # table header 
        self.headers = [
            get_ui_string('dlg.msbranch.edit.tableheader.value'),
            get_ui_string('dlg.msbranch.edit.tableheader.weight'),
            'Value', 'Weight (%)'
        ]        
        self.parser=parser
        self.valid_codes=valid_codes
        self.values, self.weights = self._sort(values, weights)
        self.is_editable = is_editable
    
    def columnCount(self, parent):
        """ only two columns exist. always return 2 """
        return 2

    def rowCount(self, parent):
        """ number of rows same as number of siblings """
        return len(self.weights)

    def addValues(self):
        """ add new row to table"""
        self.values.append('')
        self.weights.append(0)
        # required call to refresh view
        self.reset()
    
    def deleteValue(self, row):
        """ remove selected row """
        if row < 0 or row > len(self.values):
            return
        self.weights.remove(self.weights[row])
        self.values.remove(self.values[row])
        self.dataChanged.emit(self.index(row, 0), self.index(row,1))

    def headerData(self, section, orientation, role):
        """ return data to diaply for header row """        
        if role == Qt.DisplayRole:   
            if orientation == Qt.Horizontal:
                return QString(self.headers[section])
            else:
                # no vertical header
                return QVariant()
        elif role == Qt.ToolTipRole:            
            return QString('tool tip for %s' % self.headers[section])
        else:            
            return QVariant()
    
    def data(self, index, role):
        """ return data to be displayed in a cell """
        if role == Qt.DisplayRole:
            logUICall.log('retrieving data %s %s' % (index.column(), index.row()),
                             logUICall.DEBUG_L2)
            if (index.column() == 0):
                # first column, show value
                value = self.values[index.row()]
                if value is not None:
                    return QString(value)
                else:
                    return ""
            else:
                # second column, show weight
                return QString('%.2f'% self.weights[index.row()])
        elif role == Qt.ToolTipRole:
            # construct data for display in tooltip            
            if (index.column() == 0):
                value = self.values[index.row()]            
                if value is not None:
                    return build_multivalue_attribute_tooltip(self.valid_codes, self.parser.parse(value))
            else:
                return QVariant("")            
        
        else:
            return QVariant()
    
    def setData(self, index, value, role):
        """ set data modified by cell edit """
        if role == Qt.EditRole:
            if (index.column() == 0):
                # first column, change value
                taxStr = str(value.toString())
                # do nothing for empty string
                if taxStr == "":
                    return False           
                # verify taxonomy
                                
                # passed all checks. set value
                self.values[index.row()] = taxStr
            else:
                # second column, change weight
                (dVal, sucess) = value.toDouble()
                # conversion to double failed
                if not sucess:
                    raise Exception(get_ui_string("dlg.msbranch.edit.warning.invalidweight"))
                # make sure 0 <= dVal <= 100
                if dVal < 0 or dVal > 100:
                    raise Exception(get_ui_string("dlg.msbranch.edit.warning.invalidweight"))
                                    
                # passed all checks. set value
                self.weights[index.row()] = round(dVal, 1)

            self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0),self.columnCount(0)))
            return True
        return False
    
    def flags(self, index):
        """ cell condition flag """
        # NOTE: 
        #   ItemIsEditable also required data() and setData() function
        _combined_flag = Qt.ItemIsEnabled | Qt.ItemIsSelectable  
        if index.column() < 0 and index.column() > len(self.is_editable):
            return _combined_flag
        if self.is_editable[index.column()]:
            _combined_flag = _combined_flag | Qt.ItemIsEditable
        return _combined_flag 

    def sort(self, ncol, order):
        """ sort table """
        if ncol < 0 or ncol > len(self.headers):
            return
        self.layoutAboutToBeChanged.emit()
        
        if ncol == 0:
            self.values, self.weights = self._sort(self.values, self.weights, reverse_sort=order==Qt.DescendingOrder)
        else:
            self.weights, self.values = self._sort(self.weights, self.values, reverse_sort=order==Qt.DescendingOrder)            
                        
        self.layoutChanged.emit()

    def _sort(self, col1, col2, reverse_sort=False):
        dist = []
        for v, w in map(None, col1, col2):
            dist.append({v:w})
        dist.sort(reverse=reverse_sort)
        sorted_col1, sorted_col2 = [], []
        for val in dist:            
            sorted_col1.append(val.items()[0][0])
            sorted_col2.append(val.items()[0][1])
        return sorted_col1, sorted_col2
    
