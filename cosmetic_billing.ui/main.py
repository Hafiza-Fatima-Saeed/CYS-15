import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt
from cosmetic_billing import Ui_MainWindow
from datetime import datetime


STYLESHEET = """
/* ── Main Window ───────────────────────────────────────── */
QMainWindow {
    background-color: #f5f5f5;
}

QWidget {
    background-color: #f5f5f5;
    color: #1a1a1a;
    font-family: 'Segoe UI', sans-serif;
    font-size: 13px;
}

/* ── Buttons ────────────────────────────────────────────── */
QPushButton {
    background-color: #1a1a1a;
    color: #ffffff;
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
    font-size: 13px;
    font-weight: bold;
    letter-spacing: 0.5px;
}

QPushButton:hover {
    background-color: #3a3a3a;
}

QPushButton:pressed {
    background-color: #000000;
}

/* Add to Cart – pastel pink */
QPushButton#addToCartBtn {
    background-color: #f4a7b9;
    color: #1a1a1a;
}
QPushButton#addToCartBtn:hover {
    background-color: #f7bfcc;
}
QPushButton#addToCartBtn:pressed {
    background-color: #e88fa3;
}

/* Clear Cart – pastel red/rose */
QPushButton#clearCartBtn {
    background-color: #f28b82;
    color: #1a1a1a;
}
QPushButton#clearCartBtn:hover {
    background-color: #f5a49d;
}
QPushButton#clearCartBtn:pressed {
    background-color: #e07068;
}

/* Generate Bill – pastel green */
QPushButton#generateBillBtn {
    background-color: #b5ead7;
    color: #1a1a1a;
}
QPushButton#generateBillBtn:hover {
    background-color: #c8f0e3;
}
QPushButton#generateBillBtn:pressed {
    background-color: #9dd4c0;
}

/* ── ComboBox ───────────────────────────────────────────── */
QComboBox {
    background-color: #ffffff;
    color: #1a1a1a;
    border: 1.5px solid #cccccc;
    border-radius: 10px;
    padding: 8px 14px;
    font-size: 13px;
}

QComboBox:hover {
    border-color: #aaaaaa;
}

QComboBox::drop-down {
    border: none;
    width: 30px;
}

QComboBox::down-arrow {
    width: 12px;
    height: 12px;
    image: none;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 7px solid #555555;
}

QComboBox QAbstractItemView {
    background-color: #ffffff;
    color: #1a1a1a;
    border: 1.5px solid #cccccc;
    border-radius: 8px;
    selection-background-color: #d0e8ff;
    selection-color: #1a1a1a;
    padding: 4px;
}

/* ── SpinBox ────────────────────────────────────────────── */
QSpinBox {
    background-color: #ffffff;
    color: #1a1a1a;
    border: 1.5px solid #cccccc;
    border-radius: 10px;
    padding: 8px 14px;
    font-size: 13px;
}

QSpinBox:hover {
    border-color: #aaaaaa;
}

QSpinBox::up-button, QSpinBox::down-button {
    background-color: #e0e0e0;
    border-radius: 4px;
    width: 20px;
}

QSpinBox::up-button:hover, QSpinBox::down-button:hover {
    background-color: #c8c8c8;
}

QSpinBox::up-arrow {
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-bottom: 6px solid #333333;
}

QSpinBox::down-arrow {
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 6px solid #333333;
}

/* ── Table ──────────────────────────────────────────────── */
QTableWidget {
    background-color: #ffffff;
    color: #1a1a1a;
    border: 1.5px solid #dddddd;
    border-radius: 12px;
    gridline-color: #eeeeee;
    font-size: 13px;
}

QTableWidget::item {
    padding: 8px;
    border-bottom: 1px solid #eeeeee;
}

QTableWidget::item:selected {
    background-color: #d0e8ff;
    color: #1a1a1a;
}

QTableWidget::item:alternate {
    background-color: #fafafa;
}

QHeaderView::section {
    background-color: #1a1a1a;
    color: #ffffff;
    font-weight: bold;
    font-size: 13px;
    padding: 10px;
    border: none;
    border-right: 1px solid #333333;
}

QTableWidget QScrollBar:vertical {
    background: #f0f0f0;
    width: 10px;
    border-radius: 5px;
}

QTableWidget QScrollBar::handle:vertical {
    background: #bbbbbb;
    border-radius: 5px;
    min-height: 20px;
}

/* ── Plain Text Edit (bill display) ────────────────────── */
QPlainTextEdit {
    background-color: #1a1a1a;
    color: #f5f5f5;
    border: 1.5px solid #dddddd;
    border-radius: 12px;
    padding: 12px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 12px;
    selection-background-color: #b5ead7;
    selection-color: #1a1a1a;
}

/* ── Labels ─────────────────────────────────────────────── */
QLabel {
    color: #1a1a1a;
    font-size: 13px;
}

QLabel#subtotalLabel {
    color: #c0687a;
    font-size: 14px;
    font-weight: bold;
}

QLabel#totalLabel {
    color: #1a1a1a;
    font-size: 15px;
    font-weight: bold;
}

/* ── Status Bar ─────────────────────────────────────────── */
QStatusBar {
    background-color: #eeeeee;
    color: #1a1a1a;
    border-top: 1px solid #cccccc;
}

/* ── Scrollbars (global) ────────────────────────────────── */
QScrollBar:vertical {
    background: #f0f0f0;
    width: 10px;
    border-radius: 5px;
}
QScrollBar::handle:vertical {
    background: #bbbbbb;
    border-radius: 5px;
}
QScrollBar:horizontal {
    background: #f0f0f0;
    height: 10px;
    border-radius: 5px;
}
QScrollBar::handle:horizontal {
    background: #bbbbbb;
    border-radius: 5px;
}

/* ── Message Box ────────────────────────────────────────── */
QMessageBox {
    background-color: #ffffff;
    color: #1a1a1a;
}
QMessageBox QLabel {
    color: #1a1a1a;
    font-size: 13px;
}
QMessageBox QPushButton {
    min-width: 80px;
    min-height: 30px;
}
"""


class BillingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("💄 Saeed Cosmetics – Billing System")

        
        self.setStyleSheet(STYLESHEET)

        self.products = {
            "Lipstick": 250,
            "Foundation": 800,
            "Mascara": 400,
            "Eyeliner": 150,
            "Face Powder": 350,
            "Moisturizer": 600,
            "SunScreen": 650,
            "Makeup Removal Wipes": 700,
            "Concealer":500,
            "Colour Corrector": 700,
            "Sheet Mask": 1000,
            "Blush": 980,
            "Lip Tint": 300,
            "Perfume": 3000,
            "Lip Liner": 250,
            "Primer": 500,
            "Bronzer": 400,
            "Lip Gloss": 700,
            "Eye Shades Palette": 1000,
            "Makeup Setting Spray": 900,
            
        }

        self.ui.cartTable.setColumnCount(4)
        self.ui.cartTable.setHorizontalHeaderLabels(["Product", "Qty", "Price", "Total"])
        self.ui.cartTable.setColumnWidth(0, 200)
        self.ui.cartTable.setAlternatingRowColors(True)

        self.ui.productComboBox.addItems(self.products.keys())

        self.ui.addToCartBtn.clicked.connect(self.add_to_cart)
        self.ui.clearCartBtn.clicked.connect(self.clear_cart)
        self.ui.generateBillBtn.clicked.connect(self.generate_bill)

        self.update_totals()

    # ── Cart logic ────────────────────────────────────────────

    def add_to_cart(self):
        product = self.ui.productComboBox.currentText()
        qty = self.ui.quantitySpinBox.value()

        if qty == 0:
            QMessageBox.warning(self, "Warning", "Quantity cannot be 0")
            return

        price = self.products[product]
        total = price * qty

        row = self.ui.cartTable.rowCount()
        self.ui.cartTable.insertRow(row)
        self.ui.cartTable.setItem(row, 0, QTableWidgetItem(product))
        self.ui.cartTable.setItem(row, 1, QTableWidgetItem(str(qty)))
        self.ui.cartTable.setItem(row, 2, QTableWidgetItem(f"{price:.2f}"))
        self.ui.cartTable.setItem(row, 3, QTableWidgetItem(f"{total:.2f}"))

        # Center-align qty, price, total columns
        for col in range(1, 4):
            self.ui.cartTable.item(row, col).setTextAlignment(Qt.AlignCenter)

        self.update_totals()
        self.ui.quantitySpinBox.setValue(0)

    def clear_cart(self):
        self.ui.cartTable.setRowCount(0)
        self.update_totals()

    def update_totals(self):
        subtotal = 0
        for row in range(self.ui.cartTable.rowCount()):
            subtotal += float(self.ui.cartTable.item(row, 3).text())

        tax = subtotal * 0.13
        grand_total = subtotal + tax

        self.ui.subtotalLabel.setText(f"Subtotal: Rs. {subtotal:.2f}")
        self.ui.totalLabel.setText(f"Grand Total: Rs. {grand_total:.2f}")

    # ── Bill generation ───────────────────────────────────────

    def generate_bill(self):
        if self.ui.cartTable.rowCount() == 0:
            self.ui.billDisplay.setPlainText("🛒  Cart is empty – add items first!")
            return

        shop_name  = "Online Billing System"
        shop_addr  = "Main Mansoorah Bazar"
        shop_phone = "Ph: 03224-533157"
        now        = datetime.now().strftime("%Y-%m-%d  %I:%M:%S %p")

        lines = [
            "╔══════════════════════════════════════╗",
            f"║{'Saeed Cosmetics':^38}",
            f"║{shop_name:^38}",
            f"║{shop_addr:^38}",
            f"║{shop_phone:^38}",
            "╠══════════════════════════════════════╣",
            f"  Date: {now}",
            "────────────────────────────────────────",
            f"{'Product':<18} {'Qty':>4}  {'Price':>8}  {'Total':>8}",
            "────────────────────────────────────────",
        ]

        subtotal = 0
        for row in range(self.ui.cartTable.rowCount()):
            product = self.ui.cartTable.item(row, 0).text()
            qty     = self.ui.cartTable.item(row, 1).text()
            price   = self.ui.cartTable.item(row, 2).text()
            total   = self.ui.cartTable.item(row, 3).text()
            subtotal += float(total)
            lines.append(f"{product:<18} {qty:>4}  {price:>8}  {total:>8}")

        tax         = subtotal * 0.13
        grand_total = subtotal + tax

        lines += [
            "────────────────────────────────────────",
            f"{'Subtotal:':>30}  Rs.{subtotal:>8.2f}",
            f"{'Tax (13%):':>30}  Rs.{tax:>8.2f}",
            "════════════════════════════════════════",
            f"{'GRAND TOTAL:':>30}  Rs.{grand_total:>8.2f}",
            "════════════════════════════════════════",
            "",
            "      ✨ Thank you for shopping! ✨",
            "╚══════════════════════════════════════╝",
        ]

        bill_text = "\n".join(lines)
        self.ui.billDisplay.setPlainText(bill_text)

        filename = f"Bill_{datetime.now().strftime('%Y%m%d_%I%M%S_%p')}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(bill_text)

        QMessageBox.information(self, "✅ Success", f"Bill saved as:\n{filename}")
        self.clear_cart()
        return bill_text


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BillingWindow()
    window.show()
    sys.exit(app.exec())
