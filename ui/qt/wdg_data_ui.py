# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt\wdg_data.ui'
#
# Created: Thu Jun 27 13:41:14 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_widgetDataInput(object):
    def setupUi(self, widgetDataInput):
        widgetDataInput.setObjectName(_fromUtf8("widgetDataInput"))
        widgetDataInput.resize(998, 765)
        widgetDataInput.setStyleSheet(_fromUtf8(""))
        self.widgetSurvey = QtGui.QWidget(widgetDataInput)
        self.widgetSurvey.setGeometry(QtCore.QRect(430, 70, 411, 141))
        self.widgetSurvey.setObjectName(_fromUtf8("widgetSurvey"))
        self.lb_svy_select_file = QtGui.QLabel(self.widgetSurvey)
        self.lb_svy_select_file.setGeometry(QtCore.QRect(13, 105, 71, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_svy_select_file.setFont(font)
        self.lb_svy_select_file.setObjectName(_fromUtf8("lb_svy_select_file"))
        self.img_lb_svy_desc_help = QtGui.QLabel(self.widgetSurvey)
        self.img_lb_svy_desc_help.setGeometry(QtCore.QRect(240, 5, 16, 21))
        self.img_lb_svy_desc_help.setText(_fromUtf8(""))
        self.img_lb_svy_desc_help.setPixmap(QtGui.QPixmap(_fromUtf8(":/imgs/icons/help.png")))
        self.img_lb_svy_desc_help.setObjectName(_fromUtf8("img_lb_svy_desc_help"))
        self.lb_svy_desc = QtGui.QLabel(self.widgetSurvey)
        self.lb_svy_desc.setGeometry(QtCore.QRect(5, 30, 261, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_svy_desc.setFont(font)
        self.lb_svy_desc.setObjectName(_fromUtf8("lb_svy_desc"))
        self.btn_svy_select_file = QtGui.QToolButton(self.widgetSurvey)
        self.btn_svy_select_file.setEnabled(False)
        self.btn_svy_select_file.setGeometry(QtCore.QRect(360, 105, 41, 19))
        self.btn_svy_select_file.setCursor(QtCore.Qt.ArrowCursor)
        self.btn_svy_select_file.setObjectName(_fromUtf8("btn_svy_select_file"))
        self.radio_svy_sampled = QtGui.QRadioButton(self.widgetSurvey)
        self.radio_svy_sampled.setGeometry(QtCore.QRect(10, 67, 381, 17))
        self.radio_svy_sampled.setObjectName(_fromUtf8("radio_svy_sampled"))
        self.radio_svy_no_data = QtGui.QRadioButton(self.widgetSurvey)
        self.radio_svy_no_data.setGeometry(QtCore.QRect(10, 50, 381, 17))
        self.radio_svy_no_data.setChecked(True)
        self.radio_svy_no_data.setObjectName(_fromUtf8("radio_svy_no_data"))
        self.radio_svy_complete = QtGui.QRadioButton(self.widgetSurvey)
        self.radio_svy_complete.setGeometry(QtCore.QRect(10, 84, 381, 17))
        self.radio_svy_complete.setObjectName(_fromUtf8("radio_svy_complete"))
        self.txt_svy_select_file = QtGui.QLineEdit(self.widgetSurvey)
        self.txt_svy_select_file.setEnabled(False)
        self.txt_svy_select_file.setGeometry(QtCore.QRect(93, 105, 261, 20))
        self.txt_svy_select_file.setObjectName(_fromUtf8("txt_svy_select_file"))
        self.lb_svy_title = QtGui.QLabel(self.widgetSurvey)
        self.lb_svy_title.setGeometry(QtCore.QRect(5, 0, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.lb_svy_title.setFont(font)
        self.lb_svy_title.setObjectName(_fromUtf8("lb_svy_title"))
        self.widgetResult = QtGui.QWidget(widgetDataInput)
        self.widgetResult.setGeometry(QtCore.QRect(430, 320, 411, 241))
        self.widgetResult.setObjectName(_fromUtf8("widgetResult"))
        self.lb_verify_title = QtGui.QLabel(self.widgetResult)
        self.lb_verify_title.setGeometry(QtCore.QRect(10, 10, 301, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_verify_title.setFont(font)
        self.lb_verify_title.setObjectName(_fromUtf8("lb_verify_title"))
        self.img_lb_verify_fp = QtGui.QLabel(self.widgetResult)
        self.img_lb_verify_fp.setGeometry(QtCore.QRect(10, 38, 21, 21))
        self.img_lb_verify_fp.setText(_fromUtf8(""))
        self.img_lb_verify_fp.setObjectName(_fromUtf8("img_lb_verify_fp"))
        self.img_lb_verify_zones = QtGui.QLabel(self.widgetResult)
        self.img_lb_verify_zones.setGeometry(QtCore.QRect(10, 59, 21, 21))
        self.img_lb_verify_zones.setText(_fromUtf8(""))
        self.img_lb_verify_zones.setObjectName(_fromUtf8("img_lb_verify_zones"))
        self.lb_verify_fp = QtGui.QLabel(self.widgetResult)
        self.lb_verify_fp.setGeometry(QtCore.QRect(40, 38, 111, 20))
        self.lb_verify_fp.setObjectName(_fromUtf8("lb_verify_fp"))
        self.lb_verify_svy = QtGui.QLabel(self.widgetResult)
        self.lb_verify_svy.setGeometry(QtCore.QRect(40, 100, 111, 20))
        self.lb_verify_svy.setObjectName(_fromUtf8("lb_verify_svy"))
        self.lb_verify_zones = QtGui.QLabel(self.widgetResult)
        self.lb_verify_zones.setGeometry(QtCore.QRect(40, 59, 111, 20))
        self.lb_verify_zones.setObjectName(_fromUtf8("lb_verify_zones"))
        self.img_lb_verify_svy = QtGui.QLabel(self.widgetResult)
        self.img_lb_verify_svy.setGeometry(QtCore.QRect(10, 100, 21, 21))
        self.img_lb_verify_svy.setText(_fromUtf8(""))
        self.img_lb_verify_svy.setObjectName(_fromUtf8("img_lb_verify_svy"))
        self.lb_verify_aggregation = QtGui.QLabel(self.widgetResult)
        self.lb_verify_aggregation.setGeometry(QtCore.QRect(10, 133, 161, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_verify_aggregation.setFont(font)
        self.lb_verify_aggregation.setObjectName(_fromUtf8("lb_verify_aggregation"))
        self.img_lb_verify_agg_grid = QtGui.QLabel(self.widgetResult)
        self.img_lb_verify_agg_grid.setGeometry(QtCore.QRect(10, 170, 21, 21))
        self.img_lb_verify_agg_grid.setText(_fromUtf8(""))
        self.img_lb_verify_agg_grid.setObjectName(_fromUtf8("img_lb_verify_agg_grid"))
        self.img_lb_verify_agg_zone = QtGui.QLabel(self.widgetResult)
        self.img_lb_verify_agg_zone.setGeometry(QtCore.QRect(10, 150, 21, 21))
        self.img_lb_verify_agg_zone.setText(_fromUtf8(""))
        self.img_lb_verify_agg_zone.setObjectName(_fromUtf8("img_lb_verify_agg_zone"))
        self.lb_verify_agg_zone = QtGui.QLabel(self.widgetResult)
        self.lb_verify_agg_zone.setGeometry(QtCore.QRect(40, 150, 131, 20))
        self.lb_verify_agg_zone.setObjectName(_fromUtf8("lb_verify_agg_zone"))
        self.lb_verify_agg_grid = QtGui.QLabel(self.widgetResult)
        self.lb_verify_agg_grid.setGeometry(QtCore.QRect(40, 170, 131, 20))
        self.lb_verify_agg_grid.setObjectName(_fromUtf8("lb_verify_agg_grid"))
        self.txt_verify_text = QtGui.QTextBrowser(self.widgetResult)
        self.txt_verify_text.setGeometry(QtCore.QRect(170, 40, 221, 151))
        self.txt_verify_text.setObjectName(_fromUtf8("txt_verify_text"))
        self.btn_verify = QtGui.QPushButton(self.widgetResult)
        self.btn_verify.setEnabled(True)
        self.btn_verify.setGeometry(QtCore.QRect(250, 200, 141, 23))
        self.btn_verify.setCursor(QtCore.Qt.ArrowCursor)
        self.btn_verify.setObjectName(_fromUtf8("btn_verify"))
        self.img_lb_verify_pop = QtGui.QLabel(self.widgetResult)
        self.img_lb_verify_pop.setGeometry(QtCore.QRect(10, 80, 16, 21))
        self.img_lb_verify_pop.setText(_fromUtf8(""))
        self.img_lb_verify_pop.setObjectName(_fromUtf8("img_lb_verify_pop"))
        self.lb_verify_pop = QtGui.QLabel(self.widgetResult)
        self.lb_verify_pop.setGeometry(QtCore.QRect(40, 80, 111, 20))
        self.lb_verify_pop.setObjectName(_fromUtf8("lb_verify_pop"))
        self.widgetAggr = QtGui.QWidget(widgetDataInput)
        self.widgetAggr.setGeometry(QtCore.QRect(430, 210, 411, 111))
        self.widgetAggr.setObjectName(_fromUtf8("widgetAggr"))
        self.radio_aggr_grid = QtGui.QRadioButton(self.widgetAggr)
        self.radio_aggr_grid.setGeometry(QtCore.QRect(10, 75, 381, 17))
        self.radio_aggr_grid.setObjectName(_fromUtf8("radio_aggr_grid"))
        self.lb_aggr_desc = QtGui.QLabel(self.widgetAggr)
        self.lb_aggr_desc.setGeometry(QtCore.QRect(5, 35, 281, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_aggr_desc.setFont(font)
        self.lb_aggr_desc.setObjectName(_fromUtf8("lb_aggr_desc"))
        self.lb_aggr_title = QtGui.QLabel(self.widgetAggr)
        self.lb_aggr_title.setGeometry(QtCore.QRect(5, 0, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.lb_aggr_title.setFont(font)
        self.lb_aggr_title.setObjectName(_fromUtf8("lb_aggr_title"))
        self.radio_aggr_zones = QtGui.QRadioButton(self.widgetAggr)
        self.radio_aggr_zones.setGeometry(QtCore.QRect(10, 55, 381, 17))
        self.radio_aggr_zones.setObjectName(_fromUtf8("radio_aggr_zones"))
        self.img_lb_aggr_desc_help = QtGui.QLabel(self.widgetAggr)
        self.img_lb_aggr_desc_help.setGeometry(QtCore.QRect(150, 5, 16, 21))
        self.img_lb_aggr_desc_help.setText(_fromUtf8(""))
        self.img_lb_aggr_desc_help.setPixmap(QtGui.QPixmap(_fromUtf8(":/imgs/icons/help.png")))
        self.img_lb_aggr_desc_help.setObjectName(_fromUtf8("img_lb_aggr_desc_help"))
        self.widgetFootprint = QtGui.QWidget(widgetDataInput)
        self.widgetFootprint.setGeometry(QtCore.QRect(10, 280, 411, 191))
        self.widgetFootprint.setObjectName(_fromUtf8("widgetFootprint"))
        self.cb_fp_story_field = QtGui.QComboBox(self.widgetFootprint)
        self.cb_fp_story_field.setEnabled(False)
        self.cb_fp_story_field.setGeometry(QtCore.QRect(280, 130, 121, 22))
        self.cb_fp_story_field.setObjectName(_fromUtf8("cb_fp_story_field"))
        self.radio_fp_height = QtGui.QRadioButton(self.widgetFootprint)
        self.radio_fp_height.setGeometry(QtCore.QRect(10, 84, 381, 17))
        self.radio_fp_height.setObjectName(_fromUtf8("radio_fp_height"))
        self.txt_fp_select_file = QtGui.QLineEdit(self.widgetFootprint)
        self.txt_fp_select_file.setEnabled(False)
        self.txt_fp_select_file.setGeometry(QtCore.QRect(80, 105, 271, 20))
        self.txt_fp_select_file.setObjectName(_fromUtf8("txt_fp_select_file"))
        self.lb_fp_select_file = QtGui.QLabel(self.widgetFootprint)
        self.lb_fp_select_file.setGeometry(QtCore.QRect(10, 105, 71, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_fp_select_file.setFont(font)
        self.lb_fp_select_file.setObjectName(_fromUtf8("lb_fp_select_file"))
        self.radio_fp_only = QtGui.QRadioButton(self.widgetFootprint)
        self.radio_fp_only.setGeometry(QtCore.QRect(10, 67, 381, 17))
        self.radio_fp_only.setObjectName(_fromUtf8("radio_fp_only"))
        self.lb_fp_title = QtGui.QLabel(self.widgetFootprint)
        self.lb_fp_title.setGeometry(QtCore.QRect(5, 0, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.lb_fp_title.setFont(font)
        self.lb_fp_title.setObjectName(_fromUtf8("lb_fp_title"))
        self.lb_fp_desc = QtGui.QLabel(self.widgetFootprint)
        self.lb_fp_desc.setGeometry(QtCore.QRect(5, 30, 305, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_fp_desc.setFont(font)
        self.lb_fp_desc.setObjectName(_fromUtf8("lb_fp_desc"))
        self.cb_fp_proj = QtGui.QComboBox(self.widgetFootprint)
        self.cb_fp_proj.setEnabled(False)
        self.cb_fp_proj.setGeometry(QtCore.QRect(280, 155, 121, 22))
        self.cb_fp_proj.setObjectName(_fromUtf8("cb_fp_proj"))
        self.lb_fp_proj = QtGui.QLabel(self.widgetFootprint)
        self.lb_fp_proj.setGeometry(QtCore.QRect(10, 155, 151, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_fp_proj.setFont(font)
        self.lb_fp_proj.setObjectName(_fromUtf8("lb_fp_proj"))
        self.btn_fp_select_file = QtGui.QToolButton(self.widgetFootprint)
        self.btn_fp_select_file.setEnabled(False)
        self.btn_fp_select_file.setGeometry(QtCore.QRect(360, 105, 41, 19))
        self.btn_fp_select_file.setCursor(QtCore.Qt.ArrowCursor)
        self.btn_fp_select_file.setObjectName(_fromUtf8("btn_fp_select_file"))
        self.radio_fp_no_data = QtGui.QRadioButton(self.widgetFootprint)
        self.radio_fp_no_data.setGeometry(QtCore.QRect(10, 50, 381, 17))
        self.radio_fp_no_data.setChecked(True)
        self.radio_fp_no_data.setObjectName(_fromUtf8("radio_fp_no_data"))
        self.lb_fp_story_field = QtGui.QLabel(self.widgetFootprint)
        self.lb_fp_story_field.setGeometry(QtCore.QRect(10, 130, 241, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_fp_story_field.setFont(font)
        self.lb_fp_story_field.setObjectName(_fromUtf8("lb_fp_story_field"))
        self.img_lb_fp_desc_help = QtGui.QLabel(self.widgetFootprint)
        self.img_lb_fp_desc_help.setGeometry(QtCore.QRect(240, 5, 16, 21))
        self.img_lb_fp_desc_help.setText(_fromUtf8(""))
        self.img_lb_fp_desc_help.setPixmap(QtGui.QPixmap(_fromUtf8(":/imgs/icons/help.png")))
        self.img_lb_fp_desc_help.setObjectName(_fromUtf8("img_lb_fp_desc_help"))
        self.widgetTitle = QtGui.QWidget(widgetDataInput)
        self.widgetTitle.setGeometry(QtCore.QRect(0, 0, 741, 71))
        self.widgetTitle.setObjectName(_fromUtf8("widgetTitle"))
        self.lb_panel_title = QtGui.QLabel(self.widgetTitle)
        self.lb_panel_title.setGeometry(QtCore.QRect(10, 0, 761, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.lb_panel_title.setFont(font)
        self.lb_panel_title.setObjectName(_fromUtf8("lb_panel_title"))
        self.txt_panel_description = QtGui.QTextEdit(self.widgetTitle)
        self.txt_panel_description.setGeometry(QtCore.QRect(10, 30, 731, 41))
        self.txt_panel_description.setReadOnly(True)
        self.txt_panel_description.setObjectName(_fromUtf8("txt_panel_description"))
        self.widgetZones = QtGui.QWidget(widgetDataInput)
        self.widgetZones.setGeometry(QtCore.QRect(10, 70, 411, 211))
        self.widgetZones.setObjectName(_fromUtf8("widgetZones"))
        self.radio_zones_count = QtGui.QRadioButton(self.widgetZones)
        self.radio_zones_count.setGeometry(QtCore.QRect(10, 84, 391, 17))
        self.radio_zones_count.setObjectName(_fromUtf8("radio_zones_count"))
        self.radio_zones_only = QtGui.QRadioButton(self.widgetZones)
        self.radio_zones_only.setGeometry(QtCore.QRect(10, 67, 391, 17))
        self.radio_zones_only.setObjectName(_fromUtf8("radio_zones_only"))
        self.lb_zones_proj = QtGui.QLabel(self.widgetZones)
        self.lb_zones_proj.setGeometry(QtCore.QRect(10, 180, 151, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_zones_proj.setFont(font)
        self.lb_zones_proj.setObjectName(_fromUtf8("lb_zones_proj"))
        self.lb_zones_select_file = QtGui.QLabel(self.widgetZones)
        self.lb_zones_select_file.setGeometry(QtCore.QRect(10, 105, 71, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_zones_select_file.setFont(font)
        self.lb_zones_select_file.setObjectName(_fromUtf8("lb_zones_select_file"))
        self.radio_zones_no_data = QtGui.QRadioButton(self.widgetZones)
        self.radio_zones_no_data.setGeometry(QtCore.QRect(10, 50, 391, 17))
        self.radio_zones_no_data.setChecked(True)
        self.radio_zones_no_data.setObjectName(_fromUtf8("radio_zones_no_data"))
        self.cb_zones_class_field = QtGui.QComboBox(self.widgetZones)
        self.cb_zones_class_field.setEnabled(False)
        self.cb_zones_class_field.setGeometry(QtCore.QRect(280, 130, 121, 22))
        self.cb_zones_class_field.setObjectName(_fromUtf8("cb_zones_class_field"))
        self.lb_zones_class_field = QtGui.QLabel(self.widgetZones)
        self.lb_zones_class_field.setGeometry(QtCore.QRect(10, 130, 281, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_zones_class_field.setFont(font)
        self.lb_zones_class_field.setObjectName(_fromUtf8("lb_zones_class_field"))
        self.lb_zones_title = QtGui.QLabel(self.widgetZones)
        self.lb_zones_title.setGeometry(QtCore.QRect(5, 0, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.lb_zones_title.setFont(font)
        self.lb_zones_title.setObjectName(_fromUtf8("lb_zones_title"))
        self.btn_zones_select_file = QtGui.QToolButton(self.widgetZones)
        self.btn_zones_select_file.setEnabled(False)
        self.btn_zones_select_file.setGeometry(QtCore.QRect(360, 105, 41, 19))
        self.btn_zones_select_file.setCursor(QtCore.Qt.ArrowCursor)
        self.btn_zones_select_file.setObjectName(_fromUtf8("btn_zones_select_file"))
        self.cb_zones_proj = QtGui.QComboBox(self.widgetZones)
        self.cb_zones_proj.setEnabled(False)
        self.cb_zones_proj.setGeometry(QtCore.QRect(280, 180, 121, 22))
        self.cb_zones_proj.setObjectName(_fromUtf8("cb_zones_proj"))
        self.txt_zones_select_file = QtGui.QLineEdit(self.widgetZones)
        self.txt_zones_select_file.setEnabled(False)
        self.txt_zones_select_file.setGeometry(QtCore.QRect(80, 105, 271, 20))
        self.txt_zones_select_file.setObjectName(_fromUtf8("txt_zones_select_file"))
        self.lb_zones_desc = QtGui.QLabel(self.widgetZones)
        self.lb_zones_desc.setGeometry(QtCore.QRect(5, 30, 251, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_zones_desc.setFont(font)
        self.lb_zones_desc.setObjectName(_fromUtf8("lb_zones_desc"))
        self.img_lb_zones_desc_help = QtGui.QLabel(self.widgetZones)
        self.img_lb_zones_desc_help.setGeometry(QtCore.QRect(240, 5, 16, 21))
        self.img_lb_zones_desc_help.setText(_fromUtf8(""))
        self.img_lb_zones_desc_help.setPixmap(QtGui.QPixmap(_fromUtf8(":/imgs/icons/help.png")))
        self.img_lb_zones_desc_help.setObjectName(_fromUtf8("img_lb_zones_desc_help"))
        self.lb_zones_count_field = QtGui.QLabel(self.widgetZones)
        self.lb_zones_count_field.setGeometry(QtCore.QRect(10, 155, 271, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_zones_count_field.setFont(font)
        self.lb_zones_count_field.setObjectName(_fromUtf8("lb_zones_count_field"))
        self.cb_zones_count_field = QtGui.QComboBox(self.widgetZones)
        self.cb_zones_count_field.setEnabled(False)
        self.cb_zones_count_field.setGeometry(QtCore.QRect(280, 155, 121, 22))
        self.cb_zones_count_field.setObjectName(_fromUtf8("cb_zones_count_field"))
        self.lb_gem_logo = QtGui.QLabel(widgetDataInput)
        self.lb_gem_logo.setGeometry(QtCore.QRect(760, 0, 121, 61))
        self.lb_gem_logo.setText(_fromUtf8(""))
        self.lb_gem_logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/imgs/gem_logo_120X60.png")))
        self.lb_gem_logo.setScaledContents(False)
        self.lb_gem_logo.setObjectName(_fromUtf8("lb_gem_logo"))
        self.widgetPop = QtGui.QWidget(widgetDataInput)
        self.widgetPop.setGeometry(QtCore.QRect(10, 470, 411, 191))
        self.widgetPop.setObjectName(_fromUtf8("widgetPop"))
        self.radio_pop_grid = QtGui.QRadioButton(self.widgetPop)
        self.radio_pop_grid.setGeometry(QtCore.QRect(10, 67, 381, 17))
        self.radio_pop_grid.setObjectName(_fromUtf8("radio_pop_grid"))
        self.lb_pop_desc = QtGui.QLabel(self.widgetPop)
        self.lb_pop_desc.setGeometry(QtCore.QRect(5, 30, 281, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_pop_desc.setFont(font)
        self.lb_pop_desc.setObjectName(_fromUtf8("lb_pop_desc"))
        self.lb_pop_title = QtGui.QLabel(self.widgetPop)
        self.lb_pop_title.setGeometry(QtCore.QRect(5, 0, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.lb_pop_title.setFont(font)
        self.lb_pop_title.setObjectName(_fromUtf8("lb_pop_title"))
        self.radio_pop_no_data = QtGui.QRadioButton(self.widgetPop)
        self.radio_pop_no_data.setGeometry(QtCore.QRect(10, 50, 381, 17))
        self.radio_pop_no_data.setObjectName(_fromUtf8("radio_pop_no_data"))
        self.img_lb_pop_desc_help = QtGui.QLabel(self.widgetPop)
        self.img_lb_pop_desc_help.setGeometry(QtCore.QRect(170, 5, 16, 21))
        self.img_lb_pop_desc_help.setText(_fromUtf8(""))
        self.img_lb_pop_desc_help.setPixmap(QtGui.QPixmap(_fromUtf8(":/imgs/icons/help.png")))
        self.img_lb_pop_desc_help.setObjectName(_fromUtf8("img_lb_pop_desc_help"))
        self.btn_pop_select_file = QtGui.QToolButton(self.widgetPop)
        self.btn_pop_select_file.setEnabled(False)
        self.btn_pop_select_file.setGeometry(QtCore.QRect(360, 90, 41, 19))
        self.btn_pop_select_file.setCursor(QtCore.Qt.ArrowCursor)
        self.btn_pop_select_file.setObjectName(_fromUtf8("btn_pop_select_file"))
        self.txt_pop_select_file = QtGui.QLineEdit(self.widgetPop)
        self.txt_pop_select_file.setEnabled(False)
        self.txt_pop_select_file.setGeometry(QtCore.QRect(90, 90, 261, 20))
        self.txt_pop_select_file.setObjectName(_fromUtf8("txt_pop_select_file"))
        self.lb_pop_select_file = QtGui.QLabel(self.widgetPop)
        self.lb_pop_select_file.setGeometry(QtCore.QRect(10, 90, 71, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_pop_select_file.setFont(font)
        self.lb_pop_select_file.setObjectName(_fromUtf8("lb_pop_select_file"))
        self.lb_pop_pop_field = QtGui.QLabel(self.widgetPop)
        self.lb_pop_pop_field.setGeometry(QtCore.QRect(10, 115, 241, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_pop_pop_field.setFont(font)
        self.lb_pop_pop_field.setObjectName(_fromUtf8("lb_pop_pop_field"))
        self.cb_pop_pop_field = QtGui.QComboBox(self.widgetPop)
        self.cb_pop_pop_field.setEnabled(False)
        self.cb_pop_pop_field.setGeometry(QtCore.QRect(280, 115, 121, 22))
        self.cb_pop_pop_field.setObjectName(_fromUtf8("cb_pop_pop_field"))
        self.cb_pop_proj = QtGui.QComboBox(self.widgetPop)
        self.cb_pop_proj.setEnabled(False)
        self.cb_pop_proj.setGeometry(QtCore.QRect(280, 165, 121, 22))
        self.cb_pop_proj.setObjectName(_fromUtf8("cb_pop_proj"))
        self.lb_pop_proj = QtGui.QLabel(self.widgetPop)
        self.lb_pop_proj.setGeometry(QtCore.QRect(10, 165, 151, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_pop_proj.setFont(font)
        self.lb_pop_proj.setObjectName(_fromUtf8("lb_pop_proj"))
        self.lb_pop_bldg_ratio = QtGui.QLabel(self.widgetPop)
        self.lb_pop_bldg_ratio.setGeometry(QtCore.QRect(10, 140, 251, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lb_pop_bldg_ratio.setFont(font)
        self.lb_pop_bldg_ratio.setObjectName(_fromUtf8("lb_pop_bldg_ratio"))
        self.txt_pop_bldg_ratio = QtGui.QLineEdit(self.widgetPop)
        self.txt_pop_bldg_ratio.setEnabled(False)
        self.txt_pop_bldg_ratio.setGeometry(QtCore.QRect(280, 140, 121, 20))
        self.txt_pop_bldg_ratio.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_pop_bldg_ratio.setObjectName(_fromUtf8("txt_pop_bldg_ratio"))

        self.retranslateUi(widgetDataInput)
        QtCore.QMetaObject.connectSlotsByName(widgetDataInput)
        widgetDataInput.setTabOrder(self.radio_fp_no_data, self.radio_fp_height)
        widgetDataInput.setTabOrder(self.radio_fp_height, self.radio_fp_only)
        widgetDataInput.setTabOrder(self.radio_fp_only, self.txt_fp_select_file)
        widgetDataInput.setTabOrder(self.txt_fp_select_file, self.btn_fp_select_file)
        widgetDataInput.setTabOrder(self.btn_fp_select_file, self.cb_fp_story_field)
        widgetDataInput.setTabOrder(self.cb_fp_story_field, self.cb_fp_proj)
        widgetDataInput.setTabOrder(self.cb_fp_proj, self.radio_svy_no_data)
        widgetDataInput.setTabOrder(self.radio_svy_no_data, self.radio_svy_complete)
        widgetDataInput.setTabOrder(self.radio_svy_complete, self.radio_svy_sampled)
        widgetDataInput.setTabOrder(self.radio_svy_sampled, self.txt_svy_select_file)
        widgetDataInput.setTabOrder(self.txt_svy_select_file, self.btn_svy_select_file)
        widgetDataInput.setTabOrder(self.btn_svy_select_file, self.radio_aggr_zones)
        widgetDataInput.setTabOrder(self.radio_aggr_zones, self.radio_aggr_grid)
        widgetDataInput.setTabOrder(self.radio_aggr_grid, self.radio_zones_no_data)
        widgetDataInput.setTabOrder(self.radio_zones_no_data, self.radio_zones_only)
        widgetDataInput.setTabOrder(self.radio_zones_only, self.radio_zones_count)
        widgetDataInput.setTabOrder(self.radio_zones_count, self.txt_zones_select_file)
        widgetDataInput.setTabOrder(self.txt_zones_select_file, self.btn_zones_select_file)
        widgetDataInput.setTabOrder(self.btn_zones_select_file, self.cb_zones_class_field)
        widgetDataInput.setTabOrder(self.cb_zones_class_field, self.cb_zones_proj)
        widgetDataInput.setTabOrder(self.cb_zones_proj, self.btn_verify)
        widgetDataInput.setTabOrder(self.btn_verify, self.txt_panel_description)
        widgetDataInput.setTabOrder(self.txt_panel_description, self.txt_verify_text)

    def retranslateUi(self, widgetDataInput):
        widgetDataInput.setWindowTitle(QtGui.QApplication.translate("widgetDataInput", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_svy_select_file.setText(QtGui.QApplication.translate("widgetDataInput", "Select file:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_svy_desc.setText(QtGui.QApplication.translate("widgetDataInput", "What type of survey / field data do you have?", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_svy_select_file.setText(QtGui.QApplication.translate("widgetDataInput", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_svy_sampled.setText(QtGui.QApplication.translate("widgetDataInput", "Sampled buildings from survey area", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_svy_no_data.setText(QtGui.QApplication.translate("widgetDataInput", "No Data", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_svy_complete.setText(QtGui.QApplication.translate("widgetDataInput", "Complete building stock/survey area", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_svy_title.setText(QtGui.QApplication.translate("widgetDataInput", "Survey & field data", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_verify_title.setText(QtGui.QApplication.translate("widgetDataInput", "You have supplied the following types of data", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_verify_fp.setText(QtGui.QApplication.translate("widgetDataInput", "Footprint", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_verify_svy.setText(QtGui.QApplication.translate("widgetDataInput", "Survey", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_verify_zones.setText(QtGui.QApplication.translate("widgetDataInput", "Zones", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_verify_aggregation.setText(QtGui.QApplication.translate("widgetDataInput", "Output data aggregation", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_verify_agg_zone.setText(QtGui.QApplication.translate("widgetDataInput", "Zone", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_verify_agg_grid.setText(QtGui.QApplication.translate("widgetDataInput", "GED Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.txt_verify_text.setHtml(QtGui.QApplication.translate("widgetDataInput", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_verify.setText(QtGui.QApplication.translate("widgetDataInput", "Verify Input Data", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_verify_pop.setText(QtGui.QApplication.translate("widgetDataInput", "Population Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_aggr_grid.setText(QtGui.QApplication.translate("widgetDataInput", "GED Compatible 30 arc-second grid", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_aggr_desc.setText(QtGui.QApplication.translate("widgetDataInput", "How do you wish to aggregate your output data?", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_aggr_title.setText(QtGui.QApplication.translate("widgetDataInput", "Aggregation", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_aggr_zones.setText(QtGui.QApplication.translate("widgetDataInput", "Output into defined zones ", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_fp_height.setText(QtGui.QApplication.translate("widgetDataInput", "Building footprints with number of stories", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_fp_select_file.setText(QtGui.QApplication.translate("widgetDataInput", "Select file:", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_fp_only.setText(QtGui.QApplication.translate("widgetDataInput", "Building footprints without number of stories", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_fp_title.setText(QtGui.QApplication.translate("widgetDataInput", "Building footprint data", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_fp_desc.setText(QtGui.QApplication.translate("widgetDataInput", "What type of data do you have for building footprints?", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_fp_proj.setText(QtGui.QApplication.translate("widgetDataInput", "Verify projection:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_fp_select_file.setText(QtGui.QApplication.translate("widgetDataInput", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_fp_no_data.setText(QtGui.QApplication.translate("widgetDataInput", "No Data", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_fp_story_field.setText(QtGui.QApplication.translate("widgetDataInput", "Select field containing number of stories:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_panel_title.setText(QtGui.QApplication.translate("widgetDataInput", "Define required input data", None, QtGui.QApplication.UnicodeUTF8))
        self.txt_panel_description.setHtml(QtGui.QApplication.translate("widgetDataInput", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Specify input data <br />Different combination of data can be used toward generating mapping schemes and exposure. </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_zones_count.setText(QtGui.QApplication.translate("widgetDataInput", "Homogeneous zones with building count", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_zones_only.setText(QtGui.QApplication.translate("widgetDataInput", "Homogeneous zones", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_zones_proj.setText(QtGui.QApplication.translate("widgetDataInput", "Verify projection:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_zones_select_file.setText(QtGui.QApplication.translate("widgetDataInput", "Select file:", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_zones_no_data.setText(QtGui.QApplication.translate("widgetDataInput", "No Data", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_zones_class_field.setText(QtGui.QApplication.translate("widgetDataInput", "Select field containing zone identifier", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_zones_title.setText(QtGui.QApplication.translate("widgetDataInput", "Homogeneous zones data", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_zones_select_file.setText(QtGui.QApplication.translate("widgetDataInput", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_zones_desc.setText(QtGui.QApplication.translate("widgetDataInput", "What type of data do you have for zones?", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_zones_count_field.setText(QtGui.QApplication.translate("widgetDataInput", "Select field containing building count", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_pop_grid.setText(QtGui.QApplication.translate("widgetDataInput", "Population Grid from GED", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_pop_desc.setText(QtGui.QApplication.translate("widgetDataInput", "Population ", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_pop_title.setText(QtGui.QApplication.translate("widgetDataInput", "Population Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.radio_pop_no_data.setText(QtGui.QApplication.translate("widgetDataInput", "No Data", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_pop_select_file.setText(QtGui.QApplication.translate("widgetDataInput", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_pop_select_file.setText(QtGui.QApplication.translate("widgetDataInput", "Select file:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_pop_pop_field.setText(QtGui.QApplication.translate("widgetDataInput", "Select field containing population:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_pop_proj.setText(QtGui.QApplication.translate("widgetDataInput", "Verify projection:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_pop_bldg_ratio.setText(QtGui.QApplication.translate("widgetDataInput", "Average Number of People Per Building", None, QtGui.QApplication.UnicodeUTF8))

import SIDDResource_rc
