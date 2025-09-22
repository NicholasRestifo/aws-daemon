from PyQt6.QtCore import QSizeF


def bind_height_to_document(widget):
        widget.document().documentLayout().documentSizeChanged.connect(lambda height: _adjust_height(widget, height))

def _adjust_height(widget, size: QSizeF):
    # Adding a small margin to prevent scrollbars appearing prematurely
    widget.setMaximumHeight(int(size.height()) + int(widget.document().documentMargin() * 2))