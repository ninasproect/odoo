# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)
import base64
import io
try:
    import qrcode

except ImportError:
    _logger.debug('ImportError')


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    qr_code = fields.Binary('QR Code', compute="_generate_qr_code")


    @api.one
    @api.depends('name')
    def _generate_qr_code(self):
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=4)
        if self.name :
            qr.add_data(self.name)
            qr.make(fit=True)
            img = qr.make_image()
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            qrcode_img = base64.b64encode(buffer.getvalue())
            self.update({'qr_code': qrcode_img,})