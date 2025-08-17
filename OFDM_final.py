#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: geevarjos
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import blocks
import numpy
from gnuradio import digital
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip



class OFDM_final(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "OFDM_final")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.noise_std = noise_std = 0.01
        self.myconst = myconst = digital.constellation_calcdist([-1-1j, -1+1j, 1+1j, 1-1j], [0, 1, 3, 2],
        4, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        self.myconst.set_npwr(1.0)
        self.h = h = [1.0, 0.2 + 0.3j, 0.1-0.05j]
        self.FFTSIZE = FFTSIZE = 8

        ##################################################
        # Blocks
        ##################################################

        self._noise_std_range = qtgui.Range(0, 3, 0.01, 0.01, 200)
        self._noise_std_win = qtgui.RangeWidget(self._noise_std_range, self.set_noise_std, "'noise_std'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._noise_std_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            FFTSIZE, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(FFTSIZE):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccc(1, h)
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0.set_block_alias("Channel")
        self.fft_vxx_1 = fft.fft_vcc(FFTSIZE, True, [1]*FFTSIZE, False, 1)
        self.fft_vxx_0 = fft.fft_vcc(FFTSIZE, False, [1]*FFTSIZE, False, 1)
        self.digital_constellation_encoder_bc_0 = digital.constellation_encoder_bc(myconst)
        self.blocks_vector_to_stream_0_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, FFTSIZE)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, FFTSIZE)
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_gr_complex*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_stream_to_vector_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, FFTSIZE)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, FFTSIZE)
        self.blocks_stream_mux_0_0 = blocks.stream_mux(gr.sizeof_gr_complex*1, [1]*FFTSIZE)
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_gr_complex*1, [1]*(FFTSIZE+3))
        self.blocks_stream_demux_1 = blocks.stream_demux(gr.sizeof_gr_complex*1, [1]*FFTSIZE)
        self.blocks_stream_demux_0_0 = blocks.stream_demux(gr.sizeof_gr_complex*1, [1]*(FFTSIZE + 3))
        self.blocks_stream_demux_0 = blocks.stream_demux(gr.sizeof_gr_complex*1, [1]*FFTSIZE)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 4, 1000))), True)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, noise_std, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_random_source_x_0, 0), (self.digital_constellation_encoder_bc_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_stream_demux_0_0, 0))
        self.connect((self.blocks_stream_demux_0, 2), (self.blocks_stream_mux_0, 5))
        self.connect((self.blocks_stream_demux_0, 5), (self.blocks_stream_mux_0, 8))
        self.connect((self.blocks_stream_demux_0, 4), (self.blocks_stream_mux_0, 7))
        self.connect((self.blocks_stream_demux_0, 1), (self.blocks_stream_mux_0, 4))
        self.connect((self.blocks_stream_demux_0, 6), (self.blocks_stream_mux_0, 1))
        self.connect((self.blocks_stream_demux_0, 6), (self.blocks_stream_mux_0, 9))
        self.connect((self.blocks_stream_demux_0, 0), (self.blocks_stream_mux_0, 3))
        self.connect((self.blocks_stream_demux_0, 3), (self.blocks_stream_mux_0, 6))
        self.connect((self.blocks_stream_demux_0, 5), (self.blocks_stream_mux_0, 0))
        self.connect((self.blocks_stream_demux_0, 7), (self.blocks_stream_mux_0, 10))
        self.connect((self.blocks_stream_demux_0, 7), (self.blocks_stream_mux_0, 2))
        self.connect((self.blocks_stream_demux_0_0, 1), (self.blocks_null_sink_0, 1))
        self.connect((self.blocks_stream_demux_0_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_stream_demux_0_0, 2), (self.blocks_null_sink_0, 2))
        self.connect((self.blocks_stream_demux_0_0, 6), (self.blocks_stream_mux_0_0, 3))
        self.connect((self.blocks_stream_demux_0_0, 10), (self.blocks_stream_mux_0_0, 7))
        self.connect((self.blocks_stream_demux_0_0, 9), (self.blocks_stream_mux_0_0, 6))
        self.connect((self.blocks_stream_demux_0_0, 8), (self.blocks_stream_mux_0_0, 5))
        self.connect((self.blocks_stream_demux_0_0, 5), (self.blocks_stream_mux_0_0, 2))
        self.connect((self.blocks_stream_demux_0_0, 7), (self.blocks_stream_mux_0_0, 4))
        self.connect((self.blocks_stream_demux_0_0, 4), (self.blocks_stream_mux_0_0, 1))
        self.connect((self.blocks_stream_demux_0_0, 3), (self.blocks_stream_mux_0_0, 0))
        self.connect((self.blocks_stream_demux_1, 1), (self.qtgui_const_sink_x_0, 1))
        self.connect((self.blocks_stream_demux_1, 7), (self.qtgui_const_sink_x_0, 7))
        self.connect((self.blocks_stream_demux_1, 4), (self.qtgui_const_sink_x_0, 4))
        self.connect((self.blocks_stream_demux_1, 3), (self.qtgui_const_sink_x_0, 3))
        self.connect((self.blocks_stream_demux_1, 6), (self.qtgui_const_sink_x_0, 6))
        self.connect((self.blocks_stream_demux_1, 2), (self.qtgui_const_sink_x_0, 2))
        self.connect((self.blocks_stream_demux_1, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_stream_demux_1, 5), (self.qtgui_const_sink_x_0, 5))
        self.connect((self.blocks_stream_mux_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.blocks_stream_mux_0_0, 0), (self.blocks_stream_to_vector_1, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_stream_to_vector_1, 0), (self.fft_vxx_1, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_stream_demux_0, 0))
        self.connect((self.blocks_vector_to_stream_0_0, 0), (self.blocks_stream_demux_1, 0))
        self.connect((self.digital_constellation_encoder_bc_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.fft_vxx_1, 0), (self.blocks_vector_to_stream_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.blocks_add_xx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "OFDM_final")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)

    def get_noise_std(self):
        return self.noise_std

    def set_noise_std(self, noise_std):
        self.noise_std = noise_std
        self.analog_noise_source_x_0.set_amplitude(self.noise_std)

    def get_myconst(self):
        return self.myconst

    def set_myconst(self, myconst):
        self.myconst = myconst
        self.digital_constellation_encoder_bc_0.set_constellation(self.myconst)

    def get_h(self):
        return self.h

    def set_h(self, h):
        self.h = h
        self.interp_fir_filter_xxx_0.set_taps(self.h)

    def get_FFTSIZE(self):
        return self.FFTSIZE

    def set_FFTSIZE(self, FFTSIZE):
        self.FFTSIZE = FFTSIZE




def main(top_block_cls=OFDM_final, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
